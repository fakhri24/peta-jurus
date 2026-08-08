---
id: ket-contoh-2
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [keterbagian]
bentuk: uraian
kesulitan: 2
---

## Soal

Buktikan bahwa $n^3 - n$ habis dibagi $6$ untuk setiap bilangan bulat $n$.

## Petunjuk

- $6 = 2 \times 3$, dan $2$ dengan $3$ tidak punya faktor bersama. Cukup buktikan habis dibagi $2$ dan habis dibagi $3$ secara terpisah.
- Faktorkan dulu. $n^3 - n$ bisa dipecah jadi tiga faktor.
- $n^3 - n = (n-1)\,n\,(n+1)$ — hasil kali tiga bilangan bulat berurutan. Di antara tiga bilangan berurutan, pasti ada yang genap, dan pasti ada yang kelipatan tiga.

## Pembahasan

Faktorkan:

$$n^3 - n = n(n^2-1) = (n-1)\,n\,(n+1)$$

Ini hasil kali tiga bilangan bulat berurutan.

**Habis dibagi 2.** Di antara dua bilangan berurutan mana pun selalu ada satu yang genap,
apalagi di antara tiga. Jadi $2$ membagi hasil kalinya.

**Habis dibagi 3.** Setiap bilangan bulat berbentuk $3k$, $3k+1$, atau $3k+2$. Untuk
ketiga kemungkinan itu, salah satu dari $n-1$, $n$, $n+1$ pasti berbentuk $3k$. Jadi $3$
membagi hasil kalinya.

Karena $\gcd(2,3) = 1$ dan keduanya membagi $n^3-n$, maka $6 \mid n^3 - n$. $\blacksquare$

## Rubrik

- Memfaktorkan $n^3 - n$ menjadi $(n-1)n(n+1)$
- Menyebut bahwa cukup membuktikan habis dibagi $2$ dan $3$ secara terpisah, dengan alasan $\gcd(2,3)=1$
- Membuktikan keterbagian oleh $2$
- Membuktikan keterbagian oleh $3$ (misalnya lewat tiga kasus $n = 3k, 3k+1, 3k+2$)
- Menyimpulkan kembali ke $6$ — bukan berhenti di "habis dibagi 2 dan 3"
