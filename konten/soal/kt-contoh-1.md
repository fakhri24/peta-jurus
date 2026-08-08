---
id: kt-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [ketaksamaan-dasar]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Tentukan nilai terkecil dari

$$x^2 - 4x + 7$$

untuk $x$ bilangan real.

## Petunjuk

- Ada satu fakta yang menjadi dasar hampir semua soal nilai ekstrem: kuadrat bilangan real tidak pernah negatif.
- Susun ulang bentuknya sehingga peubahnya hanya muncul di dalam satu kuadrat.
- Setelah menjadi $(x-2)^2 + k$, nilai terkecilnya terbaca langsung — dan jangan lupa memeriksa bahwa nilai itu tercapai.

## Pembahasan

Lengkapkan kuadratnya. Separuh koefisien $x$ adalah $-2$, dan kuadratnya $4$:

$$x^2 - 4x + 7 = \left(x^2 - 4x + 4\right) + 3 = (x-2)^2 + 3$$

Sekarang pakai fakta dasarnya: **kuadrat bilangan real tidak pernah negatif.**

$$(x-2)^2 \ \ge\ 0 \quad\Longrightarrow\quad (x-2)^2 + 3 \ \ge\ 3$$

Jadi nilainya tidak pernah kurang dari $3$.

**Periksa bahwa $3$ tercapai.** Kesamaan berlaku tepat ketika $(x-2)^2 = 0$, yaitu
$x = 2$ — bilangan real yang sah. Substitusikan: $4 - 8 + 7 = 3$. Cocok.

Nilai terkecilnya adalah $\boxed{3}$.

**Langkah terakhir itu bagian dari jawaban, bukan pelengkap.** Menunjukkan sebuah bentuk
selalu $\ge 3$ baru membuktikan $3$ adalah batas bawah. Ia menjadi **nilai minimum** hanya
setelah ditunjukkan ada $x$ yang mencapainya.

Bedanya nyata. Bentuk $x^2 + \frac{1}{x^2+1}$ misalnya selalu lebih dari $0$, tetapi $0$
bukan nilai minimumnya — ia tidak pernah tercapai.

Pola kerja jurus ini selalu sama: **pindahkan semuanya ke satu ruas, tunjukkan sisanya
jumlah kuadrat, lalu cari kapan kuadratnya nol.**
