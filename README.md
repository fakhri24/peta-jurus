# Peta Jurus

Rute belajar olimpiade matematika SMA. Bukan gudang PDF — sebuah **peta**.

Materi OSN berlimpah tapi berserakan, dan itu membuat siswa mengerjakan soal secara acak:
merasa sibuk, tapi tidak naik levelnya. Situs ini menutup lima kebocoran yang membuat
belajar olimpiade terasa jalan di tempat.

| Kebocoran | Jawabannya di situs ini |
|---|---|
| Tidak tahu harus belajar apa berikutnya | Peta prasyarat yang menggembok jurus lanjut |
| Soal tidak bertanda | Tiap soal ditandai jurus apa yang diujinya |
| Belajar bulan ini, lupa bulan depan | Jadwal ulang **1 → 3 → 7 → 21 → 60** hari |
| Langsung baca pembahasan | Petunjuk berjenjang; pembahasan terkunci sampai dicoba |
| Kesalahan tidak dicatat | Jurnal salah bertanda sebab, lengkap dengan rekapnya |

Seluruh kemajuan siswa hanya tersimpan di peramban masing-masing. **Tidak ada server,
tidak ada akun, tidak ada data siswa yang keluar dari perangkatnya.**

---

## Ide intinya: unit belajarnya "jurus", bukan "bab"

Olimpiade bukan silabus lurus. Yang benar-benar dipakai saat mengerjakan soal bukan
"Bab 3: Teori Bilangan", melainkan gerakan bernama — *sarang merpati*, *turun tak
hingga*, *Vieta jumping*. Tiap jurus adalah satu simpul dalam graf berprasyarat.

Dan bagian paling berharga dari halaman jurus bukan rumusnya, tapi **pemicunya**:

> **Kapan dipakai.** Soal menyebut kata *habis dibagi*, *kelipatan*, *faktor*, atau
> *sisa*. Juga saat kamu melihat bentuk seperti $n \mid a$ dan ingin menariknya jadi
> persamaan.

Itu yang hampir selalu hilang dari buku, dan justru itu yang memisahkan siswa yang bisa
dari yang tidak. Karena itu bagian tersebut wajib diisi — `scripts/build.py` menolak
membangun jurus yang bagian itu kosong.

---

## Menjalankan di komputer sendiri

```sh
python3 -m http.server 8000
```

lalu buka <http://localhost:8000>.

Harus lewat server, tidak bisa klik dua kali berkasnya. Peramban melarang `fetch()`
membaca berkas dari `file://`, sehingga `data/*.json` tidak akan pernah termuat.

**Kalau halamannya seperti tidak berubah setelah kamu mengedit:** itu service worker-nya.
Ia sengaja mengutamakan cache supaya latihan tetap jalan saat offline. Muat ulang sekali
lagi, atau buka DevTools → Application → Service Workers → Unregister.

---

## Menambah atau mengubah isi

Semua tulisan ada di `konten/`. Kamu tidak menyentuh `data/*.json` — berkas itu **hasil
build**, dan akan tertimpa.

```sh
python3 scripts/build.py     # konten/ → data/
python3 tests/test_build.py  # 38 tes, terutama menjaga rumus tidak dirusak Markdown
```

Build sengaja **gagal keras**, bukan diam-diam melewatkan yang keliru. Ia berhenti kalau:

- prasyarat menunjuk jurus yang tidak ada, atau prasyaratnya berputar
- soal menunjuk jurus yang tidak ada, atau sebaliknya
- `id` tidak sama dengan nama berkasnya
- soal isian tanpa `jawaban`, atau soal uraian tanpa `## Rubrik`
- bagian `## Kapan dipakai` kosong

### Satu berkas jurus

`konten/jurus/fermat-kecil.md`

```markdown
---
id: fermat-kecil            # wajib sama dengan nama berkas
nama: Teorema Fermat Kecil
pilar: teori-bilangan
tahap: osn-p                # osn-k | osn-p | osn
prasyarat: [sistem-residu]
contoh: [fkl-contoh-1]      # soal yang dibedah bertahap
latihan: [fkl-01, fkl-02]   # soal yang dikerjakan sendiri
---

## Kapan dipakai
Pemicunya. Satu-dua kalimat. Bagian terpenting — wajib diisi.

## Intinya
Pernyataan singkat. Satu paragraf, bukan satu bab.

## Jebakan umum
- Salah yang paling sering terjadi pada jurus ini.
```

Kalau kamu belum menulis soalnya, biarkan `contoh: []` dan `latihan: []`. Build akan
menyebutkan jurus mana saja yang masih kosong di akhir jalannya.

### Satu berkas soal

`konten/soal/fkl-01.md`

```markdown
---
id: fkl-01
sumber: OSN-P 2019, soal 7   # dari mana soalnya — wajib
pilar: teori-bilangan
tahap: osn-p
jurus: [fermat-kecil]        # boleh lebih dari satu
bentuk: isian                # isian (diperiksa otomatis) | uraian (dinilai sendiri)
kesulitan: 3                 # 1..5
jawaban: "8"
jawaban_alt: []              # varian yang juga diterima
---

## Soal
Tentukan sisa pembagian $2^{2019}$ oleh $13$.

## Petunjuk
- Dorongan halus, tanpa menyebut jurusnya.
- Menyebut jurus yang dipakai.
- Langkah pertama.

## Pembahasan
...

## Rubrik                    # hanya untuk bentuk: uraian
- Langkah yang harus ada di lembar jawaban.
```

Urutan petunjuknya bukan hiasan. Petunjuk 1 tidak boleh menyebut nama jurusnya — kalau
disebut, gerbangnya kehilangan gunanya.

Pemeriksaan jawaban isian sengaja lugu: spasi dirapikan, huruf besar-kecil disamakan, dan
angka dibandingkan sebagai angka (jadi `08` sama dengan `8`). Selain itu, varian yang sah
**ditulis eksplisit** di `jawaban_alt` — bukan ditebak oleh kode.

---

## Tentang sumber soal

Soal yang ada sekarang **disusun sendiri dengan gaya OSN**, dan `sumber`-nya ditulis apa
adanya begitu. Tidak ada satu pun yang diberi atribusi tahun dan nomor palsu.

Kalau kamu memasukkan soal dari arsip sungguhan, tulis sumbernya persis — `OSN-K 2019,
soal 5`. Naskah OSN itu dokumen publik, tapi asalnya tetap harus terbaca.

---

## Yang sudah dan belum

22 jurus Teori Bilangan sudah punya pelajaran lengkap. 38 soal sudah ditulis, menutupi
**10 jurus pertama** — cukup untuk berbulan-bulan belajar dari simpul paling awal.

Belum ada soal di dua belas jurus lanjut: Bézout, Diophantine linear, Diophantine
taklinear, fungsi Euler, kongruensi linear, Legendre, LTE, orde elemen, Teorema Sisa Cina,
turun tak hingga, Vieta jumping, dan Wilson. Halaman jurusnya sudah bisa dibaca; hanya
latihannya yang kosong, dan halamannya mengatakan itu dengan jujur.

Tiga pilar lain — Aljabar, Geometri, Kombinatorika — belum disentuh. Strukturnya sudah
siap menerimanya: cukup tambahkan berkas dengan `pilar` yang berbeda, dan peta terpisah
akan muncul sendiri.

---

## Susunannya

```
index.html      peta jurus                jurus.html    satu halaman jurus
latihan.html    sesi latihan              jurnal.html   jurnal salah + rekap
simulasi.html   ujian bertimer

assets/inti.js      data · localStorage · jadwal ulang · render rumus
assets/soal-ui.js   tangga petunjuk — dipakai halaman jurus dan latihan
assets/katex/       KaTeX 0.18.1, dipasang lokal (bukan CDN, supaya offline jalan)

konten/         sumber tulisan          data/       hasil build, jangan diedit
scripts/build.py                        tests/test_build.py
```

Statis sepenuhnya. Tanpa kerangka kerja, tanpa build step untuk situsnya sendiri, tanpa
dependensi di peramban selain KaTeX. Yang di-build hanya isinya.

### Dua keputusan yang layak diketahui

**Markdown-nya ditulis sendiri, tidak memakai pustaka.** Aturan Markdown dan LaTeX
memperebutkan tanda yang sama — `_`, `*`, `\\`, `&`. Pustaka Markdown umum akan mengubah
`$a_1$` jadi huruf miring dan menelan garis miring ganda di dalam `align`. Karena itu
rumus dicabut lebih dulu, diganti penanda, baru dikembalikan setelah Markdown selesai.
Sebagian besar tes di `tests/test_build.py` menjaga tepat hal ini.

**Tata letak peta dihitung saat build, bukan di peramban.** `scripts/build.py` memberi
tiap simpul tingkat dan koordinat, jadi halamannya tinggal menggambar SVG. Tidak ada d3,
tidak ada dagre, tidak ada pustaka graf apa pun.

**Service worker-nya kebalikan dari `info-kurikulum`.** Di sana `data/*.json` diambil dari
jaringan lebih dulu karena Google Sheet sering berubah. Di sini cache didahulukan —
isinya jarang berubah, dan latihan saat offline justru intinya.
