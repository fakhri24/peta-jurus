---
id: cs-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: aljabar
tahap: osn
jurus: [cauchy-schwarz]
bentuk: isian
kesulitan: 3
jawaban: "4"
---

## Soal

Diketahui $a$ dan $b$ bilangan real positif dengan $a + b = 1$. Tentukan nilai terkecil
dari

$$\frac{1}{a} + \frac{1}{b}$$

## Petunjuk

- Yang dikunci soal jumlah $a+b$; yang ditanya jumlah pecahan berpenyebut $a$ dan $b$. Cari bentuk yang menghubungkan keduanya.
- Tulis tiap suku dengan pembilang kuadrat: $\frac1a = \frac{1^2}{a}$.
- Bentuk Engel: $\frac{p^2}{x} + \frac{q^2}{y} \ge \frac{(p+q)^2}{x+y}$ untuk $x, y > 0$.

## Pembahasan

**Siapkan bentuknya.** Tulis tiap suku dengan pembilang berupa kuadrat:

$$\frac{1}{a} + \frac{1}{b} = \frac{1^2}{a} + \frac{1^2}{b}$$

**Terapkan bentuk Engel** dari ketaksamaan Cauchy-Schwarz:

$$\frac{p^2}{x} + \frac{q^2}{y} \ \ge\ \frac{(p+q)^2}{x+y}, \qquad x, y > 0$$

Dengan $p = q = 1$, $x = a$, $y = b$:

$$\frac{1}{a} + \frac{1}{b} \ \ge\ \frac{(1+1)^2}{a+b} = \frac{4}{1} = 4$$

**Periksa kesamaannya tercapai.** Kesamaan pada bentuk Engel berlaku tepat ketika kedua
pecahan **sebanding**, yaitu $\frac{p}{x} = \frac{q}{y}$ — di sini $\frac1a = \frac1b$,
yaitu $a = b$. Digabung dengan $a+b=1$ diperoleh $a = b = \frac12$, keduanya positif.
Substitusikan: $2 + 2 = 4$. Tercapai.

Nilai terkecilnya adalah $\boxed{4}$.

**Mengapa bukan AM-GM.** Menerapkan AM-GM pada $\frac1a + \frac1b$ memberi
$\ge \frac{2}{\sqrt{ab}}$ — batas yang masih memuat $ab$, jadi belum menjawab. Ia baru
selesai setelah $ab \le \frac14$ dipakai, yaitu dua langkah. Bentuk Engel menutupnya dalam
satu langkah karena ia langsung memakai **jumlah** penyebut, dan jumlah itulah yang
dikunci soal.

**Ciri pengenalnya:** begitu kamu melihat jumlah pecahan yang penyebutnya dijumlahkan pula
oleh kendala soal, bentuk Engel adalah gerakan pertama. Kalau pembilangnya bukan kuadrat,
tulis ulang lebih dulu — misalnya $a = \frac{a^2}{a}$.
