---
id: stb-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [segiempat-talibusur]
bentuk: isian
kesulitan: 3
jawaban: "36"
---

## Soal

Sebuah segiempat talibusur mempunyai panjang sisi $4$, $5$, $7$, dan $10$.

Tentukan luasnya.

## Petunjuk

- Yang diketahui cuma keempat sisinya — tidak ada sudut, tidak ada diagonal. Ada satu rumus luas yang memang dirancang untuk keadaan itu, dan hanya berlaku kalau bangunnya setalibusur.
- Pakai rumus Brahmagupta, dengan $s$ setengah keliling.
- $s = \dfrac{4+5+7+10}{2} = 13$.

## Pembahasan

**Hitung setengah kelilingnya.**

$$s = \frac{4 + 5 + 7 + 10}{2} = \frac{26}{2} = 13$$

**Pakai Brahmagupta.**

$$L = \sqrt{(s-a)(s-b)(s-c)(s-d)} = \sqrt{9 \times 8 \times 6 \times 3}$$

**Sederhanakan sebelum mengalikan.**

$$9 \times 8 \times 6 \times 3 = (9 \times 6) \times (8 \times 3) = 54 \times 24 = 1296$$

$$L = \sqrt{1296} = \boxed{36}$$

Atau lebih rapi lewat faktor prima: $9 \cdot 8 \cdot 6 \cdot 3 = 3^2 \cdot 2^3 \cdot (2 \cdot 3)
\cdot 3 = 2^4 \cdot 3^4$, sehingga $L = 2^2 \cdot 3^2 = 36$.

### Bandingkan dengan Heron

$$\text{Heron:} \quad L = \sqrt{s(s-a)(s-b)(s-c)}$$

$$\text{Brahmagupta:} \quad L = \sqrt{(s-a)(s-b)(s-c)(s-d)}$$

Kemiripannya bukan kebetulan. Kalau $d = 0$, maka $s$ menjadi setengah keliling segitiga dan
$s - d = s$, sehingga Brahmagupta **kembali menjadi Heron**. Segiempat yang salah satu sisinya
menyusut jadi nol memang segitiga.

Hubungan itu berguna dua arah: ia cara mengingat rumusnya tanpa tertukar, dan sekaligus
pemeriksaan yang bisa kamu jalankan sendiri kapan saja.

### Syarat yang mudah dilupakan

Brahmagupta **hanya berlaku untuk segiempat talibusur**. Untuk empat panjang sisi yang sama,
ada tak hingga banyak segiempat berbeda — bayangkan bangun bersendi yang bisa digoyang tanpa
mengubah panjang sisinya — dan luasnya berubah-ubah.

Di antara semuanya, yang **setalibusur adalah yang luasnya terbesar**. Karena itu memakai
Brahmagupta pada segiempat sembarang selalu memberi hasil yang **terlalu besar**, bukan
sekadar salah arah.

Kalau soal tidak menyebut segiempatnya setalibusur, rumus ini tidak boleh dipakai — dan
soalnya biasanya memang tidak punya jawaban tunggal.

### Periksa bangunnya ada

Untuk segiempat, syaratnya sisi terpanjang harus lebih pendek daripada jumlah ketiga sisi lain:

$$4 + 5 + 7 = 16 > 10 \quad ✓$$

Kalau syarat ini gagal, salah satu faktor $(s-a)$ menjadi negatif dan akarnya tidak nyata —
tanda yang sama dengan yang diberikan Heron untuk segitiga yang tidak ada.
