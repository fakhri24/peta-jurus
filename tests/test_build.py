#!/usr/bin/env python3
"""Tes untuk scripts/build.py — jalankan: python3 tests/test_build.py

Yang paling perlu dijaga adalah rumus LaTeX. Aturan Markdown dan LaTeX memakai
tanda yang sama (_ * \\ &), jadi setiap perubahan di markdown_ke_html harus
dibuktikan tidak merusak rumus.
"""

import sys
import json
import math
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build  # noqa: E402


class TestRumusSelamat(unittest.TestCase):
    """Rumus tidak boleh disentuh aturan Markdown."""

    def test_garis_bawah_bukan_huruf_miring(self):
        h = build.markdown_ke_html("Ambil $a_1 + a_2$ saja.")
        self.assertIn("$a_1 + a_2$", h)
        self.assertNotIn("<em>", h)

    def test_bintang_di_dalam_rumus_utuh(self):
        h = build.markdown_ke_html("Hasilnya $a * b * c$ tetap.")
        self.assertIn("$a * b * c$", h)
        self.assertNotIn("<em>", h)

    def test_align_dengan_ampersand_dan_garis_miring_ganda(self):
        sumber = r"$$\begin{align} a &= b \\ c &= d \end{align}$$"
        h = build.markdown_ke_html(sumber)
        # & jadi &amp; di HTML, tapi textContent mengembalikannya jadi & untuk KaTeX.
        self.assertIn("&amp;= b", h)
        self.assertIn(r"\\", h)
        self.assertIn(r"\begin{align}", h)

    def test_kurang_dari_diescape_agar_bukan_tag(self):
        h = build.markdown_ke_html("Karena $a < b$ maka selesai.")
        self.assertIn("$a &lt; b$", h)
        self.assertNotIn("$a < b$", h)

    def test_rumus_blok_lintas_baris(self):
        sumber = "Perhatikan:\n\n$$\nx^2 + y^2\n= z^2\n$$\n\nSelesai."
        h = build.markdown_ke_html(sumber)
        self.assertIn("x^2 + y^2", h)
        self.assertIn("= z^2", h)

    def test_dua_rumus_sebaris_tidak_saling_makan(self):
        # Kalau pencocokannya serakah, 'dan' ikut tertelan jadi satu rumus panjang.
        h = build.markdown_ke_html("Ada $a$ dan $b$ di sini.")
        self.assertEqual(h, "<p>Ada $a$ dan $b$ di sini.</p>")

    def test_rumus_di_dalam_butir_daftar(self):
        h = build.markdown_ke_html("- pertama $n_1$\n- kedua $n_2$")
        self.assertIn("<li>pertama $n_1$</li>", h)
        self.assertIn("<li>kedua $n_2$</li>", h)


class TestMarkdown(unittest.TestCase):
    def test_paragraf(self):
        self.assertEqual(build.markdown_ke_html("Halo dunia."), "<p>Halo dunia.</p>")

    def test_baris_berdempet_jadi_satu_paragraf(self):
        self.assertEqual(build.markdown_ke_html("satu\ndua"), "<p>satu dua</p>")

    def test_paragraf_terpisah_baris_kosong(self):
        self.assertEqual(build.markdown_ke_html("satu\n\ndua"), "<p>satu</p><p>dua</p>")

    def test_tebal_dan_miring(self):
        h = build.markdown_ke_html("ini **tebal** dan *miring*")
        self.assertIn("<strong>tebal</strong>", h)
        self.assertIn("<em>miring</em>", h)

    def test_kode_sebaris(self):
        self.assertIn("<code>n mod 3</code>", build.markdown_ke_html("pakai `n mod 3`"))

    def test_judul_dua_pagar_jadi_h3(self):
        self.assertEqual(build.markdown_ke_html("## Intinya"), "<h3>Intinya</h3>")

    def test_daftar_tak_berurut(self):
        self.assertEqual(build.markdown_ke_html("- a\n- b"), "<ul><li>a</li><li>b</li></ul>")

    def test_daftar_berurut(self):
        self.assertEqual(build.markdown_ke_html("1. a\n2. b"), "<ol><li>a</li><li>b</li></ol>")

    def test_baris_lanjutan_tetap_di_dalam_li(self):
        # Butir panjang biasanya ditulis menyambung dengan indentasi. Kalau
        # lanjutannya terlempar keluar <li>, daftarnya patah di halaman.
        h = build.markdown_ke_html("- awal butir\n  lanjutan butir\n- butir dua")
        self.assertEqual(h, "<ul><li>awal butir lanjutan butir</li><li>butir dua</li></ul>")

    def test_daftar_berurut_juga_menyambung(self):
        h = build.markdown_ke_html("1. awal\n   sambungan\n2. dua")
        self.assertEqual(h, "<ol><li>awal sambungan</li><li>dua</li></ol>")

    def test_baris_kosong_mengakhiri_daftar(self):
        h = build.markdown_ke_html("- a\n- b\n\nparagraf lepas")
        self.assertEqual(h, "<ul><li>a</li><li>b</li></ul><p>paragraf lepas</p>")

    def test_tabel(self):
        h = build.markdown_ke_html("| a | b |\n|---|---|\n| 1 | 2 |")
        self.assertEqual(
            h,
            "<table><thead><tr><th>a</th><th>b</th></tr></thead>"
            "<tbody><tr><td>1</td><td>2</td></tr></tbody></table>",
        )

    def test_tabel_boleh_berisi_rumus(self):
        h = build.markdown_ke_html("| bentuk | nilai |\n|---|---|\n| $x^2$ | $0, 1$ |")
        self.assertIn("<td>$x^2$</td>", h)

    def test_pipa_tanpa_baris_pemisah_bukan_tabel(self):
        # Kalimat biasa yang kebetulan memuat pipa tidak boleh berubah jadi tabel.
        h = build.markdown_ke_html("| ini bukan tabel")
        self.assertNotIn("<table>", h)

    def test_kutipan(self):
        self.assertEqual(build.markdown_ke_html("> catat ini"), "<blockquote><p>catat ini</p></blockquote>")

    def test_tautan(self):
        h = build.markdown_ke_html("lihat [arsip](https://contoh.id/a)")
        self.assertIn('<a href="https://contoh.id/a">arsip</a>', h)

    def test_prosa_diescape(self):
        h = build.markdown_ke_html("kalau 2 < 3 & 4 > 1")
        self.assertIn("&lt;", h)
        self.assertIn("&amp;", h)
        self.assertNotIn("< 3", h)

    def test_kosong(self):
        self.assertEqual(build.markdown_ke_html(""), "")
        self.assertEqual(build.markdown_ke_html("   \n  "), "")


class TestBagian(unittest.TestCase):
    def test_belah_menurut_judul(self):
        bagian = build.belah_bagian("\n## Soal\nisi soal\n\n## Pembahasan\nisi bahas\n")
        self.assertEqual(bagian["soal"], "isi soal")
        self.assertEqual(bagian["pembahasan"], "isi bahas")

    def test_daftar_petunjuk_jadi_array(self):
        d = build.bagian_jadi_daftar("- satu\n- dua\n- tiga")
        self.assertEqual(d, ["satu", "dua", "tiga"])

    def test_baris_lanjutan_menempel_ke_butir_di_atasnya(self):
        d = build.bagian_jadi_daftar("- satu\n  masih satu\n- dua")
        self.assertEqual(d, ["satu masih satu", "dua"])

    def test_butir_petunjuk_tidak_dibungkus_p(self):
        d = build.bagian_jadi_daftar("- pakai $2^{12}$")
        self.assertEqual(d, ["pakai $2^{12}$"])


class TestTingkatDanTataLetak(unittest.TestCase):
    @staticmethod
    def _jurus(*pasangan):
        return {
            jid: {"id": jid, "nama": jid, "pilar": "uji", "prasyarat": list(pra)}
            for jid, pra in pasangan
        }

    def test_tanpa_prasyarat_tingkat_nol(self):
        galat = []
        j = build.hitung_tingkat(self._jurus(("a", [])), galat)
        self.assertEqual(galat, [])
        self.assertEqual(j["a"]["tingkat"], 0)

    def test_tingkat_ikut_prasyarat_terdalam(self):
        galat = []
        j = build.hitung_tingkat(
            self._jurus(("a", []), ("b", ["a"]), ("c", ["a"]), ("d", ["b", "c"])), galat
        )
        self.assertEqual(galat, [])
        self.assertEqual([j["a"]["tingkat"], j["b"]["tingkat"], j["d"]["tingkat"]], [0, 1, 2])

    def test_rantai_panjang_menang_atas_jalan_pintas(self):
        galat = []
        j = build.hitung_tingkat(
            self._jurus(("a", []), ("b", ["a"]), ("c", ["b"]), ("d", ["a", "c"])), galat
        )
        self.assertEqual(j["d"]["tingkat"], 3)

    def test_siklus_ketahuan(self):
        galat = []
        build.hitung_tingkat(self._jurus(("a", ["b"]), ("b", ["a"])), galat)
        self.assertTrue(galat)
        self.assertIn("berputar", galat[0])

    def test_koordinat_terisi_dan_tingkat_menurun(self):
        galat = []
        j = build.hitung_tingkat(self._jurus(("a", []), ("b", ["a"])), galat)
        build.tata_letak(j)
        self.assertEqual(j["a"]["y"], build.TEPI)
        self.assertGreater(j["b"]["y"], j["a"]["y"])
        self.assertIsInstance(j["a"]["x"], int)


class TestUrutanPilar(unittest.TestCase):
    """Urutan bidang di peta ditetapkan URUT_PILAR, bukan abjad slug."""

    def test_teori_bilangan_mendahului_aljabar(self):
        # Kalau urutannya jatuh ke abjad, 'aljabar' akan menang karena huruf a —
        # dan teori bilangan, satu-satunya bidang yang isinya lengkap, terlempar
        # ke dasar halaman.
        urut = [build.URUT_PILAR.index(p) for p in ("teori-bilangan", "aljabar")]
        self.assertLess(urut[0], urut[1])

    def test_semua_pilar_di_nama_pilar_peramban(self):
        # peta.js dan jurus.js memetakan slug jadi judul. Slug yang tidak ada di
        # sana tampil mentah, jadi keduanya harus memuat seluruh URUT_PILAR.
        for berkas in ("peta.js", "jurus.js"):
            isi = (build.AKAR / "assets" / berkas).read_text(encoding="utf-8")
            for pilar in build.URUT_PILAR:
                self.assertIn("'%s'" % pilar, isi, "%s belum kenal '%s'" % (berkas, pilar))


class TestPilarTahapSah(unittest.TestCase):
    def test_pilar_salah_ketik_ketahuan(self):
        galat = []
        build.periksa_pilar_tahap("x.md", "teori-bilanga", "osn-k", galat)
        self.assertTrue(any("tidak dikenal" in g for g in galat))

    def test_tahap_salah_ketik_ketahuan(self):
        galat = []
        build.periksa_pilar_tahap("x.md", "aljabar", "osnp", galat)
        self.assertTrue(any("osnp" in g for g in galat))

    def test_yang_sah_lolos(self):
        galat = []
        build.periksa_pilar_tahap("x.md", "geometri", "osn", galat)
        self.assertEqual(galat, [])


class TestTinggiPerTahap(unittest.TestCase):
    """Tinggi SVG untuk tiap batas tahap dihitung saat build, bukan di peramban."""

    @staticmethod
    def _simpul(*pasangan):
        return [{"tingkat": t, "tahap": tahap} for t, tahap in pasangan]

    def test_batas_awal_memotong_baris_bawah(self):
        h = build.tinggi_per_tahap(self._simpul((0, "osn-k"), (3, "osn")))
        self.assertLess(h["osn-k"], h["osn"])
        self.assertEqual(h["osn-k"], build.tinggi_untuk(0))
        self.assertEqual(h["osn"], build.tinggi_untuk(3))

    def test_tahap_menengah_ikut_membawa_yang_lebih_awal(self):
        # Siswa yang menyiapkan OSN-P tetap perlu melihat jurus OSN-K.
        h = build.tinggi_per_tahap(self._simpul((0, "osn-k"), (2, "osn-p"), (5, "osn")))
        self.assertEqual(h["osn-p"], build.tinggi_untuk(2))

    def test_pilar_tanpa_jurus_untuk_tahap_itu_bertinggi_nol(self):
        h = build.tinggi_per_tahap(self._simpul((4, "osn")))
        self.assertEqual(h["osn-k"], 0)
        self.assertEqual(h["osn-p"], 0)

    def test_tata_letak_menyertakan_tinggi_sampai(self):
        galat = []
        j = build.hitung_tingkat(
            {
                "a": {"id": "a", "nama": "a", "pilar": "aljabar", "tahap": "osn-k", "prasyarat": []},
                "b": {"id": "b", "nama": "b", "pilar": "aljabar", "tahap": "osn", "prasyarat": ["a"]},
            },
            galat,
        )
        ukuran = build.tata_letak(j)
        self.assertEqual(galat, [])
        self.assertEqual(ukuran["aljabar"]["tinggi_sampai"]["osn-k"], build.tinggi_untuk(0))
        self.assertEqual(ukuran["aljabar"]["tinggi_sampai"]["osn"], ukuran["aljabar"]["tinggi"])


class TestPecahSoalPerBidang(unittest.TestCase):
    """Soal dipecah per bidang; berkas gabungan lama tidak boleh tertinggal."""

    def test_berkas_gabungan_lama_tidak_ada(self):
        # Dua sumber kebenaran yang bisa berbeda diam-diam lebih berbahaya daripada
        # satu berkas besar, jadi build.py menghapusnya.
        self.assertFalse((build.DATA / "soal.json").exists())

    def test_ada_berkas_per_bidang_yang_terisi(self):
        ada = [p for p in build.DATA.glob("soal-*.json")]
        self.assertTrue(ada, "tidak ada data/soal-<pilar>.json sama sekali")
        for berkas in ada:
            pilar = berkas.stem[len("soal-"):]
            self.assertIn(pilar, build.URUT_PILAR)

    def test_tiap_soal_terdaftar_di_jurus_sebidang(self):
        # Peta soal->bidang di inti.js diturunkan dari daftar contoh/latihan tiap
        # jurus, bukan dari berkas terpisah. Kalau ada soal yang tidak terdaftar,
        # halaman yang bertolak dari id soal tidak akan tahu bidang mana yang dimuat.
        jurus = json.loads((build.DATA / "jurus.json").read_text(encoding="utf-8"))
        terdaftar = {}
        for j in jurus["simpul"]:
            for sid in j["contoh"] + j["latihan"]:
                terdaftar.setdefault(sid, set()).add(j["pilar"])

        for berkas in build.DATA.glob("soal-*.json"):
            pilar = berkas.stem[len("soal-"):]
            for s in json.loads(berkas.read_text(encoding="utf-8"))["soal"]:
                self.assertIn(s["id"], terdaftar, "%s tidak terdaftar di jurus mana pun" % s["id"])
                self.assertEqual(terdaftar[s["id"]], {pilar}, "%s terdaftar lintas bidang" % s["id"])


class TestPeriksa(unittest.TestCase):
    def test_prasyarat_hantu_ketahuan(self):
        galat = []
        build.periksa({"a": {"id": "a", "prasyarat": ["tidakada"], "contoh": [], "latihan": []}}, {}, galat)
        self.assertTrue(any("tidakada" in g for g in galat))

    def test_soal_rujukan_hantu_ketahuan(self):
        galat = []
        build.periksa({"a": {"id": "a", "prasyarat": [], "contoh": [], "latihan": ["s9"]}}, {}, galat)
        self.assertTrue(any("s9" in g for g in galat))

    def test_soal_tanpa_jurus_ketahuan(self):
        galat = []
        build.periksa({}, {"s1": {"id": "s1", "jurus": []}}, galat)
        self.assertTrue(any("belum ditandai" in g for g in galat))

    def test_soal_menunjuk_jurus_hantu(self):
        galat = []
        build.periksa({}, {"s1": {"id": "s1", "jurus": ["x"]}}, galat)
        self.assertTrue(any("'x' tidak ada" in g for g in galat))


class TestTahapPrasyarat(unittest.TestCase):
    def test_prasyarat_tidak_boleh_dari_tahap_yang_lebih_akhir(self):
        """Jurus OSN-K tidak boleh berprasyarat jurus OSN-P atau OSN.

        Saringan tahap hanya menyembunyikan simpul. Kalau jurus OSN-K
        berprasyarat jurus OSN-P, siswa yang menyaring petanya ke OSN-K melihat
        gembok yang penyebabnya tidak ada di layar — dan tidak ada cara membukanya
        tanpa keluar dari tahap yang sedang ia siapkan. Artinya jurus itu memang
        bukan OSN-K, apa pun label yang diberikan padanya.
        """
        jurus = json.loads((build.DATA / "jurus.json").read_text(encoding="utf-8"))
        tahap = {j["id"]: j["tahap"] for j in jurus["simpul"]}
        for j in jurus["simpul"]:
            for p in j["prasyarat"]:
                self.assertLessEqual(
                    build.TAHAP_SAH.index(tahap[p]), build.TAHAP_SAH.index(j["tahap"]),
                    "%s (%s) berprasyarat %s yang bertahap lebih akhir (%s)"
                    % (j["id"], j["tahap"], p, tahap[p]))


class TestArsip(unittest.TestCase):
    """Atribusi ke naskah asli harus bisa dicocokkan ke entri yang nyata.

    Aturan ini tadinya cuma ada di CLAUDE.md, artinya cuma dijaga ingatan. Yang
    dijaga di sini justru kasus yang paling mudah lolos: soal karangan yang diberi
    label tahun dan nomor, yang terbaca sebagai naskah asli begitu naskah asli
    memang ada di situs.
    """

    SATU_ENTRI = {"osn-2025": {"judul": "OSN Matematika SMA 2025"}}

    @staticmethod
    def _soal(sumber, arsip=""):
        return {"s1": {"id": "s1", "sumber": sumber, "arsip": arsip}}

    def test_atribusi_tahun_tanpa_arsip_ditolak(self):
        galat = []
        build.periksa_arsip(self._soal("OSN 2025 nomor 3"), {}, galat)
        self.assertTrue(any("arsip" in g for g in galat), galat)

    def test_atribusi_tahun_dengan_arsip_sah_lolos(self):
        galat = []
        build.periksa_arsip(self._soal("OSN 2025 nomor 3", "osn-2025"), self.SATU_ENTRI, galat)
        self.assertEqual(galat, [])

    def test_arsip_yang_tidak_terdaftar_ketahuan(self):
        galat = []
        build.periksa_arsip(self._soal("OSN 2025 nomor 3", "osn-1998"), self.SATU_ENTRI, galat)
        self.assertTrue(any("osn-1998" in g for g in galat), galat)

    def test_susunan_sendiri_tidak_ikut_tertangkap(self):
        # Menyebut nama lombanya boleh; yang dijaga adalah klaim tahunnya.
        galat = []
        build.periksa_arsip(self._soal("Latihan 1 — susunan sendiri, gaya OSN-K"), {}, galat)
        self.assertEqual(galat, [])

    def test_tahun_jauh_dari_nama_lomba_bukan_atribusi(self):
        galat = []
        build.periksa_arsip(self._soal("Latihan 2024 — susunan sendiri, gaya OSN"), {}, galat)
        self.assertEqual(galat, [])

    def test_soal_sungguhan_tidak_ada_yang_mengaku_naskah_asli(self):
        # Penjaga atas isi nyata, bukan atas data uji: kalau suatu saat ada soal
        # berlabel tahun+nomor tanpa entri arsip, tes ini yang lebih dulu berbunyi.
        galat = []
        arsip = build.muat_arsip(galat)
        soal = {}
        for berkas in build.DATA.glob("soal-*.json"):
            for s in json.loads(berkas.read_text(encoding="utf-8"))["soal"]:
                soal[s["id"]] = s
        build.periksa_arsip(soal, arsip, galat)
        self.assertEqual(galat, [])


class TestMuatArsip(unittest.TestCase):
    """Entri setengah terisi ditolak: tautan mati adalah satu-satunya risiko yang
    tersisa dari tidak menyimpan PDF, dan metadata lengkap yang menutupnya."""

    def _muat(self, teks):
        import tempfile
        galat = []
        with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False,
                                         encoding="utf-8") as f:
            f.write(teks)
            sementara = Path(f.name)
        asli = build.ARSIP
        build.ARSIP = sementara
        try:
            hasil = build.muat_arsip(galat)
        finally:
            build.ARSIP = asli
            sementara.unlink()
        return hasil, galat

    LENGKAP = (
        "osn-2025:\n"
        "  judul: OSN Matematika SMA 2025\n"
        "  penyelenggara: Puspresnas/BPTI\n"
        "  tahun: 2025\n"
        "  tahap: osn\n"
        "  tautan: https://contoh.id/naskah\n"
        "  diakses: 2026-08-09\n"
    )

    def test_entri_lengkap_lolos(self):
        hasil, galat = self._muat(self.LENGKAP)
        self.assertEqual(galat, [])
        self.assertEqual(hasil["osn-2025"]["tahun"], "2025")

    def test_tanggal_jadi_teks_agar_bisa_ditulis_json(self):
        # YAML membaca 'diakses' sebagai date, dan json.dumps tidak bisa menuliskannya.
        hasil, _ = self._muat(self.LENGKAP)
        json.dumps(hasil)
        self.assertEqual(hasil["osn-2025"]["diakses"], "2026-08-09")

    def test_kunci_yang_kurang_ketahuan(self):
        _, galat = self._muat("osn-2025:\n  judul: OSN 2025\n")
        self.assertTrue(any("kurang" in g for g in galat), galat)
        for k in ("penyelenggara", "tahun", "tahap", "tautan", "diakses"):
            self.assertIn(k, galat[0])

    def test_tahap_salah_ketik_ketahuan(self):
        _, galat = self._muat(self.LENGKAP.replace("tahap: osn", "tahap: nasional"))
        self.assertTrue(any("nasional" in g for g in galat), galat)

    def test_tautan_bukan_alamat_web_ketahuan(self):
        _, galat = self._muat(self.LENGKAP.replace("https://contoh.id/naskah", "naskah.pdf"))
        self.assertTrue(any("alamat web" in g for g in galat), galat)

    def test_berkas_kosong_sah(self):
        # Selama belum ada naskah resmi yang diunduh sendiri, kosong itu benar.
        hasil, galat = self._muat("# cuma komentar\n")
        self.assertEqual((hasil, galat), ({}, []))


class TestGambarMarkdown(unittest.TestCase):
    """Gambar dan rumus memperebutkan berkas yang sama seperti Markdown dan LaTeX.

    Yang dijaga di sini terutama satu hal: alt bukan HTML. Aturan penekanan dan
    tautan berjalan setelah <img> dirakit, jadi tanpa perlindungan mereka menggigit
    ke dalam atributnya — dan pembaca layar mengeja apa pun yang ada di sana apa
    adanya.
    """

    def test_gambar_jadi_img_bukan_tautan_bertanda_seru(self):
        # Inti Fase 4.1: pola tautan menangkap [alt](url) lebih dulu dan
        # meninggalkan '!' nyasar. Bukan galat, hanya halaman yang salah.
        h = build.markdown_ke_html("![Segitiga ABC](abc.svg)")
        self.assertIn('<img src="assets/rajah/abc.svg" alt="Segitiga ABC">', h)
        self.assertNotIn("!<a", h)
        self.assertNotIn("<a href", h)

    def test_tautan_biasa_tidak_ikut_berubah(self):
        h = build.markdown_ke_html("[arsip](https://contoh.id)")
        self.assertIn('<a href="https://contoh.id">arsip</a>', h)
        self.assertNotIn("<img", h)

    def test_penekanan_tidak_masuk_ke_dalam_alt(self):
        h = build.markdown_ke_html("![Bangun *miring* dan _garis_](a.svg)")
        self.assertIn('alt="Bangun *miring* dan _garis_"', h)
        self.assertNotIn("<em>", h)

    def test_penekanan_di_luar_gambar_tetap_bekerja(self):
        h = build.markdown_ke_html("**tebal** lalu ![Lingkaran O](o.svg) lalu *miring*")
        self.assertIn("<strong>tebal</strong>", h)
        self.assertIn("<em>miring</em>", h)
        self.assertIn('alt="Lingkaran O"', h)

    def test_kutip_ganda_di_alt_tidak_menjebol_atribut(self):
        # html.escape dipanggil dengan quote=False, jadi " sampai ke sini utuh.
        h = build.markdown_ke_html('![Titik "istimewa" ABC](a.svg)')
        self.assertIn('alt="Titik &quot;istimewa&quot; ABC"', h)

    def test_rumus_di_sebelah_gambar_selamat(self):
        h = build.markdown_ke_html(r"![Segitiga ABC](a.svg) dengan $\angle A = 90^\circ$")
        self.assertIn('<img src="assets/rajah/a.svg" alt="Segitiga ABC">', h)
        self.assertIn(r"$\angle A = 90^\circ$", h)

    def test_gambar_di_dalam_daftar_dan_tabel(self):
        h = build.markdown_ke_html("- ![Lingkaran O](o.svg) berjari-jari $r$")
        self.assertIn("<li><img src=", h)
        self.assertIn("$r$", h)
        h = build.markdown_ke_html("| Rajah |\n|---|\n| ![Segitiga ABC](a.svg) |")
        self.assertIn("<td><img src=", h)

    def test_nama_berkas_diberi_awalan_di_satu_tempat(self):
        # Penulis soal menulis nama berkas telanjang; letaknya urusan build.
        self.assertTrue(build.AWALAN_RAJAH.endswith("/"))
        h = build.markdown_ke_html("![Segitiga ABC](a.svg)")
        self.assertIn('src="%sa.svg"' % build.AWALAN_RAJAH, h)


class TestPeriksaGambar(unittest.TestCase):
    """Rujukan gambar diperiksa mesin, seperti prasyarat dan rujukan soal."""

    def _periksa(self, badan, rajah=("abc.svg",)):
        import shutil
        import tempfile
        sementara = Path(tempfile.mkdtemp())
        (sementara / "jurus").mkdir()
        (sementara / "soal").mkdir()
        (sementara / "soal" / "uji.md").write_text(
            "---\nid: uji\n---\n## Soal\n" + badan + "\n", encoding="utf-8")
        asli = build.KONTEN
        build.KONTEN = sementara
        galat = []
        try:
            dipakai = build.periksa_gambar({n: "<svg/>" for n in rajah}, galat)
        finally:
            build.KONTEN = asli
            shutil.rmtree(sementara)
        return dipakai, galat

    def test_rujukan_sah_lolos_dan_tercatat_terpakai(self):
        dipakai, galat = self._periksa("![Segitiga ABC siku-siku di B](abc.svg)")
        self.assertEqual(galat, [])
        self.assertEqual(dipakai, {"abc.svg"})

    def test_rajah_tak_ada_ketahuan(self):
        _, galat = self._periksa("![Segitiga ABC](belum-ada.svg)")
        self.assertTrue(any("belum-ada" in g for g in galat), galat)

    def test_alt_kosong_ditolak(self):
        _, galat = self._periksa("![](abc.svg)")
        self.assertTrue(any("tanpa alt" in g for g in galat), galat)

    def test_alt_malas_ditolak(self):
        for malas in ("gambar", "Gambar", "ilustrasi", "lihat gambar", "Diagram."):
            _, galat = self._periksa("![%s](abc.svg)" % malas)
            self.assertTrue(any("tidak menggantikan" in g for g in galat),
                            "%r lolos padahal tidak menggantikan gambarnya" % malas)

    def test_rumus_di_alt_ditolak(self):
        # KaTeX tidak merender di dalam atribut; pembaca layar mengeja 'dolar'.
        _, galat = self._periksa("![Sudut $ABC$ siku-siku](abc.svg)")
        self.assertTrue(any("memuat rumus" in g for g in galat), galat)

    def test_gambar_luar_ditolak(self):
        # Mematahkan latihan offline, dan menyalinnya ke sini izin yang berbeda.
        _, galat = self._periksa("![Segitiga ABC](https://situs.lain/a.svg)")
        self.assertTrue(any("alamat web" in g for g in galat), galat)

    def test_bukan_svg_ditolak(self):
        _, galat = self._periksa("![Segitiga ABC](foto.png)", rajah=("foto.png",))
        self.assertTrue(any("bukan .svg" in g for g in galat), galat)

    def test_konten_tanpa_gambar_tidak_mengeluh(self):
        dipakai, galat = self._periksa("Segitiga $ABC$ siku-siku di $B$.")
        self.assertEqual((dipakai, galat), (set(), []))


class TestPeriksaPetunjuk(unittest.TestCase):
    """Petunjuk 1 tidak boleh menyebut nama jurusnya — dulu satu-satunya aturan
    isi penting yang cuma dititipkan ke ingatan. Yang diuji di sini justru
    kelonggarannya: pemeriksaan yang menandai pengecualian sah akan dimatikan
    orang, jadi kelonggaran itu bagian dari alatnya, bukan cacatnya."""

    def _susun(self, *simpul):
        """simpul: (id, nama, [(id_soal, petunjuk_1, teks_soal), …])"""
        jurus, soal = {}, {}
        for jid, nama, butir in simpul:
            jurus[jid] = {"id": jid, "nama": nama, "latihan": [b[0] for b in butir]}
            for sid, p1, teks in butir:
                soal[sid] = {"petunjuk": [p1], "soal": teks}
        return build.periksa_petunjuk(jurus, soal)

    def test_petunjuk_yang_menyebut_nama_jurusnya_ditandai(self):
        hasil = self._susun(("hmt", "Homoteti", [
            ("h-01", "Pusat homoteti selalu pada garis kedua pusat.",
             "Dua lingkaran berjari-jari 3 dan 7."),
        ]))
        self.assertTrue(any("h-01" in x for x in hasil), hasil)

    def test_kosakata_yang_dipakai_banyak_jurus_dilewatkan(self):
        # "luas" muncul di petunjuk milik tiga jurus — itu kosakata bidangnya,
        # bukan nama teknik. Inilah yang membedakan alat ini dari pencocokan
        # kata biasa, dan yang membuat keluarannya masih layak dibaca orang.
        hasil = self._susun(
            ("lp", "Luas", [("l-01", "Bandingkan luas kedua segitiga.", "Segitiga.")]),
            ("kk", "Kekongruenan", [("k-01", "Hitung luas alasnya.", "Segitiga.")]),
            ("ph", "Pythagoras", [("p-01", "Cari luas persegi itu.", "Persegi.")]),
        )
        self.assertEqual([x for x in hasil if "l-01" in x], [])

    def test_soal_yang_menyebut_tekniknya_sendiri_tidak_bisa_bocor(self):
        hasil = self._susun(("ptl", "Teorema Ptolemy", [
            ("p-01", "Ptolemy hanya berlaku untuk segiempat talibusur.",
             "Dengan memakai teorema Ptolemy, tentukan panjang diagonalnya."),
        ]))
        self.assertEqual(hasil, [])

    def test_soal_contoh_tidak_diperiksa(self):
        # Contoh hanya tampil di jurus.html, yang judul halamannya adalah nama
        # jurus itu sendiri. Tidak ada yang bisa dibocorkan di sana.
        jurus = {"hmt": {"id": "hmt", "nama": "Homoteti",
                         "contoh": ["h-contoh-1"], "latihan": []}}
        soal = {"h-contoh-1": {"petunjuk": ["Pakai homoteti berpusat $T$."],
                               "soal": "Dua lingkaran bersinggungan di $T$."}}
        self.assertEqual(build.periksa_petunjuk(jurus, soal), [])

    def test_nama_yang_sisinya_satu_kata_tidak_dipecah(self):
        # Dipecah, "Teorema Sisa dan Faktor" menjadi "sisa" dan "faktor" — dan
        # tiap petunjuk yang menulis "sisa pembagian" ikut tertandai.
        hasil = self._susun(("tsf", "Teorema Sisa dan Faktor", [
            ("t-01", "Sisa pembagian oleh bentuk linear diperoleh dengan satu "
                     "substitusi.", "Suku banyak $P(x)$ dibagi $x-2$."),
        ]))
        self.assertEqual(hasil, [])

    def test_nama_dua_teknik_dipecah_supaya_salah_satunya_pun_tertangkap(self):
        hasil = self._susun(("sdl", "Sudut Pusat dan Sudut Keliling", [
            ("s-01", "Pakai sudut keliling yang menghadap busur itu.",
             "Lingkaran dengan tali busur $AB$."),
            ("s-02", "Yang satu bertitik sudut di keliling, yang satu di pusat.",
             "Lingkaran dengan tali busur $AB$."),
        ]))
        self.assertTrue(any("s-01" in x for x in hasil), hasil)
        self.assertEqual([x for x in hasil if "s-02" in x], [])


class TestRajah(unittest.TestCase):
    """Rajah dibaca dengan mata, jadi yang diuji bukan keluarannya melainkan
    geometrinya. Lingkaran dalam yang meleset seperseribu tidak menggagalkan apa
    pun — ia hanya mengajarkan hal yang salah."""

    def setUp(self):
        import rajah
        self.r = rajah
        self.A = rajah.titik(0, 0)
        self.B = rajah.titik(6, 0)
        self.C = rajah.titik(1.6, 4.2)

    def test_lingkaran_dalam_menyinggung_ketiga_sisi(self):
        r = self.r
        A, B, C = self.A, self.B, self.C
        I, jari = r.pusat_dalam(A, B, C), r.jari_dalam(A, B, C)
        for P, Q in ((A, B), (B, C), (C, A)):
            jarak_ke_sisi = r.jarak(I, r.kaki(I, r.garis(P, Q)))
            self.assertAlmostEqual(jarak_ke_sisi, jari, places=9)

    def test_lingkaran_luar_lewat_ketiga_titik_sudut(self):
        r = self.r
        O, jari = r.pusat_luar(self.A, self.B, self.C), r.jari_luar(self.A, self.B, self.C)
        for P in (self.A, self.B, self.C):
            self.assertAlmostEqual(r.jarak(O, P), jari, places=9)

    def test_garis_euler_segaris_dengan_perbandingan_dua_banding_satu(self):
        # Uji silang yang murah dan tajam: kalau salah satu dari ketiga titik
        # istimewa salah rumus, ketiganya berhenti segaris.
        r = self.r
        H = r.titik_tinggi(self.A, self.B, self.C)
        G = r.titik_berat(self.A, self.B, self.C)
        O = r.pusat_luar(self.A, self.B, self.C)
        silang = (G - H).x * (O - H).y - (G - H).y * (O - H).x
        self.assertAlmostEqual(silang, 0, places=9)
        self.assertAlmostEqual(r.jarak(H, G) / r.jarak(G, O), 2.0, places=9)

    def test_garis_bagi_memenuhi_teorema_garis_bagi(self):
        r = self.r
        A, B, C = self.A, self.B, self.C
        D = r.potong(r.garis_bagi(B, A, C), r.garis(B, C))
        self.assertAlmostEqual(r.jarak(B, D) / r.jarak(D, C),
                               r.jarak(A, B) / r.jarak(A, C), places=9)

    def test_titik_singgung_tegak_lurus_jari_jari(self):
        r = self.r
        P, pusat, jari = r.titik(9, 3), r.titik(2, 1), 1.5
        for T in r.singgung(P, pusat, jari):
            self.assertAlmostEqual(r.jarak(pusat, T), jari, places=9)
            self.assertAlmostEqual((T - pusat).x * (P - T).x
                                   + (T - pusat).y * (P - T).y, 0, places=9)

    def test_potong_lingkaran_berjarak_jari_jari_dari_kedua_pusat(self):
        # Fungsi ini lama berada di keadaan yang sama persis dengan busur()
        # sebelum kotak pembatasnya ketahuan salah: nol pemakai konten, nol
        # tes. Yang dijaga di sini definisinya — titik potong dua lingkaran
        # adalah titik yang berjarak r1 dari pusat pertama dan r2 dari kedua.
        r = self.r
        p1, r1 = r.titik(0, 0), 5.0
        p2, r2 = r.titik(6, 2), 4.0
        for T in r.potong_lingkaran(p1, r1, p2, r2):
            self.assertAlmostEqual(r.jarak(p1, T), r1, places=9)
            self.assertAlmostEqual(r.jarak(p2, T), r2, places=9)

    def test_potong_lingkaran_urut_kiri_lalu_kanan(self):
        # Docstring-nya menjanjikan urutan, dan rajah yang memakainya akan
        # memilih salah satu titik berdasarkan janji itu — jadi janjinya ikut
        # diuji, bukan cuma jaraknya. Sumbu y matematis: sisi kiri arah
        # p1→p2 berarti y positif.
        r = self.r
        kiri, kanan = r.potong_lingkaran(r.titik(0, 0), 5.0, r.titik(6, 0), 5.0)
        self.assertGreater(kiri.y, 0)
        self.assertLess(kanan.y, 0)
        self.assertAlmostEqual(kiri.x, kanan.x, places=9)
        self.assertAlmostEqual(kiri.y, -kanan.y, places=9)

    def test_lingkaran_yang_tak_berpotongan_dua_titik_dilempar(self):
        r = self.r
        kasus = (
            (r.titik(0, 0), 1.0, r.titik(10, 0), 2.0),   # terpisah jauh
            (r.titik(0, 0), 5.0, r.titik(1, 0), 1.0),    # satu di dalam lainnya
            (r.titik(0, 0), 3.0, r.titik(0, 0), 3.0),    # berimpit
            (r.titik(0, 0), 2.0, r.titik(5, 0), 3.0),    # bersinggungan, satu titik
        )
        for k in kasus:
            with self.assertRaises(r.GagalRajah):
                r.potong_lingkaran(*k)

    def test_bangun_mustahil_dilempar_bukan_digambar_diam_diam(self):
        r = self.r
        with self.assertRaises(r.GagalRajah):
            r.potong(r.garis(r.titik(0, 0), r.titik(1, 0)),
                     r.garis(r.titik(0, 1), r.titik(1, 1)))   # sejajar
        with self.assertRaises(r.GagalRajah):
            r.singgung(r.titik(0, 0), r.titik(0, 0), 2)       # titik di dalam

    def test_rajah_wajib_punya_alt(self):
        with self.assertRaises(self.r.GagalRajah):
            self.r.rajah("")

    def test_sumbu_y_dibalik_sekali_saat_render(self):
        # Penulis rajah berpikir dengan sumbu matematis; pembalikannya urusan
        # _layar(). Titik di atas harus keluar dengan y yang lebih kecil.
        svg = (self.r.rajah("Ruas dari A di bawah ke B di atas")
               .ruas(self.r.titik(0, 0), self.r.titik(0, 3))).svg()
        import re as _re
        y1 = float(_re.search(r'y1="(-?[\d.]+)"', svg).group(1))
        y2 = float(_re.search(r'y2="(-?[\d.]+)"', svg).group(1))
        self.assertLess(y2, y1)

    def test_proyeksi_ruang_menjaga_sejajar_dan_panjang_di_bidang_layar(self):
        # Yang dijanjikan proyeksi kabinet: rusuk sejajar tetap sejajar dan sama
        # panjang, dan panjang pada bidang xz tetap sejati. Kalau ini rusak, siswa
        # yang membaca panjang di gambar ruang dihukum karena mempercayai rajahnya.
        r = self.r
        rusuk = 4.0
        for y in (0, rusuk):
            p, q = r.ruang(0, y, 0), r.ruang(rusuk, y, 0)
            self.assertAlmostEqual(r.jarak(p, q), rusuk, places=9)
            p, q = r.ruang(0, y, 0), r.ruang(0, y, rusuk)
            self.assertAlmostEqual(r.jarak(p, q), rusuk, places=9)

        # Keempat rusuk yang searah sumbu y harus tergambar sebagai vektor yang sama.
        arah = {
            (r.ruang(x, rusuk, z) - r.ruang(x, 0, z)).__repr__()
            for x in (0, rusuk) for z in (0, rusuk)
        }
        self.assertEqual(len(arah), 1)

        # Dan arah itu memang diperpendek, bukan digambar sepanjang aslinya.
        dalam = r.jarak(r.ruang(0, 0, 0), r.ruang(0, rusuk, 0))
        self.assertAlmostEqual(dalam, rusuk * r.SUSUT, places=9)

    def test_keterangan_sudut_bisa_digeser_menjauhi_titik_sudutnya(self):
        # Pada sudut sempit, keterangan di jarak bawaan tertimpa kaki sudutnya
        # sendiri. Yang digeser hanya tulisannya; busurnya tetap di tempatnya,
        # sebab busur itulah yang menyatakan sudut mana yang dimaksud.
        import re as _re
        B, A, C = self.r.titik(0, 0), self.r.titik(3, 0), self.r.titik(0, 3)

        def jarak_teks(**tambahan):
            svg = (self.r.rajah("Sudut ABC")
                   .tanda_sudut(A, B, C, teks="40°", **tambahan)).svg()
            teks = _re.search(r'<text class="t ukur" x="(-?[\d.]+)" y="(-?[\d.]+)"', svg)
            return math.hypot(float(teks.group(1)), float(teks.group(2)))

        self.assertAlmostEqual(jarak_teks(jauh=44), 44, places=1)
        self.assertLess(jarak_teks(), 44)

    def test_busur_tidak_melebarkan_kotak_ke_seluruh_lingkarannya(self):
        # Busur pendek dari lingkaran berjari-jari besar — persis bentuk "dua busur
        # bercermin pada AB" di jurus tempat kedudukan, yang pusatnya jauh dari
        # bangunnya. Kalau kotak pembatasnya diambil dari lingkaran penuh, viewBox
        # melar berkali-kali lipat dan bangunnya menyusut sampai tidak terbaca.
        import re as _re
        r = self.r
        pusat, jari = r.titik(0, -6), 7.0
        svg = (r.rajah("Busur pendek di atas ruas AB")
               .ruas(r.titik(-3.5, 0), r.titik(3.5, 0))
               .busur(pusat, jari, 60, 120)).svg()
        kotak = [float(v) for v in
                 _re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
        # Busurnya memuncak di y = 1 dan turun sampai y = 0; tingginya sekitar satu
        # satuan, bukan dua kali jari-jari.
        self.assertLess(kotak[3], (1 + 2 * r.TEPI / r.SKALA) * r.SKALA)

    def test_busur_yang_melewati_mata_angin_tetap_termuat_utuh(self):
        # Kebalikannya: kotak yang dihitung dari kedua ujung saja memotong busur
        # yang melengkung melewati puncaknya. Busur 0..180 memuncak di y = jari,
        # dan puncak itu harus ikut terhitung meski bukan salah satu ujungnya.
        import re as _re
        r = self.r
        svg = (r.rajah("Setengah lingkaran")
               .busur(r.titik(0, 0), 3.0, 0, 180)).svg()
        kotak = [float(v) for v in
                 _re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
        self.assertAlmostEqual(kotak[3], 3 * r.SKALA + 2 * r.TEPI, places=1)

    def test_svg_membawa_alt_dan_kedua_tema(self):
        svg = (self.r.rajah("Segitiga ABC").poligon(self.A, self.B, self.C)).svg()
        self.assertIn('aria-label="Segitiga ABC"', svg)
        self.assertIn("<title>Segitiga ABC</title>", svg)
        # SVG lewat <img> tidak melihat CSS halaman, jadi paletnya harus ikut
        # di dalam berkasnya — termasuk tema gelapnya.
        self.assertIn("prefers-color-scheme:dark", svg)

    def test_alt_berkutip_dan_bertanda_lebih_kecil_di_lolos(self):
        svg = (self.r.rajah('Sudut A < B & titik "P"')
               .ruas(self.A, self.B)).svg()
        self.assertIn("&lt;", svg)
        self.assertIn("&amp;", svg)
        self.assertIn('aria-label="Sudut A &lt; B &amp; titik &quot;P&quot;"', svg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
