# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Rencana pengembangannya ada di `PLAN.md` — fase, cakupan, dan target isi per jurus.
Baca itu dulu sebelum menambah konten atau membuka bidang baru.

## Bahasa

Nama variabel, nama fungsi, komentar, pesan galat, dan seluruh dokumentasi ditulis
**dalam bahasa Indonesia** (`kertas`, `tinta`, `simpanKemajuan`, `muatData`, `galat`).
Ikuti itu untuk kode baru — pembacanya guru dan siswa, bukan hanya programmer.

## Perintah

```sh
python3 -m http.server 8000       # wajib lewat server; fetch() mati di file://
python3 scripts/build.py          # konten/ → data/*.json + assets/rajah/*.svg  (butuh pyyaml)
python3 tests/test_build.py       # 93 tes
python3 tests/test_build.py TestRumusSelamat.test_garis_bawah_bukan_huruf_miring   # satu tes
node scripts/periksa-rumus.js     # tiap rumus di data/*.json benar-benar dirender KaTeX
node scripts/periksa-muatan.js    # berkas data apa yang benar-benar diminta tiap halaman
```

Tidak ada linter, tidak ada package manager, tidak ada build step untuk situsnya —
yang di-build hanya isinya.

`periksa-rumus.js` perkakas pengembangan, **bukan** dependensi situs: ia memakai berkas
KaTeX yang sudah ada di `assets/katex/`, tanpa mengunduh apa pun. Jalankan setelah
`build.py`, karena yang diperiksa hasilnya. `tests/test_build.py` menjaga keluaran
`markdown_ke_html`; yang tidak dijaganya adalah apakah rumus yang selamat itu **sah**
menurut KaTeX. Rumus salah ketik lolos build tanpa keluhan dan baru terlihat sebagai
kotak merah di layar siswa. Alur GitHub Actions menjalankannya sebelum mengomit balik.

Ia memeriksa **soal dan jurus** — `data/soal-*.json` beserta `kapan_dipakai`, `inti`, dan
`jebakan` di `data/jurus.json`. Bagian "Intinya" justru yang paling padat rumus di seluruh
situs, dan halaman jurus dibuka jauh lebih sering daripada satu soal tertentu.

## Alur data

`konten/jurus/*.md` + `konten/soal/*.md` + `konten/arsip.yml` → `scripts/build.py` →
`data/jurus.json` + `data/soal-<pilar>.json` → halaman statis mengambilnya dengan
`fetch()`.

Rajah geometri ikut alur yang sama: `konten/rajah/*.py` → `scripts/build.py` →
`assets/rajah/*.svg`. Sumbernya berkas Python karena rajah **dihitung, bukan digambar
tangan** — `pusat_dalam()`, `kaki()`, `singgung()` di `scripts/rajah.py` memberi koordinat
yang benar, dan rajah yang meleset sedikit tidak menggagalkan apa pun, ia hanya
mengajarkan hal yang salah. Pola yang sama dengan `tata_letak()`: hitungannya di Python,
peramban tinggal menggambar. Dibangkitkan `build.py` sendiri, bukan skrip terpisah, supaya
alur GitHub Actions yang sudah mengomit balik hasil build ikut membangkitkannya.

Daftar arsip ikut di `data/jurus.json`, bukan berkas sendiri: isinya beberapa ratus bita
dan selalu dibutuhkan bersama soal mana pun yang menyebutnya.

`data/*.json` adalah **hasil build yang ikut dikomit**, jangan pernah diedit tangan —
`.github/workflows/build-konten.yml` menjalankan tes, membangun ulang, dan mengomit
balik setiap dorongan ke `main` yang menyentuh `konten/` atau `scripts/build.py`.

## scripts/build.py

- **Galat dikumpulkan, bukan dilempar di percikan pertama.** Fungsi pemeriksa menerima
  daftar `galat` dan menambahinya; `main()` mencetak semuanya sekaligus lalu keluar 1.
  Pemeriksaan baru ikut pola ini, bukan `raise`.
- **Urutan pengolahan Markdown tidak boleh diubah:** lindungi rumus (ganti dengan
  penanda NUL) → `html.escape` → aturan blok/sebaris → kembalikan rumus dalam keadaan
  ter-escape. Akibatnya `_blok()` bekerja pada teks yang sudah di-escape — di situ `>`
  sudah menjadi `&gt;` dan pencocokan blockquote memakai `&gt;`. Rumus sengaja
  di-escape karena KaTeX membaca lewat `textContent`.
- Sebagian besar `tests/test_build.py` menjaga tepat hal ini: Markdown dan LaTeX
  memperebutkan `_ * \\ &`. Setiap sentuhan pada `markdown_ke_html` harus dibuktikan
  tidak merusak `$a_1$` atau `\\` di dalam `align`.
- **Tata letak peta dihitung saat build**, bukan di peramban: `hitung_tingkat()` memberi
  kedalaman graf, `tata_letak()` memberi `x`/`y` (barycenter, 4 sapuan) plus `ukuran`
  per pilar — termasuk `tinggi_sampai`, tinggi SVG untuk tiap batas saringan tahap.
  Peramban tinggal menggambar SVG — tanpa d3, dagre, atau pustaka graf.

## Sisi klien

Semua skrip adalah IIFE tanpa modul ES, tanpa dependensi selain KaTeX (dipasang lokal
di `assets/katex/`, bukan CDN, supaya offline jalan).

- `assets/inti.js` mengekspor global `Inti`: data, localStorage, penjadwalan, render
  rumus, `lolos()` untuk escape HTML, `tulisSumber()` untuk sumber soal beserta tautan
  arsipnya kalau ada.
- **Halaman menyatakan bidang apa yang soalnya dipakai** lewat
  `Inti.muatData({ soal: … })` — `false`, daftar pilar, atau fungsi yang memutuskan
  setelah `jurus.json` termuat. Bawaannya semua bidang, jadi halaman yang lupa
  menyatakan tetap bekerja, hanya tidak hemat.
- **`jurus.json` selalu diambil lebih dulu dan sendirian**, bukan sejajar dengan soal:
  peta soal→bidang (`data.pilarSoal`) diturunkan darinya, dan bentuk fungsi di atas butuh
  data itu untuk memutuskan. Peta itu bisa diturunkan karena tiap soal terdaftar di tepat
  satu jurus — dijaga tes `test_tiap_soal_terdaftar_di_jurus_sebidang`.
- `node scripts/periksa-muatan.js` menunjukkan berkas apa yang **benar-benar** diminta tiap
  halaman, beserta ukurannya. Jalankan setiap kali menyentuh `muatData` atau pemilihan
  bidang di halaman mana pun.
- `assets/soal-ui.js` mengekspor global `SoalUI`: hanya tangga petunjuk, dipakai bersama
  oleh halaman jurus dan latihan.
- Tiap halaman punya satu skripnya sendiri dan selalu ditutup dengan pola yang sama:

  ```js
  Inti.pasangKepala('latihan.html');
  Inti.muatData().then(jalan).catch(function (e) { Inti.galat(e.message); });
  ```

- HTML-nya nyaris kosong: hanya `<header id="kepala">` dan `<main id="isi">`. Skrip
  dimuat `defer` dengan urutan tetap: katex → auto-render → inti → (soal-ui) → skrip
  halaman. Halaman baru harus mengikuti keduanya.

## Kemajuan siswa

Satu kunci localStorage, `peta-jurus/kemajuan/v1`, berisi `{ jurus, riwayat,
jurnal_salah }`. Tidak ada server, tidak ada akun.

- **Status jurus tidak disimpan, tapi dihitung ulang** oleh `statusJurus()` dari
  prasyarat + tanggal, supaya tidak pernah basi. Jangan menyimpannya mentah-mentah.
- `kemajuan()` selalu mengisi bidang yang hilang; kalau bentuk datanya berubah tak
  kompatibel, naikkan versi di `KUNCI`.
- **Tangga ulang 1→3→7→21→60 hanya naik kalau jurusnya memang jatuh tempo**
  (`jatuhTempo`). Tanpa penjaga itu, lima soal dalam satu sore melompat ke 60 hari.
- `catatJawaban()` menjadwalkan ulang **semua** jurus yang ditandai pada soal itu.

## Gerbang petunjuk

Pembahasan terkunci sampai semua petunjuk dibuka; gerbangnya lepas begitu siswa menekan
"Jawab". Ia mencegah mengintip sebelum mencoba, bukan menahan penjelasan dari orang yang
sudah mencoba. Konsekuensinya di kode: **rekam `tangga.dibuka()` sebelum memanggil
`tangga.bukaPembahasan()`** — pembukaan itu memaksa penghitung ke jumlah penuh.

## Service worker

`sw.js` cache-dulu (kebalikan dari proyek `info-kurikulum`), karena latihan saat offline
justru intinya.

- Berkas tingkat atas yang baru **wajib ditambahkan ke `KERANGKA`** — kalau tidak,
  situsnya patah saat offline. **Kecuali `data/soal-<pilar>.json` dan `assets/rajah/*.svg`**,
  yang sengaja di luar `KERANGKA`: menunggunya memanjangkan install oleh ratusan KB yang
  belum tentu dipakai hari itu. Keduanya diambil di latar setelah install, lewat
  `berkasLatar()` yang menurunkan daftarnya dari `jurus.json` — soal dari `pilar` tiap
  simpul, rajah dari kunci `rajah` yang ditulis `build.py`. Jadi bidang baru dan rajah baru
  tidak pernah terlupa. Untuk rajah itu bukan kemewahan: soal geometri tanpa bangunnya
  bukan soal yang lebih sulit, melainkan soal yang tidak bisa dikerjakan sama sekali.
- **Naikkan `CACHE`** (sekarang `peta-jurus-v13`) setiap kali aset berubah, kalau tidak
  siswa memegang versi lama.
- Kunci cache membuang query, karena `jurus.html?id=…` dan `latihan.html?soal=…` memakai
  kerangka HTML yang sama.
- Saat mengembangkan: halaman yang seperti tidak berubah biasanya service worker —
  muat ulang sekali lagi, atau Unregister lewat DevTools.

## Aturan isi

Ditegakkan `build.py` (build gagal): `id` sama dengan nama berkas · `pilar` ada di
`URUT_PILAR` dan `tahap` ada di `TAHAP_SAH` · prasyarat dan rujukan soal harus ada dan
tidak berputar · soal isian punya `jawaban` · soal uraian punya `## Rubrik` ·
**`## Kapan dipakai` tidak boleh kosong** — pemicunya, bukan rumusnya, itu bagian yang
membuat situs ini ada.

**Gambar juga ditegakkan mesin** lewat `periksa_gambar()`, yang membaca berkas mentahnya —
bukan hasil `markdown_ke_html` — justru karena yang diperiksa hilang setelah dirender.
Rujukannya wajib berupa **nama berkas telanjang** yang ada di `konten/rajah/` (jalur dan
alamat web ditolak: gambar luar mematahkan latihan offline, dan menyalinnya ke sini urusan
izin yang berbeda), dan `alt` wajib benar-benar menggantikan gambarnya — kosong ditolak,
`![gambar](…)` dan sejenisnya ditolak lewat `ALT_MALAS`, dan `$…$` di dalam alt ditolak
karena KaTeX tidak merender di dalam atribut sehingga pembaca layar mengejanya sebagai
"dolar". Rajah yang tidak dirujuk konten mana pun cuma **peringatan**, bukan galat: saat
menulis geometri, wajar rajahnya jadi lebih dulu daripada soal yang memakainya.

**Atribusi juga ditegakkan mesin** lewat `periksa_arsip()`. `sumber` yang berbunyi seperti
atribusi tahun+lomba (`OSN 2025 nomor 3` — pola `ATRIBUSI_NYATA`) wajib punya `arsip:`
yang merujuk entri sah di `konten/arsip.yml`, dan tiap entri wajib lengkap keenam kuncinya.
Polanya sengaja **tidak** menangkap `susunan sendiri, gaya OSN-K`: yang dijaga klaim
tahunnya, bukan penyebutan nama lombanya. Kalau menyentuh polanya, uji dulu terhadap
seluruh `sumber` yang sudah ada — semuanya harus tetap lolos.

Konsekuensinya untuk penulisan soal:

- Sebagian besar soal disusun sendiri dengan gaya OSN dan ditulis begitu apa adanya
  (`Latihan 1 — susunan sendiri, gaya OSN-K`). Itu jalur biasa; `arsip` dibiarkan kosong.
- Jangan pernah mengarang atribusi, dan jangan pernah memberi atribusi tahun+nomor pada
  soal dari salinan tak resmi: asal-usulnya tidak bisa diverifikasi, dan salah ketik pada
  soal olimpiade biasanya mengubahnya jadi soal lain. Kalau soalnya bagus tapi sumbernya
  tak resmi, tulis ulang sebagai soal susunan sendiri dan beri label begitu.
- **Tidak ada PDF naskah di repo ini** — arsip menyimpan metadata dan tautan ke sumber
  resminya saja. Mengunduh dan menyebarkan ulang adalah dua izin yang berbeda; rinciannya
  di `PLAN.md` Fase 5.

**Petunjuk 1 tidak boleh menyebut nama jurusnya**, dan itu sekarang **peringatan mesin**
lewat `periksa_petunjuk()` — bukan galat, karena sebagian penyebutan justru dorongan yang
benar ("Ptolemy yang biasa belum cukup" pada soal yang menuntut bentuk lain). Urutan
petunjuk berjenjang dari dorongan halus → sebut jurus → langkah pertama; kalau petunjuk 1
sudah menyebut namanya, biasanya obatnya menggeser tangganya satu anak, bukan menghapus.

Yang dicocokkan **nama jurus pemiliknya**, bukan seluruh medan `jurus:` — menyebut jurus
kedua di petunjuk pertama sering justru yang dimaksudkan. Tiga hal membuat keluarannya
tetap layak dibaca, dan ketiganya dijaga tes: nama yang sisi-sisinya satu kata tidak
dipecah di "dan" (kalau tidak, "Teorema Sisa dan Faktor" menandai tiap "sisa pembagian");
frasa yang muncul di petunjuk milik dua jurus lain atau lebih dianggap kosakata bidang,
bukan nama teknik; dan soal yang menyebut tekniknya sendiri di badan soalnya dilewatkan,
karena tidak ada yang bisa dibocorkan di situ. Soal contoh tidak diperiksa sama sekali — ia
hanya tampil di `jurus.html`, yang judul halamannya nama jurus itu sendiri.

Sisa peringatan yang memang disengaja saat ini: `grd-03`, `ptl-03`, `pwn-06`.

Tidak bisa ditegakkan mesin, tapi sama mengikatnya:

- **Varian jawaban ditulis eksplisit di `jawaban_alt`**, bukan ditebak kode.
  `periksaJawaban()` sengaja lugu: rapikan spasi, samakan huruf, bandingkan sebagai angka.
  Konsekuensinya untuk penulisan soal isian: perbandingan angkanya lewat `Number()`, dan
  `Number("3/2")` adalah `NaN` — jadi pecahan dan akar **hanya** cocok kalau siswa
  mengetiknya persis sama seperti yang tertulis di `jawaban`. Susun soal isian supaya
  jawabannya bilangan bulat; kalau tidak bisa, daftarkan tiap ejaan yang sah di
  `jawaban_alt` (`"3/2"`, `"1,5"`, `"1.5"`). Jangan menaruh $\sqrt{\ }$ di `jawaban` —
  ubah pertanyaannya, misalnya menanyakan besaran lain pada bangun yang sama.

Format frontmatter lengkap ada di README.md.

## Jebakan

- **`URUT_PILAR` di `build.py` adalah daftar bidang yang sah**, sekaligus urutan
  tampilnya di peta. Pilar di luar daftar itu menggagalkan build — itu disengaja, supaya
  salah ketik pada `pilar` tidak diam-diam membuat bidang hantu. Hal yang sama berlaku
  untuk `tahap` lewat `TAHAP_SAH`. Menambah bidang berarti menyentuh dua tempat:
  `URUT_PILAR`, dan `NAMA_PILAR` di `peta.js` + `jurus.js`. Tes
  `test_semua_pilar_di_nama_pilar_peramban` menjaga keduanya tidak terpisah.
- **Prasyarat tidak boleh dari tahap yang lebih akhir** — jurus OSN-K tidak boleh
  berprasyarat jurus OSN-P. Saringan tahap hanya menyembunyikan simpul, jadi pelanggaran
  itu memberi siswa gembok yang penyebabnya tidak ada di layar dan tidak bisa dibuka tanpa
  keluar dari tahap yang sedang ia siapkan. Dijaga
  `test_prasyarat_tidak_boleh_dari_tahap_yang_lebih_akhir`.
- `NAMA_PILAR` ada di **dua** berkas, `peta.js` dan `jurus.js`. `simulasi.js` memakai
  `pilar` untuk mengelompokkan soal di `susunNaskah()`, tapi tidak pernah menampilkan
  namanya — jadi jangan tergoda menyalin `NAMA_PILAR` ke sana hanya untuk satu kalimat.
  Yang tersalin di tiga berkas adalah peta tahapnya, dengan dua nama berbeda: `NAMA_TAHAP`
  di `peta.js` dan `jurus.js`, `TAHAP` di `simulasi.js`.
- **Naskah simulasi dibagi rata antar bidang, bukan diacak dari satu kolam.**
  `susunNaskah()` mengambil bergiliran satu per bidang; bidang yang kehabisan soal
  berhenti ikut dan jatahnya jatuh ke bidang lain, jadi naskahnya tetap penuh saat bidang
  baru masih tipis. Jangan menggantinya dengan kuota per bidang — kuota harus dijaga
  berjumlah pas, dan tidak menangani bidang tipis dengan sendirinya.
- Prasyarat lintas pilar tetap mengunci jurusnya dan garisnya tetap **tidak digambar** —
  tiap pilar punya SVG sendiri. Yang menutup lubangnya sekarang adalah penanda `↗` pada
  simpulnya plus `<title>`/`aria-label` yang menyebut nama jurus dan bidang asalnya, jadi
  gembok tidak pernah muncul tanpa sebab yang bisa dibaca. Kalau menyentuh
  `gambarSimpul()`, jangan hilangkan itu.
- **Saringan tahap hanya menyembunyikan simpul, tidak menata ulang apa pun.** Tinggi SVG
  untuk tiap batas tahap ikut dihitung `build.py` (`ukuran.tinggi_sampai`) justru supaya
  `peta.js` tidak perlu menyalin `TINGGI_BARIS` dan `TEPI`. Jangan pindahkan hitungan itu
  ke peramban.
- **Pilihan tampilan peta ada di kunci localStorage sendiri**, `peta-jurus/tampilan/v1`,
  bukan di dalam kemajuan. Kalau ikut masuk ke `peta-jurus/kemajuan/v1`, preferensi
  perangkat akan terbawa saat siswa mengekspor kemajuannya dan memindahkannya.
- **Aturan gambar di `_sebaris()` dipasang sebelum pola tautan**, supaya tanda serunya
  ikut termakan; kalau dibalik, `[alt](url)` tertangkap lebih dulu dan keluarannya
  `!<a href="…">alt</a>` — bukan galat, hanya halaman yang salah. Dan `<img>` yang sudah
  dirakit **dicabut jadi penanda NUL**, sama seperti rumus: tanpa itu aturan penekanan di
  bawahnya menggigit ke dalam atributnya dan alt berisi `<em>`. Alt bukan HTML.
- **SVG yang dimuat lewat `<img>` tidak melihat CSS halaman.** Ia dokumen terpisah:
  `var(--tinta)` dan `currentColor` mati di sana. Karena itu tiap rajah membawa paletnya
  sendiri beserta `@media (prefers-color-scheme: dark)`, dicap `scripts/rajah.py`. Kalau
  palet di `styles.css` berubah, `GAYA` di `rajah.py` harus diubah juga — tidak ada cara
  bagi SVG lepas untuk ikut sendiri.
- Semua HTML dirakit lewat `innerHTML`; teks dari data harus lewat `Inti.lolos()`, tapi
  bidang hasil build (`soal`, `pembahasan`, `petunjuk`, `inti`) sudah berupa HTML dan
  memang dipasang mentah.
