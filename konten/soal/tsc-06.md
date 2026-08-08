---
id: tsc-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [teorema-sisa-cina]
bentuk: uraian
kesulitan: 3
---

## Soal

Misalkan $m$ dan $n$ bilangan asli dengan $\gcd(m, n) = 1$. Buktikan bahwa sistem

$$x \equiv a \pmod m, \qquad x \equiv b \pmod n$$

punya solusi bulat, dan bahwa solusinya tunggal modulo $mn$.

## Petunjuk

- Ada dua hal terpisah: keberadaan solusi, dan ketunggalannya. Kerjakan berurutan.
- Untuk keberadaan, tulis $x = a + mt$ dari kongruensi pertama lalu selesaikan $t$ dari kongruensi kedua — di situ $\gcd(m,n)=1$ menjamin invers $m$ modulo $n$ ada.
- Untuk ketunggalan, ambil dua solusi lalu tinjau selisihnya: apa yang membagi selisih itu?

## Pembahasan

### Keberadaan

Dari kongruensi pertama, setiap kandidat solusi berbentuk

$$x = a + mt, \qquad t \in \mathbb{Z}$$

Masukkan ke kongruensi kedua:

$$a + mt \equiv b \pmod n \quad\Longrightarrow\quad mt \equiv b - a \pmod n$$

Karena $\gcd(m, n) = 1$, bilangan $m$ punya invers modulo $n$; sebut $m^{-1}$. Maka

$$t \equiv m^{-1}(b - a) \pmod n$$

Kongruensi ini selalu punya solusi $t$, dan setiap $t$ semacam itu memberi

$$x = a + mt$$

yang memenuhi kedua kongruensi sekaligus. Jadi solusinya ada.

### Ketunggalan modulo $mn$

Misalkan $x_1$ dan $x_2$ keduanya solusi. Maka

$$x_1 \equiv x_2 \pmod m \quad \text{dan} \quad x_1 \equiv x_2 \pmod n$$

sebab keduanya kongruen dengan $a$ modulo $m$ dan dengan $b$ modulo $n$. Artinya

$$m \mid x_1 - x_2 \quad \text{dan} \quad n \mid x_1 - x_2$$

Di sinilah syarat $\gcd(m,n) = 1$ dipakai untuk kedua kalinya: kalau dua bilangan yang
saling asing masing-masing membagi sesuatu, hasil kalinya juga membagi. Maka

$$mn \mid x_1 - x_2 \quad\Longrightarrow\quad x_1 \equiv x_2 \pmod{mn}$$

Jadi solusinya tunggal modulo $mn$. $\blacksquare$

Syarat $\gcd(m,n) = 1$ tidak bisa dilonggarkan. Ambil $m = 4$, $n = 6$, dengan
$x \equiv 1 \pmod 4$ dan $x \equiv 2 \pmod 6$: kongruensi pertama menuntut $x$ ganjil,
kedua menuntut $x$ genap, jadi tidak ada solusi sama sekali. Yang gagal adalah langkah
"$m$ punya invers modulo $n$".

## Rubrik

- Memisahkan pembuktian menjadi keberadaan dan ketunggalan
- Menulis $x = a + mt$ dan mensubstitusikannya ke kongruensi kedua
- Menyatakan invers $m$ modulo $n$ ada **karena** $\gcd(m,n) = 1$, lalu menyelesaikan $t$
- Ketunggalan: menyimpulkan $m \mid x_1 - x_2$ dan $n \mid x_1 - x_2$ dari dua solusi sembarang
- Memakai kesalingasingan untuk menyimpulkan $mn \mid x_1 - x_2$ — langkah ini tidak boleh dilewati begitu saja
