---
id: inv-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [invarian]
bentuk: uraian
kesulitan: 4
---

## Soal

Sebuah bidak berada di titik $(0,0)$ pada bidang koordinat. Sekali melangkah, bidak itu
boleh berpindah ke salah satu dari empat titik berikut:

$$(x+1,\, y+1), \quad (x+1,\, y-1), \quad (x-1,\, y+1), \quad (x-1,\, y-1)$$

Buktikan bahwa bidak itu **tidak pernah** dapat mencapai titik $(2,3)$, berapa pun banyaknya
langkah.

## Petunjuk

- Soal meminta membuktikan sesuatu **tidak mungkin**. Cari besaran yang tidak pernah berubah, lalu bandingkan nilainya di titik awal dan titik tujuan.
- Perhatikan bagaimana $x+y$ berubah pada tiap jenis langkah. Ia berubah, tetapi tidak sembarangan.
- Kalau setiap langkah mengubah $x+y$ dengan bilangan genap, apa yang kekal?

## Pembahasan

**Tebak besarannya.** Keempat langkah mengubah $x$ dan $y$ masing-masing sebesar $\pm 1$,
jadi jumlah $x+y$ adalah calon yang wajar.

**Periksa tiap langkah.** Sebut $s = x + y$.

| Langkah | Perubahan $x$ | Perubahan $y$ | Perubahan $s$ |
|---|---|---|---|
| $(x+1, y+1)$ | $+1$ | $+1$ | $+2$ |
| $(x+1, y-1)$ | $+1$ | $-1$ | $0$ |
| $(x-1, y+1)$ | $-1$ | $+1$ | $0$ |
| $(x-1, y-1)$ | $-1$ | $-1$ | $-2$ |

Pada keempat langkah, perubahan $s$ selalu $+2$, $0$, atau $-2$ — seluruhnya **genap**.
Karena itu

$$s \bmod 2 \text{ tidak pernah berubah}$$

Perhatikan keempat langkah diperiksa, bukan sebagian. Kalau ada satu langkah yang belum
diperiksa, buktinya tidak sah — dan langkah yang terlewat biasanya justru yang merusak
invariannya.

**Bandingkan awal dan tujuan.**

$$s_{\text{awal}} = 0 + 0 = 0 \quad (\text{genap})$$

$$s_{\text{tujuan}} = 2 + 3 = 5 \quad (\text{ganjil})$$

Paritasnya berbeda. Karena paritas $s$ tidak pernah berubah, titik $(2,3)$ tidak akan
pernah tercapai. $\blacksquare$

### Bacaan lain: pewarnaan papan catur

Warnai tiap titik $(x,y)$ menurut paritas $x+y$ — hitam kalau genap, putih kalau ganjil.
Keempat langkah selalu memindahkan bidak dari titik hitam ke titik hitam. Bidak berangkat
dari titik hitam $(0,0)$, sedangkan $(2,3)$ berwarna putih.

Ini invarian yang sama, hanya dinyatakan sebagai warna. Cara pandang itu yang akan
dikembangkan menjadi jurus tersendiri di tahap berikutnya.

### Batas yang tidak dibuktikan bukti ini

Bukti ini menunjukkan titik dengan $x+y$ ganjil tidak bisa dicapai. Ia **tidak**
membuktikan bahwa seluruh titik dengan $x+y$ genap bisa dicapai — untuk itu dibutuhkan
konstruksi.

Kebetulan di sini semuanya memang bisa: dari $(0,0)$, langkah $(x+1,y+1)$ dan
$(x+1,y-1)$ bersama-sama menggeser $x$ sebesar $2$ tanpa mengubah $y$, dan pasangan
langkah lain menggeser $y$ sebesar $2$ tanpa mengubah $x$. Dengan itu setiap titik berjumlah
genap dapat dicapai.

Kelengkapan seperti ini yang membedakan "syarat perlu" dari "syarat perlu dan cukup", dan
invarian sendiri hanya pernah memberi yang pertama.

## Rubrik

- Memilih besaran $x+y$ sebagai calon invarian
- Memeriksa **keempat** langkah, bukan sebagian, dan mencatat perubahan $x+y$ pada masing-masing
- Menyimpulkan perubahannya selalu genap, sehingga paritas $x+y$ kekal
- Menghitung paritas di titik awal ($0$, genap) dan titik tujuan ($5$, ganjil)
- Menyimpulkan $(2,3)$ tidak dapat dicapai karena paritasnya berbeda
- Menyatakan bahwa yang dibuktikan adalah ketidakmungkinan, dan invarian tidak membuktikan sebaliknya
