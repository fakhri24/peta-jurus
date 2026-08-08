# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Bahasa

Nama variabel, nama fungsi, komentar, pesan galat, dan seluruh dokumentasi ditulis
**dalam bahasa Indonesia** (`kertas`, `tinta`, `simpanKemajuan`, `muatData`, `galat`).
Ikuti itu untuk kode baru — pembacanya guru dan siswa, bukan hanya programmer.

## Perintah

```sh
python3 -m http.server 8000       # wajib lewat server; fetch() mati di file://
python3 scripts/build.py          # konten/*.md → data/*.json  (butuh pyyaml)
python3 tests/test_build.py       # 38 tes
python3 tests/test_build.py TestRumusSelamat.test_garis_bawah_bukan_huruf_miring   # satu tes
```

Tidak ada linter, tidak ada package manager, tidak ada build step untuk situsnya —
yang di-build hanya isinya.

## Alur data

`konten/jurus/*.md` + `konten/soal/*.md` → `scripts/build.py` → `data/jurus.json` +
`data/soal.json` → halaman statis mengambilnya dengan `fetch()`.

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
  per pilar. Peramban tinggal menggambar SVG — tanpa d3, dagre, atau pustaka graf.

## Sisi klien

Semua skrip adalah IIFE tanpa modul ES, tanpa dependensi selain KaTeX (dipasang lokal
di `assets/katex/`, bukan CDN, supaya offline jalan).

- `assets/inti.js` mengekspor global `Inti`: data, localStorage, penjadwalan, render
  rumus, `lolos()` untuk escape HTML.
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
  situsnya patah saat offline.
- **Naikkan `CACHE`** (`peta-jurus-v2`) setiap kali aset berubah, kalau tidak siswa
  memegang versi lama.
- Kunci cache membuang query, karena `jurus.html?id=…` dan `latihan.html?soal=…` memakai
  kerangka HTML yang sama.
- Saat mengembangkan: halaman yang seperti tidak berubah biasanya service worker —
  muat ulang sekali lagi, atau Unregister lewat DevTools.

## Aturan isi

Ditegakkan `build.py` (build gagal): `id` sama dengan nama berkas · prasyarat dan rujukan
soal harus ada dan tidak berputar · soal isian punya `jawaban` · soal uraian punya
`## Rubrik` · **`## Kapan dipakai` tidak boleh kosong** — pemicunya, bukan rumusnya,
itu bagian yang membuat situs ini ada.

Tidak bisa ditegakkan mesin, tapi sama mengikatnya:

- **Petunjuk 1 tidak boleh menyebut nama jurusnya.** Kalau disebut, gerbangnya kehilangan
  gunanya. Urutan petunjuk berjenjang dari dorongan halus → sebut jurus → langkah pertama.
- **`sumber` ditulis apa adanya.** Soal yang ada sekarang disusun sendiri dengan gaya OSN
  dan ditulis begitu. Jangan pernah mengarang atribusi seperti "OSN-K 2013 soal 8".
- **Varian jawaban ditulis eksplisit di `jawaban_alt`**, bukan ditebak kode.
  `periksaJawaban()` sengaja lugu: rapikan spasi, samakan huruf, bandingkan sebagai angka.

Format frontmatter lengkap ada di README.md.

## Jebakan

- `NAMA_PILAR` dan `NAMA_TAHAP` disalin di `peta.js`, `jurus.js`, dan `simulasi.js`.
  Pilar baru muncul sendiri di peta (dikelompokkan `build.py`), tapi judulnya tampil
  sebagai slug mentah sampai ketiga berkas itu ditambahi.
- Prasyarat lintas pilar tetap mengunci jurusnya, tapi garisnya **tidak digambar** —
  `gambarPilar()` melewati tepi yang pangkalnya di pilar lain.
- Semua HTML dirakit lewat `innerHTML`; teks dari data harus lewat `Inti.lolos()`, tapi
  bidang hasil build (`soal`, `pembahasan`, `petunjuk`, `inti`) sudah berupa HTML dan
  memang dipasang mentah.
