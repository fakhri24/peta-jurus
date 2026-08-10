---
id: ktg-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [ketaksamaan-geometri]
bentuk: isian
kesulitan: 4
jawaban: "3"
---

## Soal

Panjang sisi sebuah segitiga adalah $a$, $b$, dan $c$. Tentukan nilai terkecil dari

$$\frac{a}{b+c-a} + \frac{b}{c+a-b} + \frac{c}{a+b-c}$$

## Petunjuk

- Ketiga penyebutnya positif justru karena $a$, $b$, $c$ sisi segitiga. Ketiganya juga punya nama yang membuat pembilangnya ikut rapi.
- Tulis $a = y+z$, $b = z+x$, $c = x+y$ dengan $x, y, z > 0$. Penyebut yang pertama menjadi $2x$.
- Setelah disubstitusi, bentuknya menjadi jumlah enam pecahan $\dfrac{y}{x}$, $\dfrac{x}{y}$, dan seterusnya. Pasangkan tiap pecahan dengan kebalikannya.

## Pembahasan

**Substitusi Ravi.** Ambil

$$a = y+z, \qquad b = z+x, \qquad c = x+y \qquad (x, y, z > 0)$$

Penyebutnya jadi rapi seketika:

$$b+c-a = (z+x) + (x+y) - (y+z) = 2x$$

dan seterusnya $c+a-b = 2y$, $a+b-c = 2z$. Jadi yang dicari menjadi

$$S = \frac{y+z}{2x} + \frac{z+x}{2y} + \frac{x+y}{2z}$$

**Pecah dan pasangkan.** Uraikan tiap suku:

$$S = \frac12\left(\frac{y}{x} + \frac{z}{x} + \frac{z}{y} + \frac{x}{y} + \frac{x}{z} + \frac{y}{z}\right)$$

Keenam pecahan itu berpasangan: $\dfrac{y}{x}$ dengan $\dfrac{x}{y}$, $\dfrac{z}{x}$
dengan $\dfrac{x}{z}$, $\dfrac{z}{y}$ dengan $\dfrac{y}{z}$. Untuk setiap $t > 0$ berlaku
AM-GM

$$t + \frac1t \ \ge\ 2$$

sehingga ketiga pasangan itu masing-masing paling sedikit $2$:

$$S \ \ge\ \frac12 \left(2 + 2 + 2\right) = \boxed{3}$$

**Kesamaannya tercapai.** $t + \tfrac1t = 2$ tepat ketika $t = 1$, jadi ketiga pasangan
mencapai batasnya sekaligus tepat ketika

$$x = y = z \quad \Longleftrightarrow \quad a = b = c$$

Untuk segitiga sama sisi bersisi $s$, tiap suku bernilai $\dfrac{s}{s} = 1$ dan
jumlahnya $3$ ✓

### Jawabannya tidak bergantung pada ukuran segitiganya

Perhatikan bahwa soalnya sama sekali tidak menyebut keliling, luas, atau ukuran apa
pun — dan memang tidak perlu. Mengalikan $a$, $b$, $c$ dengan bilangan positif yang sama
tidak mengubah nilai $S$: pembilang dan penyebut tiap suku ikut terkali faktor yang sama.

Besaran seperti itu disebut **tak berdimensi**, dan mengenalinya berguna sebagai
pemeriksaan: kalau jawaban sebuah soal tak berdimensi keluar memuat panjang, pasti ada
yang salah. Sebaliknya, kalau soalnya memberi keliling padahal bentuknya tak berdimensi,
angka keliling itu memang tidak dipakai.

### Kenapa syarat segitiganya perlu

Tanpa syarat segitiga, bentuk itu bahkan tidak selalu terdefinisi: untuk $a = 10$,
$b = 2$, $c = 3$, penyebut pertamanya $2 + 3 - 10 = -5$, dan sukunya menjadi negatif.
Dengan tiga bilangan positif sembarang, nilainya bisa dibuat sekecil apa pun, bahkan
negatif — jadi tidak ada nilai terkecil.

Jadi syarat segitiganya bukan hiasan pada soal ini; ia yang membuat pertanyaannya
punya jawaban.

### Kalau AM-GM dipakai langsung, tanpa Ravi

Godaannya adalah menerapkan AM-GM pada ketiga sukunya sekaligus:

$$S \ \ge\ 3\sqrt[3]{\frac{abc}{(b+c-a)(c+a-b)(a+b-c)}}$$

Itu benar, tetapi belum selesai — akar di ruas kanan masih memuat $a$, $b$, $c$, dan
untuk menutupnya masih perlu ditunjukkan bahwa

$$abc \ \ge\ (b+c-a)(c+a-b)(a+b-c)$$

Ketaksamaan itu sendiri sebuah soal (lihat latihan terakhir jurus ini). Jalur Ravi
lebih pendek karena ia membelah masalahnya menjadi tiga pasangan yang masing-masing
sepele, bukan satu akar pangkat tiga yang masih harus ditaklukkan.

### Nilai sebenarnya pada beberapa segitiga

| $a$ | $b$ | $c$ | $S$ |
|---|---|---|---|
| $1$ | $1$ | $1$ | $3$ |
| $3$ | $4$ | $5$ | $\tfrac{3}{6} + \tfrac{4}{4} + \tfrac{5}{2} = 4$ |
| $5$ | $5$ | $8$ | $\tfrac{5}{8} + \tfrac{5}{8} + \tfrac{8}{2} = 5{,}25$ |
| $10$ | $10$ | $1$ | $\tfrac{10}{1} + \tfrac{10}{1} + \tfrac{1}{19} \approx 20{,}05$ |

Makin gepeng segitiganya, makin besar nilainya — tanpa batas atas. Yang ada cuma batas
bawah, dan batas itu di segitiga sama sisi.
