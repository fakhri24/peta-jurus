---
id: ie-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [inklusi-eksklusi]
bentuk: isian
kesulitan: 2
jawaban: "47"
---

## Soal

Di antara bilangan $1, 2, 3, \dots, 100$, ada berapa yang habis dibagi $3$ **atau** habis
dibagi $5$?

## Petunjuk

- Hitung dulu masing-masing kelompoknya sendiri: yang habis dibagi $3$, dan yang habis dibagi $5$.
- Menjumlahkan keduanya begitu saja memberi hasil yang kelebihan. Cari bilangan mana yang terhitung dua kali.
- Bilangan yang habis dibagi $3$ sekaligus $5$ adalah yang habis dibagi $15$.

## Pembahasan

**Hitung tiap kelompok.** Banyaknya bilangan dari $1$ sampai $100$ yang habis dibagi $d$
adalah $\left\lfloor \frac{100}{d} \right\rfloor$.

$$|A| = \left\lfloor \frac{100}{3} \right\rfloor = 33, \qquad
|B| = \left\lfloor \frac{100}{5} \right\rfloor = 20$$

dengan $A$ himpunan kelipatan $3$ dan $B$ himpunan kelipatan $5$.

**Cari yang terhitung dua kali.** Bilangan yang habis dibagi $3$ **dan** $5$ adalah yang
habis dibagi kelipatan persekutuan terkecilnya:

$$\operatorname{lcm}(3,5) = 15, \qquad
|A \cap B| = \left\lfloor \frac{100}{15} \right\rfloor = 6$$

**Terapkan inklusi–eksklusi.**

$$|A \cup B| = |A| + |B| - |A \cap B| = 33 + 20 - 6 = \boxed{47}$$

**Mengapa harus dikurangi.** Bilangan seperti $15$, $30$, $45$ terhitung sekali di $|A|$
dan sekali lagi di $|B|$ — dua kali seluruhnya, padahal ia satu bilangan. Mengurangi
$|A\cap B|$ mengembalikan hitungannya menjadi tepat satu kali.

Perhatikan **tiap anggota gabungan berakhir terhitung tepat sekali**, dan itulah ukuran
kebenaran rumus ini:

- Bilangan yang hanya kelipatan $3$: terhitung $1$ kali di $|A|$, tidak di yang lain. Total $1$.
- Bilangan yang hanya kelipatan $5$: sama, total $1$.
- Bilangan yang kelipatan keduanya: $1 + 1 - 1 = 1$.

**Kekeliruan yang sering:** memakai $|A \cap B| = \left\lfloor \frac{100}{3\cdot5}
\right\rfloor$ tanpa berpikir. Di sini kebetulan benar karena $3$ dan $5$ tidak punya
faktor bersama. Kalau soalnya "habis dibagi $4$ atau $6$", yang dipakai adalah
$\operatorname{lcm}(4,6) = 12$, **bukan** $24$ — dan memakai $24$ memberi jawaban yang
salah.
