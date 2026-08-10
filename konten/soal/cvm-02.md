---
id: cvm-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ceva-menelaus]
bentuk: isian
kesulitan: 4
jawaban: "9"
---

## Soal

Pada segitiga $ABC$, titik $D$ pada sisi $BC$ dengan $BD : DC = 1 : 2$, dan titik $E$ pada
sisi $AC$ dengan $AE : EC = 3 : 1$. Ruas $AD$ dan $BE$ berpotongan di titik $P$.

Tentukan nilai $\dfrac{AP}{PD}$.

## Petunjuk

- Cuma ada **dua** ruas, jadi Ceva belum bisa dipakai — Ceva butuh tiga yang konkuren.
- Cari segitiga yang salah satu sisinya adalah $AD$, dan yang dilintasi garis lurus $B$–$P$–$E$.
- Pakai Menelaus pada $\triangle ADC$ dengan garis lintang $BPE$: garis itu memotong $AD$ di $P$, memotong $CA$ di $E$, dan memotong perpanjangan $DC$ di $B$.

## Pembahasan

**Pilih segitiga yang tepat.** Yang ditanyakan perbandingan pada ruas $AD$, jadi $AD$ harus
menjadi salah satu **sisi** segitiga yang dipakai. Ambil $\triangle ADC$.

**Kenali garis lintangnya.** Titik $B$, $P$, $E$ terletak pada satu garis lurus, yaitu garis
$BE$. Terhadap $\triangle ADC$, garis itu memotong:

- sisi $AD$ di $P$;
- sisi $CA$ di $E$;
- perpanjangan sisi $DC$ di $B$ — sebab $B$ ada pada garis $BC$ tetapi di luar ruas $DC$.

Itu tepat bentuk Menelaus.

**Tulis Menelaus berkeliling $A \to D \to C \to A$.**

$$\frac{AP}{PD} \cdot \frac{DB}{BC} \cdot \frac{CE}{EA} = 1$$

**Isi angkanya.** Dari $BD : DC = 1 : 2$, tulis $BD = 1$, $DC = 2$, sehingga $BC = 3$:

$$\frac{DB}{BC} = \frac{1}{3}$$

Dari $AE : EC = 3 : 1$:

$$\frac{CE}{EA} = \frac{1}{3}$$

Maka

$$\frac{AP}{PD} \cdot \frac{1}{3} \cdot \frac{1}{3} = 1 \quad \Longrightarrow \quad
\frac{AP}{PD} = \boxed{9}$$

### Jebakan terbesar: memakai $DB : BC$, bukan $BD : DC$

Pada Menelaus terhadap $\triangle ADC$, sisi yang dipotong adalah $DC$, dan titik potongnya
$B$. Jadi perbandingan yang dipakai $\dfrac{DB}{BC}$ — jarak dari $D$ ke $B$, dibanding jarak
dari $B$ ke $C$.

Itu **bukan** $\dfrac{BD}{DC} = \dfrac12$ yang diberikan soal. Nilainya
$\dfrac{DB}{BC} = \dfrac{1}{3}$, karena $B$ berada di luar ruas $DC$ dan jaraknya ke $C$
adalah seluruh $BC$.

Kalau angka $\tfrac12$ dipakai begitu saja, jawabannya keluar $6$ — bilangan bulat yang
terlihat meyakinkan dan salah. Aturan yang menyelamatkan: **tulis dulu ketiga sisi segitiga
yang dipakai, baru pasangkan titik potongnya**, jangan langsung menyalin angka dari soal.

### Periksa lewat koordinat

Ambil $B(0,0)$, $C(3,0)$, dan $A(0,4)$ — pilihan apa pun boleh, karena perbandingan tidak
berubah oleh pilihan sumbu.

$$D = \left(1, 0\right) \quad \text{karena } BD:DC = 1:2$$

$$E = \tfrac14 A + \tfrac34 C = \left(\tfrac94, 1\right) \quad \text{karena } AE:EC = 3:1$$

Garis $AD$: dari $(0,4)$ ke $(1,0)$, yaitu $y = 4 - 4x$.
Garis $BE$: dari $(0,0)$ ke $\left(\tfrac94, 1\right)$, yaitu $y = \tfrac49 x$.

Samakan: $4 - 4x = \tfrac49 x \Rightarrow 36 - 36x = 4x \Rightarrow x = \tfrac{9}{10}$, dan
$y = \tfrac{4}{10}$. Jadi $P = \left(0{,}9,\ 0{,}4\right)$.

$$AP = \sqrt{0{,}9^2 + 3{,}6^2}, \qquad PD = \sqrt{0{,}1^2 + 0{,}4^2}$$

Karena $A$, $P$, $D$ segaris, perbandingannya bisa dibaca dari selisih absis saja:

$$\frac{AP}{PD} = \frac{0{,}9 - 0}{1 - 0{,}9} = \frac{0{,}9}{0{,}1} = 9 \quad ✓$$

### Cara ketiga: titik massa

Beri massa $2$ di $B$ dan $1$ di $C$, supaya $D$ jadi titik seimbangnya
($BD : DC = 1 : 2$ berarti massa berbanding terbalik). Massa di $D$ menjadi $3$.

Untuk $E$ pada $AC$ dengan $AE : EC = 3 : 1$, massa $A$ dibanding massa $C$ harus $1 : 3$.
Massa $C$ sudah $1$, jadi massa $A$ adalah $\tfrac13$. Kalikan semuanya dengan $3$ supaya
bulat: $A = 1$, $B = 6$, $C = 3$, sehingga $D = 9$.

Pada ruas $AD$, perbandingannya berbanding terbalik dengan massanya:

$$\frac{AP}{PD} = \frac{m_D}{m_A} = \frac{9}{1} = 9 \quad ✓$$

Titik massa jauh lebih cepat pada soal seperti ini, dan ia sebenarnya Menelaus yang
dibungkus jadi kebiasaan. Batasnya: ia hanya bekerja kalau semua titiknya di **dalam** sisi.
Begitu ada yang di perpanjangan, kembalilah ke Menelaus.
