---
id: lte-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [lte]
bentuk: uraian
kesulitan: 3
---

## Soal

Misalkan $p$ prima ganjil, dan $a$, $b$ bilangan bulat dengan $p \mid a - b$ tetapi
$p \nmid a$ dan $p \nmid b$. Buktikan bahwa

$$v_p\left(a^p - b^p\right) = v_p(a - b) + 1$$

## Petunjuk

- Faktorkan $a^p - b^p$ menjadi $(a-b)$ dikali sesuatu. Seluruh soal bertumpu pada faktor kedua itu.
- Yang perlu dibuktikan: faktor kedua, $S = a^{p-1} + a^{p-2}b + \cdots + b^{p-1}$, habis dibagi $p$ **tepat satu kali**.
- Tulis $a = b + kp$ dan jabarkan tiap suku $S$ modulo $p^2$. Suku-suku yang memuat $p^2$ boleh dibuang sejak awal.

## Pembahasan

Faktorkan:

$$a^p - b^p = (a - b)\underbrace{\left(a^{p-1} + a^{p-2}b + \cdots + ab^{p-2} + b^{p-1}\right)}_{S}$$

dengan $S$ memuat tepat $p$ suku. Maka

$$v_p\left(a^p - b^p\right) = v_p(a-b) + v_p(S)$$

sehingga yang perlu dibuktikan tinggal

$$v_p(S) = 1$$

yaitu $S$ habis dibagi $p$ tetapi tidak habis dibagi $p^2$.

**Tulis $a$ lewat $b$.** Karena $p \mid a - b$, ada bilangan bulat $k$ dengan

$$a = b + kp$$

**Jabarkan tiap suku modulo $p^2$.** Suku ke-$i$ dari $S$ adalah $a^{i} b^{p-1-i}$ untuk
$i = 0, 1, \ldots, p-1$. Dengan teorema binomial,

$$a^{i} = (b + kp)^{i} = b^{i} + i\, b^{i-1}(kp) + \binom{i}{2} b^{i-2}(kp)^2 + \cdots$$

Semua suku mulai dari yang ketiga memuat $p^2$, jadi modulo $p^2$:

$$a^{i} \equiv b^{i} + i\,k\,p\,b^{i-1} \pmod{p^2}$$

Kalikan dengan $b^{p-1-i}$:

$$a^{i} b^{p-1-i} \equiv b^{p-1} + i\,k\,p\,b^{p-2} \pmod{p^2}$$

**Jumlahkan seluruh $p$ suku.**

$$S \equiv \sum_{i=0}^{p-1} \left(b^{p-1} + i\,k\,p\,b^{p-2}\right)
= p\,b^{p-1} + k\,p\,b^{p-2} \sum_{i=0}^{p-1} i \pmod{p^2}$$

Jumlah $\sum_{i=0}^{p-1} i = \dfrac{p(p-1)}{2}$. Karena $p$ ganjil, $\dfrac{p-1}{2}$ bulat,
sehingga

$$k\,p\,b^{p-2} \times \frac{p(p-1)}{2} = k\,b^{p-2}\,p^2 \times \frac{p-1}{2}
\equiv 0 \pmod{p^2}$$

Suku kedua lenyap seluruhnya. Tersisa

$$S \equiv p\,b^{p-1} \pmod{p^2}$$

**Simpulkan.** Dari bentuk itu, $p \mid S$. Dan $S$ tidak habis dibagi $p^2$, sebab kalau
demikian maka $p^2 \mid p\,b^{p-1}$, yaitu $p \mid b^{p-1}$ — dan karena $p$ prima itu
berarti $p \mid b$, bertentangan dengan yang diketahui.

Jadi $v_p(S) = 1$, sehingga

$$v_p\left(a^p - b^p\right) = v_p(a-b) + 1 \qquad \blacksquare$$

Inilah lema inti LTE. Rumus umum $v_p(a^n - b^n) = v_p(a-b) + v_p(n)$ diperoleh dengan
menerapkannya berulang: setiap kali satu faktor $p$ dikupas dari eksponen, satu pangkat
bertambah — dan bagian eksponen yang tidak memuat $p$ tidak menyumbang apa-apa.

Perhatikan di mana syarat "$p$ ganjil" dipakai: pada langkah $\frac{p-1}{2}$ bulat. Untuk
$p = 2$ langkah itu gugur, dan di situlah rumus kasus $2$ menyimpang.

## Rubrik

- Memfaktorkan $a^p - b^p = (a-b)S$ dan menyatakan soalnya menyusut menjadi $v_p(S) = 1$
- Menulis $a = b + kp$ dengan memakai hipotesis $p \mid a - b$
- Menjabarkan $a^i$ dengan teorema binomial dan membuang suku bersuku $p^2$ ke atas
- Menjumlahkan seluruh $p$ suku dan mengenali $\sum i = \frac{p(p-1)}{2}$
- Menunjukkan suku kedua lenyap modulo $p^2$, **dengan menyebut $p$ ganjil sebagai alasannya**
- Menyimpulkan $S \equiv p\,b^{p-1}$, lalu memakai $p \nmid b$ untuk menutup bahwa $p^2 \nmid S$
