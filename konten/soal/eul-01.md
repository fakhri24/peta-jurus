---
id: eul-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [garis-euler]
bentuk: isian
kesulitan: 3
jawaban: "3"
---

## Soal

Pada segitiga $ABC$, titik $O$ adalah pusat lingkaran luar, $H$ titik tinggi, $G$ titik
berat, dan $N$ pusat lingkaran sembilan titik. Diketahui $OH = 18$.

Tentukan panjang $GN$.

## Petunjuk

- Keempat titik itu terletak pada satu garis. Tentukan letak masing-masing sebagai bagian dari $OH$, diukur dari $O$.
- $G$ membagi $OH$ dengan $HG : GO = 2 : 1$, jadi $OG = \tfrac13 OH$.
- $N$ adalah titik tengah $OH$, jadi $ON = \tfrac12 OH$. Yang ditanya selisihnya.

## Pembahasan

**Taruh keempatnya pada satu garis bilangan.** Semuanya di garis Euler, jadi cukup catat
jaraknya dari $O$:

$$O \text{ di } 0, \qquad H \text{ di } 18$$

**Letak $G$.** Perbandingan $HG : GO = 2 : 1$ membagi $OH$ menjadi tiga bagian, dengan $G$
satu bagian dari $O$:

$$OG = \tfrac13 \times 18 = 6$$

**Letak $N$.** Pusat lingkaran sembilan titik adalah **titik tengah $OH$**:

$$ON = \tfrac12 \times 18 = 9$$

**Selisihnya.**

$$GN = ON - OG = 9 - 6 = \boxed{3}$$

### Urutan keempat titiknya

$$O \ (0) \ \longrightarrow \ G \ (6) \ \longrightarrow \ N \ (9) \ \longrightarrow \ H \ (18)$$

Urutan itu **selalu** sama pada segitiga apa pun yang bukan sama sisi, dan nisbah jaraknya
tetap:

$$OG : GN : NH = 6 : 3 : 9 = 2 : 1 : 3$$

Angka $2 : 1 : 3$ itu layak diingat sebagai satu paket — ia menjawab semua pertanyaan tentang
jarak antar keempat titik ini sekaligus. Misalnya $GH = 12$, $NH = 9$, dan $GN = 3$ semuanya
terbaca langsung dari sana.

### Jebakan: mengira $N$ titik tengah $OG$

Kekeliruan yang paling sering, dan disebut khusus di daftar jebakan jurus ini. Titik $N$
adalah titik tengah $\boldsymbol{OH}$, bukan $OG$.

Yang licik: pada pertanyaan **ini** kekeliruan itu tidak ketahuan. Kalau $N$ dianggap titik
tengah $OG$, maka $ON = 3$ dan $GN = 6 - 3 = 3$ — jawaban yang sama. Bukan kebetulan
melainkan aljabar: yang benar memberi $\tfrac{OH}{2} - \tfrac{OH}{3} = \tfrac{OH}{6}$, yang
keliru memberi $\tfrac{OH}{3} - \tfrac{OH}{6} = \tfrac{OH}{6}$ juga.

Yang membedakan keduanya **letak**, bukan jarak:

| | $ON$ | $NH$ | $N$ berada di antara |
|---|---|---|---|
| Benar | $9$ | $9$ | $G$ dan $H$ |
| Keliru | $3$ | $15$ | $O$ dan $G$ |

Jadi jangan memakai soal ini untuk memastikan pemahamanmu benar. Ujilah dengan menanyakan
$ON$ atau $NH$: di situ kekeliruannya langsung terlihat. Pemeriksaan cepatnya, $N$ harus
berada di antara $G$ dan $H$ — dan karena $9 > 6$ ✓ letaknya benar.

### Kenapa $N$ tepat di tengah

Alasannya homoteti berpusat $H$ dengan faktor $\tfrac12$: ia memetakan lingkaran luar ke
lingkaran sembilan titik. Pusat terpetakan ke pusat, jadi

$$N = h_{H,\,1/2}(O) = \text{titik tengah } OH$$

dan jari-jarinya menjadi $\tfrac{R}{2}$. Kedua kenyataan itu — letak $N$ dan besar
jari-jarinya — datang dari satu homoteti yang sama, jadi tidak perlu dihafal terpisah.

### Kalau $OH = 0$

Untuk segitiga sama sisi, $O = G = H = N$ menyatu di satu titik dan **garis Eulernya tidak
ada**. Rumus di atas tetap memberi $GN = 0$, yang benar sebagai jarak tetapi menyesatkan
sebagai gambaran: tidak ada garis yang bisa ditunjuk.

Soal yang memberi segitiga sama sisi lalu bertanya tentang garis Euler sedang meminta hal
lain — biasanya justru menunjukkan bahwa garisnya tidak terdefinisi.
