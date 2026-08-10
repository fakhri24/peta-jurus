---
id: ktg-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [ketaksamaan-geometri]
bentuk: isian
kesulitan: 4
jawaban: "8"
---

## Soal

Panjang sisi sebuah segitiga adalah $a$, $b$, dan $c$, dengan $a + b + c = 6$.

Tentukan nilai terbesar dari

$$(a+b-c)(b+c-a)(c+a-b)$$

## Petunjuk

- Ketiga faktor itu positif, dan itu bukan kebetulan — ketiganya positif tepat ketika $a$, $b$, $c$ bisa menjadi sisi sebuah segitiga. Beri nama ketiganya.
- Tulis $a = y+z$, $b = z+x$, $c = x+y$ dengan $x, y, z > 0$. Setelah itu $x$, $y$, $z$ boleh apa saja asal positif — syarat segitiganya sudah habis terpakai.
- Ketiga faktornya menjadi $2z$, $2x$, $2y$, dan $x+y+z = 3$. Sisanya AM-GM.

## Pembahasan

**Kenali ketiga faktornya.** Syarat segitiga berbunyi $a < b+c$, $b < c+a$, $c < a+b$ —
yang berarti persis bahwa

$$b+c-a > 0, \qquad c+a-b > 0, \qquad a+b-c > 0$$

Jadi ketiga faktor yang diminta itu bukan tiga bilangan sembarang: ketiganya adalah
syarat segitiganya sendiri, ditulis ulang.

**Substitusi Ravi.** Beri nama

$$x = \frac{b+c-a}{2}, \qquad y = \frac{c+a-b}{2}, \qquad z = \frac{a+b-c}{2}$$

Ketiganya positif, dan menjumlahkannya berpasangan memberi kembali

$$a = y+z, \qquad b = z+x, \qquad c = x+y$$

Inilah untungnya. Sebelum substitusi, $a$, $b$, $c$ terikat tiga ketaksamaan yang harus
diingat terus. Sesudahnya, $x$, $y$, $z$ hanya perlu positif — dan setiap tripel positif
$(x,y,z)$ memberi kembali sebuah segitiga. Kendalanya tidak dilanggar; ia **habis
terpakai** oleh substitusinya.

![Segitiga ABC dengan lingkaran dalam berpusat I yang menyinggung sisi BC di X, sisi CA di Y, dan sisi AB di Z. Keenam ruas dari titik sudut ke titik singgung terdekatnya diberi keterangan panjang, dan yang berasal dari titik sudut yang sama selalu sama: dari A panjangnya x ke Y maupun ke Z, dari B panjangnya y ke Z maupun ke X, dan dari C panjangnya z ke X maupun ke Y. Akibatnya sisi BC sepanjang y ditambah z, sisi CA sepanjang z ditambah x, dan sisi AB sepanjang x ditambah y](segitiga-panjang-singgung.svg)

Gambar itu menunjukkan bahwa $x$, $y$, $z$ bukan singkatan yang dikarang: ketiganya
adalah **panjang singgung** dari tiap titik sudut ke lingkaran dalamnya. Dua panjang
singgung dari satu titik selalu sama, jadi tiap sisi memang terpotong menjadi dua
bagian yang namanya sudah tersedia.

**Ubah soalnya.** Dengan $a+b+c = 6$:

$$2(x+y+z) = a+b+c = 6 \quad \Longrightarrow \quad x+y+z = 3$$

dan yang dicari menjadi

$$(a+b-c)(b+c-a)(c+a-b) = (2z)(2x)(2y) = 8xyz$$

**AM-GM.** Untuk $x, y, z > 0$,

$$\sqrt[3]{xyz} \ \le\ \frac{x+y+z}{3} = 1 \quad \Longrightarrow \quad xyz \le 1$$

sehingga

$$8xyz \ \le\ \boxed{8}$$

**Kesamaannya tercapai.** AM-GM menjadi kesamaan tepat ketika $x = y = z$, di sini
berarti $x = y = z = 1$, yaitu

$$a = b = c = 2$$

Segitiga sama sisi bersisi $2$ memang berkeliling $6$, dan nilainya
$(2+2-2)^3 = 2^3 = 8$ ✓

### Kenapa langkah terakhir itu wajib

Ketaksamaan saja baru memberi **batas**. Kalau berhenti di $8xyz \le 8$, yang terbukti
hanyalah bahwa nilainya tidak pernah melebihi $8$ — belum bahwa $8$ pernah tercapai.

Bedanya nyata. Andaikan soalnya menambahkan syarat "segitiganya siku-siku": batas
$8$ tetap benar, tetapi tidak lagi tercapai, sebab segitiga sama sisi bukan siku-siku.
Jawaban yang benar untuk soal itu bukan $8$.

Jadi soal maksimum-minimum selalu dua bagian: **batasnya**, lalu **satu contoh yang
mencapainya**.

### Periksa dengan segitiga lain

Ambil beberapa segitiga berkeliling $6$ dan hitung langsung:

| $a$ | $b$ | $c$ | $(a{+}b{-}c)(b{+}c{-}a)(c{+}a{-}b)$ |
|---|---|---|---|
| $2$ | $2$ | $2$ | $2 \cdot 2 \cdot 2 = 8$ |
| $2{,}5$ | $2$ | $1{,}5$ | $3 \cdot 1 \cdot 2 = 6$ |
| $2{,}8$ | $1{,}8$ | $1{,}4$ | $3{,}2 \cdot 0{,}4 \cdot 2{,}4 \approx 3{,}07$ |
| $2{,}9$ | $2{,}9$ | $0{,}2$ | $5{,}6 \cdot 0{,}2 \cdot 0{,}2 = 0{,}224$ |

Terlihat polanya: makin gepeng segitiganya, makin kecil hasilnya, dan ia menuju $0$
saat segitiganya merosot jadi ruas garis. Nilai terbesarnya di ujung yang berlawanan —
yang paling "bulat", yaitu sama sisi.

### Yang layak dibawa pulang

Angka $8$ di sini adalah kasus khusus sebuah ketaksamaan yang berlaku untuk segitiga
apa pun, tanpa syarat keliling:

$$abc \ \ge\ (a+b-c)(b+c-a)(c+a-b)$$

Untuk $a = b = c = 2$ keduanya bernilai $8$, dan itulah sebabnya batasnya tercapai
persis di sana. Ketaksamaan itu dibuktikan di salah satu latihan jurus ini — dan dari
sana lahir ketaksamaan Euler $R \ge 2r$.
