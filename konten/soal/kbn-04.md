---
id: kbn-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [koefisien-binomial]
bentuk: isian
kesulitan: 3
jawaban: "35"
---

## Soal

Tentukan koefisien $x^{5}$ pada penjabaran

$$\left(x^{2} + \frac{1}{x}\right)^{7}$$

## Petunjuk

- Tuliskan bentuk umum sukunya, lalu kumpulkan seluruh pangkat $x$ menjadi satu.
- Bagian pertama menyumbang pangkat $2$ setiap kali terpilih; bagian kedua menyumbang $-1$.
- Susun persamaan untuk pangkatnya, lalu periksa penyelesaiannya bilangan bulat di antara $0$ dan $7$.

## Pembahasan

**Bentuk umum sukunya.**

$$\left(x^2 + \frac1x\right)^7 = \sum_{k=0}^{7} \binom{7}{k} \left(x^2\right)^{7-k}
\left(x^{-1}\right)^{k}$$

**Kumpulkan pangkatnya.**

$$\left(x^2\right)^{7-k} \cdot x^{-k} = x^{\,2(7-k)} \cdot x^{-k} = x^{\,14 - 2k - k} = x^{\,14-3k}$$

**Susun persamaannya.**

$$14 - 3k = 5 \quad\Longrightarrow\quad 3k = 9 \quad\Longrightarrow\quad k = 3$$

**Periksa penyelesaiannya sah.** Nilai $k = 3$ adalah bilangan bulat dan $0 \le 3 \le 7$,
jadi suku itu memang ada di dalam penjabaran.

**Hitung koefisiennya.**

$$\binom{7}{3} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = \boxed{35}$$

**Mengapa pangkatnya $14 - 3k$ dan bukan $14 - 2k$.** Tiap kali bagian kedua terpilih,
dua hal terjadi sekaligus: satu faktor $x^2$ **hilang** dan satu faktor $x^{-1}$
**bertambah**. Jadi tiap peningkatan $k$ menurunkan pangkatnya sebesar $2 + 1 = 3$, yaitu
selisih pangkat kedua bagian. Menyadari hal ini membuat pangkatnya bisa ditulis langsung
tanpa menjabarkan.

**Langkah pemeriksaan yang tidak boleh dilewati.** Kalau soalnya meminta koefisien $x^{4}$,
persamaannya menjadi

$$14 - 3k = 4 \quad\Longrightarrow\quad k = \frac{10}{3}$$

yang bukan bilangan bulat — artinya penjabaran ini **tidak punya** suku $x^4$ sama sekali,
dan jawabannya $0$. Begitu pula kalau $k$ yang keluar di luar rentang $0$ sampai $7$.

Menuliskan jawaban tanpa memeriksa hal ini adalah kekeliruan yang sering lolos dari
perhatian, sebab hitungannya sendiri terlihat rapi sampai akhir.

**Periksa nilai ekstremnya.** Pangkat terbesar terjadi di $k = 0$, yaitu $x^{14}$; pangkat
terkecil di $k = 7$, yaitu $x^{-7}$. Pangkat $5$ berada di antaranya, jadi wajar ia ada.
