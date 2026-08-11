---
id: eksponen-logaritma
nama: Eksponen dan Logaritma
pilar: aljabar
tahap: osn-k
prasyarat: [manipulasi-aljabar]
contoh: [el-contoh-1]
latihan: [el-01, el-02, el-03, el-04, el-05, el-06]
---

## Kapan dipakai

Peubah muncul di **pangkat**, atau soal memuat **$\log$**. Keduanya satu jurus karena
keduanya satu gagasan dibaca dua arah.

Pemicu kedua: persamaannya memuat **basis yang sama muncul berkali-kali** — $4^x$, $2^x$,
dan angka tetap dalam satu baris. Tulis semuanya dengan basis terkecil, beri nama $t = 2^x$,
dan yang tersisa hampir selalu persamaan kuadrat.

Pemicu ketiga: soal meminta **membandingkan dua bilangan berpangkat besar** tanpa
menghitungnya — mana yang lebih besar, $2^{100}$ atau $3^{70}$. Melogaritmakan keduanya
mengubah perbandingan yang mustahil dihitung menjadi perkalian dua bilangan kecil.

Pemicu keempat: soal menanyakan **ada berapa digit** sebuah bilangan, atau digit pertamanya.
Banyaknya digit $N$ adalah $\lfloor \log_{10} N \rfloor + 1$, dan itu satu-satunya cara
rapi menjawabnya.

Satu syarat yang sering terlupa dan menggugurkan jawaban: logaritma menuntut argumennya
positif, jadi tiap penyelesaian wajib diperiksa balik terhadap syarat itu — bukan sebagai
kehati-hatian, melainkan karena penyelesaian palsu memang muncul.

## Intinya

Aturan pangkat, semuanya turun dari satu gagasan — pangkat mencacah berapa kali dikalikan:

$$a^m a^n = a^{m+n}, \qquad \frac{a^m}{a^n} = a^{m-n}, \qquad \left(a^m\right)^n = a^{mn},
\qquad a^{-n} = \frac{1}{a^n}$$

Logaritma adalah kebalikannya:

$$\log_a b = c \iff a^c = b$$

sehingga aturan pangkat berubah menjadi aturan logaritma:

$$\log_a (xy) = \log_a x + \log_a y, \qquad \log_a x^n = n \log_a x,
\qquad \log_a x = \frac{\log_b x}{\log_b a}$$

Aturan terakhir — ganti basis — yang paling sering dibutuhkan, karena ia menyatukan
logaritma berbasis berbeda menjadi satu peubah.

**Untuk persamaan eksponen**, kuncinya menyamakan basis: dari $a^{f(x)} = a^{g(x)}$ dengan
$a > 0$, $a \ne 1$, diperoleh $f(x) = g(x)$.

**Untuk membandingkan pangkat besar**, samakan pangkatnya alih-alih menghitung:
$2^{100} = \left(2^{10}\right)^{10} = 1024^{10}$ dan $3^{60} = \left(3^6\right)^{10} =
729^{10}$, jadi yang pertama lebih besar.

## Jebakan umum

- **Lupa syarat domain.** Pada $\log_a x$, dibutuhkan $x > 0$, $a > 0$, dan $a \ne 1$.
  Solusi yang melanggar itu harus dibuang.
- **Mengira $\log(x+y) = \log x + \log y$.** Yang benar berlaku untuk hasil kali.
- **Membagi kedua ruas dengan $a^{f(x)}$** tanpa menyadari nilainya tidak pernah nol —
  itu aman, tetapi kebalikannya, mengalikan dengan sesuatu yang bisa nol, tidak.
