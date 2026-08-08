# Rencana: dari kerangka ke alat persiapan olimpiade

Dokumen ini menjawab satu pertanyaan: **apa saja yang masih kurang sebelum situs ini
benar-benar bisa dipakai siswa SMA menyiapkan OSN atau lomba matematika lain.**

Ditulis 8 Agustus 2026. Perbarui angkanya kalau sudah tidak cocok — rencana yang
angkanya basi lebih menyesatkan daripada tidak ada rencana.

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

22 jurus, 155 soal (132 latihan + 23 contoh), semuanya teori bilangan.
`data/soal.json` sudah 287 KB — lihat catatan pada 0.5.

Sebaran per tahap:

| Tahap | Jurus | Sudah di lantai 6 | Kosong |
|---|---|---|---|
| OSN-K | 8 | 8 | 0 |
| OSN-P | 10 | 10 | 0 |
| OSN | 4 | 4 | 0 |

**Teori bilangan tuntas sejak 8 Agustus 2026** — 22 dari 22 jurus punya minimal satu
contoh terpandu dan enam latihan, di ketiga tahap. Satu bidang penuh sudah bisa ditempuh
dari jurus tanpa prasyarat sampai jurus terdalam tanpa menabrak lubang.

Yang belum ada sama sekali adalah tiga bidang lainnya: aljabar, kombinatorika, geometri.

### Perkiraan cakupan penuh

| Bidang | Perkiraan jurus | Latihan (×6) | Contoh |
|---|---|---|---|
| Teori bilangan | 22 | 132 | ~30 |
| Aljabar | ~22 | 132 | ~30 |
| Kombinatorika | ~20 | 120 | ~28 |
| Geometri | ~22 | 132 | ~30 |
| **Total** | **~86** | **~516** | **~118** |

Sekitar **630 soal**. Dengan laju 5 soal per hari itu empat bulan kerja penuh; dengan
laju yang lebih realistis untuk kerja sambilan, satu sampai dua tahun. Rencana ini
karena itu disusun agar **aplikasinya bisa dipakai di ujung setiap fase**, bukan hanya
di ujung fase terakhir.

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

**0.5 Pisah `soal.json` per bidang — ditunda, tapi jamnya sudah berdetak.** Setelah Fase
1.2 ukurannya **227 KB untuk 127 soal** (~1,8 KB per soal, lebih besar dari perkiraan awal
1,35 KB karena soal OSN-P berpembahasan panjang). Pada 630 soal angkanya menuju ~1,1 MB,
dan **seluruhnya diambil di setiap halaman** serta ikut di-*precache* `sw.js` saat install.
Pecah jadi `data/soal-<pilar>.json` dan muat sesuai kebutuhan halaman. Tetap **paling
lambat akhir Fase 2** — tapi kalau teori bilangan saja sudah 227 KB, batas itu jangan
digeser lagi.

**0.6 Koreksi CLAUDE.md — selesai 8 Agustus 2026**, lalu diperbarui lagi mengikuti
0.1–0.4.

**Selesai kalau:** peta bisa dibuka per bidang, prasyarat lintas bidang terlihat
sebabnya, dan menambah bidang baru cuma menyentuh `URUT_PILAR` plus `NAMA_PILAR` di dua
berkas JS — dijaga tes, bukan ingatan.

**Sisa fase ini: 0.5 saja**, dan itu memang ditunda sampai Fase 2.

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

Draf daftar jurus (belum final, susun ulang saat menulis):

- Tingkat awal: manipulasi bentuk aljabar · faktorisasi · persamaan kuadrat ·
  barisan aritmetika & geometri · nilai mutlak
- Menengah: suku banyak · teorema sisa & faktor · Vieta · deret teleskopik ·
  induksi matematika · eksponen & logaritma · sistem persamaan
- Lanjut: ketaksamaan AM-GM · Cauchy-Schwarz · penataan ulang (rearrangement) ·
  persamaan fungsional · fungsi dan sifatnya · bilangan kompleks & akar satuan ·
  substitusi simetri · polinomial berkoefisien bulat

`polinomial-berkoefisien-bulat` sengaja diberi prasyarat `keterbagian` dari teori
bilangan — itu prasyarat lintas bidang pertama yang sungguhan, dan pembuktian bahwa 0.1
bekerja.

**Selesai kalau:** aljabar tuntas untuk OSN-K dan OSN-P (jalur OSN boleh menyusul), dan
simulasi bisa menyusun naskah dua bidang.

---

## Fase 3 — Kombinatorika

Draf daftar jurus:

- Tingkat awal: aturan jumlah & kali · permutasi · kombinasi · permutasi dengan
  pengulangan
- Menengah: koefisien binomial & identitasnya · inklusi-eksklusi · sarang merpati ·
  pencacahan ganda · bijeksi · stars and bars · probabilitas diskret
- Lanjut: rekursi · invarian & monovarian · pewarnaan · ekstremal · graf dasar ·
  teori permainan · fungsi pembangkit

Sebagian besar soal kombinatorika berbentuk uraian, jadi **rubriknya yang menentukan
mutu** — `build.py` sudah mewajibkan `## Rubrik` untuk soal uraian, tapi mewajibkan ada
bukan menjamin berguna. Rubrik yang cuma menulis "jawaban benar: 7 poin" tidak menolong
siswa menilai dirinya sendiri.

---

## Fase 4 — Geometri

**Terhalang dukungan gambar.** `markdown_ke_html` tidak mengenal `![alt](url)`: pola
tautan di `scripts/build.py:76` menangkap `[alt](url)` dan meninggalkan tanda seru
nyasar, sehingga keluarannya `!<a href="…">alt</a>`. Tidak ada aturan `img` di
`assets/styles.css`, dan tidak ada tes yang menjaganya.

**4.1 Dukungan gambar** sebelum satu jurus geometri pun ditulis:

- aturan `![alt](berkas)` → `<img>` di `_sebaris()`, dipasang **sebelum** pola tautan
  supaya tanda serunya ikut termakan
- `build.py` memeriksa berkas gambarnya benar-benar ada — pola yang sama dengan
  pemeriksaan prasyarat dan rujukan soal
- `alt` wajib diisi dan tidak boleh sekadar "gambar"; bagi siswa yang memakai pembaca
  layar, itu satu-satunya isi soalnya
- gambar berformat **SVG**, bukan PNG: tajam di segala ukuran, kecil, dan ikut berubah
  warna mengikuti tema
- aturan CSS supaya gambar tidak tumpah di layar ponsel
- tes di `tests/test_build.py` yang menjaga gambar dan rumus tidak saling merusak
- `sw.js`: gambar geometri masuk cache — tanpa itu, latihan offline menampilkan soal
  tanpa bangunnya, yang artinya tanpa soal

**4.2 Daftar jurus** (draf): sudut & garis · kekongruenan · kesebangunan · Pythagoras dan
perluasannya · luas dan perbandingan luas · garis-garis istimewa segitiga · titik-titik
istimewa · sudut pusat & sudut keliling · segiempat talibusur · Ptolemy · kuasa titik ·
garis singgung · Ceva & Menelaus · aturan sinus & kosinus · garis Euler & lingkaran
sembilan titik · transformasi · homoteti · geometri analitik · geometri ruang ·
ketaksamaan geometri · tempat kedudukan

Geometri paling lambat ditulis karena setiap soal butuh bangun. Jadwalkan waktunya
kira-kira dua kali lipat bidang lain.

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

### 5.1 Daftar arsip

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

`build.py` memeriksa `arsip` yang dirujuk memang ada di `arsip.yml` — pola yang sama
dengan prasyarat dan rujukan soal. Dengan itu, atribusi ke naskah asli kembali jadi
sesuatu yang **diperiksa mesin**, bukan teks bebas.

Mengutip satu soal untuk dibahas bukan hal yang sama dengan menyebarkan ulang seluruh
naskah, dan pembahasan itulah inti situs ini.

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

Bedanya dengan sebelumnya, ini sekarang **bisa ditegakkan mesin**: `build.py` menolak
`sumber` yang berpola atribusi nyata (tahun empat angka berdampingan "OSN"/"KSN") kalau
soal itu tidak punya `arsip` yang merujuk entri sah. Tidak lagi sekadar peringatan —
ada daftar arsip untuk dicocokkan, jadi jadikan galat. Tambahkan pemeriksaan ini
bersamaan dengan 5.1, jangan ditunda.

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
