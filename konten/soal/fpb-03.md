---
id: fpb-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [fungsi-pembangkit]
bentuk: isian
kesulitan: 2
jawaban: "45"
---

## Soal

Tentukan koefisien $x^{8}$ pada

$$\frac{1}{(1-x)^{3}}$$

## Petunjuk

- Tuliskan $\frac{1}{1-x}$ sebagai deret lebih dulu, lalu pikirkan apa arti memangkatkannya tiga.
- Mengalikan tiga deret berarti memilih satu suku dari tiap faktor dan menjumlahkan pangkatnya.
- Koefisien $x^8$ karena itu mencacah penyelesaian sebuah persamaan yang sudah kamu kenal.

## Pembahasan

**Tuliskan deretnya.**

$$\frac{1}{1-x} = 1 + x + x^2 + x^3 + \cdots = \sum_{n \ge 0} x^{n}$$

**Baca perkaliannya sebagai pencacahan.**

$$\frac{1}{(1-x)^3} = \left(\sum_{a \ge 0} x^{a}\right)\left(\sum_{b \ge 0} x^{b}\right)
\left(\sum_{c \ge 0} x^{c}\right)$$

Mengalikannya berarti memilih pangkat $a$, $b$, $c$ dari ketiga faktor, dan sumbangannya
adalah $x^{a+b+c}$. Maka koefisien $x^8$ adalah banyaknya penyelesaian

$$a + b + c = 8, \qquad a,b,c \ge 0$$

**Hitung.**

$$\binom{8+3-1}{3-1} = \binom{10}{2} = \frac{10 \times 9}{2} = \boxed{45}$$

**Bentuk umumnya**, yang layak dihafal:

$$\frac{1}{(1-x)^{k}} = \sum_{n \ge 0} \binom{n+k-1}{k-1} x^{n}$$

**Perhatikan ini persis rumus membagi objek identik.** Koefisien $x^n$ pada
$\frac{1}{(1-x)^k}$ sama dengan banyaknya cara membagi $n$ benda identik ke $k$ wadah
berbeda — dan itu bukan kebetulan. Kedua hal itu mencacah objek yang sama, hanya ditulis
dengan bahasa yang berbeda:

| Bahasa deret | Bahasa pencacahan |
|---|---|
| satu faktor $\frac{1}{1-x}$ | satu wadah |
| pangkat yang dipilih dari faktor itu | isi wadah tersebut |
| koefisien $x^n$ | pembagian yang totalnya $n$ |

**Mengapa deret ini layak dikenali seketika.** Ia muncul di hampir setiap soal fungsi
pembangkit, sebab "boleh dipakai berapa pun" selalu menghasilkan faktor $\frac{1}{1-x^c}$.
Mengenalinya menghemat langkah menurunkan ulang koefisiennya tiap kali.

**Periksa untuk kasus kecil.** Untuk $k = 2$: $\frac{1}{(1-x)^2} = 1 + 2x + 3x^2 + \cdots$,
dan rumusnya memberi $\binom{n+1}{1} = n+1$. Memang koefisien $x^2$ adalah $3$, sesuai
penyelesaian $a+b = 2$ yaitu $(0,2), (1,1), (2,0)$.
