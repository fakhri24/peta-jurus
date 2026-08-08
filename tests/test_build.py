#!/usr/bin/env python3
"""Tes untuk scripts/build.py — jalankan: python3 tests/test_build.py

Yang paling perlu dijaga adalah rumus LaTeX. Aturan Markdown dan LaTeX memakai
tanda yang sama (_ * \\ &), jadi setiap perubahan di markdown_ke_html harus
dibuktikan tidak merusak rumus.
"""

import sys
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
