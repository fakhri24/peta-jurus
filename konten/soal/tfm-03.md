---
id: tfm-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [transformasi]
bentuk: isian
kesulitan: 3
jawaban: "11"
---

## Soal

Sebuah sungai lurus dengan kedua tepinya sejajar memisahkan kota $A$ dan kota $B$. Lebar
sungainya $1$. Kota $A$ berjarak $2$ dari tepi terdekatnya, kota $B$ berjarak $4$ dari tepi
di seberangnya, dan jarak antara kedua kaki tegak lurusnya, diukur sepanjang arah sungai,
adalah $8$.

Sebuah jembatan akan dibangun **tegak lurus** sungai. Tentukan panjang lintasan terpendek
dari $A$ ke $B$ yang melewati jembatan itu.

## Petunjuk

- Panjang jembatannya sudah pasti $1$ ke mana pun ia ditaruh. Jadi yang perlu diperkecil cuma jumlah dua ruas darat.
- Kalau jembatannya bisa "dilipat" hingga panjangnya nol, kedua ruas darat itu akan bersambung. Transformasi apa yang melakukannya?
- Geser $A$ sejauh $1$ tegak lurus sungai, ke arah $B$. Setelah itu jaraknya menjadi soal garis lurus biasa.

## Pembahasan

**Pisahkan bagian yang tetap.** Lintasannya terdiri dari tiga bagian: dari $A$ ke pangkal
jembatan, jembatannya sendiri, lalu dari ujung jembatan ke $B$. Bagian tengahnya selalu $1$,
di mana pun jembatan ditaruh — jadi ia tidak ikut menentukan pilihan.

Yang perlu diperkecil hanya jumlah kedua bagian darat.

**Pakai translasi untuk menyambungkan keduanya.** Geser $A$ sejauh $1$, tegak lurus sungai,
ke arah seberang. Sebut hasilnya $A''$.

Karena jembatannya juga tegak lurus sungai dan panjangnya juga $1$, ruas dari $A$ ke pangkal
jembatan sejajar dan sama panjang dengan ruas dari $A''$ ke **ujung** jembatan. Jadi kedua
bagian darat itu, setelah digeser, menjadi lintasan dari $A''$ langsung ke $B$ — patah di
ujung jembatan.

**Sekarang soalnya soal garis lurus.** Jumlah kedua bagian darat paling kecil ketika $A''$,
ujung jembatan, dan $B$ segaris:

$$\text{darat terkecil} = A''B$$

**Hitung.** Ambil arah sungai sebagai sumbu $x$, dan $A$ di titik asal:

$$A(0, 0), \qquad A''(0, 1)$$

Kota $B$ berada $8$ ke arah sungai, dan tegak lurus sungai sejauh $2 + 1 + 4 = 7$ dari $A$:

$$B(8, 7)$$

$$A''B = \sqrt{8^2 + (7-1)^2} = \sqrt{64 + 36} = 10$$

**Tambahkan kembali jembatannya.**

$$\text{lintasan terpendek} = 10 + 1 = \boxed{11}$$

### Kenapa translasi, bukan pencerminan

Pada soal lintasan terpendek yang menyentuh garis, yang dipakai pencerminan. Di sini yang
dipakai translasi. Pembedanya jelas kalau ditanyakan begini: **apa yang menghalangi
lintasannya menjadi garis lurus?**

- Kalau halangannya "harus menyentuh sebuah garis" → **pencerminan**;
- Kalau halangannya "harus melewati ruas berarah tetap dengan panjang tetap" → **translasi**.

Translasi menghapus ruas tetap itu dengan menggesernya keluar dari soal, dan yang tersisa
persoalan garis lurus.

### Jebakan: menggeser ke arah yang salah

Menggeser $A$ menjauhi sungai memberi jarak tegak lurus $2 + 1 + 4 + 1 = 8$ alih-alih $6$,
dan hasilnya $\sqrt{64+64} = 8\sqrt2 \approx 11{,}31$, lalu ditambah $1$ menjadi
$\approx 12{,}31$ — lebih besar dari jawaban yang benar, dan tidak bisa dicapai lintasan
apa pun.

Pemeriksaan yang cepat: setelah digeser, jarak tegak lurus antara $A''$ dan $B$ harus sama
dengan jarak total dikurangi lebar sungai, yaitu $7 - 1 = 6$ ✓.

### Batas bawah yang wajar

Berapa pun letaknya, lintasan tidak mungkin lebih pendek daripada jarak lurus $AB$ sendiri:

$$AB = \sqrt{8^2 + 7^2} = \sqrt{113} \approx 10{,}63$$

Jawaban $11$ lebih besar dari itu ✓, dan selisihnya kecil — masuk akal, sebab syarat "tegak
lurus" hanya sedikit memaksa lintasannya menyimpang dari garis lurus.

Perbandingan semacam ini murah dan menangkap kesalahan arah geseran dengan sekali lihat.

### Kalau jembatannya boleh miring

Tanpa syarat tegak lurus, lintasan terpendeknya jelas $AB = \sqrt{113}$ langsung, dan
jembatannya cukup bagian dari ruas itu yang melintasi sungai. Syarat "tegak lurus" itulah
yang membuat soal ini punya isi — dan dalam kenyataan syarat itu memang wajar, karena
jembatan miring lebih panjang dan lebih mahal.
