---
id: lb-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [luas-bidang]
bentuk: isian
kesulitan: 2
jawaban: "30"
---

## Soal

Segitiga $ABC$ mempunyai luas $60$. Titik $D$ terletak pada sisi $BC$ dengan $BD : DC = 2 : 1$,
dan titik $E$ terletak pada ruas $AD$ dengan $AE : ED = 3 : 1$.

![Segitiga ABC dengan alas BC mendatar. Titik D pada alas BC, dua pertiga jarak dari B ke C. Ruas AD digambar dan titik E terletak padanya, tiga perempat jarak dari A ke D. Ruas BE digambar dan segitiga ABE diarsir](segitiga-dua-bagi.svg)

Tentukan luas segitiga $ABE$.

## Petunjuk

- Panjang sisi segitiganya tidak diberikan sama sekali, dan tingginya juga tidak. Kalau jawabannya tetap tunggal, yang dipakai pasti perbandingan, bukan ukuran.
- Dua segitiga yang tingginya sama punya perbandingan luas sama dengan perbandingan alasnya. Cari sepasang segitiga yang memenuhi itu untuk tiap langkah.
- Kerjakan bertahap: dari $\triangle ABC$ ke $\triangle ABD$ dulu, baru dari $\triangle ABD$ ke $\triangle ABE$.

## Pembahasan

**Aturan tunggal yang dipakai dua kali.** Dua segitiga yang **tingginya sama** punya
perbandingan luas sama dengan perbandingan alasnya. Seluruh soal ini tidak lain dari
menerapkannya dua kali, pada dua pasangan yang berbeda.

**Langkah pertama: dari $\triangle ABC$ ke $\triangle ABD$.**

Segitiga $ABD$ dan $ABC$ sama-sama berpuncak di $A$, dengan alas $BD$ dan $BC$ yang terletak
pada satu garis. Jadi tinggi dari $A$ ke garis itu sama untuk keduanya, dan

$$\frac{[ABD]}{[ABC]} = \frac{BD}{BC} = \frac{2}{3}$$

$$[ABD] = \tfrac{2}{3} \times 60 = 40$$

**Langkah kedua: dari $\triangle ABD$ ke $\triangle ABE$.**

Sekarang segitiga $ABE$ dan $ABD$ sama-sama berpuncak di $B$, dengan alas $AE$ dan $AD$ pada
satu garis. Tinggi dari $B$ ke garis $AD$ sama untuk keduanya, sehingga

$$\frac{[ABE]}{[ABD]} = \frac{AE}{AD} = \frac{3}{4}$$

$$[ABE] = \tfrac{3}{4} \times 40 = \boxed{30}$$

### Bagian yang paling sering keliru: puncak mana yang dipakai

Pada langkah pertama puncaknya $A$, pada langkah kedua puncaknya $B$. Kalau puncaknya salah
dipilih, "tinggi yang sama" tidak berlaku dan seluruh perbandingannya batal.

Cara memeriksanya cepat: **alas kedua segitiga harus terletak pada satu garis lurus, dan
puncaknya harus titik yang sama.**

- Langkah pertama: alas $BD$ dan $BC$ sama-sama pada garis $BC$ ✓, puncak $A$ ✓.
- Langkah kedua: alas $AE$ dan $AD$ sama-sama pada garis $AD$ ✓, puncak $B$ ✓.

### Kalikan saja nisbahnya

Dua langkah tadi bisa digabung menjadi satu:

$$[ABE] = \frac{AE}{AD} \times \frac{BD}{BC} \times [ABC]
= \tfrac{3}{4} \times \tfrac{2}{3} \times 60 = 30$$

Bentuk ini enak dipakai, tetapi hanya sah kalau tiap langkahnya memang memenuhi syarat "tinggi
sama". Menyusunnya langsung tanpa memeriksa itu adalah cara tercepat mendapat jawaban yang
terlihat wajar tetapi salah.

### Yang tidak pernah dibutuhkan

Perhatikan bahwa panjang $AB$, $BC$, $AC$, tinggi segitiga, dan besar sudut-sudutnya **tidak
satu pun dipakai**. Luas $60$ pun hanya dikalikan di akhir; kalau soal menanyakan
$\dfrac{[ABE]}{[ABC]}$, jawabannya $\dfrac{1}{2}$ tanpa perlu angka apa pun.

Itulah maksud "luas dipakai sebagai alat, bukan sebagai jawaban" — dan itu ciri khas soal luas
di olimpiade.
