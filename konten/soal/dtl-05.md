---
id: dtl-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [diophantine-taklinear]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa sebuah bilangan asli $n$ dapat dituliskan sebagai selisih dua kuadrat
bilangan bulat jika dan hanya jika $n$ ganjil atau $n$ habis dibagi $4$.

## Petunjuk

- Faktorkan $x^2 - y^2$ dan periksa apa yang dipaksakan oleh paritas kedua faktornya.
- Arah pertama: kalau $n = (x-y)(x+y)$, tunjukkan kedua faktor berparitas sama, lalu tarik kesimpulan tentang $n$.
- Arah kedua bersifat membangun: untuk $n$ ganjil coba $x = \frac{n+1}{2}$; untuk $n = 4m$ coba $x = m + 1$.

## Pembahasan

Tulis $n = x^2 - y^2 = (x - y)(x + y)$ dan sebut $u = x - y$, $v = x + y$.

### Arah pertama: jika $n$ selisih dua kuadrat, maka $n$ ganjil atau $4 \mid n$

Jumlah kedua faktor adalah

$$u + v = (x-y) + (x+y) = 2x$$

yang genap. Dua bilangan bulat berjumlah genap pasti berparitas sama. Ada dua kemungkinan:

- **Keduanya ganjil.** Maka $n = uv$ ganjil.
- **Keduanya genap.** Tulis $u = 2u'$ dan $v = 2v'$, sehingga $n = 4u'v'$, yaitu
  $4 \mid n$.

Jadi $n$ ganjil atau habis dibagi $4$. Tidak ada kemungkinan ketiga, sehingga bilangan
yang bersisa $2$ modulo $4$ tidak pernah menjadi selisih dua kuadrat.

### Arah kedua: jika $n$ ganjil atau $4 \mid n$, maka $n$ selisih dua kuadrat

Cukup ditunjukkan penulisannya secara nyata.

**Kalau $n$ ganjil**, tulis $n = 2m + 1$. Ambil

$$x = m + 1, \qquad y = m$$

Maka

$$x^2 - y^2 = (m+1)^2 - m^2 = 2m + 1 = n$$

**Kalau $4 \mid n$**, tulis $n = 4m$. Ambil

$$x = m + 1, \qquad y = m - 1$$

Maka

$$x^2 - y^2 = (m+1)^2 - (m-1)^2 = 4m = n$$

Kedua arah terbukti. $\blacksquare$

Perhatikan bahwa pada arah kedua, $y$ boleh bernilai $0$ — misalnya $n = 4$ memberi
$x = 2$, $y = 0$. Kalau soal menuntut $x$ dan $y$ keduanya **asli**, kasus $n = 4$ gugur,
dan pernyataannya perlu dirumuskan ulang.

## Rubrik

- Memfaktorkan $n = (x-y)(x+y)$ dan menamai kedua faktornya
- Menunjukkan jumlah kedua faktor genap, sehingga keduanya berparitas sama
- Menangani kedua kasus paritas: keduanya ganjil memberi $n$ ganjil, keduanya genap memberi $4 \mid n$
- Arah sebaliknya untuk $n$ ganjil, dengan penulisan nyata yang diperiksa
- Arah sebaliknya untuk $4 \mid n$, dengan penulisan nyata yang diperiksa
- Menyatakan kedua arah sudah lengkap, sehingga kesetaraannya terbukti
