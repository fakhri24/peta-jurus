---
id: tth-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [turun-tak-hingga]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa $\sqrt[3]{2}$ bukan bilangan rasional.

## Petunjuk

- Alurnya sama seperti pada akar kuadrat, hanya pangkatnya berubah. Mulai dari pengandaian rasional.
- Dari $a^3 = 2b^3$, simpulkan paritas $a$ — ingat bahwa pangkat tiga ganjil selalu ganjil.
- Setelah $a = 2a_1$ disubstitusikan, perhatikan bahwa yang muncul adalah $b^3 = 4a_1^3$, dan dari situ $b$ juga genap.

## Pembahasan

Andaikan $\sqrt[3]{2}$ rasional, sehingga ada bilangan asli $a$ dan $b$ dengan

$$\sqrt[3]{2} = \frac{a}{b} \quad\Longrightarrow\quad a^3 = 2b^3$$

**Langkah turun.** Ruas kanan genap, jadi $a^3$ genap. Karena pangkat tiga bilangan ganjil
selalu ganjil, $a$ sendiri genap. Tulis $a = 2a_1$:

$$8a_1^3 = 2b^3 \quad\Longrightarrow\quad b^3 = 4a_1^3$$

Ruas kanan genap, jadi $b^3$ genap dan $b$ genap. Tulis $b = 2b_1$:

$$8b_1^3 = 4a_1^3 \quad\Longrightarrow\quad a_1^3 = 2b_1^3$$

Bentuknya kembali seperti semula, dengan

$$a_1 = \frac{a}{2} < a, \qquad b_1 = \frac{b}{2} < b$$

**Kontradiksinya.** Prosesnya bisa diulang selamanya, memberi barisan bilangan asli yang
menurun tegas tanpa henti — mustahil. Jadi $\sqrt[3]{2}$ tidak rasional. $\blacksquare$

Bentuk yang lebih ringkas: pilih sejak awal $b$ **terkecil** di antara semua penulisan
$\sqrt[3]{2} = a/b$. Menemukan $b_1 < b$ langsung menutup soal.

Argumen yang sama bekerja untuk $\sqrt[n]{2}$ dengan $n$ berapa pun — yang dipakai hanya
bahwa pangkat bilangan ganjil tetap ganjil. Lebih umum lagi, dengan faktorisasi prima
tunggal: $a^n = 2b^n$ mustahil karena pangkat $2$ di ruas kiri kelipatan $n$, sedangkan di
ruas kanan bersisa $1$ modulo $n$.

## Rubrik

- Mengandaikan $\sqrt[3]{2} = a/b$ untuk bilangan asli $a, b$, lalu menurunkan $a^3 = 2b^3$
- Menyimpulkan $a$ genap, dengan alasan pangkat tiga bilangan ganjil selalu ganjil
- Mensubstitusikan $a = 2a_1$ dan menurunkan $b^3 = 4a_1^3$ dengan benar
- Menyimpulkan $b$ genap juga, lalu kembali ke bentuk $a_1^3 = 2b_1^3$
- Menyatakan pasangan barunya bilangan asli dan benar-benar lebih kecil
- Menutup dengan kemustahilan penurunan tak hingga, atau dengan pemilihan $b$ terkecil sejak awal
