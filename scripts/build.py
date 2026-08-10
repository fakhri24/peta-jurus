#!/usr/bin/env python3
"""Ubah tulisan di konten/ menjadi data/jurus.json dan data/soal.json.

Jalankan dari akar proyek:

    python3 scripts/build.py

Skrip ini hanya butuh PyYAML. Markdown-nya ditangani sendiri (lihat markdown_ke_html)
karena rumus LaTeX harus dilindungi lebih dulu — pustaka Markdown umum akan merusak
$a_1$ jadi huruf miring dan menelan garis miring ganda di dalam align.
"""

import html
import importlib.util
import json
import re
import sys
from pathlib import Path

import yaml

AKAR = Path(__file__).resolve().parent.parent
KONTEN = AKAR / "konten"
DATA = AKAR / "data"

# Rajah geometri: sumbernya berkas Python yang menghitung bangunnya, keluarannya
# SVG. Lihat scripts/rajah.py untuk alasannya dihitung, bukan digambar tangan.
RAJAH_SUMBER = KONTEN / "rajah"
RAJAH_KELUAR = AKAR / "assets" / "rajah"

# Ditulis di markdown sebagai nama berkas telanjang — 'segitiga-abc.svg', bukan
# jalur atau alamat web. Awalannya dipasang di sini supaya letak berkasnya bisa
# pindah tanpa menyunting ratusan soal.
AWALAN_RAJAH = "assets/rajah/"

# Tata letak peta: tingkat jadi baris, dari atas ke bawah.
LEBAR_SIMPUL = 168
JARAK_X = 28
TINGGI_BARIS = 112
TEPI = 24

# Urutan bidang di halaman peta, ditetapkan di sini dan bukan diserahkan ke abjad
# slug. Tanpa daftar ini, menambah 'aljabar' melempar 'teori-bilangan' ke dasar
# halaman hanya karena huruf a. Urutannya mengikuti urutan pengerjaan di PLAN.md.
# Daftar ini sekaligus jadi satu-satunya pilar yang sah — salah ketik pada 'pilar'
# tidak lagi diam-diam membuat bidang hantu yang muncul sebagai peta kosong.
URUT_PILAR = ("teori-bilangan", "aljabar", "kombinatorika", "geometri")

# Dari yang paling awal ke paling akhir. Urutannya dipakai saringan tahap di peta:
# siswa yang menyiapkan OSN-P tetap perlu melihat jurus OSN-K.
TAHAP_SAH = ("osn-k", "osn-p", "osn")

# Naskah asli yang boleh dijadikan atribusi. Isinya metadata dan tautan saja —
# tidak ada PDF naskah di repo ini, karena "gratis diunduh" dan "bebas disebarkan
# ulang" adalah dua izin yang berbeda. Lihat PLAN.md Fase 5.
ARSIP = KONTEN / "arsip.yml"
WAJIB_ARSIP = ("judul", "penyelenggara", "tahun", "tahap", "tautan", "diakses")

# Atribusi ke naskah asli: 'OSN' atau 'KSN' berdampingan dengan tahun empat angka.
# 'susunan sendiri, gaya OSN-K' sengaja tidak tertangkap — yang dijaga adalah klaim
# tahunnya, bukan penyebutan nama lombanya. Jarak antar-keduanya dibatasi supaya
# 'Latihan 3 — susunan sendiri, gaya OSN' yang kebetulan bertetangga dengan angka
# lain tidak ikut kena.
ATRIBUSI_NYATA = re.compile(
    r"\b(?:OSN|KSN)\b[-\w\s]{0,15}?\b(?:19|20)\d{2}\b"
    r"|\b(?:19|20)\d{2}\b[-\w\s]{0,15}?\b(?:OSN|KSN)\b",
    re.IGNORECASE,
)


class GagalBuild(Exception):
    pass


# ---------------------------------------------------------------- rumus & markdown

RUMUS_BLOK = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
RUMUS_SEBARIS = re.compile(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$", re.DOTALL)


def lindungi_rumus(teks):
    """Cabut semua rumus, ganti dengan penanda yang tak tersentuh aturan Markdown.

    Penandanya memakai NUL — karakter yang tidak pernah muncul di tulisan dan tidak
    mengandung *, _, ` atau [ sehingga aturan Markdown melewatinya begitu saja.
    """
    simpanan = []

    def cabut(m):
        simpanan.append(m.group(0))
        return "\x00M%d\x00" % (len(simpanan) - 1)

    teks = RUMUS_BLOK.sub(cabut, teks)
    teks = RUMUS_SEBARIS.sub(cabut, teks)
    return teks, simpanan


def kembalikan_rumus(html_teks, simpanan):
    """Pasang lagi rumusnya, dalam keadaan sudah di-escape.

    Rumus sengaja di-escape seperti prosa biasa: KaTeX membaca lewat textContent,
    yang sudah menerjemahkan &lt; kembali jadi <. Jadi $a < b$ aman, dan tanda &
    pada align juga selamat.
    """

    def pasang(m):
        return html.escape(simpanan[int(m.group(1))], quote=False)

    return re.sub(r"\x00M(\d+)\x00", pasang, html_teks)


# Sengaja membiarkan alt kosong tertangkap: yang kosong harus **ditolak** dengan
# pesan yang jelas, bukan lolos diam-diam sebagai tautan bertanda seru nyasar.
GAMBAR = re.compile(r"!\[([^\]]*)\]\(([^)\s]*)\)")


def _sebaris(teks):
    """Aturan Markdown dalam satu baris. Teks masuk sudah di-escape."""
    teks = re.sub(r"`([^`]+)`", r"<code>\1</code>", teks)

    # Gambar dicabut jadi penanda, bukan langsung ditulis sebagai <img>. Kalau
    # ditulis langsung, aturan di bawahnya menggigit ke dalam atribut yang baru
    # saja dibuat: alt 'Bangun *miring*' keluar sebagai alt="Bangun <em>miring</em>",
    # dan alt bukan HTML — pembaca layar mengejanya apa adanya. Penandanya memakai
    # NUL dengan alasan yang sama dengan lindungi_rumus().
    simpanan = []

    def cabut(m):
        # html.escape dipanggil dengan quote=False, jadi kutip ganda di alt masih
        # utuh sampai di sini — dan di dalam atribut ia menutup atributnya lebih awal.
        simpanan.append('<img src="%s%s" alt="%s">'
                        % (AWALAN_RAJAH, m.group(2), m.group(1).replace('"', "&quot;")))
        return "\x00G%d\x00" % (len(simpanan) - 1)

    # Sebelum pola tautan, supaya tanda serunya ikut termakan. Kalau dibalik,
    # '[alt](url)' tertangkap lebih dulu dan menyisakan '!' di depan <a>.
    teks = GAMBAR.sub(cabut, teks)

    teks = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', teks)
    teks = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", teks)
    teks = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", teks)
    teks = re.sub(r"(?<!\w)_([^_\n]+)_(?!\w)", r"<em>\1</em>", teks)

    return re.sub(r"\x00G(\d+)\x00", lambda m: simpanan[int(m.group(1))], teks)


AWAL_BLOK_LAIN = re.compile(r"^\s*(#{2,4}\s|&gt;)")


def _kumpulkan_butir(baris, i, pola_awal):
    """Kumpulkan butir daftar, termasuk baris lanjutannya.

    Butir yang panjang biasanya ditulis menyambung di baris berikutnya dengan
    indentasi. Tanpa aturan ini, lanjutannya terlempar keluar dari <li> dan
    muncul sebagai paragraf sendiri di bawah daftar.
    """
    butir = []
    while i < len(baris):
        if re.match(pola_awal, baris[i]):
            butir.append(re.sub(pola_awal, "", baris[i]).strip())
        elif baris[i].strip() and butir and not AWAL_BLOK_LAIN.match(baris[i]):
            butir[-1] += " " + baris[i].strip()
        else:
            break
        i += 1
    return butir, i


def _sel_tabel(baris):
    """Pecah satu baris tabel jadi sel, tanpa pipa kosong di ujung."""
    return [s.strip() for s in baris.strip().strip("|").split("|")]


def _pemisah_tabel(baris, i):
    """Baris kedua tabel harus berupa |---|---| supaya tidak salah tangkap."""
    if i >= len(baris):
        return False
    return bool(re.match(r"^\s*\|[\s:|-]*-[\s:|-]*\|?\s*$", baris[i]))


def _tabel(baris, i):
    kepala = _sel_tabel(baris[i])
    isi = []
    j = i + 2
    while j < len(baris) and baris[j].lstrip().startswith("|"):
        isi.append(_sel_tabel(baris[j]))
        j += 1
    thead = "".join("<th>%s</th>" % _sebaris(s) for s in kepala)
    tbody = "".join(
        "<tr>%s</tr>" % "".join("<td>%s</td>" % _sebaris(s) for s in r) for r in isi
    )
    return "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (thead, tbody)


def _blok(teks):
    """Aturan Markdown antar-baris. Teks masuk sudah di-escape."""
    keluar = []
    baris = teks.split("\n")
    i = 0
    while i < len(baris):
        b = baris[i]
        kosong = not b.strip()

        if kosong:
            i += 1
            continue

        if b.strip() == "---":
            keluar.append("<hr>")
            i += 1
            continue

        cocok = re.match(r"^(#{2,4})\s+(.*)$", b)
        if cocok:
            n = len(cocok.group(1)) + 1  # ## di berkas jadi <h3> di halaman
            keluar.append("<h%d>%s</h%d>" % (n, _sebaris(cocok.group(2).strip()), n))
            i += 1
            continue

        if b.lstrip().startswith("|") and _pemisah_tabel(baris, i + 1):
            keluar.append(_tabel(baris, i))
            while i < len(baris) and baris[i].lstrip().startswith("|"):
                i += 1
            continue

        if re.match(r"^\s*[-*]\s+", b):
            butir, i = _kumpulkan_butir(baris, i, r"^\s*[-*]\s+")
            keluar.append(
                "<ul>%s</ul>" % "".join("<li>%s</li>" % _sebaris(x) for x in butir)
            )
            continue

        if re.match(r"^\s*\d+[.)]\s+", b):
            butir, i = _kumpulkan_butir(baris, i, r"^\s*\d+[.)]\s+")
            keluar.append(
                "<ol>%s</ol>" % "".join("<li>%s</li>" % _sebaris(x) for x in butir)
            )
            continue

        if b.lstrip().startswith("&gt; "):  # '>' sudah jadi &gt; saat escape
            kutipan = []
            while i < len(baris) and baris[i].lstrip().startswith("&gt;"):
                kutipan.append(re.sub(r"^\s*&gt;\s?", "", baris[i]))
                i += 1
            keluar.append("<blockquote>%s</blockquote>" % _blok("\n".join(kutipan)))
            continue

        # Baris pertama selalu ikut termakan, apa pun isinya. Tanpa itu, baris
        # yang tidak cocok dengan satu pun aturan blok — misalnya '|' yang bukan
        # awal tabel — membuat pencacah tidak pernah maju.
        paragraf = [b.strip()]
        i += 1
        while i < len(baris) and baris[i].strip() and not re.match(
            r"^\s*([-*]\s|\d+[.)]\s|#{2,4}\s|&gt;|\|)", baris[i]
        ):
            paragraf.append(baris[i].strip())
            i += 1
        keluar.append("<p>%s</p>" % _sebaris(" ".join(paragraf)))

    return "".join(keluar)


def markdown_ke_html(teks):
    """Markdown subset → HTML, dengan rumus LaTeX dibiarkan utuh untuk KaTeX."""
    if not teks or not teks.strip():
        return ""
    teks, simpanan = lindungi_rumus(teks)
    teks = html.escape(teks, quote=False)
    return kembalikan_rumus(_blok(teks), simpanan)


def markdown_sebaris(teks):
    """Untuk potongan pendek yang tidak boleh dibungkus <p>."""
    if not teks or not teks.strip():
        return ""
    teks, simpanan = lindungi_rumus(teks.strip())
    teks = html.escape(teks, quote=False)
    return kembalikan_rumus(_sebaris(teks), simpanan)


# ---------------------------------------------------------------- baca berkas

def baca_berkas(jalur):
    """Pisahkan frontmatter YAML dari badan tulisan."""
    isi = jalur.read_text(encoding="utf-8")
    if not isi.startswith("---"):
        raise GagalBuild("%s: tidak diawali frontmatter '---'" % jalur.name)
    bagian = isi.split("---", 2)
    if len(bagian) < 3:
        raise GagalBuild("%s: frontmatter tidak ditutup '---'" % jalur.name)
    try:
        depan = yaml.safe_load(bagian[1]) or {}
    except yaml.YAMLError as e:
        raise GagalBuild("%s: frontmatter tidak terbaca — %s" % (jalur.name, e))
    if not isinstance(depan, dict):
        raise GagalBuild("%s: frontmatter harus berupa pasangan kunci-nilai" % jalur.name)
    return depan, bagian[2]


def belah_bagian(badan):
    """Pecah badan tulisan menurut judul '## ', jadi {judul_kecil: isi}."""
    bagian = {}
    judul = None
    baris_tampung = []
    for baris in badan.split("\n"):
        cocok = re.match(r"^##\s+(.*)$", baris)
        if cocok:
            if judul is not None:
                bagian[judul] = "\n".join(baris_tampung).strip()
            judul = cocok.group(1).strip().lower()
            baris_tampung = []
        else:
            baris_tampung.append(baris)
    if judul is not None:
        bagian[judul] = "\n".join(baris_tampung).strip()
    return bagian


def bagian_jadi_daftar(teks):
    """Ubah daftar '- ' jadi array string HTML. Baris lanjutan menempel ke butir di atasnya."""
    if not teks or not teks.strip():
        return []
    butir = []
    for baris in teks.split("\n"):
        if re.match(r"^\s*[-*]\s+", baris):
            butir.append(re.sub(r"^\s*[-*]\s+", "", baris).strip())
        elif baris.strip() and butir:
            butir[-1] += " " + baris.strip()
    return [markdown_sebaris(x) for x in butir]


# ---------------------------------------------------------------- muat konten

WAJIB_JURUS = ("id", "nama", "pilar")
WAJIB_SOAL = ("id", "sumber", "pilar", "jurus", "bentuk")
BENTUK_SAH = ("isian", "uraian")


def periksa_pilar_tahap(nama_berkas, pilar, tahap, galat):
    """Pilar dan tahap harus dari daftar yang sah, bukan teks bebas.

    Keduanya menentukan tempat jurus di peta dan apakah ia lolos saringan tahap.
    Salah ketik satu huruf akan membuatnya hilang dari kedua-duanya tanpa keluhan
    apa pun, jadi lebih baik build-nya berhenti di sini.
    """
    if pilar not in URUT_PILAR:
        galat.append("%s: pilar '%s' tidak dikenal — pilih %s"
                     % (nama_berkas, pilar, ", ".join(URUT_PILAR)))
    if tahap not in TAHAP_SAH:
        galat.append("%s: tahap '%s' tidak dikenal — pilih %s"
                     % (nama_berkas, tahap, ", ".join(TAHAP_SAH)))


def muat_arsip(galat):
    """Baca daftar naskah asli dari konten/arsip.yml.

    Daftar kosong adalah keadaan yang sah — selama belum ada naskah resmi yang
    diunduh sendiri, memang tidak ada yang boleh diberi atribusi tahun dan nomor.
    Yang tidak sah adalah entri setengah terisi: tautan tanpa tahun, atau tahun
    tanpa penyelenggara, membuat naskahnya tidak bisa dikenali lagi begitu
    tautannya mati — dan tautan mati adalah satu-satunya risiko yang tersisa dari
    keputusan tidak menyimpan PDF.
    """
    if not ARSIP.exists():
        return {}
    try:
        isi = yaml.safe_load(ARSIP.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        galat.append("arsip.yml: tidak terbaca — %s" % e)
        return {}
    if not isinstance(isi, dict):
        galat.append("arsip.yml: isinya harus pasangan kunci-nilai")
        return {}

    hasil = {}
    for kunci, entri in sorted(isi.items()):
        if not isinstance(entri, dict):
            galat.append("arsip.yml: entri '%s' harus pasangan kunci-nilai" % kunci)
            continue
        hilang = [k for k in WAJIB_ARSIP if not entri.get(k)]
        if hilang:
            galat.append("arsip.yml: entri '%s' kurang %s" % (kunci, ", ".join(hilang)))
        if entri.get("tahap") and entri["tahap"] not in TAHAP_SAH:
            galat.append("arsip.yml: entri '%s' bertahap '%s' — pilih %s"
                         % (kunci, entri["tahap"], ", ".join(TAHAP_SAH)))
        tautan = str(entri.get("tautan") or "")
        if tautan and not tautan.startswith(("http://", "https://")):
            galat.append("arsip.yml: entri '%s' tautannya bukan alamat web — "
                         "tulis halaman resmi tempat naskahnya diunduh" % kunci)
        # Distringkan setelah diperiksa: 'diakses' terbaca YAML sebagai date, dan
        # json.dumps tidak bisa menuliskannya.
        hasil[kunci] = {k: str(v) for k, v in entri.items()}
    return hasil


def bangun_rajah(galat):
    """Jalankan tiap konten/rajah/*.py, kumpulkan SVG-nya — belum ditulis ke disk.

    Ditahan di memori dulu supaya mengikuti aturan main(): keluaran baru ditulis
    kalau seluruh pemeriksaan lolos. Kalau tidak, satu soal yang salah rujukan
    meninggalkan berkas SVG setengah jadi di pohon kerja.
    """
    if not RAJAH_SUMBER.exists():
        return {}

    hasil = {}
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    try:
        for jalur in sorted(RAJAH_SUMBER.glob("*.py")):
            try:
                spec = importlib.util.spec_from_file_location(
                    "rajah_" + jalur.stem, jalur)
                modul = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modul)
            except Exception as e:
                galat.append("rajah/%s: gagal dijalankan — %s: %s"
                             % (jalur.name, type(e).__name__, e))
                continue
            if not hasattr(modul, "RAJAH"):
                galat.append("rajah/%s: tidak menetapkan RAJAH" % jalur.name)
                continue
            try:
                hasil[jalur.stem + ".svg"] = modul.RAJAH.svg()
            except Exception as e:
                galat.append("rajah/%s: gagal dirender — %s: %s"
                             % (jalur.name, type(e).__name__, e))
    finally:
        sys.path.pop(0)
    return hasil


# Alt yang tidak menggantikan apa pun. Bagi siswa yang memakai pembaca layar,
# alt adalah satu-satunya isi soalnya — "gambar" memberitahunya bahwa ia sedang
# melewatkan sesuatu, tanpa memberitahu apa.
ALT_MALAS = frozenset((
    "gambar", "rajah", "ilustrasi", "diagram", "sketsa", "bangun", "gambarnya",
    "gambar geometri", "gambar soal", "lihat gambar",
))


def periksa_gambar(rajah, galat):
    """Periksa tiap ![alt](berkas) di seluruh konten; kembalikan yang terpakai.

    Dibaca ulang dari berkas mentahnya, bukan dari hasil markdown_ke_html: yang
    diperiksa justru hal-hal yang hilang setelah dirender — alt kosong sudah
    telanjur jadi atribut kosong, dan $ di dalam alt sudah telanjur diselamatkan
    lindungi_rumus() sebagai rumus yang tak akan pernah dirender KaTeX.
    """
    dipakai = set()
    for sub in ("jurus", "soal"):
        for jalur in sorted((KONTEN / sub).glob("*.md")):
            nama = "%s/%s" % (sub, jalur.name)
            for m in GAMBAR.finditer(jalur.read_text(encoding="utf-8")):
                alt, berkas = m.group(1).strip(), m.group(2).strip()

                if not berkas:
                    galat.append("%s: gambar tanpa nama berkas" % nama)
                elif "/" in berkas or "//" in berkas or ":" in berkas:
                    galat.append(
                        "%s: rujukan gambar '%s' memuat jalur atau alamat web — "
                        "tulis nama berkasnya saja. Gambar luar mematahkan latihan "
                        "offline, dan menyalinnya ke sini soal izin yang berbeda."
                        % (nama, berkas))
                elif not berkas.endswith(".svg"):
                    galat.append(
                        "%s: gambar '%s' bukan .svg — rajah geometri dibangkitkan "
                        "dari konten/rajah/*.py, lihat scripts/rajah.py"
                        % (nama, berkas))
                elif berkas not in rajah:
                    galat.append(
                        "%s: gambar '%s' tidak ada — buat dulu konten/rajah/%s.py"
                        % (nama, berkas, berkas[:-4]))
                else:
                    dipakai.add(berkas)

                if not alt:
                    galat.append(
                        "%s: gambar '%s' tanpa alt. Bagi siswa yang memakai pembaca "
                        "layar, alt itu satu-satunya isi soalnya — sebutkan bangunnya, "
                        "bukan bahwa ada gambar." % (nama, berkas or "?"))
                elif alt.lower().rstrip(".") in ALT_MALAS:
                    galat.append(
                        "%s: alt '%s' tidak menggantikan gambarnya — sebutkan titik, "
                        "sisi, dan hubungan yang terlihat di rajah itu" % (nama, alt))
                if "$" in alt:
                    galat.append(
                        "%s: alt '%s' memuat rumus. KaTeX tidak merender di dalam "
                        "atribut, jadi pembaca layar akan mengejanya sebagai 'dolar'. "
                        "Tulis dengan kata: 'sudut ABC', bukan '$\\angle ABC$'."
                        % (nama, alt))
    return dipakai


def muat_jurus(galat):
    hasil = {}
    for jalur in sorted((KONTEN / "jurus").glob("*.md")):
        try:
            depan, badan = baca_berkas(jalur)
        except GagalBuild as e:
            galat.append(str(e))
            continue

        hilang = [k for k in WAJIB_JURUS if not depan.get(k)]
        if hilang:
            galat.append("%s: frontmatter kurang %s" % (jalur.name, ", ".join(hilang)))
            continue

        jid = depan["id"]
        if jid != jalur.stem:
            galat.append("%s: id '%s' tidak sama dengan nama berkas" % (jalur.name, jid))
        if jid in hasil:
            galat.append("%s: id '%s' dipakai dua kali" % (jalur.name, jid))
            continue

        periksa_pilar_tahap(jalur.name, depan["pilar"], depan.get("tahap", "osn-k"), galat)

        bagian = belah_bagian(badan)
        hasil[jid] = {
            "id": jid,
            "nama": depan["nama"],
            "pilar": depan["pilar"],
            "tahap": depan.get("tahap", "osn-k"),
            "prasyarat": list(depan.get("prasyarat") or []),
            "contoh": list(depan.get("contoh") or []),
            "latihan": list(depan.get("latihan") or []),
            "kapan_dipakai": markdown_ke_html(bagian.get("kapan dipakai", "")),
            "inti": markdown_ke_html(bagian.get("intinya", "")),
            "jebakan": markdown_ke_html(bagian.get("jebakan umum", "")),
        }

        if not hasil[jid]["kapan_dipakai"]:
            galat.append("%s: bagian '## Kapan dipakai' kosong — itu bagian terpenting" % jalur.name)
    return hasil


def muat_soal(galat):
    hasil = {}
    for jalur in sorted((KONTEN / "soal").glob("*.md")):
        try:
            depan, badan = baca_berkas(jalur)
        except GagalBuild as e:
            galat.append(str(e))
            continue

        hilang = [k for k in WAJIB_SOAL if not depan.get(k)]
        if hilang:
            galat.append("%s: frontmatter kurang %s" % (jalur.name, ", ".join(hilang)))
            continue

        sid = depan["id"]
        if sid != jalur.stem:
            galat.append("%s: id '%s' tidak sama dengan nama berkas" % (jalur.name, sid))
        if sid in hasil:
            galat.append("%s: id '%s' dipakai dua kali" % (jalur.name, sid))
            continue

        bentuk = depan["bentuk"]
        if bentuk not in BENTUK_SAH:
            galat.append("%s: bentuk '%s' tidak dikenal — pilih %s"
                         % (jalur.name, bentuk, " atau ".join(BENTUK_SAH)))
            continue

        periksa_pilar_tahap(jalur.name, depan["pilar"], depan.get("tahap", "osn-k"), galat)

        bagian = belah_bagian(badan)
        jawaban = depan.get("jawaban")
        jawaban = "" if jawaban is None else str(jawaban)

        if bentuk == "isian" and not jawaban:
            galat.append("%s: soal isian wajib punya 'jawaban'" % jalur.name)

        butir_soal = markdown_ke_html(bagian.get("soal", ""))
        if not butir_soal:
            galat.append("%s: bagian '## Soal' kosong" % jalur.name)

        rubrik = bagian_jadi_daftar(bagian.get("rubrik", ""))
        if bentuk == "uraian" and not rubrik:
            galat.append("%s: soal uraian wajib punya '## Rubrik' untuk menilai sendiri" % jalur.name)

        hasil[sid] = {
            "id": sid,
            "sumber": depan["sumber"],
            # Kosong untuk soal susunan sendiri, yaitu hampir semuanya. Ikut ditulis
            # apa adanya seperti 'jawaban' dan 'rubrik' supaya bentuk datanya sama
            # untuk tiap soal.
            "arsip": str(depan.get("arsip") or ""),
            "nomor": str(depan.get("nomor") or ""),
            "pilar": depan["pilar"],
            "tahap": depan.get("tahap", "osn-k"),
            "jurus": list(depan.get("jurus") or []),
            "bentuk": bentuk,
            "kesulitan": int(depan.get("kesulitan", 2)),
            "soal": butir_soal,
            "jawaban": jawaban,
            "jawaban_alt": [str(x) for x in (depan.get("jawaban_alt") or [])],
            "petunjuk": bagian_jadi_daftar(bagian.get("petunjuk", "")),
            "pembahasan": markdown_ke_html(bagian.get("pembahasan", "")),
            "rubrik": rubrik,
        }
    return hasil


# ---------------------------------------------------------------- periksa & tata letak

def periksa(jurus, soal, galat):
    for j in jurus.values():
        for p in j["prasyarat"]:
            if p not in jurus:
                galat.append("jurus/%s.md: prasyarat '%s' tidak ada" % (j["id"], p))
        for s in j["contoh"] + j["latihan"]:
            if s not in soal:
                galat.append("jurus/%s.md: soal '%s' tidak ada" % (j["id"], s))
    for s in soal.values():
        if not s["jurus"]:
            galat.append("soal/%s.md: belum ditandai jurus apa pun" % s["id"])
        for j in s["jurus"]:
            if j not in jurus:
                galat.append("soal/%s.md: jurus '%s' tidak ada" % (s["id"], j))


def periksa_arsip(soal, arsip, galat):
    """Atribusi ke naskah asli wajib punya entri arsip yang sah.

    Begitu ada satu naskah asli di dalam situs, soal asli dan soal susunan sendiri
    duduk berdampingan — dan siswa tidak lagi bisa menganggap semuanya susunan
    sendiri. Justru di situ labelnya jadi genting: soal karangan berlabel
    'OSN 2015 nomor 3' sekarang terbaca sebagai naskah asli, karena naskah asli
    memang ada. Sebelum ada arsip.yml, aturan ini cuma bisa dititipkan ke ingatan;
    sekarang ada daftar untuk dicocokkan, jadi jadikan galat.
    """
    for s in sorted(soal.values(), key=lambda s: s["id"]):
        kunci = s.get("arsip", "")
        if kunci and kunci not in arsip:
            galat.append("soal/%s.md: arsip '%s' tidak terdaftar di konten/arsip.yml"
                         % (s["id"], kunci))
            continue
        if ATRIBUSI_NYATA.search(s["sumber"]) and not kunci:
            galat.append(
                "soal/%s.md: sumber '%s' berbunyi seperti atribusi ke naskah asli, "
                "tapi soalnya tidak punya 'arsip'. Kalau ini susunan sendiri, tulis "
                "begitu tanpa tahun; kalau naskahnya memang kamu unduh sendiri dari "
                "situs resmi, daftarkan dulu di konten/arsip.yml."
                % (s["id"], s["sumber"]))


def hitung_tingkat(jurus, galat):
    """tingkat = 0 kalau tanpa prasyarat, selain itu 1 + tingkat prasyarat terdalam."""
    memo = {}

    def tingkat(jid, jejak):
        if jid in memo:
            return memo[jid]
        if jid in jejak:
            rantai = " → ".join(list(jejak) + [jid])
            raise GagalBuild("prasyarat berputar: %s" % rantai)
        pra = [p for p in jurus[jid]["prasyarat"] if p in jurus]
        n = 0 if not pra else 1 + max(tingkat(p, jejak + [jid]) for p in pra)
        memo[jid] = n
        return n

    for jid in jurus:
        try:
            jurus[jid]["tingkat"] = tingkat(jid, [])
        except GagalBuild as e:
            galat.append(str(e))
            jurus[jid]["tingkat"] = 0
    return jurus


def tata_letak(jurus):
    """Beri koordinat x/y supaya peramban tinggal menggambar SVG — tanpa pustaka graf.

    Simpul dalam satu tingkat diurutkan menurut rata-rata posisi prasyaratnya
    (barycenter). Beberapa kali sapuan sudah cukup merapikan garis silang untuk
    peta sebesar ini.
    """
    per_pilar = {}
    for j in jurus.values():
        per_pilar.setdefault(j["pilar"], []).append(j)

    ukuran = {}
    for pilar, simpul in per_pilar.items():
        baris = {}
        for j in simpul:
            baris.setdefault(j["tingkat"], []).append(j)
        for t in baris:
            baris[t].sort(key=lambda j: j["nama"])

        posisi = {}
        for t in sorted(baris):
            for i, j in enumerate(baris[t]):
                posisi[j["id"]] = i

        for _ in range(4):
            for t in sorted(baris):
                if t == 0:
                    continue
                def berat(j):
                    pra = [posisi[p] for p in j["prasyarat"] if p in posisi]
                    return sum(pra) / len(pra) if pra else posisi[j["id"]]
                baris[t].sort(key=berat)
                for i, j in enumerate(baris[t]):
                    posisi[j["id"]] = i

        terlebar = max(len(v) for v in baris.values())
        lebar_total = terlebar * LEBAR_SIMPUL + (terlebar - 1) * JARAK_X

        for t, deret in baris.items():
            lebar_baris = len(deret) * LEBAR_SIMPUL + (len(deret) - 1) * JARAK_X
            geser = (lebar_total - lebar_baris) / 2
            for i, j in enumerate(deret):
                j["x"] = round(TEPI + geser + i * (LEBAR_SIMPUL + JARAK_X))
                j["y"] = TEPI + t * TINGGI_BARIS

        ukuran[pilar] = {
            "lebar": lebar_total + TEPI * 2,
            "tinggi": tinggi_untuk(max(baris)),
            # Tinggi SVG kalau saringan tahap dipasang. Dihitung di sini, bukan di
            # peramban: kalau peta.js menghitungnya sendiri ia harus menyalin
            # TINGGI_BARIS dan TEPI, dan konstanta tata letak yang tersalin di dua
            # tempat adalah persis jebakan yang sudah kita punya satu.
            "tinggi_sampai": tinggi_per_tahap(simpul),
        }
    return ukuran


def tinggi_untuk(tingkat_terdalam):
    return (tingkat_terdalam + 1) * TINGGI_BARIS + TEPI * 2


def tinggi_per_tahap(simpul):
    """Tinggi SVG untuk tiap batas tahap, memakai posisi y yang sudah ditetapkan.

    Menyaring tahap hanya menyembunyikan simpul — koordinat yang lain tidak
    bergeser sedikit pun. Yang berubah cuma sampai baris ke berapa petanya perlu
    digambar, dan itu yang dihitung di sini. Pilar yang belum punya jurus sama
    sekali untuk suatu tahap diberi 0, dan peta.js menampilkan pesan kosong.
    """
    hasil = {}
    for batas in TAHAP_SAH:
        tampak = [j for j in simpul if urutan_tahap(j.get("tahap")) <= urutan_tahap(batas)]
        hasil[batas] = tinggi_untuk(max(j["tingkat"] for j in tampak)) if tampak else 0
    return hasil


def urutan_tahap(tahap):
    """Tahap tak dikenal dianggap paling awal — tata letak tidak boleh meledak
    karena data uji yang tidak menyertakan tahap."""
    return TAHAP_SAH.index(tahap) if tahap in TAHAP_SAH else 0


# ---------------------------------------------------------------- utama

def tulis_rajah(rajah):
    """Tulis SVG yang berubah saja, dan buang yang sumbernya sudah tidak ada.

    Menulis ulang berkas yang isinya sama membuat git menandainya berubah setiap
    build — dan alur GitHub Actions mengomit balik hasil build, jadi itu berarti
    komit kosong pada tiap dorongan.
    """
    RAJAH_KELUAR.mkdir(parents=True, exist_ok=True)
    for nama, isi in sorted(rajah.items()):
        berkas = RAJAH_KELUAR / nama
        if not berkas.exists() or berkas.read_text(encoding="utf-8") != isi:
            berkas.write_text(isi, encoding="utf-8")
    for berkas in RAJAH_KELUAR.glob("*.svg"):
        if berkas.name not in rajah:
            berkas.unlink()


def main():
    galat = []
    arsip = muat_arsip(galat)
    rajah = bangun_rajah(galat)
    jurus = muat_jurus(galat)
    soal = muat_soal(galat)
    periksa(jurus, soal, galat)
    periksa_arsip(soal, arsip, galat)
    dipakai_rajah = periksa_gambar(rajah, galat)
    hitung_tingkat(jurus, galat)

    if galat:
        print("Build gagal — %d masalah:\n" % len(galat), file=sys.stderr)
        for g in galat:
            print("  • %s" % g, file=sys.stderr)
        return 1

    ukuran = tata_letak(jurus)
    DATA.mkdir(exist_ok=True)
    tulis_rajah(rajah)

    (DATA / "jurus.json").write_text(
        json.dumps(
            {
                "ukuran": ukuran,
                # Daftar rajah yang benar-benar dirujuk konten. Ikut di sini karena
                # sw.js-lah yang membutuhkannya — ia menurunkan daftar berkas untuk
                # diambil di latar dari jurus.json, pola yang sama dengan berkasSoal().
                # Ditulis mesin supaya rajah baru tidak pernah terlupa dari cache.
                "rajah": sorted(dipakai_rajah),
                # Ikut di jurus.json, bukan berkas sendiri: daftarnya beberapa ratus
                # bita dan selalu dibutuhkan bersama soal mana pun yang menyebutnya,
                # jadi berkas terpisah cuma menambah satu permintaan jaringan.
                "arsip": arsip,
                # Urutan simpul di sini yang menentukan urutan bidang di halaman
                # peta: inti.js menyusun urutJurus dari daftar ini, dan peta.js
                # mengelompokkannya lewat Object.keys tanpa mengurutkan ulang.
                "simpul": sorted(
                    jurus.values(),
                    key=lambda j: (URUT_PILAR.index(j["pilar"]), j["tingkat"], j["x"]),
                ),
            },
            ensure_ascii=False,
            indent=1,
        ) + "\n",
        encoding="utf-8",
    )
    # Soal dipecah per bidang, bukan satu berkas besar. Halaman menyatakan bidang apa
    # yang dipakainya lewat Inti.muatData, jadi jurus.html tidak lagi mengunduh soal
    # bidang lain. Berkas lama data/soal.json sengaja dihapus supaya tidak ada dua
    # sumber kebenaran yang bisa berbeda diam-diam.
    lama = DATA / "soal.json"
    if lama.exists():
        lama.unlink()

    per_pilar = {}
    for s in soal.values():
        per_pilar.setdefault(s["pilar"], []).append(s)

    for pilar in URUT_PILAR:
        berkas = DATA / ("soal-%s.json" % pilar)
        isi = sorted(per_pilar.get(pilar, []), key=lambda s: s["id"])
        if not isi:
            # Bidang tanpa soal tidak diberi berkas; peramban memang tidak akan memintanya.
            if berkas.exists():
                berkas.unlink()
            continue
        berkas.write_text(
            json.dumps({"soal": isi}, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )

    tanpa_latihan = [j["id"] for j in jurus.values() if not j["latihan"]]
    print("Selesai. %d jurus, %d soal, %d rajah." % (len(jurus), len(soal), len(rajah)))
    if tanpa_latihan:
        print("Belum ada latihan di: %s" % ", ".join(sorted(tanpa_latihan)))
    # Peringatan, bukan galat: saat menulis geometri, wajar rajahnya jadi lebih
    # dulu daripada soal yang memakainya. Yang tidak wajar adalah lupa.
    nganggur = sorted(set(rajah) - dipakai_rajah)
    if nganggur:
        print("Rajah belum dirujuk konten mana pun: %s" % ", ".join(nganggur))
    return 0


if __name__ == "__main__":
    sys.exit(main())
