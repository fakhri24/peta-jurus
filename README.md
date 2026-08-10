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
python3 scripts/build.py     # konten/ → data/ + assets/rajah/
python3 tests/test_build.py  # 91 tes, terutama menjaga rumus tidak dirusak Markdown
```

Build sengaja **gagal keras**, bukan diam-diam melewatkan yang keliru. Ia berhenti kalau:

- prasyarat menunjuk jurus yang tidak ada, atau prasyaratnya berputar
- soal menunjuk jurus yang tidak ada, atau sebaliknya
- `id` tidak sama dengan nama berkasnya
- soal isian tanpa `jawaban`, atau soal uraian tanpa `## Rubrik`
- bagian `## Kapan dipakai` kosong
- gambar menunjuk rajah yang tidak ada, atau alt-nya kosong, malas, atau berumus

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
sumber: Latihan 1 — susunan sendiri, gaya OSN-P   # dari mana soalnya — wajib
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

### Satu rajah geometri

Rajah **tidak digambar tangan dan tidak diambil dari mana pun** — ia dihitung. Sumbernya
berkas Python di `konten/rajah/`, keluarannya SVG di `assets/rajah/` yang dibangkitkan
`build.py` bersama sisanya.

`konten/rajah/segitiga-lingkaran-dalam.py`

```python
from rajah import *

A, B, C = titik(0, 0), titik(6, 0), titik(1.6, 4.2)
I = pusat_dalam(A, B, C)              # dihitung, bukan ditaksir
X = kaki(I, garis(B, C))              # titik singgung, pasti tepat di lingkaran

RAJAH = (rajah("Segitiga ABC dengan lingkaran dalam berpusat I, menyinggung BC di X")
         .poligon(A, B, C)
         .lingkaran(I, jari_dalam(A, B, C), gaya="bantu")
         .ruas(I, X, gaya="bantu", putus=True)
         .tanda_siku(B, X, I)
         .titik(A, "A").titik(B, "B").titik(C, "C").titik(I, "I").titik(X, "X"))
```

Dipakai di soal dengan nama berkasnya saja:

```markdown
![Segitiga ABC dengan lingkaran dalam berpusat I, menyinggung BC di X](segitiga-lingkaran-dalam.svg)
```

Alasan dihitung: rajah dibaca dengan mata, dan siswa menyimpulkan dari apa yang
dilihatnya. Lingkaran dalam yang meleset sedikit tidak menggagalkan apa pun — ia hanya
mengajarkan hal yang salah, diam-diam. Sumbu $y$ di `konten/rajah/` **naik ke atas**
seperti di buku; pembalikannya ke koordinat SVG dikerjakan sekali saat render.

Dua aturan yang ditegakkan build:

- **`alt` wajib dan harus menggantikan gambarnya.** Bagi siswa yang memakai pembaca
  layar, alt itu satu-satunya isi soalnya — `![gambar](…)` ditolak, begitu juga alt
  yang memuat `$…$`, karena KaTeX tidak merender di dalam atribut.
- **Hanya nama berkas, bukan jalur atau alamat web.** Gambar dari luar mematahkan
  latihan offline, dan menyalinnya ke sini urusan izin yang berbeda — lihat `PLAN.md`
  Fase 5.

---

## Tentang sumber soal

Seluruh soal yang ada sekarang **disusun sendiri dengan gaya OSN**, dan `sumber`-nya
ditulis apa adanya begitu. Tidak ada satu pun yang diberi atribusi tahun dan nomor palsu.

Atribusi ke naskah asli — `OSN 2025 nomor 3` — punya syarat, dan syaratnya dijaga mesin:
naskahnya harus **kamu unduh sendiri dari situs resmi** penyelenggara dan terdaftar di
`konten/arsip.yml`, lalu soalnya memuat `arsip:` yang merujuk entri itu.

```yaml
sumber: OSN 2025 nomor 3
arsip: osn-2025
nomor: 3
```

`build.py` menolak setiap `sumber` yang berbunyi seperti atribusi tahun+lomba tapi tidak
punya `arsip` yang sah. Alasannya: begitu ada satu naskah asli di dalam situs, soal
karangan berlabel `OSN 2015 nomor 3` terbaca sebagai naskah asli — karena naskah asli
memang ada.

Dua hal yang sering dikira sama:

- **"Gratis diunduh" bukan "bebas disebarkan ulang."** Karena itu tidak ada PDF naskah di
  repo ini; `arsip.yml` menyimpan metadata dan tautan ke berkas resminya saja.
- **Naskah dari simpanan orang lain tidak boleh diberi atribusi tahun dan nomor.**
  Asal-usulnya tidak bisa diverifikasi, dan salinan tak resmi sering memuat salah ketik —
  pada soal olimpiade, salah ketik biasanya mengubah soalnya jadi soal lain. Kalau soalnya
  bagus, tulis ulang sebagai soal susunan sendiri dan beri label begitu.

---

## Yang sudah dan belum

**74 dari 85 jurus terisi, 519 soal**, di empat bidang:

| Bidang | OSN-K | OSN-P | OSN | Soal | Status |
|---|---|---|---|---|---|
| Teori bilangan | 8 | 10 | 4 | 155 | tuntas |
| Aljabar | 10 | 7 | 5 | 154 | tuntas |
| Kombinatorika | 10 | 6 | 4 | 140 | tuntas |
| Geometri | 10 | 7 | 4 | 70 | tahap OSN-K tuntas |

Tuntas artinya tiap jurus punya minimal satu contoh terpandu dan enam latihan — enam,
karena tangga ulangnya lima langkah, dan jurus dengan tiga soal berarti siswa bertemu soal
yang sama untuk ketiga kalinya pada ulangan hari ke-21.

Ketiga tahap dapat ditempuh utuh di tiga bidang pertama; di geometri, **seluruh jalur
OSN-K** sudah bisa ditempuh tanpa menabrak jurus kosong. Simulasi menyusun naskah campuran
yang dibagi rata antar bidang.

Tiga jalur lintas bidang bisa ditempuh sungguhan: `keterbagian` (teori bilangan) →
`polinomial-bulat` (aljabar), `induksi` (aljabar) → `rekursi` (kombinatorika), dan
`persamaan-kuadrat` (aljabar) → `geometri-analitik` (geometri).

Dari 519 soal, **108 berbentuk uraian** yang dinilai sendiri dengan rubrik. Porsinya paling
besar di kombinatorika tingkat lanjut, karena invarian, pewarnaan, dan prinsip ekstremal
memang teknik pembuktian — soal isian akan menguji hal yang berbeda dari yang dilatih.

Yang belum: **11 jurus geometri tahap OSN-P dan OSN**. Rencananya di `PLAN.md`.

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
