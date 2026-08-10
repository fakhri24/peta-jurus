---
id: hmt-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [homoteti]
bentuk: isian
kesulitan: 3
jawaban: "9"
---

## Soal

Dua lingkaran berjari-jari $3$ dan $7$ punya pusat yang berjarak $12$ satu sama lain.

Tentukan jarak dari pusat homoteti **luar** kedua lingkaran itu ke pusat lingkaran yang
kecil.

## Petunjuk

- Pusat homoteti selalu terletak pada garis yang menghubungkan kedua pusat lingkaran.
- Homoteti berpusat $E$ memetakan lingkaran kecil ke lingkaran besar dengan faktor $k = \tfrac{7}{3}$, jadi $EO_2 = \tfrac73 EO_1$.
- Pusat homoteti **luar** berada di luar ruas $O_1O_2$, pada sisi lingkaran yang kecil — jadi $EO_2 - EO_1 = 12$.

## Pembahasan

**Letakkan $E$ pada garis pusatnya.** Homoteti yang memetakan lingkaran satu ke lingkaran
lain memetakan pusat ke pusat, jadi $E$, $O_1$, dan $O_2$ **segaris**.

**Tentukan faktornya.** Homoteti itu memetakan jari-jari $3$ menjadi jari-jari $7$, jadi
untuk pusat homoteti luar

$$k = \frac{7}{3} > 0$$

**Pakai definisinya.** Karena $\overrightarrow{EO_2} = k\,\overrightarrow{EO_1}$:

$$EO_2 = \frac{7}{3}\,EO_1$$

Faktornya positif, jadi $O_1$ dan $O_2$ sepihak terhadap $E$ — dengan kata lain $E$ berada
**di luar** ruas $O_1O_2$, di sisi lingkaran kecil. Maka

$$EO_2 - EO_1 = O_1O_2 = 12$$

**Selesaikan.**

$$\frac{7}{3}EO_1 - EO_1 = 12 \quad \Longrightarrow \quad \frac{4}{3}EO_1 = 12
\quad \Longrightarrow \quad EO_1 = \boxed{9}$$

Sekalian, $EO_2 = 21$.

### Periksa

$$\frac{EO_1}{EO_2} = \frac{9}{21} = \frac{3}{7} \quad ✓ \qquad
EO_2 - EO_1 = 21 - 9 = 12 \quad ✓$$

Kedua syarat terpenuhi sekaligus.

Periksa juga letaknya masuk akal: $E$ berjarak $9$ dari pusat lingkaran kecil yang
berjari-jari $3$, jadi $E$ di luar lingkaran kecil ✓ — dan memang harus, sebab dari pusat
homoteti luar bisa ditarik garis singgung ke kedua lingkaran.

### Pusat homoteti yang satu lagi

Setiap pasangan lingkaran punya **dua** pusat homoteti. Yang dalam, sebut $I$, memakai
$k = -\tfrac73$ dan karena itu terletak **di antara** kedua pusat:

$$\frac{IO_1}{IO_2} = \frac37, \qquad IO_1 + IO_2 = 12$$

$$IO_1 = \frac{3}{10} \times 12 = 3{,}6, \qquad IO_2 = 8{,}4$$

Melupakan yang satu ini adalah jebakan baku jurus ini: kesimpulan yang bentuknya benar
tetapi titiknya salah. Kalau soal menyebut "garis singgung persekutuan luar", yang dipakai
$E$; kalau "dalam", yang dipakai $I$.

### Cara mengingat letaknya tanpa rumus

- **Pusat homoteti luar** — arah kedua bangun sama, jadi ia berada di **luar** ruas
  penghubungnya, di sisi lingkaran yang lebih kecil. Kalau kedua jari-jarinya sama, ia lari
  ke tak hingga dan homotetinya merosot jadi translasi.
- **Pusat homoteti dalam** — arahnya berlawanan, jadi ia berada di **antara** kedua pusat,
  dan ia selalu ada.

Uji cepat pada kasus $r_1 = r_2$: rumus $EO_1 = \dfrac{d\,r_1}{r_2 - r_1}$ berpenyebut nol —
persis tanda bahwa pusat luarnya tidak ada, sesuai gambaran di atas.

### Kegunaannya

Ketiga pusat homoteti luar dari **tiga** lingkaran selalu segaris — itu **teorema Monge**,
akibat langsung dari kenyataan bahwa gabungan dua homoteti adalah homoteti lagi yang
pusatnya segaris dengan keduanya.

Karena itu menghitung letak pusat homoteti bukan latihan kosong: ia sering menjadi titik yang
kesegarisannya justru diminta soal.
