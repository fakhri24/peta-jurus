---
id: fkt-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [faktorisasi]
bentuk: isian
kesulitan: 2
jawaban: "2"
---

## Soal

Ada berapa pasangan bilangan asli $(a, b)$ dengan $a \le b$ yang memenuhi

$$ab + a + b + 1 = 12\ ?$$

## Petunjuk

- Ruas kirinya bukan bentuk baku, tetapi susunannya mencurigakan. Coba kelompokkan dua-dua.
- $ab + a + b + 1 = a(b+1) + (b+1)$ — sekarang ada faktor persekutuan.
- Setelah menjadi $(a+1)(b+1) = 12$, ingat bahwa $a, b \ge 1$ membatasi kedua faktornya.

## Pembahasan

Kelompokkan dua suku pertama dan dua suku terakhir:

$$ab + a + b + 1 = a(b+1) + 1(b+1) = (a+1)(b+1)$$

Persamaannya menjadi

$$(a+1)(b+1) = 12$$

**Pasang batasnya.** Karena $a \ge 1$ dan $b \ge 1$, kedua faktornya paling sedikit $2$.
Dan syarat $a \le b$ berarti $a + 1 \le b + 1$.

Pasangan pembagi $12$ dengan kedua faktor $\ge 2$ dan yang pertama tidak melebihi yang
kedua:

| $a+1$ | $b+1$ | $a$ | $b$ |
|---|---|---|---|
| $2$ | $6$ | $1$ | $5$ |
| $3$ | $4$ | $2$ | $3$ |

Pasangan $(1, 12)$ gugur karena memberi $a = 0$, dan $(12,1)$ maupun $(6,2)$ gugur karena
melanggar $a \le b$.

Ada $\boxed{2}$ pasangan: $(1,5)$ dan $(2,3)$.

Periksa: $1 \cdot 5 + 1 + 5 + 1 = 12$ dan $2 \cdot 3 + 2 + 3 + 1 = 12$. Keduanya cocok.

Pengelompokan seperti ini bekerja setiap kali kamu melihat $ab + a + b$: tambahkan $1$
untuk melengkapinya menjadi $(a+1)(b+1)$. Di soal bilangan bulat, mengubah jumlah menjadi
**hasil kali** hampir selalu kemajuan besar, sebab hasil kali membatasi kemungkinannya
menjadi berhingga.
