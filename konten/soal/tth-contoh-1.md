---
id: tth-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [turun-tak-hingga]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa $\sqrt{2}$ bukan bilangan rasional.

## Petunjuk

- Andaikan ia rasional. Tulis sebagai pecahan, lalu cari sesuatu yang bisa diperkecil terus-menerus.
- Dari $a^2 = 2b^2$, paritas $a$ terkunci. Apa yang bisa disimpulkan tentang $a$, lalu tentang $b$?
- Setelah $a$ dan $b$ keduanya genap, kamu punya pecahan baru dengan pembilang dan penyebut lebih kecil — dan prosesnya bisa diulang selamanya.

## Pembahasan

Andaikan $\sqrt{2}$ rasional. Maka ada bilangan asli $a$ dan $b$ dengan

$$\sqrt{2} = \frac{a}{b} \quad\Longrightarrow\quad a^2 = 2b^2$$

**Langkah turun.** Ruas kanan genap, jadi $a^2$ genap. Kuadrat bilangan ganjil selalu
ganjil, jadi $a$ sendiri genap. Tulis $a = 2a_1$:

$$4a_1^2 = 2b^2 \quad\Longrightarrow\quad b^2 = 2a_1^2$$

Bentuknya persis sama seperti semula, hanya dengan pasangan $(b, a_1)$. Dengan alasan yang
sama, $b$ genap; tulis $b = 2b_1$, sehingga

$$a_1^2 = 2b_1^2$$

Jadi dari pasangan bilangan asli $(a, b)$ yang memenuhi $a^2 = 2b^2$, selalu bisa dibuat
pasangan bilangan asli lain $(a_1, b_1)$ yang juga memenuhinya, dengan

$$a_1 = \frac{a}{2} < a, \qquad b_1 = \frac{b}{2} < b$$

**Kontradiksinya.** Prosesnya bisa diulang tanpa henti, menghasilkan barisan bilangan asli

$$a > a_1 > a_2 > a_3 > \cdots$$

yang menurun terus dan semuanya positif. Itu mustahil: barisan bilangan asli yang menurun
tegas pasti berhenti setelah berhingga langkah.

Jadi pengandaian awalnya salah, dan $\sqrt{2}$ tidak rasional. $\blacksquare$

Bentuk yang lebih ringkas: ambil sejak awal pecahan $a/b$ dengan $b$ **terkecil**. Setelah
menemukan $(a_1, b_1)$ dengan $b_1 < b$, kontradiksinya langsung — tidak perlu mengulang
prosesnya sama sekali. Kedua bentuk ini setara, dan yang kedua biasanya lebih rapi ditulis.

## Rubrik

- Memulai dengan pengandaian $\sqrt{2} = a/b$ untuk bilangan asli $a, b$, lalu menurunkan $a^2 = 2b^2$
- Menyimpulkan $a$ genap dari $a^2$ genap, dengan alasan bahwa kuadrat ganjil selalu ganjil
- Mensubstitusikan $a = 2a_1$ dan menurunkan $b^2 = 2a_1^2$, lalu menyimpulkan $b$ genap juga
- Menunjukkan pasangan barunya **benar-benar lebih kecil** dan tetap bilangan asli
- Menutup dengan kemustahilan barisan bilangan asli yang menurun selamanya — atau, setara, dengan memilih $b$ terkecil sejak awal
