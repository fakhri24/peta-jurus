---
id: ktg-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [ketaksamaan-geometri, trigonometri-segitiga]
bentuk: isian
kesulitan: 4
jawaban: "4"
---

## Soal

Pada segitiga $ABC$, jari-jari lingkaran luarnya $R = 10$ dan berlaku

$$\cos A + \cos B + \cos C = \frac{7}{5}$$

Tentukan jari-jari lingkaran dalamnya.

## Petunjuk

- Jumlah ketiga kosinus itu bukan besaran lepas: ia bisa ditulis ulang seluruhnya dengan kedua jari-jari lingkaran segitiga itu.
- Buktikan atau pakai kesamaan $\cos A + \cos B + \cos C = 1 + \dfrac{r}{R}$.
- Setelah $r$ ketemu, periksa apakah segitiganya memang ada — ada satu ketaksamaan baku yang mengikat $R$ dan $r$.

## Pembahasan

**Kesamaan yang dipakai.** Untuk setiap segitiga berlaku

$$\cos A + \cos B + \cos C = 1 + \frac{r}{R}$$

**Menurunkannya.** Proyeksikan sisi-sisinya. Rumus proyeksi memberi

$$a = b\cos C + c\cos B, \qquad b = c\cos A + a\cos C, \qquad c = a\cos B + b\cos A$$

Jumlahkan ketiganya, lalu kelompokkan menurut kosinusnya:

$$a+b+c = \cos A\,(b+c) + \cos B\,(c+a) + \cos C\,(a+b)$$

Dengan $a+b+c = 2s$ dan $a = 2R\sin A$ pekerjaannya bisa diteruskan, tetapi jalur yang
lebih pendek lewat setengah sudut. Dari rumus baku

$$\cos A + \cos B + \cos C = 1 + 4\sin\frac{A}{2}\sin\frac{B}{2}\sin\frac{C}{2}
\qquad\text{dan}\qquad r = 4R \sin\frac{A}{2}\sin\frac{B}{2}\sin\frac{C}{2}$$

langsung diperoleh

$$\cos A + \cos B + \cos C = 1 + \frac{r}{R}$$

**Masukkan angkanya.**

$$1 + \frac{r}{10} = \frac{7}{5} \quad \Longrightarrow \quad \frac{r}{10} = \frac{2}{5}
\quad \Longrightarrow \quad r = \boxed{4}$$

### Periksa dulu segitiganya ada

Di sinilah jurus ini masuk. Ketaksamaan Euler berbunyi

$$R \ \ge\ 2r$$

Dengan $R = 10$ dan $r = 4$: $10 \ge 8$ ✓. Jadi tidak ada yang mustahil, dan memang ada
segitiga yang memenuhinya — misalnya yang bersisi

$$a \approx 10{,}64, \qquad b \approx 19{,}03, \qquad c \approx 19{,}39$$

yang memberi $R = 10$ dan $r = 4$ tepat.

Pemeriksaan itu bukan basa-basi. Andaikan soalnya menulis $\cos A + \cos B + \cos C =
\tfrac{8}{5}$, maka $\tfrac{r}{R} = \tfrac35$ dan $r = 6$, sehingga $R = 10 < 12 = 2r$ —
melanggar Euler. **Tidak ada segitiga seperti itu**, dan jawaban "$r = 6$" akan menjawab
soal yang tidak punya jawaban.

### Batas atas jumlah ketiga kosinus

Kesamaan tadi mengubah ketaksamaan Euler menjadi pernyataan tentang kosinus. Karena
$\dfrac{r}{R} \le \dfrac12$,

$$\cos A + \cos B + \cos C \ \le\ \frac{3}{2}$$

untuk **setiap** segitiga, dengan kesamaan tepat pada yang sama sisi — di sana ketiga
sudutnya $60^\circ$ dan jumlahnya $3 \cdot \tfrac12 = \tfrac32$ ✓

Nilai $\tfrac75 = 1{,}4$ pada soal ini berada di bawah $1{,}5$, seperti seharusnya.
Nisbah $\tfrac{r}{R} = 0{,}4$ juga memberi tahu bahwa segitiganya tidak jauh dari sama
sisi, dan ketiga sisi di atas memang tidak terlalu timpang.

### Batas bawahnya juga ada

Di ujung yang lain, $r > 0$ memberi

$$\cos A + \cos B + \cos C \ >\ 1$$

Batas $1$ tidak pernah tercapai, tetapi didekati saat segitiganya merosot jadi ruas
garis. Jadi jumlah ketiga kosinus segitiga apa pun selalu terkurung di

$$1 \ <\ \cos A + \cos B + \cos C \ \le\ \frac{3}{2}$$

Itu selang yang sempit, dan berguna sebagai pemeriksaan cepat: jumlah kosinus yang
keluar $0{,}8$ atau $1{,}7$ pasti salah hitung.

### Kenapa lewat $r/R$, bukan mencari sudutnya

Godaannya adalah mencari $A$, $B$, $C$ satu per satu dari $\cos A + \cos B + \cos C =
\tfrac75$. Itu tidak bisa: satu persamaan untuk tiga sudut, dan tak berhingga banyak
segitiga memenuhinya — yang bersisi $10{,}64 : 19{,}03 : 19{,}39$ hanya salah satunya.

Yang **sama** untuk semuanya justru $\dfrac{r}{R}$, dan soalnya menanyakan tepat besaran
itu. Mengenali bahwa yang ditanya invarian, bukan bentuk segitiganya, memangkas
seluruh pekerjaan.
