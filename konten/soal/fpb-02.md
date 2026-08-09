---
id: fpb-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [fungsi-pembangkit]
bentuk: isian
kesulitan: 3
jawaban: "21"
---

## Soal

Ada berapa penyelesaian bilangan bulat dari

$$x_1 + x_2 + x_3 = 10$$

yang memenuhi $0 \le x_i \le 5$ untuk setiap $i$?

## Petunjuk

- Tiap peubah punya batas atas, jadi deretnya terpotong. Tuliskan faktor untuk satu peubah lebih dulu.
- Faktor untuk peubah yang bernilai $0$ sampai $5$ adalah $1 + x + x^2 + \cdots + x^5$.
- Jawabannya adalah koefisien $x^{10}$ pada hasil kali ketiga faktor itu.

## Pembahasan

**Susun fungsi pembangkitnya.** Tiap peubah boleh bernilai $0$ sampai $5$, sehingga faktornya

$$1 + x + x^2 + x^3 + x^4 + x^5 = \frac{1-x^{6}}{1-x}$$

Ada tiga peubah, sehingga

$$F(x) = \left(\frac{1-x^{6}}{1-x}\right)^{3} = \left(1-x^{6}\right)^{3} \cdot \frac{1}{(1-x)^{3}}$$

**Jabarkan tiap bagian.**

$$\left(1-x^6\right)^3 = 1 - 3x^6 + 3x^{12} - x^{18}$$

$$\frac{1}{(1-x)^3} = \sum_{n\ge0}\binom{n+2}{2}x^{n}$$

**Ambil koefisien $x^{10}$.** Hanya dua suku dari faktor pertama yang bisa menyumbang, sebab
pangkat $12$ dan $18$ sudah melewati $10$:

$$\left[x^{10}\right]F = 1 \cdot \binom{12}{2} - 3 \cdot \binom{6}{2}$$

$$= 66 - 3 \times 15 = 66 - 45 = \boxed{21}$$

**Bandingkan dengan inklusi–eksklusi langsung.** Tanpa batas atas ada $\binom{12}{2} = 66$
penyelesaian; yang melanggar pada satu peubah tertentu digeser menjadi jumlah $10-6 = 4$,
memberi $\binom62 = 15$ untuk tiap peubah, sehingga $3 \times 15 = 45$. Dua pelanggaran
sekaligus menuntut jumlah paling sedikit $12 > 10$, jadi mustahil.

$$66 - 45 = 21$$

**Hasilnya sama, dan itu bukan kebetulan.** Faktor $\left(1-x^6\right)^3$ ketika dijabarkan
menghasilkan tanda berselang-seling $1, -3, +3, -1$ — persis suku-suku inklusi–eksklusi,
lengkap dengan koefisien $\binom3k$-nya. Fungsi pembangkit menuliskan inklusi–eksklusi
sebagai aljabar, sehingga tidak ada lagi yang perlu diingat tentang kapan menambah dan kapan
mengurangi.

**Di situlah keunggulannya terasa.** Kalau batas atas tiap peubah berbeda-beda — misalnya
$x_1 \le 3$, $x_2 \le 5$, $x_3 \le 7$ — inklusi–eksklusi harus dikerjakan dengan hati-hati
per kasus, sedangkan fungsi pembangkitnya tinggal

$$\left(1-x^{4}\right)\left(1-x^{6}\right)\left(1-x^{8}\right) \cdot \frac{1}{(1-x)^3}$$

dan tandanya keluar sendiri dari penjabarannya.
