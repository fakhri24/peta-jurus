---
id: smp-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [sarang-merpati]
bentuk: isian
kesulitan: 4
jawaban: "51"
---

## Soal

Beberapa bilangan dipilih dari $\{1, 2, 3, \dots, 100\}$.

Paling sedikit berapa bilangan harus dipilih supaya **pasti** ada dua di antaranya yang
salah satunya membagi yang lain?

## Petunjuk

- Cari dulu kelompok bilangan sebesar mungkin yang tidak satu pun membagi yang lain. Bagian atas himpunan itu tempat yang baik untuk dicoba.
- Setiap bilangan asli dapat ditulis sebagai bilangan ganjil dikali suatu pangkat dua. Bilangan ganjil itu yang menjadi sarangnya.
- Kalau dua bilangan punya bagian ganjil yang sama, keduanya berbentuk $g \cdot 2^{a}$ dan $g \cdot 2^{b}$ — dan di situ yang berpangkat kecil pasti membagi yang besar.

## Pembahasan

Soal ini punya dua bagian yang sama pentingnya: menunjukkan $50$ **belum** cukup, dan
menunjukkan $51$ **sudah** pasti.

### Bagian 1 — dengan $50$ bilangan masih bisa lolos

Ambil

$$\{51, 52, 53, \dots, 100\}$$

yang berisi tepat $50$ bilangan. Kalau $a$ dan $b$ keduanya di dalamnya dengan $a < b$,
maka

$$\frac{b}{a} \le \frac{100}{51} < 2$$

Karena hasil bagi dua bilangan asli yang berbeda dengan $a \mid b$ paling sedikit $2$,
mustahil $a$ membagi $b$. Jadi tidak satu pun membagi yang lain, dan $50$ belum menjamin
apa-apa.

### Bagian 2 — dengan $51$ bilangan pasti terjadi

**Susun sarangnya lewat bagian ganjil.** Setiap bilangan asli $n$ dapat ditulis secara
tunggal sebagai

$$n = g \cdot 2^{a}$$

dengan $g$ ganjil dan $a \ge 0$. Sebut $g$ sebagai **bagian ganjil** dari $n$.

Bilangan ganjil di antara $1$ dan $100$ ada

$$1, 3, 5, \dots, 99 \quad\Longrightarrow\quad 50 \text{ buah}$$

Inilah sarangnya: $k = 50$.

**Terapkan prinsipnya.** Kalau dipilih $51$ bilangan, dua di antaranya pasti punya bagian
ganjil yang sama. Sebut keduanya

$$x = g \cdot 2^{a}, \qquad y = g \cdot 2^{b}, \qquad a < b$$

Maka

$$\frac{y}{x} = 2^{\,b-a}$$

yang merupakan bilangan bulat. Jadi $x \mid y$.

$$\boxed{51}$$

**Mengapa bagian ganjil yang dipilih sebagai sarang.** Syarat yang diminta adalah
keterbagian, dan keterbagian oleh $2$ adalah satu-satunya sumber keterbagian yang bisa
dijamin muncul di sini. Menyingkirkan seluruh faktor $2$ dari sebuah bilangan menyisakan
tepat satu penanda, dan dua bilangan dengan penanda sama otomatis berhubungan lewat pangkat
dua.

**Perhatikan kedua bagian bertemu di angka yang sama.** Bagian 1 menemukan kelompok bebas
berukuran $50$; bagian 2 menunjukkan tidak ada yang berukuran $51$. Kalau kedua angka itu
tidak bertemu, salah satu bagiannya belum optimal — dan itu tanda pekerjaannya belum
selesai.
