---
id: tfm-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [transformasi]
bentuk: uraian
kesulitan: 3
---

## Soal

Titik $A$ dan $B$ terletak pada sisi yang sama dari garis $\ell$, dan keduanya tidak pada
$\ell$. Misalkan $A'$ cerminan $A$ terhadap $\ell$, dan $P_0$ titik potong ruas $A'B$
dengan $\ell$.

Buktikan bahwa untuk setiap titik $P$ pada $\ell$ berlaku

$$AP + PB \ \ge\ AP_0 + P_0B$$

dan bahwa kesamaannya hanya tercapai ketika $P = P_0$.

## Petunjuk

- Pencerminan menjaga jarak. Apa yang bisa kamu katakan tentang $AP$ dan $A'P$ untuk $P$ pada $\ell$?
- Setelah $AP$ diganti $A'P$, ruas kirinya menjadi lintasan patah dari $A'$ ke $B$ lewat $P$. Ketaksamaan apa yang berlaku untuk lintasan patah?
- Ketaksamaan segitiga, beserta syarat kesamaannya: kesamaan tercapai tepat ketika ketiga titiknya segaris dengan titik tengahnya di antara kedua ujung.

## Pembahasan

**Langkah 1 — pencerminan menjaga jarak ke titik pada sumbunya.**

Misalkan $P$ sembarang titik pada $\ell$. Karena $\ell$ sumbu cermin yang memetakan $A$ ke
$A'$, garis $\ell$ tak lain **sumbu ruas** $AA'$: ia tegak lurus $AA'$ di titik tengahnya.

Setiap titik pada sumbu sebuah ruas berjarak sama ke kedua ujung ruas itu, sehingga

$$AP = A'P \qquad \text{untuk setiap } P \text{ pada } \ell$$

Khususnya juga $AP_0 = A'P_0$, sebab $P_0$ ada pada $\ell$.

**Langkah 2 — ganti dan pakai ketaksamaan segitiga.**

$$AP + PB = A'P + PB$$

Ruas kanannya adalah panjang lintasan patah dari $A'$ ke $B$ yang melewati $P$. Menurut
ketaksamaan segitiga,

$$A'P + PB \ \ge\ A'B$$

**Langkah 3 — tunjukkan bahwa $P_0$ mencapai batas itu.**

Titik $A$ dan $B$ berada di sisi yang sama dari $\ell$, jadi $A'$ dan $B$ berada di sisi yang
**berlawanan**. Karena itu ruas $A'B$ benar-benar memotong $\ell$, dan titik potongnya $P_0$
berada **di antara** $A'$ dan $B$. Maka

$$A'P_0 + P_0B = A'B$$

Digabung dengan Langkah 1:

$$AP_0 + P_0B = A'P_0 + P_0B = A'B$$

**Langkah 4 — rangkai.**

$$AP + PB = A'P + PB \ \ge\ A'B = AP_0 + P_0B \qquad \blacksquare$$

**Syarat kesamaan.** Ketaksamaan segitiga $A'P + PB \ge A'B$ berubah jadi kesamaan tepat
ketika $P$ terletak pada ruas $A'B$. Titik pada $\ell$ yang sekaligus pada ruas $A'B$ hanya
ada satu, yaitu $P_0$ — sebab dua garis yang tidak sejajar berpotongan di paling banyak satu
titik, dan $A'B$ tidak sejajar $\ell$ karena ia menembusnya.

Jadi kesamaannya tercapai hanya untuk $P = P_0$ $\blacksquare$

### Langkah yang paling sering dilewati

Bagian yang gampang hilang adalah **Langkah 3**: menunjukkan bahwa $P_0$ betul-betul ada dan
berada di antara $A'$ dan $B$. Tanpa itu, $A'P_0 + P_0B$ belum tentu sama dengan $A'B$ — untuk
titik $P_0$ di luar ruas $A'B$, jumlahnya justru lebih besar.

Alasannya sendiri sederhana dan cuma butuh satu kalimat: pencerminan memindahkan $A$ ke sisi
seberang $\ell$, jadi $A'$ dan $B$ terpisah oleh $\ell$.

### Kenapa buktinya perlu, padahal gambarnya jelas

Gambar memperlihatkan bahwa $P_0$ terlihat terbaik, tetapi tidak membuktikan bahwa tidak ada
$P$ lain yang lebih baik — dan "terlihat terbaik" bukan alasan. Yang mengubahnya jadi bukti
adalah ketaksamaan segitiga, sebab ia berlaku untuk **semua** $P$ sekaligus, bukan untuk
beberapa yang dicoba.

Pola itu berulang di seluruh soal minimum geometri: ubah besaran yang dicari menjadi panjang
sebuah lintasan, lalu bandingkan dengan ruas lurus yang menghubungkan kedua ujungnya.

### Akibat yang layak diingat

Pada penyelesaiannya, $A'$, $P_0$, $B$ segaris, sehingga sudut yang dibentuk $A'P_0$ dengan
$\ell$ sama dengan sudut yang dibentuk $P_0B$ dengan $\ell$ (bertolak belakang). Karena sudut
$AP_0$ terhadap $\ell$ adalah cerminan sudut $A'P_0$ terhadap $\ell$, keduanya sama besar.

Jadi pada lintasan terpendek, **sudut datang sama dengan sudut pantul**. Hukum pemantulan
cahaya dan soal lintasan terpendek adalah pernyataan yang sama.

## Rubrik

- Menyatakan bahwa $\ell$ adalah sumbu ruas $AA'$, dan menyimpulkan $AP = A'P$ untuk setiap
  $P$ pada $\ell$
- Mengganti $AP$ dengan $A'P$ sehingga ruas kirinya menjadi lintasan dari $A'$ ke $B$
- Memakai ketaksamaan segitiga $A'P + PB \ge A'B$
- Menyebut bahwa $A'$ dan $B$ berada di sisi berlawanan dari $\ell$, sebagai alasan ruas
  $A'B$ memotong $\ell$ dan $P_0$ berada di antara keduanya
- Menyimpulkan $AP_0 + P_0B = A'B$ dan merangkai seluruh ketaksamaannya
- Menyatakan syarat kesamaan ketaksamaan segitiga, dan menunjukkan hanya $P_0$ yang
  memenuhinya

Bukti yang hanya menghitung $AP + PB$ untuk beberapa letak $P$ lalu menyimpulkan $P_0$
terbaik dinilai tidak sah: mencoba beberapa titik tidak menyingkirkan yang tak terhingga
banyaknya.
