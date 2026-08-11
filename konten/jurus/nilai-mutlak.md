---
id: nilai-mutlak
nama: Nilai Mutlak
pilar: aljabar
tahap: osn-k
prasyarat: [manipulasi-aljabar]
contoh: [nm-contoh-1]
latihan: [nm-01, nm-02, nm-03, nm-04, nm-05, nm-06]
---

## Kapan dipakai

Ada tanda **$|\cdot|$** dalam persamaan atau pertidaksamaan. Gerakan pertamanya selalu sama:
cari titik nol tiap bentuk di dalam tanda mutlak, lalu pecah garis bilangan di titik-titik
itu.

Pemicu kedua, dan ini yang mengubah soal panjang menjadi soal pendek: soal berbicara tentang
**jarak**. Pada garis bilangan $|x-a|$ adalah jarak $x$ ke $a$, jadi $|x-2| + |x+3|$
menanyakan jumlah jarak ke dua titik — dan membacanya begitu sering menjawabnya tanpa satu
kasus pun dipecah.

Pemicu ketiga: soal meminta **nilai terkecil dari jumlah beberapa nilai mutlak**. Jawabannya
selalu tercapai pada salah satu titik kritis, dan untuk jumlah jarak ke sederet titik ia
tercapai di titik tengahnya.

Pemicu keempat: soal memuat **nilai mutlak bersarang** atau nilai mutlak di kedua ruas.
Mengkuadratkan kedua ruas sah di sini justru karena keduanya tak negatif — salah satu dari
sedikit tempat pengkuadratan tidak memasukkan penyelesaian palsu.

Yang paling sering menggugurkan jawaban: setiap kasus punya **syarat berlakunya sendiri**,
dan penyelesaian yang jatuh di luar syarat kasusnya harus dibuang, bukan dikumpulkan.

## Intinya

Definisinya berupa dua kasus, dan hampir semua soal diselesaikan dengan memecah kasus itu:

$$|x| = \begin{cases} x & x \ge 0 \\ -x & x < 0 \end{cases}$$

Yang menentukan batas kasus adalah **titik nol tiap bentuk di dalam tanda mutlak**. Untuk
$|x-2| + |x+3|$, titik kritisnya $x = 2$ dan $x = -3$, sehingga garis bilangan terbagi
menjadi tiga daerah — periksa satu per satu.

Dua sifat yang memangkas banyak pekerjaan:

$$|x| = a \iff x = \pm a \quad (a \ge 0), \qquad |x| < a \iff -a < x < a$$

$$|x| > a \iff x < -a \text{ atau } x > a$$

Dan ketaksamaan segitiga:

$$|x + y| \le |x| + |y|$$

dengan kesamaan tepat ketika $x$ dan $y$ bertanda sama.

**Tafsiran jarak** sering menyelesaikan soal tanpa perhitungan sama sekali: $|x-2| + |x+3|$
adalah jumlah jarak $x$ ke $2$ dan ke $-3$, jadi nilai terkecilnya $5$ — dicapai di seluruh
ruas di antaranya.

## Jebakan umum

- **Mengira $\sqrt{x^2} = x$.** Yang benar $\sqrt{x^2} = |x|$.
- **Mengkuadratkan tanpa syarat.** Dari $|x-1| = x-3$, mengkuadratkan memberi solusi palsu;
  ruas kanan harus tak negatif lebih dulu.
- **Lupa memeriksa solusi terhadap daerah kasusnya.** Solusi yang lahir di kasus $x < 0$
  tetapi bernilai positif harus dibuang.
