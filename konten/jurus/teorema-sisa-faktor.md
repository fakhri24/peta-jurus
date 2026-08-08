---
id: teorema-sisa-faktor
nama: Teorema Sisa dan Faktor
pilar: aljabar
tahap: osn-p
prasyarat: [suku-banyak]
contoh: []
latihan: []
---

## Kapan dipakai

Soal menanyakan **sisa pembagian** polinomial, atau menanyakan apakah suatu bentuk linear
merupakan faktornya, atau memberi keterangan berupa nilai $P$ di beberapa titik.

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
