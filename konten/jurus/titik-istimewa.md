---
id: titik-istimewa
nama: Titik-titik Istimewa Segitiga
pilar: geometri
tahap: osn-p
prasyarat: [garis-istimewa]
contoh: [tis-contoh-1]
latihan: [tis-01, tis-02, tis-03, tis-04, tis-05, tis-06]
---

## Kapan dipakai

Soal menyebut **titik berat**, **titik tinggi**, **pusat lingkaran dalam**, atau **pusat
lingkaran luar** — atau menyebutnya tanpa nama: "titik potong ketiga garis berat", "titik
yang berjarak sama ke ketiga sisi".

Pemicu yang paling sering luput: soal menyebut satu titik berjarak sama ke ketiga **titik
sudut** dan kamu memperlakukannya sebagai pusat lingkaran dalam. Berjarak sama ke titik
sudut adalah pusat lingkaran **luar**; berjarak sama ke **sisi** barulah lingkaran dalam.

Pemicu ketiga: soal memberi dua titik istimewa sekaligus. Itu hampir selalu isyarat
memakai hubungan di antara keduanya, dan pada tahap berikutnya menjadi garis Euler.

## Intinya

Empat titik yang wajib dikenali beserta ciri penentunya:

| Titik | Perpotongan | Cirinya |
|---|---|---|
| Titik berat $G$ | ketiga garis berat | membagi tiap garis berat $2 : 1$ dari titik sudut |
| Titik tinggi $H$ | ketiga garis tinggi | bisa di luar segitiga kalau tumpul |
| Pusat dalam $I$ | ketiga garis bagi | berjarak sama ke ketiga **sisi**; selalu di dalam |
| Pusat luar $O$ | ketiga garis sumbu | berjarak sama ke ketiga **titik sudut** |

**Titik berat** membagi tiap garis berat dengan perbandingan $2 : 1$ diukur dari titik
sudut. Koordinatnya rata-rata ketiga titik sudut:

$$G = \left( \frac{x_A + x_B + x_C}{3}, \frac{y_A + y_B + y_C}{3} \right)$$

**Pusat dalam** dan jari-jari lingkaran dalam:

$$r = \frac{L}{s}$$

dengan $L$ luas dan $s$ setengah keliling. Panjang dari titik sudut ke titik singgung
terdekat adalah $s-a$, $s-b$, $s-c$.

**Pusat luar** dan jari-jarinya:

$$R = \frac{abc}{4L}$$

Letaknya bergantung jenis segitiga: di dalam kalau lancip, **pada titik tengah sisi
miring** kalau siku-siku, dan di luar kalau tumpul.

**Sudut pada pusat dalam** yang sering menyelesaikan soal dalam satu langkah:

$$\angle BIC = 90^\circ + \tfrac{1}{2}\angle A$$

## Jebakan umum

- **Menukar pusat dalam dengan pusat luar.** Ciri pembedanya jarak sama ke **sisi** lawan
  jarak sama ke **titik sudut**. Ini kekeliruan paling sering di seluruh jurus ini.
- **Mengira semua titik istimewa ada di dalam segitiga.** Hanya $I$ dan $G$ yang selalu di
  dalam; $H$ dan $O$ keluar pada segitiga tumpul.
- **Perbandingan titik berat dipakai terbalik.** Dari titik sudut ke $G$ dua bagian, dari
  $G$ ke titik tengah sisi satu bagian — bukan sebaliknya.
- **Mengira garis bagi bertemu di titik yang sama dengan garis sumbu.** Keduanya hanya
  berimpit pada segitiga sama sisi, di mana keempat titik itu menyatu jadi satu.
