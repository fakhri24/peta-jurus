---
id: fk-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [fpb-kpk]
bentuk: isian
kesulitan: 3
jawaban: "2"
---

## Soal

Diketahui $\gcd(a,b) = 6$ dan $\operatorname{lcm}(a,b) = 210$ untuk bilangan asli $a < b$.
Ada berapa pasangan $(a,b)$ yang memenuhi?

## Petunjuk

- Kalau FPB-nya $6$, tulis $a$ dan $b$ sebagai kelipatan $6$ — dan perhatikan syarat apa yang harus dipenuhi sisanya.
- $a = 6\alpha$, $b = 6\beta$ dengan $\gcd(\alpha,\beta) = 1$.
- Maka $\operatorname{lcm}(a,b) = 6\alpha\beta = 210$, sehingga $\alpha\beta = 35$. Tinggal mencacah pasangan relatif prima.

## Pembahasan

Karena $\gcd(a,b) = 6$, tulis

$$a = 6\alpha, \qquad b = 6\beta, \qquad \gcd(\alpha, \beta) = 1$$

Syarat $\gcd(\alpha,\beta) = 1$ itu wajib — tanpa itu FPB-nya akan lebih besar dari $6$.

Dengan penulisan ini $\operatorname{lcm}(a,b) = 6\alpha\beta$, sehingga

$$6\alpha\beta = 210 \quad\Longrightarrow\quad \alpha\beta = 35$$

Pasangan bulat positif dengan hasil kali $35$: $(1,35)$, $(5,7)$, $(7,5)$, $(35,1)$.
Keempatnya relatif prima. Syarat $a < b$ berarti $\alpha < \beta$, menyisakan

$$(\alpha,\beta) = (1,35) \ \text{dan}\ (5,7)$$

yaitu $(a,b) = (6, 210)$ dan $(30, 42)$ — ada $\boxed{2}$ pasangan.

Cek: $\gcd(30,42) = 6$ dan $\operatorname{lcm}(30,42) = 210$. Cocok.
