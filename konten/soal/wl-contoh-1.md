---
id: wl-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [wilson]
bentuk: isian
kesulitan: 2
jawaban: "12"
---

## Soal

Tentukan sisa pembagian $12!$ oleh $13$.

## Petunjuk

- Jangan menghitung $12!$. Perhatikan hubungan antara $12$ dan $13$ — bukan kebetulan bahwa keduanya berselisih satu.
- $13$ prima, dan yang dihitung adalah $(13-1)!$. Ada teorema yang persis menjawab bentuk itu.
- Teorema Wilson: $(p-1)! \equiv -1 \pmod p$ untuk $p$ prima.

## Pembahasan

Bilangan $13$ prima, dan yang ditanyakan adalah $(13-1)!$ modulo $13$ — persis bentuk yang
dijawab Teorema Wilson:

$$(p-1)! \equiv -1 \pmod p$$

Maka

$$12! \equiv -1 \pmod{13}$$

Sisanya harus ditulis dalam rentang $0$ sampai $12$, jadi

$$-1 \equiv 13 - 1 = \boxed{12} \pmod{13}$$

Alasan teoremanya sendiri layak diingat, karena itulah yang membuatnya bisa diterapkan di
soal lain. Kalikan seluruh $1, 2, \ldots, 12$. Setiap unsur berpasangan dengan inversnya
modulo $13$, dan hasil kali tiap pasangan adalah $1$:

$$2 \times 7 = 14 \equiv 1, \qquad 3 \times 9 = 27 \equiv 1, \qquad
4 \times 10 = 40 \equiv 1, \qquad 5 \times 8 = 40 \equiv 1, \qquad 6 \times 11 = 66 \equiv 1$$

Yang tersisa adalah unsur yang menjadi invers bagi dirinya sendiri, yaitu yang memenuhi
$x^2 \equiv 1 \pmod{13}$ — hanya $x = 1$ dan $x = 12$. Jadi

$$12! \equiv 1 \times 12 \times \underbrace{1 \times 1 \times \cdots \times 1}_{\text{lima pasangan}}
= 12 \equiv -1 \pmod{13}$$

Jawaban $-1$ dan $12$ adalah bilangan yang sama modulo $13$. Menuliskannya sebagai $-1$
biasanya lebih berguna dalam perhitungan lanjutan; sebagai jawaban akhir, $12$ yang
diminta.
