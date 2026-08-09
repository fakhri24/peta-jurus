---
id: fpb-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [fungsi-pembangkit]
bentuk: isian
kesulitan: 4
jawaban: "25"
---

## Soal

Tiga dadu setimbang bermata $1$ sampai $6$ dilempar bersamaan.

Ada berapa cara ketiga mata dadu itu berjumlah $12$? (Ketiga dadu dianggap dapat dibedakan.)

## Petunjuk

- Tiap dadu menyumbang satu faktor. Perhatikan mata dadu dimulai dari $1$, bukan $0$ — jadi faktornya tidak memuat suku tetap.
- Faktor untuk satu dadu adalah $x + x^2 + \cdots + x^6$, dan ia dapat ditulis sebagai $x\left(1+x+\cdots+x^5\right)$.
- Mengeluarkan faktor $x$ dari tiap dadu menggeser pangkat yang dicari, dan sisanya menjadi soal yang sudah kamu kenal.

## Pembahasan

**Susun fungsi pembangkitnya.** Satu dadu memberi

$$x + x^2 + x^3 + x^4 + x^5 + x^6 = x\left(1 + x + \cdots + x^5\right) = x \cdot \frac{1-x^6}{1-x}$$

Tiga dadu memberi

$$F(x) = x^{3} \left(\frac{1-x^{6}}{1-x}\right)^{3}$$

**Geser pangkatnya.** Faktor $x^3$ di depan berarti

$$\left[x^{12}\right]F(x) = \left[x^{9}\right]\left(\frac{1-x^{6}}{1-x}\right)^{3}$$

Pergeseran ini adalah terjemahan aljabar dari langkah "sisihkan dulu satu untuk tiap dadu":
mata dadu $1$ sampai $6$ berubah menjadi $0$ sampai $5$, dan jumlah $12$ berubah menjadi $9$.

**Jabarkan.**

$$\left(1-x^6\right)^3 = 1 - 3x^{6} + 3x^{12} - x^{18}, \qquad
\frac{1}{(1-x)^3} = \sum_{n\ge0}\binom{n+2}{2}x^{n}$$

Ambil koefisien $x^9$. Hanya dua suku pertama yang bisa menyumbang, sebab $x^{12}$ dan
$x^{18}$ sudah melewati $x^9$:

$$\left[x^{9}\right] = 1 \cdot \binom{11}{2} - 3 \cdot \binom{5}{2}$$

$$= 55 - 3 \times 10 = 55 - 30 = \boxed{25}$$

**Periksa dengan simetri.** Jumlah tiga dadu berjalan dari $3$ sampai $18$, dan sebarannya
simetris terhadap $10{,}5$ — sebab mengganti tiap mata $m$ dengan $7-m$ memetakan jumlah $s$
menjadi $21-s$. Karena itu banyaknya cara berjumlah $12$ sama dengan berjumlah
$21-12 = 9$.

Sebaran lengkapnya untuk jumlah $3$ sampai $18$:

$$1,\ 3,\ 6,\ 10,\ 15,\ 21,\ 25,\ 27,\ 27,\ 25,\ 21,\ 15,\ 10,\ 6,\ 3,\ 1$$

Jumlah seluruhnya $216 = 6^3$, sesuai. Nilai untuk jumlah $12$ memang $25$, dan sama dengan
nilai untuk jumlah $9$.

**Mengapa mengeluarkan faktor $x$ itu penting.** Tanpa langkah itu, deret $x + \cdots + x^6$
harus ditangani apa adanya dan bentuk bakunya tidak langsung terlihat. Mengeluarkan pangkat
terkecil mengubahnya menjadi deret yang dimulai dari $1$ — bentuk yang koefisiennya sudah
dikenal.

Kebiasaan itu berlaku umum: **selalu keluarkan pangkat terkecil dari tiap faktor lebih
dulu**, lalu kerjakan sisanya dengan bentuk baku.
