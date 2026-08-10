---
id: kkr-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kekongruenan]
bentuk: isian
kesulitan: 3
jawaban: "13"
---

## Soal

Pada segitiga $ABC$, titik $M$ adalah titik tengah sisi $BC$. Ruas $AM$ diperpanjang melewati
$M$ sampai titik $D$, sedemikian sehingga $MD = AM$.

![Segitiga ABC dengan M titik tengah sisi BC. Ruas AM diperpanjang lurus melewati M sampai titik D dengan MD sama panjang dengan AM, lalu D dihubungkan ke B dan ke C](garis-berat-diperpanjang.svg)

Jika $AB = 9$ dan $AC = 13$, tentukan panjang $BD$.

## Petunjuk

- Ruas $BD$ yang ditanyakan dan ruas $AC$ yang diketahui berada di dua sisi gambar yang berlawanan. Perhatikan apa saja yang bertemu di titik $M$.
- Di $M$ ada dua pasang ruas sama panjang — $BM = MC$ dari titik tengah, dan $AM = MD$ dari susunannya. Ditambah sudut bertolak belakang, bahannya sudah lengkap.
- Buktikan $\triangle BMD \cong \triangle CMA$, lalu baca sisi yang bersesuaian.

## Pembahasan

**Perhatikan titik $M$.** Di situ dua ruas berpotongan: $BC$ dan $AD$. Perpotongan seperti itu
selalu membawa satu unsur gratis — **sudut bertolak belakang** — dan di sini kedua ruas itu
juga terbagi dua sama panjang.

**Bandingkan $\triangle BMD$ dan $\triangle CMA$.**

1. $BM = CM$ — karena $M$ titik tengah $BC$;
2. $\angle BMD = \angle CMA$ — sudut bertolak belakang;
3. $MD = MA$ — diberikan soal.

Sudutnya diapit kedua sisi itu, jadi **S-Sd-S**:

$$\triangle BMD \cong \triangle CMA$$

**Baca sisi yang bersesuaian.** Pasangannya $B \leftrightarrow C$, $M \leftrightarrow M$,
$D \leftrightarrow A$, sehingga

$$BD = CA = \boxed{13}$$

**Perhatikan bahwa $AB = 9$ tidak dipakai sama sekali.** Ia memang tidak diperlukan untuk
menjawab pertanyaan ini — dan itu bukan kekeliruan penyusun soal, melainkan bagian dari
soalnya. Kalau setiap angka di soal terasa harus dipakai, kamu akan memaksakan langkah yang
tidak ada.

### Bangun yang baru saja kamu buat

Karena $BD = CA$ dan (dari kekongruenan yang sama) $\angle DBM = \angle ACM$ — sudut dalam
berseberangan pada $BD$ dan $CA$ yang dipotong $BC$ — maka $BD \parallel CA$. Sepasang sisi
yang sejajar **dan** sama panjang: bangun $ABDC$ adalah **jajaran genjang**, dengan $AD$ dan
$BC$ sebagai kedua diagonalnya yang saling membagi dua sama panjang.

Itulah isi sesungguhnya dari langkah "perpanjang garis berat sejauh dirinya sendiri".

### Kenapa jurus ini layak dihafal sebagai gerakan

Menghadapi soal yang memuat **titik tengah**, perpanjangan semacam ini mengubah gambar yang
sulit menjadi jajaran genjang yang mudah. Kegunaannya: ia **memindahkan** ruas $AC$ ke posisi
baru $BD$ yang bersentuhan langsung dengan $AB$ — dan sesudah itu $AB$, $BD$, serta $AD$ semua
berada pada **satu** segitiga $ABD$.

Dari situ ketaksamaan segitiga pada $\triangle ABD$ memberi

$$|AC - AB| < AD < AC + AB \quad \Longrightarrow \quad 4 < 2\,AM < 22$$

sehingga $2 < AM < 11$. Batas untuk panjang garis berat itu tidak terbaca sama sekali dari
gambar semula; ia muncul hanya setelah ketiga panjangnya dikumpulkan ke dalam satu segitiga.
