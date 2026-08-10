---
id: gan-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-analitik]
bentuk: isian
kesulitan: 2
jawaban: "10"
---

## Soal

Diketahui titik $A(2, -1)$ dan $B(6, 7)$. Sumbu ruas $AB$ — yaitu garis yang tegak lurus $AB$
dan melalui titik tengahnya — memotong sumbu $x$ di suatu titik.

Tentukan absis titik potong itu.

## Petunjuk

- Untuk menuliskan persamaan sebuah garis, kamu butuh dua hal: satu titik yang dilaluinya, dan gradiennya.
- Titik yang dilaluinya adalah titik tengah $AB$; gradiennya diperoleh dari syarat tegak lurus.
- Setelah persamaannya ada, substitusikan $y = 0$.

## Pembahasan

**Titik tengah $AB$.**

$$M = \left(\frac{2+6}{2}, \frac{-1+7}{2}\right) = (4, 3)$$

**Gradien $AB$, lalu gradien tegak lurusnya.**

$$m_{AB} = \frac{7 - (-1)}{6 - 2} = \frac{8}{4} = 2$$

Dua garis tegak lurus kalau hasil kali gradiennya $-1$, sehingga

$$m = -\frac{1}{2}$$

**Tulis persamaan sumbunya.**

$$y - 3 = -\tfrac{1}{2}(x - 4) \quad \Longrightarrow \quad y = -\tfrac{1}{2}x + 5$$

**Potong sumbu $x$**, yaitu $y = 0$:

$$0 = -\tfrac{1}{2}x + 5 \quad \Longrightarrow \quad x = \boxed{10}$$

### Periksa dengan sifat yang mendefinisikannya

Setiap titik pada sumbu ruas $AB$ berjarak sama ke $A$ dan ke $B$. Uji pada $(10, 0)$:

$$\text{ke } A: \sqrt{(10-2)^2 + (0+1)^2} = \sqrt{64 + 1} = \sqrt{65}$$

$$\text{ke } B: \sqrt{(10-6)^2 + (0-7)^2} = \sqrt{16 + 49} = \sqrt{65}$$

Sama ✓. Pemeriksaan ini memakai definisi sumbu ruas, bukan langkah-langkah yang tadi dipakai
— jadi ia benar-benar menguji.

### Cara kedua: langsung dari sifat jarak

Titik $(x, 0)$ berjarak sama ke $A$ dan $B$ berarti

$$(x-2)^2 + 1 = (x-6)^2 + 49$$

$$x^2 - 4x + 5 = x^2 - 12x + 85$$

$$8x = 80 \quad \Longrightarrow \quad x = 10$$

Perhatikan bahwa $x^2$ hilang di kedua ruas — pola yang sama dengan yang muncul saat mencari
kaki garis tinggi lewat dua kali Pythagoras. Setiap kali dua jarak disamakan, suku kuadratnya
saling meniadakan dan yang tersisa persamaan linear.

Cara ini sering lebih pendek, dan sekaligus menghindari satu jebakan: ia tidak memakai gradien
sama sekali.

### Kapan syarat tegak lurus tidak bisa dipakai

Syarat $m_1 m_2 = -1$ **gagal** ketika salah satu garisnya tegak, sebab garis tegak tidak punya
gradien. Kalau $A$ dan $B$ punya ordinat yang sama, ruas $AB$ mendatar dan sumbunya tegak —
persamaannya $x = \dfrac{x_1+x_2}{2}$, dan tidak ada gradien yang perlu dihitung.

Periksa kasus itu sebelum memakai gradien, terutama pada soal yang koordinatnya berupa huruf.
