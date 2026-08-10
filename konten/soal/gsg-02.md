---
id: gsg-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [garis-singgung]
bentuk: isian
kesulitan: 2
jawaban: "132"
---

## Soal

Dari titik $P$ di luar lingkaran berpusat $O$ ditarik dua garis singgung, menyentuh lingkaran
di $A$ dan $B$. Diketahui $\angle APB = 48^\circ$.

![Lingkaran berpusat O dengan titik P di luarnya di sebelah kanan. Dari P ditarik dua garis singgung yang menyentuh lingkaran di A di atas dan B di bawah. Jari-jari OA dan OB digambar dan keduanya tegak lurus garis singgungnya. Ruas OP digambar putus-putus. Sudut APB besarnya 48 derajat dan sudut AOB ditanyakan](dua-singgung-titik-luar.svg)

Tentukan besar $\angle AOB$ dalam derajat.

## Petunjuk

- Keempat titik $O$, $A$, $P$, $B$ membentuk sebuah segiempat. Berapa jumlah sudut dalamnya, dan sudut mana saja yang sudah kamu ketahui?
- Jari-jari tegak lurus garis singgung, jadi sudut di $A$ dan di $B$ masing-masing $90^\circ$.
- Jumlah sudut segiempat $360^\circ$.

## Pembahasan

**Pandang segiempat $OAPB$.** Keempat titiknya membentuk segiempat, dan dua sudutnya sudah
diketahui secara gratis:

$$\angle OAP = 90^\circ, \qquad \angle OBP = 90^\circ$$

sebab jari-jari tegak lurus garis singgung di titik singgungnya.

**Pakai jumlah sudut segiempat.**

$$\angle AOB + \angle OAP + \angle APB + \angle PBO = 360^\circ$$

$$\angle AOB + 90^\circ + 48^\circ + 90^\circ = 360^\circ$$

$$\angle AOB = 360^\circ - 228^\circ = \boxed{132^\circ}$$

**Periksa.** $132^\circ + 48^\circ = 180^\circ$ — kedua sudut itu selalu berpelurus, sebab dua
sudut siku-sikunya sudah memakan $180^\circ$ dari jatah $360^\circ$.

### Bentuk yang layak diingat

$$\angle AOB + \angle APB = 180^\circ$$

Hubungan ini berlaku untuk **setiap** titik $P$ di luar lingkaran. Akibat langsungnya: keempat
titik $O$, $A$, $P$, $B$ terletak pada satu lingkaran — sudut berhadapannya berjumlah lurus —
yaitu lingkaran berdiameter $OP$. Masuk akal, sebab $A$ dan $B$ dua-duanya melihat $OP$ dengan
sudut siku-siku.

### Cara kedua: lewat separuhnya

Ruas $OP$ membagi gambar menjadi dua bagian yang kongruen, sebab $PA = PB$, $OA = OB$, dan $OP$
dipakai bersama. Jadi

$$\angle APO = \tfrac{1}{2} \times 48^\circ = 24^\circ$$

Pada $\triangle OAP$ yang siku-siku di $A$,

$$\angle AOP = 90^\circ - 24^\circ = 66^\circ$$

dan $\angle AOB = 2 \times 66^\circ = 132^\circ$ ✓.

Cara ini lebih panjang, tetapi ia memberi sesuatu yang tidak diberikan cara pertama: kenyataan
bahwa **$OP$ membagi dua sama besar** baik $\angle APB$ maupun $\angle AOB$. Soal lanjutan
sering memerlukan justru itu.

### Kalau sudutnya diperbesar

Semakin dekat $P$ ke lingkaran, semakin besar $\angle APB$ — mendekati $180^\circ$ saat $P$
menyentuh lingkaran. Sebaliknya, $P$ yang sangat jauh membuat $\angle APB$ mendekati $0^\circ$
dan $\angle AOB$ mendekati $180^\circ$, yakni $AB$ mendekati diameter.

Memeriksa kedua ujung seperti ini adalah cara murah memastikan rumus yang baru kamu susun tidak
terbalik arah.
