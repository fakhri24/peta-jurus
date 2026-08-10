---
id: garis-euler
nama: Garis Euler dan Lingkaran Sembilan Titik
pilar: geometri
tahap: osn
prasyarat: [titik-istimewa, homoteti]
contoh: []
latihan: []
---

## Kapan dipakai

Soal memuat **dua atau lebih titik istimewa sekaligus** — misalnya titik tinggi bersama
pusat lingkaran luar — dan menanyakan jarak, perbandingan, atau kesegarisan di antaranya.
Itu pemicunya: begitu $H$, $G$, dan $O$ muncul bersama, hubungannya sudah tetap dan tidak
perlu dicari lagi.

Pemicu kedua: soal menyebut beberapa dari sembilan titik ini — titik tengah sisi, kaki
garis tinggi, atau titik tengah antara titik tinggi dan titik sudut — dan meminta
membuktikan keempatnya **setalibusur**. Semuanya sudah pada satu lingkaran sejak awal.

Pemicu ketiga: muncul panjang $R/2$, atau jari-jari yang setengah jari-jari lingkaran luar.
Itu sidik jari lingkaran sembilan titik.

## Intinya

**Garis Euler.** Pada setiap segitiga yang bukan sama sisi, titik tinggi $H$, titik berat
$G$, dan pusat lingkaran luar $O$ **segaris**, dengan

$$HG : GO = 2 : 1$$

Ditulis sebagai vektor dari $O$, hubungannya bahkan lebih ringkas:

$$\overrightarrow{OH} = 3\,\overrightarrow{OG} = \overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC}$$

Pada segitiga sama sisi keempat titik istimewa menyatu, dan garisnya tidak terdefinisi —
itu satu-satunya kekecualian.

**Lingkaran sembilan titik.** Kesembilan titik berikut terletak pada **satu** lingkaran:

- ketiga titik tengah sisi;
- ketiga kaki garis tinggi;
- ketiga titik tengah antara $H$ dan tiap titik sudut.

Pusatnya, $N$, adalah **titik tengah $OH$** — jadi ia ikut terletak pada garis Euler — dan
jari-jarinya tepat setengah jari-jari lingkaran luar:

$$N = \text{titik tengah } OH, \qquad r_N = \frac{R}{2}$$

**Dari mana asalnya.** Homoteti berpusat $H$ dengan faktor $\tfrac{1}{2}$ memetakan
lingkaran luar ke lingkaran sembilan titik. Itu sekaligus penjelasan mengapa jari-jarinya
separuh dan mengapa pusatnya jatuh di tengah $OH$ — bukan kebetulan yang perlu dihafal
terpisah.

**Teorema Feuerbach**, sebagai perluasan: lingkaran sembilan titik menyinggung lingkaran
dalam dan ketiga lingkaran singgung luarnya.

## Jebakan umum

- **Memakai perbandingan $2:1$ dengan urutan terbalik.** Yang dua bagian $HG$, diukur dari
  titik tinggi; yang satu bagian $GO$. Menukarnya menempatkan $G$ di sisi yang salah.
- **Memakainya pada segitiga sama sisi.** Di sana $H = G = O = I$, dan garis Euler tidak
  ada. Soal yang memberi segitiga sama sisi sedang meminta hal lain.
- **Mengira kaki garis tinggi selalu di dalam sisi.** Pada segitiga tumpul kakinya jatuh
  di perpanjangan, tetapi ia tetap salah satu dari sembilan titiknya.
- **Menghitung $N$ sebagai titik tengah $OG$.** Ia titik tengah $OH$; $G$ kebetulan juga
  di garis itu, dan itu yang membuat keliru ini terlihat masuk akal.
