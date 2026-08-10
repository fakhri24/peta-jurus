---
id: cvm-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ceva-menelaus, garis-istimewa]
bentuk: isian
kesulitan: 4
jawaban: "3/2"
jawaban_alt: ["1,5", "1.5"]
---

## Soal

Pada segitiga $ABC$, titik $M$ adalah titik tengah sisi $BC$. Titik $P$ terletak pada ruas
$AM$ dengan $AP : PM = 3 : 1$. Garis $BP$ diperpanjang sampai memotong sisi $AC$ di titik $Q$.

Tentukan nilai $\dfrac{AQ}{QC}$.

## Petunjuk

- Kata "titik tengah" adalah garis berat yang belum disebut namanya, dan ia memberi satu perbandingan gratis: $BM : MC = 1 : 1$.
- Cari segitiga yang memuat ruas $AM$ sebagai sisi dan dilintasi garis $B$–$P$–$Q$.
- Pakai Menelaus pada $\triangle AMC$: garisnya memotong $AM$ di $P$, memotong $CA$ di $Q$, dan memotong perpanjangan $MC$ di $B$.

## Pembahasan

**Pilih segitiganya.** Yang diketahui perbandingan pada $AM$, yang ditanyakan perbandingan
pada $AC$. Segitiga yang memuat keduanya sebagai sisi adalah $\triangle AMC$.

**Kenali garis lintangnya.** Titik $B$, $P$, $Q$ segaris. Terhadap $\triangle AMC$, garis itu
memotong sisi $AM$ di $P$, sisi $CA$ di $Q$, dan perpanjangan sisi $MC$ di $B$.

**Tulis Menelaus berkeliling $A \to M \to C \to A$.**

$$\frac{AP}{PM} \cdot \frac{MB}{BC} \cdot \frac{CQ}{QA} = 1$$

**Isi angkanya.** Karena $M$ titik tengah $BC$, berlaku $MB = \tfrac12 BC$, sehingga

$$\frac{MB}{BC} = \frac12$$

Perhatikan sekali lagi bahwa yang dipakai $\dfrac{MB}{BC}$, bukan $\dfrac{BM}{MC} = 1$ —
sisi yang dipotong adalah $MC$, dan titik potongnya $B$ yang berada di luarnya.

$$\frac{3}{1} \cdot \frac{1}{2} \cdot \frac{CQ}{QA} = 1 \quad \Longrightarrow \quad
\frac{CQ}{QA} = \frac{2}{3}$$

$$\frac{AQ}{QC} = \boxed{\frac32}$$

### Periksa lewat koordinat

Ambil $B(0,0)$, $C(4,0)$, $A(0,4)$. Maka $M(2,0)$, dan

$$P = A + \tfrac34\left(M - A\right) = \left(\tfrac32,\ 1\right)$$

Garis $BP$: dari $(0,0)$ ke $\left(\tfrac32, 1\right)$, yaitu $y = \tfrac23 x$.
Garis $AC$: dari $(0,4)$ ke $(4,0)$, yaitu $y = 4 - x$.

Samakan: $\tfrac23 x = 4 - x \Rightarrow \tfrac53 x = 4 \Rightarrow x = \tfrac{12}{5}$, jadi
$Q = \left(2{,}4,\ 1{,}6\right)$.

Karena $A$, $Q$, $C$ segaris, perbandingannya terbaca dari absisnya:

$$\frac{AQ}{QC} = \frac{2{,}4 - 0}{4 - 2{,}4} = \frac{2{,}4}{1{,}6} = \frac32 \quad ✓$$

### Kalau $P$ kebetulan titik berat

Menarik dibandingkan: kalau $AP : PM = 2 : 1$, maka $P$ adalah titik berat segitiga, dan
Menelaus memberi

$$2 \cdot \frac12 \cdot \frac{CQ}{QA} = 1 \quad \Longrightarrow \quad \frac{CQ}{QA} = 1$$

Jadi $Q$ menjadi titik tengah $AC$ — persis sesuai yang sudah diketahui tentang titik berat:
garis dari $B$ lewat titik berat adalah garis berat, dan ia berakhir di titik tengah sisi
seberangnya.

Kecocokan itu pemeriksaan yang bagus untuk rumus yang baru disusun: masukkan kasus yang
jawabannya sudah kamu ketahui, dan lihat apakah keluar benar. Di sini keluar benar, jadi
susunan Menelausnya bisa dipercaya.

### Kenapa bukan Ceva

Godaannya besar: ada segitiga, ada titik di dalam, ada ruas dari titik sudut. Tetapi Ceva
memerlukan **tiga** ruas yang konkuren, dan di sini hanya ada dua — $AM$ dan $BQ$.

Ruas ketiganya bisa saja ditambahkan sendiri (tarik $CP$ sampai memotong $AB$), dan Ceva lalu
berlaku. Tetapi itu menambah satu titik yang tidak diketahui apa-apa, jadi tidak membantu.
Aturan praktisnya: **dua ruas berpotongan → Menelaus; tiga ruas konkuren → Ceva.**
