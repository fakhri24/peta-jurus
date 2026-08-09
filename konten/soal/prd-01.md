---
id: prd-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [probabilitas-diskret]
bentuk: isian
kesulitan: 1
jawaban: "1/2"
jawaban_alt: ["3/6", "0,5", "0.5"]
---

## Soal

Sebuah dadu setimbang bermata $1$ sampai $6$ dilempar sekali.

Berapa peluang muncul mata dadu berupa **bilangan prima**? (Tulis sebagai pecahan paling
sederhana.)

## Petunjuk

- Daftar seluruh hasil yang mungkin, lalu tandai mana yang memenuhi syarat.
- Periksa dengan teliti mana di antara $1$ sampai $6$ yang bilangan prima. Perhatikan kedudukan angka $1$.
- Bagi banyaknya hasil yang diinginkan dengan banyaknya seluruh hasil.

## Pembahasan

**Ruang sampelnya** adalah $\{1,2,3,4,5,6\}$, dan keenam hasil sama mungkin karena dadunya
setimbang:

$$|S| = 6$$

**Daftar bilangan primanya.** Bilangan prima adalah bilangan asli lebih dari $1$ yang hanya
punya dua pembagi positif, yaitu $1$ dan dirinya sendiri.

| Mata | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|
| Prima? | tidak | ya | ya | tidak | ya | tidak |

Jadi $A = \{2, 3, 5\}$ dan $|A| = 3$.

**Hitung.**

$$P(A) = \frac{|A|}{|S|} = \frac{3}{6} = \boxed{\frac12}$$

**Angka $1$ bukan bilangan prima,** dan itu jebakan utama soal ini. Ia hanya punya satu
pembagi positif, yaitu dirinya sendiri — sedangkan prima menuntut tepat dua. Memasukkan $1$
memberi $\frac46 = \frac23$, yang salah.

Ketetapan itu bukan kesepakatan sembarangan. Kalau $1$ dianggap prima, faktorisasi prima
sebuah bilangan tidak lagi tunggal — $6 = 2\times3$ bisa ditulis juga $1\times2\times3$ dan
seterusnya tanpa henti.

**Angka $4$ dan $6$ juga bukan prima,** masing-masing habis dibagi $2$. Yang tersisa hanya
$2$, $3$, dan $5$ — dan $2$ adalah satu-satunya bilangan prima yang genap.

**Kebiasaan yang menolong pada soal peluang sederhana:** daftar seluruh ruang sampelnya
kalau memang cukup kecil, lalu tandai satu per satu. Untuk enam hasil, mendaftar jauh lebih
aman daripada mengandalkan ingatan.
