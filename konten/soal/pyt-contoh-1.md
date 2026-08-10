---
id: pyt-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [pythagoras]
bentuk: isian
kesulitan: 2
jawaban: "12"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 13$, $BC = 14$, dan $AC = 15$. Dari $A$ ditarik garis
tinggi yang memotong $BC$ tegak lurus di titik $D$.

![Segitiga ABC dengan alas BC mendatar sepanjang 14, sisi AB sepanjang 13, dan sisi AC sepanjang 15. Dari puncak A ditarik garis tinggi yang memotong alas tegak lurus di titik D, yang terletak di antara B dan C tetapi bukan di titik tengahnya](segitiga-garis-tinggi.svg)

Tentukan panjang $AD$.

## Petunjuk

- Segitiganya bukan siku-siku, tetapi garis tinggi itu memotong gambar menjadi dua bagian yang masing-masing punya sudut siku-siku.
- Namai $BD = x$, sehingga $DC = 14 - x$. Sekarang $AD$ bisa dihitung dari dua sisi berbeda.
- Tuliskan $AD^2$ dua kali — lewat $\triangle ABD$ dan lewat $\triangle ACD$ — lalu samakan keduanya.

## Pembahasan

**Kenali pemicunya.** Segitiga $ABC$ tidak siku-siku, jadi Pythagoras belum bisa dipakai
langsung. Tetapi garis tinggi $AD$ **membuat** sudut siku-siku: ia memotong segitiga menjadi
$\triangle ABD$ dan $\triangle ACD$, keduanya siku-siku di $D$.

Ini pemicu Pythagoras yang paling sering muncul di olimpiade — bukan segitiga siku-siku yang
sudah tersedia, melainkan segitiga sembarang yang dipotong garis tinggi.

**Beri nama pada yang belum diketahui.** Letak $D$ tidak diberikan, jadi namai

$$BD = x \qquad \Longrightarrow \qquad DC = 14 - x$$

**Hitung $AD^2$ dua kali.** Dari $\triangle ABD$ yang siku-siku di $D$:

$$AD^2 = AB^2 - BD^2 = 13^2 - x^2 = 169 - x^2$$

Dari $\triangle ACD$ yang juga siku-siku di $D$:

$$AD^2 = AC^2 - DC^2 = 15^2 - (14-x)^2 = 225 - (196 - 28x + x^2) = 29 + 28x - x^2$$

**Samakan keduanya.** Ruas $AD$ hanya satu, jadi kedua nilai itu harus sama:

$$169 - x^2 = 29 + 28x - x^2$$

Suku $x^2$ hilang di kedua ruas — dan itu bukan kebetulan, melainkan yang membuat cara ini
selalu bekerja:

$$169 = 29 + 28x \quad \Longrightarrow \quad 28x = 140 \quad \Longrightarrow \quad x = 5$$

**Kembali ke yang ditanyakan.**

$$AD^2 = 169 - 5^2 = 169 - 25 = 144 \quad \Longrightarrow \quad AD = \boxed{12}$$

### Mengapa $x^2$ selalu hilang

Kedua persamaan menghitung besaran yang sama, $AD^2$, lewat dua segitiga yang berbagi kaki
$AD$. Suku $x^2$ muncul di keduanya dengan tanda yang sama, jadi ia lenyap saat disamakan.
Akibatnya persamaan yang tersisa **linear**, betapapun rumit angkanya.

Jadi langkah ini tidak pernah melahirkan persamaan kuadrat, dan itu alasan kuat untuk
memakainya alih-alih menebak letak $D$.

### Periksa hasilnya dari arah lain

Dengan $x = 5$ diperoleh $BD = 5$, $DC = 9$, dan $AD = 12$. Periksa:

- $\triangle ABD$: $5^2 + 12^2 = 25 + 144 = 169 = 13^2$ ✓ — tripel $(5, 12, 13)$.
- $\triangle ACD$: $9^2 + 12^2 = 81 + 144 = 225 = 15^2$ ✓ — tripel $(9, 12, 15)$, kelipatan
  tiga dari $(3,4,5)$.

Luas segitiganya $\tfrac{1}{2} \times 14 \times 12 = 84$. Dengan Heron, setengah kelilingnya
$s = 21$ dan

$$\sqrt{21 \times 8 \times 7 \times 6} = \sqrt{7056} = 84$$

Dua jalan berbeda memberi angka yang sama — pemeriksaan yang jauh lebih meyakinkan daripada
mengulang perhitungan yang sama dua kali.

### Kalau $D$ jatuh di luar

Andaikan $AC$ diganti menjadi $20$. Menjalankan langkah yang sama memberi

$$169 - x^2 = 400 - (14-x)^2 \quad \Longrightarrow \quad 169 = 204 + 28x
\quad \Longrightarrow \quad x = -\tfrac{5}{4}$$

Tanda negatif itu **bukan kekeliruan**: ia memberitahu bahwa kaki garis tingginya jatuh di
perpanjangan $CB$ melewati $B$, bukan di antara $B$ dan $C$. Segitiganya tumpul di $B$.
Biasakan membaca tanda negatif sebagai keterangan tentang gambar, bukan sebagai isyarat untuk
mengulang hitungan.
