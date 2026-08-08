---
id: tsf-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [teorema-sisa-faktor, suku-banyak]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan teorema sisa: untuk polinomial $P$ dan bilangan $a$, sisa pembagian $P(x)$ oleh
$(x-a)$ adalah $P(a)$. Turunkan pula teorema faktor darinya.

## Petunjuk

- Mulai dari algoritma pembagian untuk polinomial: $P(x) = (x-a)Q(x) + R(x)$ dengan syarat pada derajat $R$.
- Syarat derajatnya yang menentukan bentuk $R$. Berapa derajat pembaginya, dan apa artinya bagi $R$?
- Setelah $R$ diketahui berupa konstanta, substitusikan $x = a$.

## Pembahasan

### Teorema sisa

Menurut algoritma pembagian untuk polinomial, untuk pembagi tak nol $(x-a)$ ada polinomial
$Q$ dan $R$ yang **tunggal** dengan

$$P(x) = (x-a)\,Q(x) + R(x), \qquad \deg R < \deg(x-a)$$

Karena $\deg(x-a) = 1$, syaratnya menjadi $\deg R < 1$. Polinomial berderajat kurang dari
$1$ adalah **konstanta** — termasuk polinomial nol. Tulis $R(x) = r$.

Jadi

$$P(x) = (x-a)\,Q(x) + r$$

dan persamaan ini berlaku untuk **setiap** nilai $x$, sebab kedua ruas polinomial yang
sama.

Substitusikan $x = a$:

$$P(a) = (a-a)\,Q(a) + r = 0 \cdot Q(a) + r = r$$

Jadi sisanya $r = P(a)$. $\blacksquare$

### Teorema faktor

$(x-a)$ merupakan faktor $P$ tepat ketika pembagiannya bersisa nol, yaitu $r = 0$. Dan
menurut yang baru dibuktikan, $r = P(a)$. Maka

$$(x-a) \mid P(x) \iff P(a) = 0$$

$\blacksquare$

### Catatan atas langkah-langkahnya

**Langkah "$\deg R < 1$ berarti $R$ konstanta" itu inti pembuktiannya.** Tanpa syarat
derajat pada algoritma pembagian, $R$ bisa berupa polinomial apa pun dan substitusi $x = a$
tidak memberi keterangan tunggal.

**Langkah "berlaku untuk setiap $x$" juga perlu dinyatakan.** Yang dilakukan bukan
menyelesaikan persamaan, melainkan memanfaatkan bahwa kedua ruasnya polinomial identik —
sehingga nilai apa pun boleh dimasukkan, termasuk $x = a$ yang membuat pembaginya nol.

Perhatikan pula bahwa $Q$ tidak pernah dihitung. Itulah penghematan yang ditawarkan
teorema ini: pertanyaan tentang pembagian dijawab tanpa membagi sama sekali.

Untuk pembagi berderajat lebih tinggi, gagasan yang sama diperluas. Sisa pembagian oleh
$(x-a)(x-b)$ berderajat kurang dari $2$, jadi berbentuk $px+q$; mensubstitusikan $x = a$
dan $x = b$ memberi dua persamaan yang menentukan keduanya.

## Rubrik

- Memanggil algoritma pembagian dengan syarat derajat sisanya
- Menyimpulkan $R$ konstanta **dari** syarat $\deg R < 1$, bukan mengandaikannya
- Menyatakan persamaannya berlaku untuk setiap $x$ karena kedua ruas polinomial yang sama
- Mensubstitusikan $x = a$ dan menyimpulkan $r = P(a)$
- Menurunkan teorema faktor sebagai kasus $r = 0$, dengan kesetaraan dua arah
