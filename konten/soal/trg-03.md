---
id: trg-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [trigonometri-segitiga]
bentuk: isian
kesulitan: 4
jawaban: "50"
---

## Soal

Diketahui segitiga $ABC$ dengan $\angle A = 30^\circ$, $BC = 5\sqrt{2}$, dan $AC = 10$.
Ternyata ada lebih dari satu segitiga yang memenuhi keterangan itu.

Tentukan hasil kali semua nilai yang mungkin bagi $AB$.

## Petunjuk

- Yang diketahui dua sisi dan sebuah sudut yang **tidak** diapit keduanya. Susunan itu yang menimbulkan lebih dari satu jawaban.
- Jangan cari kedua nilainya satu per satu. Tulis aturan kosinus dengan $AB$ sebagai yang belum diketahui, lalu perhatikan bentuk persamaannya.
- Persamaannya kuadrat dalam $AB$. Hasil kali akar-akarnya bisa dibaca langsung dari koefisiennya.

## Pembahasan

**Tulis aturan kosinus dengan sudut yang diketahui.** Sudut $A$ diapit oleh sisi $AB$ dan
$AC$, dan berhadapan dengan $BC$. Misalkan $AB = c$:

$$BC^2 = AB^2 + AC^2 - 2 \cdot AB \cdot AC \cos A$$

$$\left(5\sqrt2\right)^2 = c^2 + 10^2 - 2 \cdot c \cdot 10 \cdot \frac{\sqrt3}{2}$$

$$50 = c^2 + 100 - 10\sqrt3\, c$$

**Susun sebagai persamaan kuadrat.**

$$c^2 - 10\sqrt3\, c + 50 = 0$$

**Baca hasil kalinya dari koefisien.** Untuk $c^2 + pc + q = 0$, hasil kali akarnya $q$:

$$c_1 c_2 = \boxed{50}$$

Tidak perlu menghitung kedua akarnya sama sekali — dan di situlah letak jalan pintasnya.

### Periksa bahwa memang ada dua

Hasil kali akar tidak berarti apa-apa kalau akarnya tidak nyata dan tidak positif. Periksa
diskriminannya:

$$\Delta = \left(10\sqrt3\right)^2 - 4 \cdot 50 = 300 - 200 = 100 > 0$$

$$c = \frac{10\sqrt3 \pm 10}{2} = 5\sqrt3 \pm 5$$

Jadi $c_1 = 5\sqrt3 + 5 \approx 13{,}66$ dan $c_2 = 5\sqrt3 - 5 \approx 3{,}66$. Keduanya
positif, jadi keduanya sungguh-sungguh panjang sisi. Hasil kalinya

$$\left(5\sqrt3+5\right)\left(5\sqrt3-5\right) = 75 - 25 = 50 \quad ✓$$

### Dua segitiga itu benar-benar berbeda

Hitung sudut yang lain untuk masing-masing, dengan aturan sinus:

$$\sin B = \frac{AC \sin A}{BC} = \frac{10 \cdot \tfrac12}{5\sqrt2} = \frac{5}{5\sqrt2}
= \frac{1}{\sqrt2}$$

Nilai itu dipenuhi oleh $B = 45^\circ$ **dan** $B = 135^\circ$ — dan keduanya sah, karena
$30^\circ + 45^\circ$ maupun $30^\circ + 135^\circ$ masih di bawah $180^\circ$:

| | $\angle A$ | $\angle B$ | $\angle C$ | $AB$ |
|---|---|---|---|---|
| Segitiga 1 | $30^\circ$ | $45^\circ$ | $105^\circ$ | $5\sqrt3+5$ |
| Segitiga 2 | $30^\circ$ | $135^\circ$ | $15^\circ$ | $5\sqrt3-5$ |

Satu lancip di $B$, satu tumpul di $B$. Inilah **kasus mendua** pada aturan sinus, dan
persamaan kuadrat tadi adalah wajah aljabarnya: dua akar positif, dua segitiga.

### Kapan mendua, kapan tidak

Untuk keterangan berupa sisi $a$, sisi $b$, dan sudut $A$ di hadapan $a$:

- $a < b \sin A$ — tidak ada segitiga;
- $a = b \sin A$ — tepat satu, dan siku-siku;
- $b \sin A < a < b$ — **dua** segitiga;
- $a \ge b$ — tepat satu.

Di sini $b \sin A = 10 \cdot \tfrac12 = 5$, dan $5 < 5\sqrt2 \approx 7{,}07 < 10$ ✓ — persis
di selang yang memberi dua.

Daftar itu tidak perlu dihafal kalau kamu selalu lewat persamaan kuadratnya: banyaknya
segitiga sama dengan banyaknya **akar positif**, dan diskriminan beserta tanda koefisiennya
sudah menjawab keduanya.

### Kenapa hasil kali, bukan jumlah

Soal menanyakan hasil kali justru karena bentuk itu yang paling murni terbaca dari
persamaannya — ia suku tetapnya, $50$, sebuah bilangan bulat. Jumlahnya $10\sqrt3$, juga
terbaca langsung, tetapi memuat akar.

Kebiasaan yang berguna: begitu soal menyebut "semua nilai yang mungkin", periksa apakah
nilai-nilai itu akar dari satu persamaan yang sama. Kalau ya, jumlah dan hasil kalinya
tersedia tanpa perlu mencari akarnya satu-satu.
