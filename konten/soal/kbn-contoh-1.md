---
id: kbn-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [koefisien-binomial]
bentuk: isian
kesulitan: 2
jawaban: "40"
---

## Soal

Tentukan koefisien $x^3$ pada penjabaran

$$(x+2)^5$$

## Petunjuk

- Jangan menjabarkan seluruhnya. Ada rumus yang memberi satu suku saja tanpa menghitung yang lain.
- Tiap suku penjabaran berbentuk (bilangan) $\times\ x^{a} \times 2^{b}$ dengan $a + b = 5$. Tentukan $a$ dan $b$ yang dibutuhkan.
- Bilangan di depannya adalah $\binom{5}{b}$, dengan $b$ menyatakan berapa kali angka $2$ terpilih.

## Pembahasan

**Tuliskan bentuk umum sukunya.** Menurut teorema binomial,

$$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k}\, x^{\,n-k}\, y^{\,k}$$

Dengan $y = 2$ dan $n = 5$:

$$(x+2)^5 = \sum_{k=0}^{5} \binom{5}{k}\, x^{\,5-k}\, 2^{\,k}$$

**Cari $k$ yang memberi $x^3$.**

$$5 - k = 3 \quad\Longrightarrow\quad k = 2$$

**Hitung sukunya.**

$$\binom{5}{2}\, x^{3}\, 2^{2} = 10 \times x^3 \times 4 = 40x^3$$

Koefisiennya $\boxed{40}$.

**Mengapa $\binom{5}{k}$ muncul di sana.** Menjabarkan $(x+2)^5$ berarti mengalikan lima
kurung $(x+2)$, dan dari tiap kurung dipilih $x$ atau $2$. Suku yang memuat $x^3$ muncul
setiap kali $x$ terpilih dari tiga kurung dan $2$ dari dua kurung sisanya. Banyaknya cara
memilih kurung mana yang menyumbang $2$ adalah $\binom{5}{2} = 10$ — dan tiap cara
menyumbang $x^3 \cdot 4$.

Jadi teorema binomial bukan rumus hafalan; ia soal pencacahan yang sudah selesai
dikerjakan.

**Dua kekeliruan yang paling sering:**

- **Tertukar pangkat.** Pada suku dengan $\binom{5}{k}$, yang berpangkat $k$ adalah suku
  **kedua**, di sini angka $2$. Memakai $\binom53 \cdot 2^3$ memberi $80$ — salah.
- **Lupa memangkatkan angkanya.** Menulis $\binom52 \times 2 = 20$ melupakan bahwa angka
  $2$ terpilih dua kali, sehingga menyumbang $2^2$.

**Periksa dengan menjabarkan langsung** — perkalian ini cukup kecil untuk diperiksa:

$$(x+2)^5 = x^5 + 10x^4 + 40x^3 + 80x^2 + 80x + 32$$

Koefisien $x^3$ memang $40$.
