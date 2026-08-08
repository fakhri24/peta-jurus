---
id: ket-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [keterbagian]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa $n^5 - n$ habis dibagi $30$ untuk setiap bilangan bulat $n$.

## Petunjuk

- $30$ terlalu besar untuk diserang langsung. Pecah dulu jadi bagian-bagian yang lebih kecil.
- $30 = 2 \times 3 \times 5$, dan ketiganya saling asing — jadi cukup buktikan keterbagian oleh masing-masing.
- Mulai dengan memfaktorkan: $n^5 - n = n(n^4 - 1) = (n-1)n(n+1)(n^2+1)$.

## Pembahasan

Karena $30 = 2 \times 3 \times 5$ dengan ketiga faktornya saling asing, cukup dibuktikan
bahwa $n^5 - n$ habis dibagi $2$, oleh $3$, dan oleh $5$ secara terpisah.

Faktorkan lebih dulu:

$$n^5 - n = n(n^4 - 1) = n(n^2-1)(n^2+1) = (n-1)\,n\,(n+1)\,(n^2+1)$$

**Habis dibagi $2$ dan $3$.** Bagian $(n-1)n(n+1)$ adalah tiga bilangan bulat berurutan.
Di antara tiga bilangan berurutan pasti ada yang genap, jadi hasil kalinya habis dibagi
$2$. Pasti pula ada tepat satu yang habis dibagi $3$, jadi hasil kalinya habis dibagi $3$.

**Habis dibagi $5$.** Tinjau $n$ menurut sisanya dibagi $5$.

- Jika $n \equiv 0 \pmod 5$, maka $5 \mid n$.
- Jika $n \equiv 1 \pmod 5$, maka $5 \mid n - 1$.
- Jika $n \equiv 4 \pmod 5$, maka $5 \mid n + 1$.
- Jika $n \equiv 2$ atau $n \equiv 3 \pmod 5$, maka $n^2 \equiv 4 \pmod 5$, sehingga
  $n^2 + 1 \equiv 5 \equiv 0 \pmod 5$.

Kelima kemungkinan sisa sudah tercakup, jadi $5 \mid n^5 - n$ selalu.

Karena $2$, $3$, dan $5$ saling asing dan ketiganya membagi $n^5 - n$, hasil kalinya juga
membagi:

$$30 \mid n^5 - n \qquad \blacksquare$$

Dua kasus terakhir itu yang paling mudah terlewat. Kalau kamu hanya melihat
$(n-1)n(n+1)$, kamu kehilangan $n \equiv 2, 3$ — dan di situlah faktor $n^2+1$ bekerja.

## Rubrik

- Memecah $30$ menjadi $2 \times 3 \times 5$ dan menyebutkan bahwa ketiganya saling asing, sehingga keterbagian boleh dibuktikan terpisah lalu digabung
- Memfaktorkan $n^5 - n = (n-1)n(n+1)(n^2+1)$
- Menyimpulkan keterbagian oleh $2$ dan oleh $3$ dari tiga bilangan berurutan
- Membuktikan keterbagian oleh $5$ dengan meninjau seluruh sisa $n$ modulo $5$
- Menangani kasus $n \equiv 2, 3 \pmod 5$ lewat faktor $n^2 + 1$
- Menggabungkan ketiganya menjadi kesimpulan $30 \mid n^5 - n$
