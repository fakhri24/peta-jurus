---
id: ksb-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kesebangunan]
bentuk: isian
kesulitan: 3
jawaban: "16"
---

## Soal

Pada segitiga $ABC$, titik $D$ terletak pada sisi $BC$ sedemikian sehingga

$$\angle BAD = \angle BCA$$

![Segitiga ABC dengan alas BC mendatar dan puncak A di atas. Titik D terletak pada alas BC, lebih dekat ke B daripada ke C, dan dihubungkan ke A. Sudut BAD dan sudut BCA ditandai sama besar](segitiga-sudut-sama.svg)

Diketahui $AB = 8$ dan $BD = 4$.

Tentukan panjang $BC$.

## Petunjuk

- Sudut yang sama besar itu berada di dua segitiga yang berbeda. Segitiga mana saja, dan apakah keduanya punya sesuatu yang dipakai bersama?
- Bandingkan $\triangle BAD$ dengan $\triangle BCA$. Selain sudut yang diberikan soal, keduanya berbagi sudut di titik $B$.
- Susun perbandingan sisinya dengan pasangan $B \leftrightarrow B$, $A \leftrightarrow C$, $D \leftrightarrow A$.

## Pembahasan

**Temukan kedua segitiganya.** Sudut $\angle BAD$ ada di $\triangle BAD$, dan sudut
$\angle BCA$ ada di $\triangle BCA$. Kedua segitiga itu bertumpuk — yang kecil di dalam yang
besar — dan berbagi titik $B$.

**Kumpulkan sudutnya.**

1. $\angle BAD = \angle BCA$ — diberikan soal;
2. $\angle ABD = \angle CBA$ — **sudut yang sama**, yaitu sudut di $B$, sebab $D$ terletak pada
   $BC$ sehingga sinar $BD$ berimpit dengan sinar $BC$.

Dua pasang sudut sudah cukup:

$$\triangle BAD \sim \triangle BCA \quad (\text{Sd-Sd})$$

**Susun perbandingannya menurut pasangannya.** Pasangan titiknya $B \leftrightarrow B$,
$A \leftrightarrow C$, $D \leftrightarrow A$, sehingga sisi $BA$ bersesuaian dengan $BC$ dan
sisi $BD$ bersesuaian dengan $BA$:

$$\frac{BA}{BC} = \frac{BD}{BA}$$

**Kalikan silang.**

$$BA^2 = BC \times BD$$

$$8^2 = BC \times 4 \quad \Longrightarrow \quad BC = \frac{64}{4} = \boxed{16}$$

**Periksa.** $\dfrac{BA}{BC} = \dfrac{8}{16} = \dfrac{1}{2}$ dan $\dfrac{BD}{BA} =
\dfrac{4}{8} = \dfrac{1}{2}$ ✓. Perhatikan juga $BD = 4 < 16 = BC$, jadi $D$ memang jatuh di
dalam ruas $BC$ — kalau perhitungan memberi $BD > BC$, gambarnya mustahil.

### Bentuk $BA^2 = BC \cdot BD$ layak dikenali

Yang muncul di sini bukan perbandingan biasa, melainkan **satu panjang yang menjadi rata-rata
geometri dari dua panjang lain**. Bentuk ini menandai satu konfigurasi tertentu, dan setiap
kali kamu melihat $x^2 = y \cdot z$ pada gambar geometri, curigai ada dua segitiga sebangun
yang bertumpuk.

Contoh lain dari bentuk yang sama:

- Pada segitiga siku-siku bergaris tinggi: $h^2 = pq$ dan $a^2 = cp$.
- Pada lingkaran: kuasa titik, $PA \cdot PB = PT^2$ — yang akan kamu temui di tahap
  berikutnya.

Ketiganya lahir dari mekanisme yang sama: dua segitiga sebangun yang berbagi satu sudut, dengan
sisi bersama muncul di dua tempat berbeda pada perbandingannya.

### Kenapa nilai sudutnya tidak pernah dibutuhkan

Perhatikan bahwa besar $\angle BAD$ tidak pernah dipakai — cukup diketahui ia **sama** dengan
$\angle BCA$. Karena itu jawabannya tidak bergantung pada bentuk segitiganya: berapa pun sudut
di $B$, selama kedua sudut itu sama besar, $BC$ tetap $16$.

Itu isyarat umum yang berguna: kalau sebuah nilai tidak muncul di perhitungan, ia memang tidak
menentukan jawabannya — dan mencarinya cuma membuang waktu.
