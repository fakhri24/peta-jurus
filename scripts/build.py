#!/usr/bin/env python3
"""Ubah tulisan di konten/ menjadi data/jurus.json dan data/soal.json.

Jalankan dari akar proyek:

    python3 scripts/build.py

Skrip ini hanya butuh PyYAML. Markdown-nya ditangani sendiri (lihat markdown_ke_html)
karena rumus LaTeX harus dilindungi lebih dulu — pustaka Markdown umum akan merusak
$a_1$ jadi huruf miring dan menelan garis miring ganda di dalam align.
"""

import html
import json
import re
import sys
from pathlib import Path

import yaml

AKAR = Path(__file__).resolve().parent.parent
KONTEN = AKAR / "konten"
DATA = AKAR / "data"

# Tata letak peta: tingkat jadi baris, dari atas ke bawah.
LEBAR_SIMPUL = 168
JARAK_X = 28
TINGGI_BARIS = 112
TEPI = 24


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


def _sebaris(teks):
    """Aturan Markdown dalam satu baris. Teks masuk sudah di-escape."""
    teks = re.sub(r"`([^`]+)`", r"<code>\1</code>", teks)
    teks = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', teks)
    teks = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", teks)
    teks = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", teks)
    teks = re.sub(r"(?<!\w)_([^_\n]+)_(?!\w)", r"<em>\1</em>", teks)
    return teks


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
            "tinggi": (max(baris) + 1) * TINGGI_BARIS + TEPI * 2,
        }
    return ukuran


# ---------------------------------------------------------------- utama

def main():
    galat = []
    jurus = muat_jurus(galat)
    soal = muat_soal(galat)
    periksa(jurus, soal, galat)
    hitung_tingkat(jurus, galat)

    if galat:
        print("Build gagal — %d masalah:\n" % len(galat), file=sys.stderr)
        for g in galat:
            print("  • %s" % g, file=sys.stderr)
        return 1

    ukuran = tata_letak(jurus)
    DATA.mkdir(exist_ok=True)

    (DATA / "jurus.json").write_text(
        json.dumps(
            {
                "ukuran": ukuran,
                "simpul": sorted(jurus.values(), key=lambda j: (j["pilar"], j["tingkat"], j["x"])),
            },
            ensure_ascii=False,
            indent=1,
        ) + "\n",
        encoding="utf-8",
    )
    (DATA / "soal.json").write_text(
        json.dumps(
            {"soal": sorted(soal.values(), key=lambda s: s["id"])},
            ensure_ascii=False,
            indent=1,
        ) + "\n",
        encoding="utf-8",
    )

    tanpa_latihan = [j["id"] for j in jurus.values() if not j["latihan"]]
    print("Selesai. %d jurus, %d soal." % (len(jurus), len(soal)))
    if tanpa_latihan:
        print("Belum ada latihan di: %s" % ", ".join(sorted(tanpa_latihan)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
