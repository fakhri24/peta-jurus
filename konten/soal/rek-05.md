---
id: rek-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [rekursi]
bentuk: isian
kesulitan: 3
jawaban: "377"
---

## Soal

Ada berapa himpunan bagian dari $\{1, 2, 3, \dots, 12\}$ yang **tidak memuat dua bilangan
berurutan**? (Himpunan kosong ikut terhitung.)

## Petunjuk

- Beri nama untuk jawaban pada himpunan $\{1,\dots,n\}$, lalu pecah menurut apakah unsur terbesar ikut terpilih.
- Kalau $n$ tidak ikut, sisanya adalah persoalan yang sama pada $\{1,\dots,n-1\}$.
- Kalau $n$ ikut, unsur $n-1$ sudah pasti tidak boleh ikut — jadi yang bebas tinggal $\{1,\dots,n-2\}$.

## Pembahasan

Sebut $c_n$ banyaknya himpunan bagian dari $\{1,\dots,n\}$ tanpa dua unsur berurutan.

**Pecah menurut unsur terbesar.**

- **$n$ tidak terpilih.** Yang tersisa adalah himpunan bagian sah dari $\{1,\dots,n-1\}$,
  tanpa syarat tambahan. Banyaknya $c_{n-1}$.
- **$n$ terpilih.** Maka $n-1$ **tidak boleh** terpilih, sebab keduanya berurutan. Unsur
  $1$ sampai $n-2$ masih bebas asalkan memenuhi syarat di antara mereka sendiri. Banyaknya
  $c_{n-2}$.

Kedua kelompok lepas dan menutupi semuanya, sehingga

$$c_n = c_{n-1} + c_{n-2}$$

**Kasus dasarnya**, dengan mendaftar:

$$c_1 = 2 \quad \bigl(\varnothing,\ \{1\}\bigr)$$

$$c_2 = 3 \quad \bigl(\varnothing,\ \{1\},\ \{2\}\bigr) \ \text{--- } \{1,2\} \text{ dibuang}$$

**Hitung.**

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $c_n$ | $2$ | $3$ | $5$ | $8$ | $13$ | $21$ | $34$ | $55$ | $89$ | $144$ | $233$ | $\boxed{377}$ |

**Periksa $c_3 = 5$:** $\varnothing$, $\{1\}$, $\{2\}$, $\{3\}$, $\{1,3\}$. Tepat $5$ —
$\{1,2\}$, $\{2,3\}$, dan $\{1,2,3\}$ dibuang.

**Perhatikan himpunan kosong ikut terhitung,** dan itu menentukan kasus dasarnya. Kalau soal
menuntut himpunan bagian **tak kosong**, seluruh jawabannya berkurang satu menjadi $376$ —
sebab himpunan kosong terhitung tepat sekali, berapa pun $n$.

**Soal ini dan soal barisan biner tanpa dua angka $1$ berdampingan adalah soal yang sama.**
Padanannya langsung: sebuah himpunan bagian dapat ditulis sebagai barisan $0$ dan $1$
sepanjang $n$, dengan angka $1$ di tempat ke-$i$ berarti unsur $i$ terpilih. Syarat "tidak
ada dua unsur berurutan" persis menjadi "tidak ada dua angka $1$ berdampingan".

Karena itu kedua barisan jawabannya sama persis, termasuk kasus dasarnya — tidak seperti
soal tangga, yang bergeser satu suku.

**Mengapa pemecahannya memakai unsur terbesar,** bukan terkecil. Keduanya sah dan memberi
rekurens yang sama; yang penting adalah memilih satu ujung dan tetap konsisten. Memecah dari
tengah akan menghasilkan dua bagian yang saling memengaruhi, dan rekurensnya tidak lagi
sederhana.
