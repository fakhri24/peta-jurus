---
id: cvm-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ceva-menelaus, kesebangunan]
bentuk: uraian
kesulitan: 4
---

## Soal

Sebuah garis lurus $\ell$ memotong garis $BC$ di $D$, garis $CA$ di $E$, dan garis $AB$ di
$F$, dengan $\ell$ tidak melalui satu pun titik sudut segitiga $ABC$.

Buktikan teorema Menelaus:

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$

## Petunjuk

- Ketiga perbandingan itu diukur pada tiga garis yang berbeda. Adakah satu besaran yang bisa mengukur ketiganya sekaligus?
- Turunkan tegak lurus dari $A$, $B$, dan $C$ ke garis $\ell$, dan namai ketiga panjangnya.
- Tiap perbandingan pada sisi segitiga sama dengan perbandingan dua di antara ketiga panjang itu, lewat sepasang segitiga sebangun.

## Pembahasan

**Buat satu alat ukur bersama.** Dari $A$, $B$, dan $C$ turunkan tegak lurus ke garis $\ell$.
Namai kakinya $A'$, $B'$, $C'$ dan panjangnya

$$x = AA', \qquad y = BB', \qquad z = CC'$$

Ketiganya positif, sebab $\ell$ tidak melalui satu pun titik sudut.

**Perbandingan pertama.** Titik $D$ ada pada garis $BC$ dan pada $\ell$. Segitiga $DBB'$ dan
$DCC'$ keduanya siku-siku (di $B'$ dan di $C'$), dan sudutnya di $D$ sama besar — bertolak
belakang kalau $B$ dan $C$ berada di sisi berlawanan dari $\ell$, atau sudut yang sama persis
kalau keduanya di sisi yang sama. Maka

$$\triangle DBB' \sim \triangle DCC' \quad \Longrightarrow \quad \frac{BD}{DC} = \frac{y}{z}$$

**Perbandingan kedua dan ketiga.** Dengan alasan yang sama persis, dari $E$ pada garis $CA$
dan dari $F$ pada garis $AB$:

$$\frac{CE}{EA} = \frac{z}{x}, \qquad \frac{AF}{FB} = \frac{x}{y}$$

**Kalikan.**

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB}
= \frac{y}{z} \cdot \frac{z}{x} \cdot \frac{x}{y} = 1 \qquad \blacksquare$$

### Apa yang membuat bukti ini bekerja

Ketiga perbandingan awalnya hidup di tiga garis yang berbeda dan tidak bisa dibandingkan satu
sama lain. Yang dilakukan bukti ini adalah **memindahkan ketiganya ke satu ukuran bersama** —
jarak ke $\ell$ — sehingga hasil kalinya menjadi teleskopik dan lenyap.

Pola itu berulang di banyak tempat: kalau sebuah hasil kali perbandingan harus bernilai $1$,
cari besaran yang membuat tiap suku berbentuk $\tfrac{p_i}{p_{i+1}}$.

### Kenapa $\ell$ tidak boleh lewat titik sudut

Kalau $\ell$ melalui, misalnya, titik $A$, maka $x = 0$ dan dua di antara pecahan tadi tidak
terdefinisi. Secara gambar pun rusak: $E$ dan $F$ keduanya jatuh di $A$, dan perbandingan
$\tfrac{CE}{EA}$ berpenyebut nol.

Syarat itu karena itu bukan kehati-hatian berlebihan — ia bagian dari pernyataan teoremanya.

### Tandanya, dan kenapa versi bertanda lebih berguna

Bukti di atas memakai panjang tak bertanda, sehingga hasilnya $1$. Kalau perbandingannya
diukur **bertanda** — positif bila arahnya searah, negatif bila berlawanan — maka tepat satu
atau tepat tiga di antara ketiga titik jatuh di perpanjangan sisinya, sehingga hasil kalinya

$$\frac{\overline{BD}}{\overline{DC}} \cdot \frac{\overline{CE}}{\overline{EA}}
\cdot \frac{\overline{AF}}{\overline{FB}} = -1$$

Versi bertanda inilah yang membedakan Menelaus dari Ceva, sebab Ceva memberi $+1$. Dengan
tanda, kedua teorema beserta kebalikannya bisa dipakai tanpa perlu melihat gambar sama
sekali — dan itu berharga justru pada soal yang gambarnya belum jelas saat teoremanya
dipakai.

### Kebalikannya, dan mengapa ia perlu dibuktikan terpisah

Kebalikan Menelaus berbunyi: kalau hasil kali bertandanya $-1$, maka $D$, $E$, $F$ segaris.
Ia tidak otomatis ikut dari bukti di atas, dan buktinya punya bentuk baku yang layak dihafal:

Andaikan hasil kalinya $-1$. Tarik garis lewat $D$ dan $E$; ia memotong garis $AB$ di suatu
titik $F'$. Menurut teorema Menelaus yang baru dibuktikan, hasil kali dengan $F'$ juga
$-1$. Menyamakan keduanya memberi

$$\frac{\overline{AF}}{\overline{FB}} = \frac{\overline{AF'}}{\overline{F'B}}$$

Karena pada garis $AB$ hanya ada **satu** titik yang membaginya menurut perbandingan bertanda
tertentu, maka $F = F'$, sehingga $F$ ada pada garis $DE$ $\blacksquare$

Pola "andaikan titik lain, buktikan ia sama dengan yang asli" itu bentuk baku untuk semua
kebalikan teorema jenis ini — termasuk kebalikan Ceva dan kebalikan kuasa titik.

## Rubrik

- Menurunkan tegak lurus dari ketiga titik sudut ke $\ell$ dan menamai ketiga panjangnya
- Menyatakan $\triangle DBB' \sim \triangle DCC'$ beserta kedua alasannya: sudut siku-siku,
  dan sudut di $D$ yang sama besar
- Menyimpulkan $\dfrac{BD}{DC} = \dfrac{y}{z}$, lalu menyatakan kedua perbandingan lainnya
  dengan alasan yang serupa
- Mengalikan ketiganya dan menunjukkan semuanya saling meniadakan
- Menyebut bahwa $\ell$ tidak melalui titik sudut sebagai alasan ketiga panjangnya tidak nol

Bukti yang memakai garis bantu sejajar — misalnya menarik garis lewat $C$ sejajar $AB$ —
dinilai penuh asalkan tiap kesebangunan yang dipakai disebut beserta alasannya.
