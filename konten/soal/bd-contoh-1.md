---
id: bd-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [barisan-deret]
bentuk: isian
kesulitan: 2
jawaban: "62"
---

## Soal

Sebuah barisan aritmetika mempunyai suku pertama $5$ dan beda $3$. Tentukan suku ke-$20$.

## Petunjuk

- Suku ke-$n$ diperoleh dari suku pertama dengan menambahkan beda beberapa kali. Berapa kali, tepatnya?
- Dari $U_1$ ke $U_{20}$ ada $19$ langkah, bukan $20$.
- $U_n = a + (n-1)b$.

## Pembahasan

Suku ke-$n$ barisan aritmetika:

$$U_n = a + (n-1)b$$

Yang menentukan adalah $(n-1)$, bukan $n$. Alasannya sederhana: $U_1$ adalah titik
berangkat, jadi belum ada beda yang ditambahkan sama sekali. Untuk sampai ke $U_{20}$
dibutuhkan $19$ langkah.

Substitusikan $a = 5$, $b = 3$, $n = 20$:

$$U_{20} = 5 + (20-1) \times 3 = 5 + 57 = \boxed{62}$$

Periksa dengan menghitung beberapa suku: $5, 8, 11, 14, \ldots$ Suku ke-$4$ adalah
$5 + 3\times 3 = 14$ — cocok dengan pola.

Kekeliruan yang paling sering terjadi adalah memakai $a + nb$, yang memberi $65$. Selisih
satu langkah itu muncul di banyak tempat: banyaknya suku dari $U_p$ sampai $U_q$ adalah
$q - p + 1$, bukan $q - p$.
