---
id: pcg-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [pencacahan-ganda]
bentuk: uraian
kesulitan: 4
---

## Soal

Buktikan bahwa untuk setiap bilangan bulat $n \ge 1$ berlaku

$$\sum_{k=1}^{n} k \binom{n}{k} = n \cdot 2^{\,n-1}$$

dengan **pencacahan ganda** — yaitu dengan menghitung satu himpunan yang sama lewat dua
cara, bukan dengan manipulasi aljabar.

## Petunjuk

- Nyatakan lebih dulu himpunan yang akan dicacah. Ruas kirinya menjumlahkan atas ukuran, jadi himpunan itu pasti memuat sesuatu yang berukuran.
- Bayangkan memilih sebuah tim tak kosong dari $n$ orang, lalu menunjuk seorang ketua dari dalam tim itu.
- Untuk cara kedua, balik urutan keputusannya: tunjuk ketua lebih dulu, baru tentukan siapa lagi yang ikut.

## Pembahasan

**Nyatakan himpunannya.** Tinjau

$$T = \bigl\{(A, x) : A \subseteq \{1,2,\dots,n\},\ x \in A \bigr\}$$

yaitu pasangan berupa sebuah himpunan bagian $A$ beserta satu unsur terpilih $x$ dari dalam
$A$. Bacaan sehari-harinya: sebuah tim beserta ketuanya.

Perhatikan $A$ tidak mungkin kosong, sebab $x$ harus berada di dalamnya.

### Cara A — pilih himpunannya dulu

Pecah $T$ menurut ukuran $A$. Kelompok-kelompok ini lepas dan menutupi seluruh $T$, sebab
tiap pasangan punya tepat satu ukuran $|A|$.

Untuk ukuran $k$ tertentu:

- himpunan bagian berukuran $k$ ada $\dbinom{n}{k}$;
- tiap himpunan semacam itu punya $k$ pilihan unsur terpilih.

Menurut aturan kali, kelompok berukuran $k$ menyumbang $k\binom{n}{k}$ pasangan. Menurut
aturan jumlah,

$$|T| = \sum_{k=1}^{n} k \binom{n}{k}$$

### Cara B — pilih unsur terpilihnya dulu

Tentukan $x$ lebih dulu. Ia boleh unsur mana pun:

$$n \text{ pilihan}$$

Setelah $x$ tetap, himpunan $A$ tinggal ditentukan oleh $n-1$ unsur sisanya, dan
masing-masing bebas ikut atau tidak ikut — tanpa syarat apa pun, sebab $A$ dijamin tak
kosong oleh keberadaan $x$:

$$2^{\,n-1}$$

Banyaknya pilihan ini sama untuk tiap $x$, sehingga aturan kali sah:

$$|T| = n \cdot 2^{\,n-1}$$

### Simpulkan

Kedua cara mencacah himpunan $T$ yang sama, sehingga hasilnya wajib sama:

$$\sum_{k=1}^{n} k \binom{n}{k} = n \cdot 2^{\,n-1} \qquad \blacksquare$$

### Mengapa penjumlahannya lenyap pada cara kedua

Pada cara A, pilihan unsur terpilih bergantung pada ukuran $A$ — itulah yang memaksa
penjumlahan atas $k$. Pada cara B, urutan keputusannya dibalik: begitu $x$ ditetapkan
lebih dulu, sisa keputusannya seragam untuk setiap $x$, dan tidak ada lagi yang perlu
dijumlahkan.

**Mencari urutan keputusan yang membuat penjumlahan lenyap** adalah keterampilan inti
jurus ini, dan ia terpakai jauh melampaui identitas ini.

### Periksa untuk $n = 3$

Ruas kiri: $1\binom31 + 2\binom32 + 3\binom33 = 3 + 6 + 3 = 12$.

Ruas kanan: $3 \cdot 2^{2} = 12$. Cocok.

Daftar pasangannya memang $12$: tiga tim berukuran satu (masing-masing satu pilihan ketua),
tiga tim berukuran dua (masing-masing dua pilihan), dan satu tim berukuran tiga (tiga
pilihan) — yaitu $3 + 6 + 3$.

## Rubrik

- Menyatakan dengan jelas himpunan yang dicacah, yaitu pasangan himpunan bagian dan unsur terpilih di dalamnya
- Menyebut bahwa himpunan bagiannya tidak mungkin kosong
- Cara A: memecah menurut ukuran, dan menyatakan kelompoknya lepas serta lengkap
- Cara A: menghitung sumbangan tiap ukuran sebagai $k\binom{n}{k}$
- Cara B: menghitung $n$ pilihan unsur terpilih, lalu $2^{n-1}$ untuk sisanya
- Cara B: menyebut bahwa banyaknya pilihan sisa itu sama untuk tiap unsur terpilih
- Menyimpulkan kedua ruas sama karena mencacah himpunan yang sama
