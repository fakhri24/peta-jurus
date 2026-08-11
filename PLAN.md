# Rencana: dari kerangka ke alat persiapan olimpiade

Dokumen ini menjawab satu pertanyaan: **apa saja yang masih kurang sebelum situs ini
benar-benar bisa dipakai siswa SMA menyiapkan OSN atau lomba matematika lain.**

**Pertanyaan itu sudah terjawab pada 11 Agustus 2026** — definisi "siap" di bagian 1
terpenuhi seluruhnya, keempat bidang penuh. Bagian 1 sampai Fase 5 karena itu dibiarkan
apa adanya sebagai catatan bagaimana ke sana, termasuk taksiran yang meleset; yang
menjawab "apa berikutnya" adalah **Fase 6**, dan pertanyaannya sudah berbeda.

Ditulis 8 Agustus 2026, diperbarui 11 Agustus 2026. Perbarui angkanya kalau sudah tidak
cocok — rencana yang angkanya basi lebih menyesatkan daripada tidak ada rencana. Angka di
Fase 6 semuanya bisa dihitung ulang: `node scripts/periksa-muatan.js` untuk muatan
halaman, `python3 scripts/build.py` untuk jumlah jurus, soal, dan rajah.

---

## 1. Definisi "siap"

Supaya tidak jadi perdebatan rasa, "siap" dipatok ke hal yang bisa dicek:

1. **Keempat bidang OSN ada** — teori bilangan, aljabar, kombinatorika, geometri.
2. **Setiap jurus punya minimal 6 latihan.** Angka 6 bukan karangan: tangga ulangnya
   1 → 3 → 7 → 21 → 60 hari, lima langkah. Kalau satu jurus cuma punya 3 soal, pada
   ulangan hari ke-21 siswa sudah bertemu soal yang sama untuk ketiga kalinya — yang
   teruji ingatannya pada jawaban, bukan penguasaan jurusnya. Enam soal adalah lantai,
   bukan target.
3. **Setiap jurus punya minimal 1 contoh yang sudah dibahas tuntas**, supaya jurus baru
   tidak langsung melempar siswa ke soal kosong.
4. **Setiap tahap bisa dilatih utuh.** Siswa yang menyiapkan OSN-K bisa menyelesaikan
   seluruh jalur OSN-K tanpa menabrak jurus kosong; begitu juga OSN-P dan OSN.
5. **Simulasi bisa menyusun naskah campuran empat bidang** dengan komposisi yang masuk
   akal, bukan acak dari satu kolam.
6. **Aturan isi di CLAUDE.md ditegakkan tanpa kecuali** — `## Kapan dipakai` terisi,
   petunjuk 1 tidak menyebut nama jurus, `sumber` tidak dikarang.

Poin 2 dan 4 yang paling mahal. Selebihnya pekerjaan kode yang terukur.

---

## 2. Keadaan sekarang

**85 jurus, 596 soal** (510 latihan + 86 contoh) di empat bidang, dan **keempatnya
tuntas**.

| Bidang | OSN-K | OSN-P | OSN | Soal | Status |
|---|---|---|---|---|---|
| Teori bilangan | 8 | 10 | 4 | 155 | **tuntas** |
| Aljabar | 10 | 7 | 5 | 154 | **tuntas** |
| Kombinatorika | 10 | 6 | 4 | 140 | **tuntas** |
| Geometri | 10 | 7 | 4 | 147 | **tuntas** |

Ke-85 jurus punya minimal satu contoh terpandu dan enam latihan; `build.py` tidak lagi
mencetak baris "Belum ada latihan di:" sama sekali.

Jalur lintas bidang ada **empat** dan semuanya nyata: `polinomial-bulat` (aljabar)
berprasyarat `keterbagian` (teori bilangan), `rekursi` (kombinatorika) berprasyarat
`induksi` (aljabar), `geometri-analitik` berprasyarat `persamaan-kuadrat` (aljabar), dan
`ketaksamaan-geometri` berprasyarat `am-gm` (aljabar). **Keempatnya kini bisa ditempuh
sungguhan** — yang terakhir sejak `ketaksamaan-geometri` punya soal.

Fase 0, 1, 2, 3, 4, dan 5.1 selesai. **Definisi "siap" di bagian 1 sudah terpenuhi
seluruhnya.**

Itu mengubah sifat rencana ini. Sampai di sini urutannya ditentukan satu hal — bidang mana
yang belum ada — dan pertanyaan "apa berikutnya" menjawab dirinya sendiri. Sekarang tidak
lagi. **Fase 6 karena itu ditulis dari pengukuran, bukan dari daftar keinginan**, dan
tiap butirnya menyebutkan angka yang membuatnya masuk daftar. Yang tidak punya angka tidak
masuk.

### Perkiraan cakupan penuh, diadu dengan hasilnya

Tabel ini dulunya perkiraan. Sekarang ada angka sebenarnya untuk dibandingkan, dan
perbandingan itu lebih berguna daripada perkiraannya.

| Bidang | Perkiraan jurus | Nyata | Perkiraan latihan | Nyata |
|---|---|---|---|---|
| Teori bilangan | 22 | 22 | 132 | 132 |
| Aljabar | ~22 | 22 | 132 | 132 |
| Kombinatorika | ~20 | 20 | 120 | 120 |
| Geometri | ~22 | 21 | 132 | 126 |
| **Total** | **~86** | **85** | **~516** | **510** |

Perkiraan jurus dan latihannya nyaris tepat — meleset 1 jurus dan 6 latihan, seluruhnya
dari geometri yang keluar 21 jurus, bukan 22. Yang meleset jauh adalah contohnya:
diperkirakan ~118, nyatanya **86** — satu contoh terpandu per jurus ternyata cukup, dan
hanya satu jurus di teori bilangan yang memerlukan dua. Totalnya 596 soal, bukan ~630.

Perkiraan waktunya yang paling salah, dan itu layak dicatat justru karena taksiran waktu
selalu yang paling sering meleset: rencana ini menaksir "satu sampai dua tahun untuk kerja
sambilan". Nyatanya **empat hari** — komit pertama 8 Agustus 2026, Fase 4 tuntas 11
Agustus 2026, 27 komit. Penyebabnya bukan lajunya lebih rajin; asumsi cara kerjanya yang
berubah, dan taksiran yang asumsinya berubah tidak bisa diselamatkan dengan menyetel
angkanya.

Yang tetap berlaku dari paragraf lamanya adalah keputusannya, dan itu terbukti benar:
rencana ini disusun agar **aplikasinya bisa dipakai di ujung setiap fase**, bukan hanya di
ujung fase terakhir. Tiap fase memang meninggalkan situs yang utuh — dan karena selesainya
jauh lebih cepat dari taksiran, sifat itu tidak pernah diuji dalam keadaan darurat. Ia
tetap keputusan yang benar untuk fase berikutnya.

---

## Fase 0 — Kerangka, sebelum konten masuk

Semua di fase ini tidak bergantung pada konten dan jauh lebih murah dikerjakan sekarang
saat baru 22 jurus daripada nanti saat sudah 86.

**0.1 Prasyarat lintas bidang — selesai 8 Agustus 2026.** Garisnya tetap tidak digambar
(tiap pilar punya SVG sendiri), tapi simpulnya kini diberi penanda `↗` dan
`<title>`/`aria-label` yang menyebut nama jurus beserta bidang asalnya. Gembok tidak lagi
muncul tanpa sebab yang bisa dibaca.

**0.2 Urutan bidang eksplisit — selesai 8 Agustus 2026.** `URUT_PILAR` di `build.py`
menetapkan urutannya mengikuti urutan pengerjaan fase, dan sekaligus jadi daftar pilar
yang sah: pilar di luar daftar itu menggagalkan build, jadi salah ketik pada `pilar`
tidak lagi diam-diam membuat bidang hantu. `TAHAP_SAH` melakukan hal yang sama untuk
`tahap`.

**0.3 Navigasi per bidang — selesai 8 Agustus 2026.** Peta digambar satu bidang pada satu
waktu dengan bilah tab. Tabnya menyembunyikan diri selama bidangnya baru satu, dan muncul
sendiri begitu bidang kedua masuk. Pilihan terakhir diingat.

**0.4 Saringan tahap — selesai 8 Agustus 2026.** Pemilih "Tampilkan sampai tahap"
menyembunyikan jurus di atas target — OSN-K memangkas teori bilangan dari 22 simpul jadi
8. Menyaring hanya menyembunyikan; tidak ada koordinat yang dihitung ulang di peramban,
dan tinggi SVG untuk tiap batas ikut dibangun sebagai `ukuran.tinggi_sampai`.

Pilihan bidang dan tahap disimpan di kunci localStorage sendiri,
`peta-jurus/tampilan/v1` — sengaja terpisah dari kemajuan, supaya preferensi perangkat
tidak ikut terbawa saat kemajuan diekspor dan dipindah.

**0.5 Pisah `soal.json` per bidang — selesai 9 Agustus 2026.**

Sebelum dikerjakan, ongkosnya diukur dulu — dan hasilnya mengoreksi asumsi rencana ini.
Mengurai `soal.json` 600 KB ternyata hanya **1 ms**, jadi "seluruhnya diambil di setiap
halaman" bukan masalah kecepatan halaman. Yang benar-benar mahal adalah **muatan
install**: `KERANGKA` menahan 1052 KB sebelum service worker siap, dan `soal.json`
46% di antaranya.

Karena itu pemecahan per bidang saja **tidak cukup** — selama seluruh berkasnya tetap di
`KERANGKA`, muatan installnya tidak berkurang sedikit pun. Yang dikerjakan dua hal
sekaligus:

1. `build.py` memecah menjadi `data/soal-<pilar>.json`, dan halaman menyatakan bidang yang
   dipakainya lewat `Inti.muatData({ soal: … })`.
2. Berkas soal **dikeluarkan dari `KERANGKA`** dan diambil di latar setelah install.
   Daftarnya diturunkan dari `jurus.json`, bukan ditulis tangan.

Hasilnya:

| | Sebelum | Sesudah |
|---|---|---|
| Muatan install (`KERANGKA`) | 1052 KB | **454 KB** |
| `jurus.html?id=…` | 685 KB | **398 KB** |
| `jurnal.html` | 685 KB | **83 KB** |
| `latihan.html` (siswa baru) | 685 KB | **370 KB** |
| `index.html` | 83 KB | 83 KB |
| `simulasi.html` | 685 KB | 685 KB (memang perlu semua) |

`latihan.html` bisa dipersempit karena pemilihan sesinya sebenarnya tidak menyentuh isi
soal sama sekali — daftar id ada di `jurus.json` dan "sudah dikerjakan" dibaca dari
riwayat. Jadi bidangnya sudah bisa ditentukan sebelum satu berkas soal pun diambil.

Ukur ulang kapan saja dengan `node scripts/periksa-muatan.js`.

**0.6 Koreksi CLAUDE.md — selesai 8 Agustus 2026**, lalu diperbarui lagi mengikuti
0.1–0.4.

**0.7 Komposisi naskah simulasi — selesai 9 Agustus 2026.** Definisi "siap" poin 5
menuntut naskah campuran "dengan komposisi yang masuk akal, bukan acak dari satu kolam",
tetapi `simulasi.js` justru melakukan persis yang dilarang itu: `acak(kolam).slice(0, n)`.
Terdengar adil, hasilnya tidak — yang menentukan isi naskah adalah bidang mana yang
kebetulan punya soal terbanyak, jadi naskah 10 soal bisa keluar 8 teori bilangan dan 2
aljabar.

Sekarang naskahnya dibagi rata antar bidang lewat `susunNaskah()`: tiap bidang diacak
sendiri, lalu diambil bergiliran satu-satu. Cara bergiliran dipilih daripada menghitung
kuota per bidang karena bidang yang kehabisan soal berhenti ikut dengan sendirinya dan
jatahnya jatuh ke bidang lain — jadi naskahnya tetap penuh saat bidang baru masih tipis,
yang pasti terjadi tiap kali bidang dibuka. Urutan bidangnya ikut diacak supaya sisa
pembagian tidak selalu jatuh ke bidang yang sama.

Dikerjakan sekarang, bukan nanti: pekerjaannya sama saja saat empat bidang, bedanya
simulasinya sudah setahun menghasilkan naskah timpang.

**Selesai kalau:** peta bisa dibuka per bidang, prasyarat lintas bidang terlihat
sebabnya, dan menambah bidang baru cuma menyentuh `URUT_PILAR` plus `NAMA_PILAR` di dua
berkas JS — dijaga tes, bukan ingatan.

**Fase ini tuntas.**

---

## Fase 1 — Tutup teori bilangan

Bidang ini strukturnya sudah lengkap; yang kurang isinya. Dikerjakan menurut tahap,
karena tahap itulah yang menentukan seorang siswa bisa memakai situs ini atau tidak.

**1.1 Naikkan 8 jurus OSN-K ke lantai 6 latihan — selesai 8 Agustus 2026.** 26 soal
ditambahkan (18 isian, 8 uraian), semuanya susunan sendiri. Seluruh jalur OSN-K teori
bilangan kini bisa ditempuh tanpa menabrak jurus kosong.

Catatan untuk penambahan berikutnya: setiap jawaban numerik diverifikasi lebih dulu
dengan Python sebelum soalnya ditulis, dan seluruh berkas diperiksa ulang setelah
dibangun — rumus yang rusak dimakan Markdown, `$` yang tak tertutup, dan kelengkapan
petunjuk/rubrik. Pada volume segini, ketelitian tangan saja tidak cukup.

**1.2 Isi 10 jurus OSN-P ke lantai 6 — selesai 8 Agustus 2026.** 63 soal ditambahkan
(55 latihan + 8 contoh; 48 isian, 15 uraian). Kesepuluh jurus OSN-P kini punya minimal
satu contoh terpandu dan enam latihan.

Porsi uraian sengaja jauh lebih besar daripada di 1.1 — 15 dari 63, dibanding 8 dari 26.
Sebabnya bukan selera: `turun-tak-hingga` dan sebagian besar `bezout` memang teknik
**pembuktian**, dan mengubahnya jadi soal isian akan menguji hal yang berbeda dari yang
dilatih. Konsekuensinya rubrik memikul beban lebih berat di tahap ini — dan rubrik yang
hanya menulis "jawaban benar" tidak akan menolong siswa menilai dirinya sendiri.

**1.3 Isi 4 jurus OSN — selesai 8 Agustus 2026.** `vieta-jumping`, `wilson`,
`orde-elemen`, `lte`: 28 soal (24 latihan + 4 contoh; 22 isian, 6 uraian). **Teori
bilangan tuntas.**

Fase ini juga melahirkan `scripts/periksa-rumus.js`. Saat menulis 28 soal berisi rumus
padat, kebutuhannya jadi jelas: `tests/test_build.py` menjaga keluaran `markdown_ke_html`,
tetapi tidak ada apa pun yang memeriksa apakah rumus yang selamat itu **sah** menurut
KaTeX. Rumus salah ketik lolos build tanpa keluhan dan baru terlihat sebagai kotak merah
di layar siswa. Pemeriksa itu kini jalan di GitHub Actions sebelum data dikomit balik.

**Selesai kalau:** tidak ada jurus teori bilangan dengan latihan di bawah 6, dan
`build.py` tidak lagi mencetak baris "Belum ada latihan di: …".

---

## Fase 2 — Aljabar

Dipilih sebagai bidang kedua karena bobotnya besar di semua tahap, tidak butuh gambar,
dan punya sambungan prasyarat yang nyata ke teori bilangan — jadi sekaligus menguji
hasil kerja 0.1.

### 2.1 Kerangka bidang — selesai 8 Agustus 2026

22 jurus beserta graf prasyaratnya, masing-masing lengkap dengan "Kapan dipakai",
"Intinya", dan "Jebakan umum". Sebarannya **10 OSN-K, 7 OSN-P, 5 OSN**, kedalaman $t_0$
sampai $t_5$ — dasarnya lebar, puncaknya sempit, seperti teori bilangan.

| Tingkat | Jurus |
|---|---|
| $t_0$ | manipulasi-aljabar |
| $t_1$ | faktorisasi · barisan-deret · nilai-mutlak · eksponen-logaritma · ketaksamaan-dasar · fungsi |
| $t_2$ | persamaan-kuadrat · sistem-persamaan · deret-teleskopik · induksi · am-gm |
| $t_3$ | vieta · suku-banyak · cauchy-schwarz · penataan-ulang · persamaan-fungsional |
| $t_4$ | akar-suku-banyak · teorema-sisa-faktor · substitusi-simetri · polinomial-bulat |
| $t_5$ | bilangan-kompleks |

`polinomial-bulat` berprasyarat `keterbagian` dari teori bilangan — prasyarat lintas
bidang pertama yang sungguhan. Hasil Fase 0 terbukti pada konten nyata: urutan tab
**Teori Bilangan lalu Aljabar** (abjad akan membalikkannya), dan simpulnya membawa
keterangan lengkap tentang gemboknya.

### 2.2 Soal — selesai 9 Agustus 2026

154 soal: 22 jurus × (1 contoh terpandu + 6 latihan), dikerjakan bertahap menurut tahap —
OSN-K (10 jurus, 70 soal), OSN-P (7 jurus, 49 soal), OSN (5 jurus, 35 soal).

`polinomial-bulat` akhirnya punya soal, sehingga jalur lintas bidang dari `keterbagian`
di teori bilangan ke aljabar bisa ditempuh sungguhan — bukan hanya digambar di peta.

**Selesai kalau:** ketiga tahap aljabar tuntas di lantai 6, `build.py` tidak lagi
mencetak "Belum ada latihan di:", dan simulasi bisa menyusun naskah dua bidang.

Catatan: bidang ini tidak berhenti di OSN-P. Draf awal rencana ini membolehkan jalur OSN
menyusul; itu ditarik, karena membiarkan satu bidang setengah terisi sambil membuka bidang
berikutnya persis yang dilarang di bagian Risiko.

---

## Fase 3 — Kombinatorika

### 3.1 Kerangka bidang — selesai 9 Agustus 2026

20 jurus beserta graf prasyaratnya, masing-masing lengkap dengan "Kapan dipakai",
"Intinya", dan "Jebakan umum". Sebarannya **10 OSN-K, 6 OSN-P, 4 OSN**, kedalaman $t_0$
sampai $t_5$ — dasarnya lebar, puncaknya sempit, seperti dua bidang sebelumnya.

| Tingkat | Jurus |
|---|---|
| $t_0$ | aturan-pencacahan |
| $t_1$ | inklusi-eksklusi · permutasi · sarang-merpati |
| $t_2$ | kombinasi · permutasi-berulang · permutasi-siklik · invarian |
| $t_3$ | koefisien-binomial · probabilitas-diskret · stars-and-bars · pencacahan-ganda · rekursi · pewarnaan · derangement |
| $t_4$ | bijeksi · graf-dasar · teori-permainan · fungsi-pembangkit |
| $t_5$ | ekstremal |

Dua penempatan yang perlu dicatat karena tidak mengikuti draf awal. **`inklusi-eksklusi`
diletakkan di $t_1$**, sebelum kombinasi, karena ia sebenarnya aturan jumlah yang
diperbaiki untuk kelompok beririsan — $|A \cup B| = |A| + |B| - |A \cap B|$ tidak
memerlukan $\binom{n}{k}$ sama sekali. **`ekstremal` berprasyarat `graf-dasar`**, bukan
berdiri sendiri, karena penerapan bakunya memang pada graf: ambil lintasan terpanjang,
lalu perhatikan tetangga titik ujungnya.

`rekursi` berprasyarat `induksi` dari aljabar — **prasyarat lintas bidang kedua**, dan
alasannya nyata: rumus tertutup yang ditebak dari beberapa suku pertama harus dibuktikan
dengan induksi. Gemboknya terbaca lengkap di peta ("Prasyarat dari bidang lain: Induksi
Matematika (Aljabar)").

Fase ini juga menutup dua celah yang baru terlihat sekarang:

- **Aturan tahap prasyarat kini dijaga tes.** Jurus OSN-K tidak boleh berprasyarat jurus
  OSN-P atau OSN — kalau melanggar, siswa yang menyaring peta ke OSN-K melihat gembok
  yang penyebabnya tidak ada di layar, dan tidak bisa membukanya tanpa keluar dari tahap
  yang sedang ia siapkan. Kedua bidang lama ternyata sudah memenuhinya; sekarang aturan
  itu tidak lagi bergantung pada ingatan.
- **`periksa-rumus.js` ternyata tidak pernah memeriksa halaman jurus** — ia hanya membaca
  `data/soal-*.json`. Padahal "Intinya" justru bagian paling padat rumus di seluruh situs,
  dan halaman jurus dibuka jauh lebih sering daripada satu soal tertentu. Sekarang
  keduanya diperiksa: 10.305 rumus, naik dari 9.288, dan 1.017 selisihnya itu rumus
  halaman jurus yang selama ini tidak pernah diuji. Semuanya lolos.

### 3.2 Soal — selesai 9 Agustus 2026

140 soal: 20 jurus × (1 contoh terpandu + 6 latihan), dikerjakan bertahap menurut tahap —
OSN-K (10 jurus, 70 soal), OSN-P (6 jurus, 42 soal), OSN (4 jurus, 28 soal).

Sebarannya **108 isian, 32 uraian**, dan porsi uraiannya naik tajam menurut tahap:

| Tahap | Soal | Uraian | Porsi |
|---|---|---|---|
| OSN-K | 70 | 10 | 14% |
| OSN-P | 42 | 12 | 29% |
| OSN | 28 | 10 | 36% |

Kenaikan itu mengikuti isinya, bukan target. Jurus OSN-K kombinatorika sebagian besar
soal hitung; `invarian`, `pencacahan-ganda`, `bijeksi`, `pewarnaan`, `ekstremal`, dan
`teori-permainan` semuanya teknik **pembuktian**, dan mengubahnya jadi soal isian akan
menguji hal yang berbeda dari yang dilatih.

Yang paling jelas pada `invarian`: menebak besaran yang kekal itu mudah, dan yang
sesungguhnya menentukan adalah **membuktikan tiap langkah tidak mengubahnya**. Bagian itu
tidak punya tempat di soal isian. Rubriknya karena itu memikul beban paling berat di bidang
ini — dan tiap rubrik menyebut langkah yang harus terlihat di lembar jawaban, bukan sekadar
"jawaban benar".

**Verifikasi menangkap satu kekeliruan** sebelum soalnya ditulis: rumus tertutup untuk
$a_n = 2a_{n-1}+3a_{n-2}$ yang semula diturunkan sebagai $\frac{3^n+3(-1)^n}{4}$ tidak
cocok dengan rekurensnya; yang benar $\frac{3^n+(-1)^n}{2}$. Soal `rek-04` sekarang
menekankan mencocokkan rumus tertutup dengan beberapa suku pertama sebelum dipakai —
persis langkah yang menangkapnya. Tabel sebaran empat warna pada `pwn-06` juga dikoreksi
setelah dihitung ulang.

Fase ini juga menutup dua celah kerangka: `periksa-rumus.js` ternyata tidak pernah
memeriksa halaman jurus (lihat 3.1), dan aturan tahap prasyarat kini dijaga tes.

**Selesai kalau:** ketiga tahap kombinatorika tuntas di lantai 6, `build.py` tidak lagi
mencetak "Belum ada latihan di:", dan simulasi bisa menyusun naskah tiga bidang. **Ketiganya
terpenuhi**, dan naskah tiga bidang sudah diperiksa di peramban.

---

## Fase 4 — Geometri

### 4.1 Dukungan gambar — selesai 10 Agustus 2026

Dikerjakan sebelum satu jurus geometri pun ditulis. Yang terpasang:

- aturan `![alt](berkas)` → `<img>` di `_sebaris()`, dipasang **sebelum** pola tautan
  supaya tanda serunya ikut termakan
- `build.py` memeriksa rujukan gambarnya lewat `periksa_gambar()` — pola yang sama dengan
  pemeriksaan prasyarat dan rujukan soal
- `alt` wajib diisi dan tidak boleh sekadar "gambar"; bagi siswa yang memakai pembaca
  layar, itu satu-satunya isi soalnya
- gambar berformat **SVG**, bukan PNG: tajam di segala ukuran, kecil, dan ikut tema
- aturan `img` di `styles.css` supaya gambar tidak tumpah di layar ponsel
- 26 tes baru di `tests/test_build.py` (63 → 89)
- `sw.js`: rajah masuk cache lewat `berkasLatar()`, `CACHE` naik ke v11

**Rajah dihitung, bukan digambar tangan.** Ini keputusan terbesar fase ini dan tidak ada
di draf rencana. `scripts/rajah.py` menyediakan primitif (ruas, poligon, lingkaran, busur,
tanda sudut/sama/siku) plus konstruksi terhitung — `pusat_dalam`, `pusat_luar`,
`titik_tinggi`, `kaki`, `potong`, `singgung`, `garis_bagi`. Sumbernya `konten/rajah/*.py`,
keluarannya `assets/rajah/*.svg`, dibangkitkan `build.py` sendiri supaya alur GitHub
Actions yang sudah mengomit balik hasil build ikut membangkitkannya.

Alasannya sama dengan alasan situs ini memakai verifikasi Python untuk jawaban: rajah
dibaca dengan mata, dan lingkaran dalam yang meleset sedikit tidak menggagalkan apa pun —
ia hanya mengajarkan hal yang salah, diam-diam. Yang diuji karena itu bukan keluaran
SVG-nya melainkan geometrinya: lingkaran dalam benar-benar menyinggung ketiga sisi,
lingkaran luar lewat ketiga titik sudut, dan $H$, $G$, $O$ segaris dengan $HG : GO = 2 : 1$.
Uji garis Euler itu yang paling murah dan paling tajam — kalau salah satu dari ketiga titik
istimewa salah rumus, ketiganya berhenti segaris.

**Satu janji di rencana ini ternyata salah dan sudah dikoreksi.** Draf 4.1 menjanjikan
gambar "ikut berubah warna mengikuti tema". Dengan `<img src="rajah.svg">` itu **tidak
terjadi**: SVG yang dimuat lewat `<img>` adalah dokumen terpisah yang tidak melihat CSS
halaman sama sekali, jadi `var(--tinta)` dan `currentColor` mati di sana. Yang berlaku
adalah media query milik SVG-nya sendiri, jadi tiap rajah kini membawa paletnya sendiri
beserta `@media (prefers-color-scheme: dark)`, dicap `rajah.py`. Kebetulan situs ini
memang hanya mengikuti tema OS tanpa tombol tema manual, jadi cara itu cukup — tapi harus
disengaja. Sudah diperiksa di peramban sungguhan: WebKit dan Blink dua-duanya
menghormatinya, dan rajah 700 px di wadah 289 px menyusut dengan nisbah terjaga tanpa
membuat halaman menggulung mendatar.

Konsekuensinya untuk perawatan: **palet tersalin di dua tempat**, `styles.css` dan
`GAYA` di `rajah.py`. Tidak ada cara bagi SVG lepas untuk ikut sendiri; yang bisa
dilakukan cuma mencatatnya, dan itu sudah ada di CLAUDE.md.

### 4.2 Kerangka bidang — selesai 10 Agustus 2026

21 jurus beserta graf prasyaratnya, masing-masing lengkap dengan "Kapan dipakai",
"Intinya", dan "Jebakan umum". Sebarannya **10 OSN-K, 7 OSN-P, 4 OSN**, kedalaman $t_0$
sampai $t_5$ — dasarnya lebar, puncaknya sempit, seperti tiga bidang sebelumnya.

| Tingkat | Jurus |
|---|---|
| $t_0$ | sudut-garis |
| $t_1$ | kekongruenan · pythagoras · sudut-lingkaran |
| $t_2$ | kesebangunan · luas-bidang · segiempat-talibusur · garis-singgung |
| $t_3$ | geometri-analitik · geometri-ruang · garis-istimewa · trigonometri-segitiga · kuasa-titik · ceva-menelaus · transformasi |
| $t_4$ | titik-istimewa · ptolemy · homoteti · ketaksamaan-geometri · tempat-kedudukan |
| $t_5$ | garis-euler |

Saringan tahap memberi 10 → 17 → 21 simpul, sudah diperiksa di peramban bersama tinggi
SVG-nya (496 → 608 → 720).

Tiga penempatan yang perlu dicatat karena tidak mengikuti daftar draf.

**`geometri-ruang` diletakkan di OSN-K**, bukan di tahap yang lebih tinggi seperti kesan
namanya. Bangun ruang materi SMA baku dan muncul di tingkat kabupaten; yang membuatnya
terasa sulit bukan tahapnya melainkan langkah pertamanya, dan langkah itu — pisahkan satu
bidang datar dari gambarnya, lalu kerjakan sebagai soal bidang — ditulis eksplisit di
"Kapan dipakai".

**`transformasi` tidak berprasyarat `geometri-analitik`.** Draf awal menghubungkan
keduanya, dan itu ditarik: transformasi di olimpiade dipakai secara sintetik — rotasi
$60^\circ$ pada bangun sama sisi, pencerminan untuk lintasan terpendek — dan koordinat
hanya salah satu cara menuliskannya, bukan prasyaratnya. Selain lebih jujur, penarikan itu
sekaligus menjaga kedalaman bidang ini tetap $t_5$ seperti tiga bidang lain, bukan $t_6$.

**`ekstremal`-nya geometri adalah `ketaksamaan-geometri`**, dan ia berprasyarat `am-gm`
dari aljabar — **prasyarat lintas bidang ketiga**. Alasannya nyata dan spesifik:
substitusi Ravi mengubah ketiga sisi segitiga menjadi tiga peubah positif yang bebas,
dan begitu kendalanya hilang, yang mengerjakan sisanya memang AM-GM. Prasyarat lintas
bidang keempat, `geometri-analitik` ← `persamaan-kuadrat`, juga nyata: memotongkan garis
dengan lingkaran menghasilkan persamaan kuadrat, dan diskriminannya yang menjawab
menyinggung atau memotong.

Verifikasi ikut dijalankan sebelum menulis, mengikuti kebiasaan fase-fase sebelumnya:
klaim lingkaran sembilan titik dihitung ulang pada tiga segitiga berbeda — kesembilan
titiknya jatuh pada lingkaran berpusat titik tengah $OH$ berjari-jari $R/2$ dengan
simpangan $10^{-16}$, dan $HG : GO$ keluar tepat $2$. Angka-angka itu baru ditulis ke
`garis-euler.md` setelah cocok.

Ongkos yang perlu diketahui: `data/jurus.json` naik dari 126 KB ke **189 KB**, dan ia ada
di `KERANGKA` — jadi muatan install ikut naik sekitar 63 KB. Masih jauh di bawah 1052 KB
sebelum Fase 0.5, tetapi ini bidang keempat dari empat, jadi angkanya tidak akan naik lagi
karena bidang baru.

### 4.3 Soal geometri

21 jurus × (1 contoh terpandu + 6 latihan) = **147 soal**, dikerjakan bertahap menurut
tahap seperti Fase 2.2 dan 3.2: OSN-K (10 jurus, 70 soal), OSN-P (7 jurus, 49 soal), OSN
(4 jurus, 28 soal).

Geometri paling lambat ditulis karena sebagian besar soal butuh bangun, dan tiap bangun
adalah satu berkas di `konten/rajah/`. Jadwalkan waktunya kira-kira dua kali lipat bidang
lain. Yang meringankan: rajahnya dihitung, jadi ongkos terbesarnya memilih koordinat yang
enak dilihat — bukan memastikan gambarnya benar.

**Tahap OSN-K — selesai 10 Agustus 2026.** 10 jurus, 70 soal (58 isian, 12 uraian), dengan
26 rajah.

**Tahap OSN-P — selesai 10 Agustus 2026.** 7 jurus, 49 soal (36 isian, 13 uraian), dengan
11 rajah baru sehingga seluruhnya menjadi 37. Porsi uraiannya **27%**, naik dari 17% di
OSN-K dan sejajar dengan OSN-P di dua bidang sebelumnya — dan seperti di sana, kenaikannya
mengikuti isinya. `ceva-menelaus` dan `ptolemy` teoremanya sendiri yang perlu dibuktikan;
`transformasi` hanya sah di lembar jawaban kalau peta tiap titik disebut; `titik-istimewa`
separuhnya perkara alasan, bukan hitungan.

Verifikasi menangkap satu kekeliruan sebelum soalnya ditulis, seperti di 3.2. Draf `tis-04`
menyatakan bahwa pada segitiga tumpul $\angle AHB$ berubah menjadi $\angle C$; perhitungan
ulang menunjukkan yang menentukan bukan tumpul atau tidaknya segitiga, melainkan **sudut
mana** yang tumpul. Kalau $\angle A$ dan $\angle B$ keduanya lancip — termasuk saat
$\angle C$ sendiri tumpul — hubungan $180^\circ - \angle C$ tetap berlaku. Pembahasannya
sekarang memuat percabangan itu beserta alasannya.

Yang perlu dicatat untuk tahap terakhir, karena baru terlihat saat menulis:

- **`ukuran()` menaruh label lewat "menjauhi pusat", dan pusat itu rata-rata semua titik
  acuan** — termasuk titik bantu di luar bangunnya. Pada bangun pipih (segitiga tumpul
  4-13-15), pada titik yang nyaris menempel sisi (P di segitiga sama sisi), dan pada sisi
  yang titik tengahnya justru dipakai titik lain (O di titik tengah sisi miring), arah
  bawaannya meleset dan angkanya jatuh di tempat yang salah baca. Tiga rajah di tahap ini
  karena itu memakai `label(..., arah=…, gaya="ukur")` dengan arah yang ditentukan tangan
  beserta alasannya di komentar.
- **Rajah yang menjawab soalnya sendiri tidak berguna.** Titik hasil putaran pada
  `sama-sisi-titik-dalam` dan cerminan A pada `cermin-lintasan-terpendek` sengaja tidak
  digambar: menemukannya seluruh isi soalnya. Yang digambar hanya apa yang disebut soal.
- **Rajah kuasa titik wajib dihitung mundur dari panjang yang diminta.** Siswa mengukur di
  gambar, jadi gambar yang meleset mengajarkan hasil kali yang salah.
  `talibusur-berpotongan` menolak berkasnya sendiri kalau hasil kali kedua ujungnya tidak
  sama dengan kuasa titiknya.

**Tahap OSN — selesai 11 Agustus 2026.** 4 jurus, 28 soal (17 isian, 11 uraian), dengan
12 rajah baru sehingga seluruhnya menjadi 49. Porsi uraiannya **39%**, melanjutkan
17% → 27% → 39% yang mengikuti isinya, bukan target: `ketaksamaan-geometri` seluruhnya
teknik pembuktian, dan `tempat-kedudukan` menuntut bukti **dua arah** sehingga tidak
punya bentuk isian yang jujur.

| Jurus | Contoh + latihan | Yang menjadi tulang punggungnya |
|---|---|---|
| `homoteti` | 7 | pusat homoteti pada dua lingkaran bersinggungan |
| `garis-euler` | 7 | $OH^2 = 9R^2 - (a^2+b^2+c^2)$, lingkaran sembilan titik |
| `ketaksamaan-geometri` | 7 | substitusi Ravi, pencerminan, putaran $60^\circ$ |
| `tempat-kedudukan` | 7 | bukti dua arah, garis kuasa, garis kutub |

Empat hal yang perlu dicatat, karena baru terlihat saat menulis tahap ini:

- **`busur()` di `rajah.py` melebarkan viewBox ke seluruh lingkarannya.** Ia mencatat
  kotak pembatas lingkaran penuh, bukan busurnya. Selama 43 rajah pertama tidak ada yang
  memakainya, jadi tidak ada yang tahu. Rajah "dua busur bercermin pada AB" langsung
  menabraknya: pusatnya jauh di seberang $AB$, dan viewBox-nya melar dari 277×118 menjadi
  sekitar 462×862 — bangunnya menyusut sampai tidak terbaca di halaman yang mengecilkannya
  agar muat. Sekarang batasnya dihitung dari kedua ujung busur plus arah mata angin yang
  dilewatinya, dijaga dua tes: satu menuntut kotaknya tidak melar, satu lagi menuntut
  busur yang melengkung melewati puncaknya tetap termuat utuh. Tes kedua itu yang mencegah
  perbaikannya jadi terlalu bersemangat.
- **Jawaban isian tidak boleh berbentuk akar atau pecahan yang tidak persis.**
  `periksaJawaban()` membandingkan sebagai angka lewat `Number()`, dan `Number("3/2")`
  adalah `NaN` — jadi pecahan hanya cocok kalau siswa mengetiknya persis sama. Draf
  `ktg-03` semula menanyakan nilai terbesar $\cos A + \cos B + \cos C$, yang jawabannya
  $\tfrac32$. Soalnya ditulis ulang menjadi mencari $r$ dari $R = 10$ dan jumlah kosinus
  $\tfrac75$ — jawabannya $4$, dan versi barunya justru lebih baik karena menuntut
  memeriksa dulu bahwa segitiganya ada, lewat $R \ge 2r$.
- **Verifikasi menangkap satu kekeliruan lagi**, seperti di 3.2 dan 4.3 OSN-P. Draf
  `ktg-04` menyebut segitiga merosot sama kaki ($a=b=1$, $c \to 2$) sebagai keluarga yang
  mendekatkan $\sum \tfrac{a}{b+c}$ ke batas $2$. Hitungan menunjukkan keluarga itu
  berhenti di $\tfrac53$; yang benar-benar mendekati $2$ adalah yang merosot **dan
  timpang**, $1 : t : t+\tfrac12$ dengan $t$ besar. Soalnya sekarang menjadikan perbedaan
  itu bagian yang dinilai, sebab persis di situ kekeliruannya.
- **Tempat kedudukan menuntut rajah yang menahan diri lebih keras daripada biasanya.**
  Pada `talibusur-lewat-titik-tetap`, menggambar lingkaran berdiameter $OA$ berarti
  menuliskan jawabannya; menggambar $OM$ berarti menuliskan buktinya. Lebih halus lagi:
  arah tali busurnya tidak boleh sembarangan — yang searah $OA$ menjatuhkan titik tengah
  tepat di $O$, yang tegak lurus $OA$ menjatuhkannya tepat di $A$, dan dua-duanya
  terbaca sebagai kebetulan. Draf pertama kena yang pertama, dan berkasnya sekarang
  menolak arah yang terlalu dekat ke keduanya.

**Selesai kalau:** ketiga tahap geometri tuntas di lantai 6, `build.py` tidak lagi
mencetak "Belum ada latihan di:", dan simulasi bisa menyusun naskah empat bidang.
**Ketiganya terpenuhi.**

---

## Fase 5 — Soal asli: tautkan, jangan simpan ulang

**Diputuskan 8 Agustus 2026.** Sebagian besar soal tetap susunan sendiri dengan gaya OSN.
Di atas itu, naskah asli boleh dipakai — untuk sekarang **satu naskah, OSN 2025**, yang
diunduh sendiri dari situs resmi penyelenggara.

### Satu perbedaan yang menentukan seluruh rancangan ini

"Gratis diunduh" dan "bebas disebarkan ulang" adalah dua izin yang berbeda. Situs resmi
memberi izin mengunduh dan memakai; menaruh salinan berkasnya di repo publik ini adalah
**penyebaran ulang**, izin terpisah yang tidak otomatis ikut. UU 28/2014 Pasal 42
mengecualikan peraturan perundang-undangan, putusan pengadilan, dan pidato kenegaraan
dari hak cipta — naskah ujian tidak ada di daftar itu, jadi hak ciptanya kemungkinan
tetap ada pada penerbitnya. Ini catatan, bukan nasihat hukum.

**Karena itu: tidak ada PDF yang disimpan di repo ini.** Yang disimpan hanya metadata
dan tautan ke berkas resminya. Keputusan ini bukan sekadar main aman — ia menghapus
seluruh pekerjaan yang tadinya menempel pada penyimpanan PDF: repo tidak bengkak (git
tidak mengompres PDF antar-revisi), `sw.js` tidak perlu disentuh, dan `KERANGKA` tidak
terancam gagal install karena satu berkas besar meleset.

Risiko yang tersisa adalah tautan mati. Ditangani dengan mencatat metadata cukup lengkap
supaya naskahnya tetap teridentifikasi meski tautannya suatu saat pindah.

### 5.1 Daftar arsip — selesai 9 Agustus 2026

Skemanya dibangun lebih dulu, **daftarnya masih kosong**, dan itu keadaan yang benar:
belum ada naskah resmi yang diunduh sendiri, jadi belum ada yang boleh diberi atribusi.
Yang penting sudah berdiri adalah penegakannya, dan itu yang selama ini cuma dititipkan
ke ingatan — CLAUDE.md sudah menulis aturan `konten/arsip.yml` sejak lama padahal
berkasnya belum ada dan tidak ada apa pun yang memeriksanya.

Satu naskah menaungi banyak soal, jadi jangan tempelkan tautan di tiap berkas soal —
akan terduplikasi dan tidak bisa dijaga konsisten. Sebagai gantinya `konten/arsip.yml`:

```yaml
osn-2025:
  judul: OSN Matematika SMA 2025
  penyelenggara: Puspresnas/BPTI, Kemendikbudristek
  tahun: 2025
  tahap: osn          # sesuaikan: osn-k / osn-p / osn
  tautan: https://…   # halaman resmi tempat naskahnya diunduh
  diakses: 2026-08-08
```

Berkas soal lalu merujuknya:

```yaml
sumber: OSN 2025 nomor 3
arsip: osn-2025
nomor: 3
```

`build.py` sekarang memeriksa tiga hal, semuanya lewat `galat` yang dikumpulkan seperti
pemeriksaan lain:

1. tiap entri `arsip.yml` lengkap keenam kuncinya, tahapnya sah, dan tautannya benar-benar
   alamat web — entri setengah terisi membuat naskahnya tidak bisa dikenali lagi begitu
   tautannya mati, dan tautan mati satu-satunya risiko yang tersisa dari tidak menyimpan
   PDF;
2. `arsip` yang dirujuk soal memang ada di daftar — pola yang sama dengan prasyarat dan
   rujukan soal;
3. `sumber` yang berbunyi seperti atribusi tahun+lomba (`OSN 2025 nomor 3`) **wajib**
   punya `arsip` yang sah.

Yang ketiga itu penegakan atas "Atribusi merayap" di bagian Risiko. Polanya sengaja
tidak menangkap `susunan sendiri, gaya OSN-K` — yang dijaga klaim tahunnya, bukan
penyebutan nama lombanya — dan seluruh 309 soal yang ada lolos tanpa satu pun perlu
disunting. Contoh di README yang tadinya berbunyi `sumber: OSN-P 2019, soal 7` ikut
diperbaiki, karena dokumentasi itu justru mengajarkan pola yang kini ditolak.

Dengan itu, atribusi ke naskah asli jadi sesuatu yang **diperiksa mesin**, bukan teks
bebas. Mengutip satu soal untuk dibahas bukan hal yang sama dengan menyebarkan ulang
seluruh naskah, dan pembahasan itulah inti situs ini.

### 5.2 Aturan naskah dari simpanan orang lain

Naskah tahun-tahun sebelumnya dari simpanan orang lain **beda perkara**, dan posisinya
lebih lemah, bukan lebih kuat:

- asal-usulnya tidak bisa diverifikasi — kamu tidak tahu itu naskah resmi atau ketikan
  ulang seseorang;
- salinan tak resmi sering memuat salah ketik, dan salah ketik pada soal olimpiade
  biasanya mengubah soalnya jadi soal lain, kadang jadi soal yang tidak punya jawaban.

Aturannya: **hanya naskah yang kamu unduh sendiri dari situs resmi yang boleh diberi
atribusi tahun dan nomor.** Kalau soal dari sumber tak resmi ternyata bagus, tulis ulang
sebagai soal susunan sendiri dan beri label begitu. Itu jujur, dan hasilnya sering lebih
berguna karena bisa diarahkan ke satu jurus tertentu.

### 5.3 Penempatannya di rencana

Naskah OSN 2025 masuk ke tahap sesuai jenjangnya: kalau itu naskah OSN-K ia memperkuat
Fase 1.1, kalau OSN nasional ia masuk Fase 1.3 yang dikerjakan paling akhir. Isi `tahap`
di `arsip.yml` sesuai naskah yang ada di tanganmu.

Fase ini kecil — skema arsip plus satu entri — dan bisa dikerjakan kapan saja setelah
Fase 0. Membangunnya sekarang dengan satu naskah justru bagus: skemanya teruji pada
kasus nyata selagi ongkos ubahnya masih nol.

**Keadaan 11 Agustus 2026: `konten/arsip.yml` masih kosong isinya** — 53 baris, seluruhnya
komentar. Penegakannya berdiri, daftarnya belum. Itu bukan kelalaian: belum ada naskah
resmi yang diunduh sendiri, jadi belum ada yang boleh diberi atribusi. Fase ini tidak bisa
dijadwalkan sendirian karena langkah pertamanya bukan pekerjaan kode.

---

## Fase 6 — Sesudah keempat bidang penuh

Ditulis 11 Agustus 2026, setelah Fase 4 tuntas. Semua yang di bawah ini punya angka atau
pemicu yang bisa dilihat orang lain; yang cuma terasa perlu tidak dimasukkan.

Urutannya **bukan** menurut mana yang lebih cepat terasa oleh siswa — itu argumen yang
sudah ditolak di bagian Risiko. Urutannya menurut mana yang paling mahal diperbaiki kalau
ditunda.

### 6.1 Muatan yang diunduh tapi tidak pernah dibaca

Dua pengukuran, keduanya dengan pola yang sama dan keduanya baru terlihat setelah bidang
keempat masuk.

**Simulasi mengunduh 1829 KB — `jurus.json` 193 KB plus keempat berkas soal 1637 KB — dan
dari berkas soalnya ia hanya membaca 138 KB.** `susunNaskah()` memang perlu keempat
bidang; itu sudah diputuskan di 0.7 dan tidak berubah. Yang tidak perlu adalah isinya:
`simulasi.js` hanya menyentuh `id`, `soal`, `jawaban`, `bentuk`, `kesulitan`, `pilar`, dan
`tahap`. Ia tidak pernah merender pembahasan — untuk itu ia menautkan ke
`latihan.html?soal=…`, jadi ini bukan tebakan melainkan bisa dibaca di
`assets/simulasi.js`.

| Bagian tiap soal | Ukuran | Dipakai simulasi? |
|---|---|---|
| `pembahasan` | 1050 KB | tidak |
| `petunjuk` | 176 KB | tidak |
| `rubrik` | 72 KB | tidak |
| `soal` | 115 KB | ya |
| sisanya (`id`, `pilar`, `tahap`, …) | 61 KB | sebagian |

Dari 1474 KB nilai medan di keempat berkas soal, **1336 KB — 91% — tidak pernah dibaca**,
dan pembahasan sendirian 71%. Diukur terhadap seluruh 1829 KB yang diunduh halaman itu,
yang terbuang 73%.

**Peta mengunduh 193 KB untuk menggambar 7 KB.** `data/jurus.json` ada di `KERANGKA`,
jadi tiap install membayarnya — 193 KB dari 567 KB, sepertiga lebih. Dari 170 KB isi
simpulnya, yang dipakai `peta.js` untuk menggambar cuma `id`, `nama`, `pilar`, `tahap`,
`prasyarat`, dan koordinatnya. Sisanya prosa halaman jurus: `inti` 82 KB, `jebakan` 45 KB,
`kapan_dipakai` 30 KB.

Bentuk perbaikannya sudah ada presedennya di 0.5, termasuk pelajaran pahitnya: **memecah
berkas saja tidak cukup kalau pecahannya tetap di `KERANGKA`.** Yang perlu dijaga saat
mengerjakannya:

- `jurus.json` diambil lebih dulu dan sendirian karena `data.pilarSoal` diturunkan
  darinya, dan `berkasLatar()` di `sw.js` menurunkan daftar soal serta rajah dari situ
  juga. Pemecahan apa pun harus menjaga keduanya tetap ada di berkas yang diambil pertama.
- Naskah simulasi yang sudah berjalan tetap harus bisa membuka pembahasan sesudah waktu
  habis. Kalau isinya dipisah, jalur itu berubah dari "sudah ada di memori" menjadi
  "diambil saat diklik" — dan itu terjadi persis ketika siswa baru selesai ujian, jadi
  perilakunya saat luring harus diputuskan sadar, bukan kebetulan.
  **Diputuskan 11 Agustus 2026: bagian beratnya tetap ikut disimpan** — masuk daftar
  `berkasLatar()` di `sw.js`, sama seperti berkas soal sekarang. Yang dihemat pemecahan ini
  jadi muatan saat halaman dibuka (simulasi 1829 KB → sekitar 330 KB), bukan ruang simpan
  di perangkat. Pilihan sebaliknya menghemat ~1,3 MB tapi mematikan pembahasan saat luring
  tepat sesudah simulasi selesai, dan itu bertentangan dengan premis `sw.js` sendiri:
  latihan saat luring justru intinya.
- Ukur ulang dengan `node scripts/periksa-muatan.js` sebelum dan sesudah. Angka di atas
  keluar dari sana plus hitungan per-bagian; jangan percaya perkiraan.

Dikerjakan lebih dulu di antara butir-butir Fase 6 bukan karena paling terasa, melainkan
karena **jumlah bidang tidak akan bertambah lagi** — jadi angka-angka ini sudah pada
bentuk akhirnya, dan pemecahan yang dirancang sekarang tidak akan perlu dirancang ulang.

### 6.2 Primitif rajah yang tidak dipakai konten mana pun

`scripts/rajah.py` punya satu fungsi yang **tidak dipanggil satu rajah pun dan tidak
disentuh satu tes pun**: `potong_lingkaran`. `garis_bagi` juga tidak dipakai konten, tetapi
setidaknya dijaga `test_garis_bagi_memenuhi_teorema_garis_bagi`.

Ini bukan kerapian. `busur()` berada persis di keadaan itu sampai 11 Agustus 2026 — nol
pemakai, nol tes — dan ternyata mencatat kotak pembatas **lingkaran penuh**, bukan
busurnya. Rajah pertama yang memakainya keluar dengan viewBox sekitar 462×862 padahal
isinya 277×118. Bug itu duduk diam sepanjang 43 rajah karena tidak ada yang memanggilnya.

Pilihannya dua, dan dua-duanya sah:

1. **beri tes** yang menguji geometrinya, seperti tes primitif lain — misalnya kedua titik
   potong dua lingkaran benar-benar berjarak $r_1$ dan $r_2$ dari kedua pusatnya; atau
2. **hapus**, dan kembalikan kalau nanti ada rajah yang membutuhkannya.

Yang tidak sah adalah membiarkannya. Aturan yang layak dipegang seterusnya: **primitif di
`rajah.py` harus punya pemakai konten atau tes — kalau tidak keduanya, ia kode yang belum
pernah dijalankan siapa pun.**

### 6.3 Pemeriksaan kasar "petunjuk 1 bocor"

Bagian Risiko sudah menyebut ini dengan syarat "kalau sudah puluhan jurus". Sekarang 85,
jadi syaratnya lewat.

Aturannya — petunjuk 1 tidak boleh menyebut nama jurusnya — satu-satunya aturan isi
penting yang masih dititipkan ke ingatan. Versi kasarnya sudah dicoba tangan saat menulis
14 soal terakhir dan menemukan satu hal yang menentukan rancangannya: **yang dicocokkan
harus nama jurus pemiliknya, bukan semua jurus di medan `jurus:`.** Soal boleh menandai
beberapa jurus, dan menyebut jurus kedua di petunjuk 1 justru dorongan yang benar —
`tkd-03` menyebut "sudut keliling" pada petunjuk pertamanya, dan itu memang yang
dimaksudkan. Pencocokan terhadap seluruh medan `jurus:` menandainya sebagai pelanggaran
padahal bukan.

Karena itu: **peringatan, bukan galat**, mengikuti pola `periksa_gambar()` untuk rajah
nganggur. Akan ada pengecualian yang sah, dan pemeriksaan yang menggagalkan build karena
pengecualian sah adalah pemeriksaan yang akan dimatikan orang.

### 6.4 Lantai enam, dan apa yang di atasnya

Bagian 1 menulis "Enam soal adalah lantai, bukan target". Sekarang **ke-85 jurus punya
tepat enam latihan** — bukan rata-rata enam, melainkan enam persis, semuanya. Tidak ada
sebaran sama sekali: 596 soal terdiri atas 510 latihan (85 × 6) dan 86 contoh.

Lantai yang dipenuhi serentak seperti itu adalah tanda bahwa angkanya yang mengemudi,
bukan isinya — dan itu masuk akal selama tujuannya memang menutup keempat bidang. Sekarang
tujuannya sudah tercapai, jadi asumsinya layak ditinjau.

Itu berarti keputusan yang selama ini bisa ditunda kini harus diambil, dan ia keputusan
isi, bukan keputusan kode:

- **Menaikkan lantai secara merata** (misalnya ke 8) menambah sekitar 170 soal, dan
  memperlakukan semua jurus sama padahal beban ujiannya tidak sama.
- **Menambah kedalaman terpilih** pada jurus yang paling sering muncul di OSN memberi
  lebih banyak latihan di tempat yang paling dipakai, dengan ongkos: jurus lain tetap di
  enam, dan tangga ulang 60 hari pada jurus itu tetap mengulang soal yang sama.
- **Berhenti menambah soal** dan menganggap lantai enam cukup, lalu mengalihkan tenaga ke
  6.1–6.3 dan ke arsip.

**Diputuskan 11 Agustus 2026: kedalaman terpilih.** Perluas soal pada jurus yang
memerlukannya, sisanya dibiarkan di enam. Rambunya yang menentukan, dan ia sudah ada di
Risiko: **soal yang tidak memberi latihan mengenali pemicu tidak menambah apa pun meski
menaikkan angka.** Enam soal yang melatih enam pemicu berbeda lebih berharga daripada dua
belas soal yang melatih satu pemicu dua belas kali.

Rambu itu sekaligus memberi kriteria "yang perlu", dan kriterianya bukan seberapa penting
jurusnya: **jurus perlu diperluas kalau pemicunya lebih banyak daripada enam slotnya.**
Jurus dengan tiga pemicu tidak menjadi lebih baik dengan delapan soal; jurus dengan
sembilan pemicu sudah kekurangan pada enam.

#### Prasyaratnya: `kapan_dipakai` yang sebanding antarbidang

Kriteria itu **belum bisa dijalankan hari ini**, dan sebabnya terukur. `kapan_dipakai`
menebal sepanjang Fase 1→4, jadi jurus yang ditulis lebih dulu mendaftarkan pemicunya jauh
lebih sedikit — bukan karena pemicunya memang sedikit:

| Bidang | Median kata `kapan_dipakai` | Jurus tanpa satu pun pemicu ditandai |
|---|---|---|
| Teori bilangan | 23 | 3/22 |
| Aljabar | 23 | 10/22 |
| Kombinatorika | 54 | 2/20 |
| Geometri | 94 | 0/21 |

Setiap peringkat yang disusun dari medan ini karena itu memeringkat **fase penulisannya**,
bukan luas pemicunya — dicoba sekali dan seluruh sepuluh besarnya geometri. `build.py`
menegakkan medan ini tidak kosong, tetapi tidak ada yang menegakkan ia lengkap, dan untuk
medan yang disebut CLAUDE.md sebagai "bagian yang membuat situs ini ada" itu celah yang
lebih besar daripada jumlah soalnya.

Urutan kerjanya jadi tertentu:

1. **Tulis ulang `kapan_dipakai` aljabar dan teori bilangan** setara geometri — 44 jurus,
   13 di antaranya tanpa penanda sama sekali. Tidak ada soal baru di langkah ini.
2. **Baru daftarkan pemicu tiap jurus dan adu dengan enam latihannya.** Pemicu yang tidak
   punya soal itulah daftar perluasannya, dan tiap soal baru lahir dengan alasan yang
   tertulis.
3. **Perluas hanya jurus itu.**

Membalik urutannya berarti memilih soal dengan perasaan, yaitu persis yang dilarang rambu
di atas.

Dua sinyal yang **tidak** ikut terseret gaya penulisan sudah bisa dipakai sebagai calon
sementara, meski tak satu pun menggantikan langkah 2:

- **Dipakai soal jurus lain paling sering** — luas permukaan pemicu yang terlihat dari
  pemakaian: Keterbagian dan Ketaksamaan Dasar (5×), Barisan dan Deret, Teorema Pythagoras,
  Garis Singgung Lingkaran (4×).
- **Sebaran kesulitan tersempit** — enam latihan yang menumpuk di dua tingkat. Untuk jurus
  tahap OSN ini wajar dan bukan cacat; yang layak dilihat adalah yang di OSN-K/OSN-P,
  terutama **Induksi Matematika**, satu-satunya yang sekaligus dipakai 3× oleh jurus lain.

### 6.5 Gerbang nama jurus di sesi campuran — selesai 11 Agustus 2026

Ditemukan saat menilai situs ini sebagai kurikulum, bukan sebagai repo, dan ia lebih besar
daripada seluruh 6.3: **`assets/latihan.js` mencetak `Jurus: <nama>` tepat di atas soal,
sebelum siswa mencoba, di semua mode latihan.**

Aturan "petunjuk 1 tidak boleh menyebut nama jurusnya" ada supaya siswa berlatih mengenali
pemicu. Tapi kepala halamannya menyebutkan nama itu tanpa syarat — jadi gerbang petunjuk
menjaga pintu di tembok yang sisi lainnya terbuka. Akibat sebenarnya: siswa yang membuka
sesi harian tiap hari **tidak pernah sekali pun melatih keahlian yang jadi alasan situs ini
ada**. Ia selalu sudah diberi tahu jawabannya sebelum bertanya.

Ada dua kebocoran di halaman yang sama, bukan satu — baris `Jurus:` itu, dan `judulSesi`
yang pada satu cabang memang diisi nama jurus.

Perbaikannya **tidak seragam**, dan itu intinya:

- **Digerbang** kalau sesinya mencampur jurus — "Ulangan hari ini" (mode paling sering
  dibuka) dan `?soal=ID`. Namanya diganti "tebak dulu — muncul setelah dijawab", lalu
  dibuka oleh `bukaTandaJurus()` di dua jalur selesainya percobaan: sesudah "Jawab" pada
  isian, sesudah "Saya sudah mengerjakan" pada uraian. Sejalan dengan gerbang pembahasan —
  menahan intipan sebelum mencoba, bukan sesudah.
- **Tidak digerbang** pada latihan satu jurus berurutan (`?jurus=ID`, dan sesi baru yang
  seluruh soalnya dari satu jurus). Di situ siswa sudah tahu jurusnya dari cara ia masuk,
  dan judul sesinya memang menyebut namanya. Menyembunyikannya cuma sandiwara.

Simulasi sudah bersih sejak awal — ia hanya menampilkan nomor, tahap, dan bintang
kesulitan. Jadi kemampuan ini sebenarnya sudah ada di situs, hanya tidak dipakai di halaman
yang paling sering dibuka.

Diperiksa di peramban, bukan hanya di tes: tersembunyi sebelum dijawab, muncul sesudah.
`CACHE` dinaikkan ke `peta-jurus-v14`. Pelajaran samping yang layak diingat — muat ulang
pertama menampilkan versi lama, persis peringatan service worker di CLAUDE.md.

### 6.6 Lubang silabus — calon jurus baru

Berbeda dari 6.4. 6.4 tentang jurus yang **ada** tapi kurang dilatih; ini tentang teknik
yang **tidak ada sama sekali**. Empat, semuanya masih di dalam jangkauan OSN, dan semuanya
di bidang yang sudah ada — tidak ada pilar baru, jadi `URUT_PILAR` tidak tersentuh.

| Calon | Bidang | Tahap | Kenapa masuk daftar |
|---|---|---|---|
| Residu kuadratik / simbol Legendre | teori bilangan | osn-p | "apakah $x^2 \equiv a \pmod p$ punya solusi" alat baku; ketiadaannya paling terasa |
| Kecekungan dan Jensen (plus SOS) | aljabar | osn | tempat jatuhnya ketaksamaan OSN ketika AM-GM dan Cauchy mentok |
| Sudut berarah | geometri | osn-p | bukan teorema melainkan teknik; mencegah salah konfigurasi, penyebab kehilangan angka yang khas |
| Teorema Hall / pemadanan | kombinatorika | osn | satu-satunya cara baku menjawab soal "bisakah dipasangkan" |

Sudut berarah adalah yang paling tidak lazim di antara keempatnya karena ia bukan jurus
dalam arti "teorema yang dipakai", melainkan kebiasaan menulis. Kalau bentuk `kapan_dipakai`
terasa dipaksakan untuknya, itu tanda ia lebih tepat menjadi bagian `jebakan` di jurus-jurus
lingkaran daripada simpul sendiri — putuskan saat menulisnya, jangan sekarang.

Sebelum satu pun ditulis, ingat urutan yang sudah ditetapkan 6.4: **`kapan_dipakai` yang
sebanding lebih dulu.** Menambah jurus baru sementara 13 jurus lama belum mendaftarkan
pemicunya berarti memperlebar peta yang setengahnya belum terbaca.

### 6.7 Yang sengaja belum masuk Fase 6

Supaya tidak dikira terlupa:

- **Menempuh satu jalur utuh sebagai siswa sungguhan**, dari jurus pertama sampai simulasi,
  belum pernah dilakukan. Ini menggoda ditulis sebagai butir rencana, tetapi ia bukan
  pekerjaan yang bisa diselesaikan — ia pemeriksaan yang hasilnya melahirkan butir lain.
  Kerjakan kalau ingin, jangan jadwalkan.
- **Ukuran `data/soal-geometri.json` yang 602 KB**, terbesar di antara keempat bidang
  karena pembahasan geometri memuat rajah dan percabangan kasus. Ia tidak di `KERANGKA`
  dan diambil di latar, jadi belum ada angka yang menunjukkan ia masalah. Kalau 6.1
  dikerjakan, angka ini ikut turun dengan sendirinya.

**Selesai kalau:** tidak ada lagi berkas data yang diunduh sebuah halaman tanpa dibaca
sebagian besarnya, `rajah.py` tidak punya fungsi tanpa pemakai sekaligus tanpa tes, dan
aturan petunjuk 1 tidak lagi bergantung pada ingatan. Arahnya 6.4 sudah **diputuskan**
(kedalaman terpilih), jadi yang tersisa di sana pekerjaan: `kapan_dipakai` sebanding
antarbidang lebih dulu, daftar pemicu sesudahnya, soal baru paling akhir. 6.5 sudah
selesai; 6.6 menunggu langkah pertama 6.4.

Satu hal yang **tidak** akan selesai di dalam repo ini, dan sebaiknya ditulis supaya tidak
diam-diam dianggap tertutup: naskah OSN asli dan **seseorang yang membaca pembuktianmu**.
Rubrik penilaian sendiri bisa memeriksa apakah langkahnya ada, tapi tidak bisa memberi tahu
bahwa argumenmu berlubang di tempat yang kamu kira rapat. Berapa pun soal ditambahkan, itu
tetap harus datang dari luar.

---

## Yang sengaja tidak dikerjakan

Ditulis supaya tidak berulang kali diperdebatkan:

- **Tidak ada akun dan tidak ada server.** Kemajuan tetap di localStorage. Ekspor/impor
  sudah ada di `assets/inti.js:321` dan terpasang di halaman jurnal — itu jalur pindah
  perangkat, dan itu cukup.
- **Tidak ada penilaian otomatis untuk soal uraian.** Rubrik dan penilaian sendiri.
  Memeriksa bukti secara otomatis adalah proyek lain.
- **Tidak ada papan peringkat, lencana, atau runtun harian.** Tangga ulangnya sudah jadi
  alasan untuk kembali; menumpuk pemicu di atasnya menggeser tujuan dari menguasai
  jurus ke menjaga angka.
- **Tidak ada pustaka graf, kerangka kerja, atau langkah build untuk situsnya.** Yang
  di-build hanya isinya.
- **Tidak ada `jawaban_alt` yang ditebak kode.** `periksaJawaban()` tetap lugu; setiap
  varian ditulis eksplisit.
- **Tidak ada PDF naskah yang disimpan di repo ini.** Arsip hanya menyimpan metadata dan
  tautan ke berkas resminya — lihat Fase 5. Mengunduh dan menyebarkan ulang adalah dua
  izin yang berbeda.

---

## Risiko

**Melebar sebelum dalam.** Godaan terbesarnya adalah membuka empat bidang sekaligus dan
mengisi masing-masing sepertiga. Hasilnya empat bidang setengah jadi yang tidak bisa
dipakai siapa pun untuk apa pun. Urutan fase di atas ada justru untuk mencegah itu:
satu bidang ditutup tuntas sampai tahap tertinggi sebelum bidang berikutnya dibuka.

**Tergoda mempercepat supaya cepat dipakai.** Ini bukan tujuan proyek, dan ditulis di
sini supaya tidak menyelinap masuk lewat pintu belakang. Situs ini akan dipakai ketika
sudah terbukti bisa ditempuh utuh dari awal sampai akhir — bukan ketika sudah "cukup
untuk sebagian siswa". Karena itu, saat memilih urutan pekerjaan, argumen "ini lebih
cepat berdampak" tidak sah; yang sah adalah kelengkapan dan ketahanan jangka panjang.
Konsekuensi praktisnya: lantai 6 latihan tidak boleh dilonggarkan, jurus tidak boleh
dibiarkan setengah terisi untuk mengejar bidang berikutnya, dan pekerjaan kerangka
tidak ditunda dengan alasan kontennya lebih terlihat.

**Mutu soal turun saat mengejar jumlah.** Lantai 6 latihan per jurus bisa dipenuhi
dengan enam soal seragam yang melatih satu pola yang sama. Yang membuat situs ini ada
adalah `## Kapan dipakai` — pemicunya, bukan rumusnya. Soal yang tidak memberi latihan
mengenali pemicu tidak menambah apa pun meski menaikkan angka.

**Atribusi merayap.** Begitu ada satu naskah asli di dalam situs, soal asli dan soal
susunan sendiri duduk berdampingan — dan siswa tidak lagi bisa menganggap semuanya
susunan sendiri. Justru di situ labelnya jadi genting: soal karangan yang diberi label
`OSN-K 2015 nomor 3` sekarang terbaca sebagai naskah asli, karena naskah asli memang ada.

Bedanya dengan sebelumnya, ini sekarang **ditegakkan mesin** — dikerjakan bersama 5.1
pada 9 Agustus 2026: `build.py` menolak `sumber` yang berpola atribusi nyata (tahun empat
angka berdampingan "OSN"/"KSN") kalau soal itu tidak punya `arsip` yang merujuk entri sah.
Bukan peringatan, tapi galat, karena sekarang ada daftar arsip untuk dicocokkan.

**Petunjuk 1 bocor.** Aturan "petunjuk 1 tidak boleh menyebut nama jurus" tidak bisa
ditegakkan mesin, dan paling mudah dilanggar saat menulis banyak soal sekaligus. Kalau
sudah puluhan jurus, pertimbangkan pemeriksaan kasar di `build.py` yang menandai
petunjuk pertama memuat nama jurusnya sebagai peringatan — bukan galat, karena akan ada
pengecualian yang sah.

**`sw.js` menyembunyikan pembaruan.** Setiap aset berubah, `CACHE` di `sw.js:8` harus
naik, dan berkas tingkat atas yang baru harus masuk `KERANGKA`. Terlewat sekali, dan
siswa memegang versi lama tanpa tanda apa pun bahwa ada yang baru. Sekarang situsnya
sudah tayang di <https://fakhri24.github.io/peta-jurus/>, jadi ini menyentuh pengunjung
sungguhan, bukan lagi cuma menyulitkan saat mengembangkan.
