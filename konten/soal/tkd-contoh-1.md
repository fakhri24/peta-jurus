---
id: tkd-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [tempat-kedudukan]
bentuk: isian
kesulitan: 4
jawaban: "4"
---

## Soal

Titik $A$ dan $B$ tetap dengan $AB = 6$. Titik $P$ bergerak sehingga

$$\frac{PA}{PB} = 2$$

Tempat kedudukan $P$ ternyata sebuah lingkaran. Tentukan jari-jarinya.

## Petunjuk

- Perbandingan jarak yang tetap tidak memberi garis, kecuali perbandingannya $1$. Untuk mengetahui bangunnya, beri koordinat pada $A$ dan $B$ lalu tulis syaratnya sebagai persamaan.
- Taruh $A$ di pangkal dan $B$ di $(6,0)$. Syaratnya $PA^2 = 4\,PB^2$; kuadratkan supaya akarnya hilang.
- Ada jalan yang lebih cepat: pada garis $AB$ sendiri ada tepat dua titik yang memenuhi syaratnya, dan keduanya berseberangan pada lingkaran itu.

## Pembahasan

### Cara analitik

Taruh $A = (0,0)$ dan $B = (6,0)$. Untuk $P = (x, y)$, syaratnya $PA = 2\,PB$, jadi

$$PA^2 = 4\,PB^2$$

$$x^2 + y^2 = 4\left[(x-6)^2 + y^2\right]$$

Uraikan ruas kanannya:

$$x^2 + y^2 = 4x^2 - 48x + 144 + 4y^2$$

$$0 = 3x^2 - 48x + 144 + 3y^2$$

Bagi $3$:

$$x^2 - 16x + 48 + y^2 = 0$$

Lengkapkan kuadratnya:

$$(x - 8)^2 + y^2 = 64 - 48 = 16$$

Itu lingkaran berpusat $(8, 0)$ dengan jari-jari

$$\boxed{4}$$

### Cara kedua: lewat kedua titik pembagi

Cara ini lebih cepat, dan lebih layak dihafal.

Pada garis $AB$ ada tepat **dua** titik yang memenuhi $PA = 2\,PB$:

- **Pembagi dalam** $D$, yang membagi ruas $AB$ dengan $AD : DB = 2 : 1$. Karena
  $AB = 6$, diperoleh $AD = 4$, jadi $D = (4, 0)$.
- **Pembagi luar** $E$, yang ada di perpanjangan $AB$ melewati $B$, dengan
  $AE : EB = 2 : 1$. Dari $AE = 2\,EB$ dan $AE - EB = AB = 6$ diperoleh $EB = 6$ dan
  $AE = 12$, jadi $E = (12, 0)$.

Kedua titik itu adalah ujung-ujung **diameter** lingkarannya. Maka

$$\text{jari-jari} = \frac{DE}{2} = \frac{12 - 4}{2} = 4 \quad ✓$$

dan pusatnya di tengah $DE$, yaitu $(8, 0)$ ✓ — cocok dengan cara analitik.

Lingkaran ini disebut **lingkaran Apollonius** untuk pasangan $A$, $B$ dan nisbah $2$.

### Kenapa $D$ dan $E$ berseberangan

Bukan kebetulan. $D$ dan $E$ membagi $AB$ dengan nisbah yang sama, satu di dalam dan
satu di luar; pasangan seperti itu disebut **sekawan harmonik** terhadap $A$ dan $B$.

Untuk sembarang $P$ pada lingkarannya, $PD$ adalah garis bagi dalam $\angle APB$ dan
$PE$ garis bagi luarnya — sebab teorema garis bagi berbunyi bahwa garis bagi $\angle APB$
memotong $AB$ dengan nisbah $PA : PB$, dan di sini nisbah itu tetap $2$ untuk setiap $P$
pada lingkarannya. Garis bagi dalam dan luar suatu sudut selalu saling tegak lurus,
sehingga

$$\angle DPE = 90^\circ$$

Menurut teorema sudut keliling pada setengah lingkaran, tempat kedudukan titik yang
melihat $DE$ dengan sudut siku-siku adalah lingkaran berdiameter $DE$ — persis yang
keluar dari hitungan tadi.

### Periksa beberapa titik

Pusatnya $(8,0)$, jari-jari $4$. Ambil beberapa titik pada lingkaran itu:

| $P$ | $PA$ | $PB$ | $PA/PB$ |
|---|---|---|---|
| $(12, 0)$ | $12$ | $6$ | $2$ ✓ |
| $(4, 0)$ | $4$ | $2$ | $2$ ✓ |
| $(8, 4)$ | $\sqrt{64+16} = \sqrt{80}$ | $\sqrt{4+16} = \sqrt{20}$ | $\sqrt{4} = 2$ ✓ |
| $(8, -4)$ | $\sqrt{80}$ | $\sqrt{20}$ | $2$ ✓ |

### Yang sering terlewat

**Nisbahnya menentukan sisi mana yang dikelilingi.** Lingkarannya melingkupi $B$, titik
yang **lebih dekat**. Itu masuk akal: $PA/PB = 2$ berarti $P$ selalu lebih dekat ke $B$,
jadi $P$ tidak mungkin jauh dari $B$.

**Nisbah $1$ merosot.** Kalau $\dfrac{PA}{PB} = 1$, persamaannya menjadi
$x^2 + y^2 = (x-6)^2 + y^2$, yang memberi $x = 3$ — sebuah **garis**, bukan lingkaran.
Suku $x^2$ saling menghapus, dan tanpa suku kuadrat tidak ada lingkaran. Itulah sebabnya
soal selalu menyebut $k \ne 1$; kalau tidak menyebut, kasus $k = 1$ harus ditangani
sendiri.

**Menukar $A$ dan $B$ memberi lingkaran lain.** Nisbah $\tfrac{PA}{PB} = \tfrac12$
memberi lingkaran berpusat $(-2, 0)$ berjari-jari $4$, yang melingkupi $A$. Jadi urutan
penyebutan dalam soal bukan hiasan.
