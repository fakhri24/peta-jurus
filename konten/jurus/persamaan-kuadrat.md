---
id: persamaan-kuadrat
nama: Persamaan Kuadrat
pilar: aljabar
tahap: osn-k
prasyarat: [faktorisasi]
contoh: [pk-contoh-1]
latihan: [pk-01, pk-02, pk-03, pk-04, pk-05, pk-06]
---

## Kapan dipakai

Ada **$x^2$ sebagai pangkat tertinggi** — langsung, atau setelah substitusi yang mengubah
soalnya jadi berbentuk kuadrat. Bentuk $x^4 + bx^2 + c$ dan $2^{2t} - 5 \cdot 2^t + 6$
keduanya kuadrat yang menyamar.

Pemicu kedua, dan inilah yang paling sering muncul di olimpiade: soal menanyakan **syarat
agar akarnya** ada, berbeda, atau kembar — tanpa pernah menanyakan akarnya. Kalimat
"tentukan semua $m$ agar persamaan itu punya dua akar berbeda" adalah soal tentang
diskriminan, bukan tentang $x$.

Pemicu ketiga: soal meminta **nilai terbesar atau terkecil** sebuah bentuk kuadrat.
Melengkapkan kuadrat menjawabnya langsung, lengkap dengan titik tempat nilai itu tercapai.

Bedakan dari Rumus Vieta: kalau yang ditanya jumlah atau hasil kali kedua akarnya, akarnya
tidak perlu dihitung sama sekali.

## Intinya

Untuk $ax^2 + bx + c = 0$ dengan $a \ne 0$:

$$x = \frac{-b \pm \sqrt{D}}{2a}, \qquad D = b^2 - 4ac$$

**Diskriminan $D$ menjawab pertanyaan tentang akar tanpa menghitung akarnya:**

- $D > 0$: dua akar real berbeda
- $D = 0$: satu akar kembar
- $D < 0$: tidak ada akar real

Di olimpiade, $D$ jauh lebih sering dipakai untuk ini daripada untuk menghitung akar.
Soal "tentukan $m$ agar persamaan punya dua akar berbeda" adalah soal tentang $D$, bukan
tentang $x$.

**Melengkapkan kuadrat** sering lebih berguna daripada rumus akar:

$$ax^2+bx+c = a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$$

Dari bentuk itu, nilai ekstremnya terbaca langsung: untuk $a > 0$ nilai minimumnya
$c - \frac{b^2}{4a}$ di $x = -\frac{b}{2a}$.

**Substitusi** memperluas jangkauannya. Persamaan $x^4 - 5x^2 + 4 = 0$ menjadi kuadrat
dengan $u = x^2$; $2^{2x} - 3 \cdot 2^x + 2 = 0$ menjadi kuadrat dengan $u = 2^x$.

## Jebakan umum

- **Lupa syarat $a \ne 0$.** Kalau $a$ memuat parameter, kasus $a = 0$ harus diperiksa
  terpisah — di situ persamaannya linear, bukan kuadrat.
- **Lupa mengembalikan substitusi.** Menemukan $u = 4$ belum menjawab apa pun sampai
  $x^2 = 4$ diselesaikan.
- **Membuang akar negatif pada substitusi yang menuntut positif.** Untuk $u = 2^x$, nilai
  $u \le 0$ harus dibuang karena $2^x$ selalu positif.
