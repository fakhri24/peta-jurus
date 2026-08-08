---
id: ind-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [induksi]
bentuk: uraian
kesulitan: 2
---

## Soal

Buktikan bahwa untuk setiap bilangan asli $n$,

$$1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}$$

## Petunjuk

- Pernyataannya berlaku untuk **setiap** $n$, dan bentuk untuk $n+1$ bisa disusun dari bentuk untuk $n$. Itu tanda paling jelas.
- Ada dua langkah wajib: periksa kasus terkecil, lalu tunjukkan kebenaran di $k$ menurunkan kebenaran di $k+1$.
- Pada langkah kedua, tulis $S_{k+1} = S_k + (k+1)$ lalu ganti $S_k$ dengan hipotesisnya.

## Pembahasan

Sebut pernyataan yang akan dibuktikan sebagai $P(n)$.

### Langkah 1: basis

Untuk $n = 1$:

$$\text{ruas kiri} = 1, \qquad \text{ruas kanan} = \frac{1 \cdot 2}{2} = 1$$

Cocok, jadi $P(1)$ benar.

### Langkah 2: langkah induksi

Andaikan $P(k)$ benar untuk suatu bilangan asli $k$, yaitu

$$1 + 2 + \cdots + k = \frac{k(k+1)}{2}$$

Akan ditunjukkan $P(k+1)$ juga benar, yaitu jumlahnya sampai $k+1$ bernilai
$\frac{(k+1)(k+2)}{2}$.

Jumlah sampai $k+1$ adalah jumlah sampai $k$ ditambah satu suku:

$$\underbrace{1 + 2 + \cdots + k}_{\text{pakai hipotesis}} + (k+1)
= \frac{k(k+1)}{2} + (k+1)$$

Keluarkan $(k+1)$ sebagai faktor persekutuan:

$$= (k+1)\left(\frac{k}{2} + 1\right) = (k+1) \cdot \frac{k+2}{2} = \frac{(k+1)(k+2)}{2}$$

Itu persis bentuk yang diminta untuk $n = k+1$, jadi $P(k+1)$ benar.

### Kesimpulan

$P(1)$ benar, dan $P(k)$ selalu menurunkan $P(k+1)$. Menurut prinsip induksi matematika,
$P(n)$ benar untuk setiap bilangan asli $n$. $\blacksquare$

**Perhatikan di mana hipotesis dipakai** — pada langkah mengganti $1+2+\cdots+k$ dengan
$\frac{k(k+1)}{2}$. Kalau pembuktian $P(k+1)$ berjalan tanpa menyentuh $P(k)$, yang kamu
tulis bukan pembuktian induksi, dan biasanya ada yang keliru.

Basisnya juga bukan formalitas. Tanpa basis, langkah induksi saja bisa "membuktikan"
pernyataan yang salah: dari $1+2+\cdots+n = \frac{n(n+1)}{2} + 5$, langkah $k \to k+1$
tetap berjalan mulus — hanya basisnya yang gagal.

Ada bukti lain tanpa induksi, yang konon ditemukan Gauss saat kecil: jumlahkan deretnya
dengan dirinya sendiri dalam urutan terbalik. Tiap pasangan berjumlah $n+1$, dan ada $n$
pasangan, jadi $2S = n(n+1)$.

## Rubrik

- Memeriksa basis pada $n = 1$, dengan kedua ruas dihitung
- Menuliskan hipotesis induksi secara eksplisit untuk $n = k$
- Menyatakan dengan jelas apa yang akan dibuktikan untuk $n = k+1$
- Menulis jumlah sampai $k+1$ sebagai jumlah sampai $k$ ditambah $(k+1)$, dan **memakai hipotesis** di situ
- Menyederhanakan sampai berbentuk $\frac{(k+1)(k+2)}{2}$
- Menutup dengan menyatakan prinsip induksinya
