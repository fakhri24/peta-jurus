---
id: teorema-sisa-faktor
nama: Teorema Sisa dan Faktor
pilar: aljabar
tahap: osn-p
prasyarat: [suku-banyak]
contoh: [tsf-contoh-1]
latihan: [tsf-01, tsf-02, tsf-03, tsf-04, tsf-05, tsf-06]
---

## Kapan dipakai

Soal menanyakan **sisa pembagian** polinomial oleh bentuk linear, atau menanyakan apakah
bentuk linear itu **faktornya**. Keduanya dijawab dengan satu substitusi, bukan dengan
pembagian bersusun.

Pemicu kedua, dan ini yang paling sering tidak dikenali sebagai jurus ini: soal memberi
**nilai $P$ di beberapa titik** lalu menanyakan sisa pembagian oleh hasil kali bentuk
linearnya. Sisa pembagian oleh $(x-a)(x-b)$ berbentuk $px+q$ — dua bilangan tak diketahui,
dan dua nilai yang diberikan tepat cukup menentukannya.

Pemicu ketiga: soal menyatakan sebuah polinomial **habis dibagi** sesuatu, lalu menanyakan
koefisiennya. Ubah menjadi "nilainya nol di titik itu" dan koefisiennya jatuh dari persamaan
biasa.

Pemicu keempat: soal memberi $P(x) - c$ yang punya beberapa akar, atau menyebut $P(a) = P(b)
= P(c)$. Selisihnya yang punya akar, bukan $P$-nya — dan menuliskan $P(x) - c = (x-a)(x-b)
(x-c)Q(x)$ biasanya langkah yang membuka seluruh soal.

Bedakan dari Suku Banyak: pembagian oleh bentuk berderajat dua ke atas yang tak terfaktorkan
menuntut pembagian sungguhan, bukan substitusi.

## Intinya

**Teorema sisa.** Sisa pembagian $P(x)$ oleh $(x - a)$ adalah $P(a)$.

Alasannya satu baris: tulis $P(x) = (x-a)Q(x) + r$ dengan $r$ konstanta, lalu masukkan
$x = a$.

**Teorema faktor.** $(x-a)$ faktor $P(x)$ tepat ketika $P(a) = 0$.

Keduanya mengubah soal tentang pembagian menjadi soal tentang **nilai** — dan menghitung
nilai jauh lebih murah daripada membagi bersusun.

Untuk pembagi berderajat lebih tinggi, gagasannya diperluas. Sisa pembagian oleh
$(x-a)(x-b)$ berbentuk $px+q$, sehingga

$$P(x) = (x-a)(x-b)Q(x) + px + q$$

Masukkan $x = a$ dan $x = b$ untuk memperoleh dua persamaan:

$$P(a) = pa + q, \qquad P(b) = pb + q$$

Dua persamaan, dua bilangan tak diketahui — selesai tanpa menyentuh $Q$ sama sekali.

**Akar rasional.** Kalau $P$ berkoefisien bulat dan $\frac{p}{q}$ akarnya dalam bentuk
paling sederhana, maka $p$ membagi konstanta dan $q$ membagi koefisien utama. Ini menyaring
kandidat akar dari tak hingga menjadi beberapa saja.

## Jebakan umum

- **Salah tanda.** Sisa pembagian oleh $(x + 3)$ adalah $P(-3)$, bukan $P(3)$.
- **Memakai pembagi berkoefisien bukan satu tanpa menyesuaikan.** Sisa pembagian oleh
  $(2x - 1)$ adalah $P\!\left(\frac12\right)$.
- **Lupa bentuk sisa untuk pembagi derajat tinggi.** Untuk pembagi berderajat tiga,
  sisanya berbentuk kuadrat — tiga bilangan tak diketahui, jadi butuh tiga nilai.
