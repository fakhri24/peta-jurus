---
id: sg-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [sudut-garis]
bentuk: isian
kesulitan: 2
jawaban: "105"
---

## Soal

Garis $l$ dan garis $m$ sejajar. Titik $B$ terletak pada $l$, titik $D$ terletak pada $m$,
dan titik $E$ terletak di antara kedua garis itu.

![Garis l dan garis m sejajar mendatar, dengan B pada garis l dan D pada garis m. Titik A pada garis l di sebelah kanan B, titik C pada garis m di sebelah kanan D, dan titik E di antara kedua garis dihubungkan ke B dan ke D membentuk zigzag. Sudut ABE 42 derajat, sudut CDE 63 derajat, sudut BED ditanyakan](sejajar-zigzag.svg)

Diketahui $\angle ABE = 42^\circ$ dan $\angle CDE = 63^\circ$.

Tentukan besar $\angle BED$ dalam derajat.

## Petunjuk

- Kedua sudut yang diketahui berada di tempat yang berjauhan, dan sudut yang ditanyakan tidak menyentuh keduanya. Adakah garis yang bisa kamu tambahkan supaya ketiganya bertemu?
- Tarik garis lewat $E$ yang sejajar $l$ dan $m$. Garis itu memotong $\angle BED$ menjadi dua bagian.
- Sudut dalam berseberangan sama besar. Terapkan pada pasangan $l$ dengan garis bantu, lalu pada pasangan $m$ dengan garis bantu.

## Pembahasan

**Kenali kesulitannya lebih dulu.** Sudut $42^\circ$ ada di $B$, sudut $63^\circ$ ada di $D$,
dan sudut yang dicari ada di $E$ — tidak satu pun dari ketiganya berbagi kaki dengan yang
lain. Selama gambarnya dibiarkan seperti itu, tidak ada aturan yang bisa dipakai. Yang
kurang bukan rumus, melainkan **satu garis**.

**Tarik garis bantu.** Lewat $E$, tarik garis $n$ yang sejajar $l$ (karena $l \parallel m$,
otomatis $n$ juga sejajar $m$). Namai arah $n$ yang menuju ke kiri sebagai $EF$. Garis itu
membelah $\angle BED$ menjadi

$$\angle BED = \angle BEF + \angle FED$$

**Pindahkan sudut pertama.** Perhatikan garis $BE$ yang memotong dua garis sejajar $l$ dan
$n$. Sudut $\angle ABE$ dan $\angle BEF$ adalah **sudut dalam berseberangan**, jadi

$$\angle BEF = \angle ABE = 42^\circ$$

**Pindahkan sudut kedua.** Sekarang garis $DE$ memotong dua garis sejajar $m$ dan $n$. Dengan
alasan yang sama,

$$\angle FED = \angle CDE = 63^\circ$$

**Jumlahkan.**

$$\angle BED = 42^\circ + 63^\circ = \boxed{105^\circ}$$

### Mengapa garis bantunya harus sejajar, bukan sembarang

Garis bantu berguna hanya kalau ia **membawa aturan** ke dalam gambar. Garis lewat $E$ yang
arahnya sembarang memang tetap membelah $\angle BED$ menjadi dua, tetapi tidak ada satu pun
sifat yang menghubungkan kedua bagian itu dengan $42^\circ$ dan $63^\circ$. Yang membuat
langkah ini bekerja adalah kesejajarannya: begitu $n \parallel l$, sudut dalam berseberangan
langsung berlaku.

Ini pola yang akan terpakai berkali-kali: **kalau dua hal yang diketahui berjauhan, cari
garis yang menyeret keduanya ke satu titik.**

### Pola yang layak dikenali

Bentuk zigzag seperti ini sering muncul, dan hasilnya selalu sama:

$$\angle BED = \angle ABE + \angle CDE$$

selama $E$ berada **di antara** kedua garis sejajar dan kedua sudut diukur ke arah yang
sama. Mengenali polanya menghemat waktu, tetapi jangan menghafalnya tanpa garis bantunya —
begitu $E$ pindah ke luar kedua garis, rumusnya berubah menjadi **selisih**, dan hanya
gambar dengan garis bantu yang memberitahu kapan itu terjadi.

### Periksa kewajarannya

$\angle BED = 105^\circ$ tumpul, dan memang di gambar sudut itu terlihat lebih besar dari
siku-siku. Pemeriksaan kasar semacam ini tidak membuktikan apa pun, tetapi menangkap
kekeliruan tanda dan kekeliruan "seharusnya selisih, bukan jumlah" dengan ongkos satu detik.
