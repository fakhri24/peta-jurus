---
id: kkr-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kekongruenan]
bentuk: uraian
kesulitan: 3
---

## Soal

Seorang siswa menulis aturan berikut di buku catatannya:

> Kalau dua segitiga mempunyai dua pasang sisi sama panjang dan sepasang sudut sama besar,
> maka kedua segitiga itu kongruen.

Tunjukkan bahwa aturan itu **salah**, dengan memberikan sepasang segitiga yang memenuhi
seluruh syarat di atas tetapi tidak kongruen. Sebutkan ukurannya, dan jelaskan mengapa
keduanya tidak kongruen.

## Petunjuk

- Aturan yang ditulis siswa itu tidak menyebut di mana letak sudutnya. Coba susun contohmu supaya sudut yang sama besar itu **tidak** terapit kedua sisi yang sama panjang.
- Bangun yang setangkup memberi dua sudut sama besar secara cuma-cuma. Mulailah dari segitiga sama kaki, lalu tarik satu ruas dari puncaknya ke suatu titik pada alasnya.
- Ambil segitiga sama kaki $ABC$ dengan $AB = AC$ dan titik $D$ pada $BC$ yang **bukan** titik tengahnya, lalu bandingkan $\triangle ABD$ dengan $\triangle ACD$.

## Pembahasan

**Susun contohnya.** Ambil segitiga sama kaki $ABC$ dengan

$$AB = AC = 5, \qquad BC = 6$$

Titik $D$ diletakkan pada sisi $BC$ dengan

$$BD = 1, \qquad DC = 5$$

![Segitiga ABC sama kaki dengan puncak A dan alas BC mendatar, sisi AB dan AC ditandai sama panjang, kedua sudut alas ditandai sama besar. Titik D pada alas BC terletak dekat ke B, jauh dari titik tengahnya, dan dihubungkan ke A](sama-kaki-titik-dalam.svg)

**Hitung $AD$.** Titik tengah $BC$ sebut $M$, sehingga $BM = MC = 3$ dan tinggi dari $A$
adalah

$$AM = \sqrt{5^2 - 3^2} = \sqrt{16} = 4$$

Karena $BD = 1$, jarak $D$ ke $M$ adalah $DM = 3 - 1 = 2$, sehingga

$$AD = \sqrt{AM^2 + DM^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}$$

**Periksa ketiga syarat pada $\triangle ABD$ dan $\triangle ACD$.**

| Unsur | $\triangle ABD$ | $\triangle ACD$ | Alasan |
|---|---|---|---|
| Sisi pertama | $AB = 5$ | $AC = 5$ | diberikan, segitiga sama kaki |
| Sisi kedua | $AD = 2\sqrt{5}$ | $AD = 2\sqrt{5}$ | ruas yang dipakai bersama |
| Sudut | $\angle ABD$ | $\angle ACD$ | sudut alas segitiga sama kaki, keduanya sama besar |

Ketiga syarat aturan itu terpenuhi: dua pasang sisi sama panjang, dan sepasang sudut sama
besar. Besar kedua sudut itu pun bisa disebut, sebab $\cos \angle ABC = \tfrac{3}{5}$.

**Tunjukkan keduanya tidak kongruen.** Sisi ketiganya

$$BD = 1 \qquad \text{sedangkan} \qquad CD = 5$$

Dua segitiga yang kongruen mempunyai ketiga pasang sisi sama panjang. Di sini sisi ketiganya
berbeda jauh, jadi $\triangle ABD$ dan $\triangle ACD$ **tidak kongruen**. Aturan yang ditulis
siswa itu salah. $\blacksquare$

### Di mana persisnya aturan itu bocor

Bandingkan letak sudutnya:

- Pada $\triangle ABD$, kedua sisi yang diketahui adalah $AB$ dan $AD$. Sudut yang **diapit**
  keduanya adalah $\angle BAD$ — bukan $\angle ABD$.
- Sudut yang dipakai, $\angle ABD$, terletak di antara $AB$ dan $BD$; sedangkan $BD$ justru
  sisi yang tidak diketahui.

Jadi susunannya **S-S-Sd**, dengan sudut yang tidak diapit. Itu satu-satunya susunan tiga
unsur yang gagal — dan gagalnya bukan karena kurang informasi, melainkan karena informasi
yang sama benar-benar cocok untuk **dua** segitiga yang berbeda.

Kalau sudut yang sama besar itu diganti dengan $\angle BAD$ dan $\angle CAD$, aturannya
menjadi S-Sd-S dan kesimpulannya sah — dan pada contoh di atas syarat itu memang tidak
terpenuhi: $\angle BAD \ne \angle CAD$, sebab $D$ bukan titik tengah.

### Mengapa contoh tandingan lebih kuat daripada penjelasan

Untuk membantah pernyataan berbentuk "setiap ... pasti ...", **satu** contoh tandingan sudah
cukup dan tuntas. Tidak perlu menjelaskan mengapa aturannya terasa masuk akal, tidak perlu
menyebut ketiga aturan yang sah. Yang perlu hanyalah satu bangun berukuran jelas yang memenuhi
seluruh syaratnya dan gagal pada kesimpulannya.

Sebaliknya, untuk membuktikan pernyataan semacam itu **benar**, satu contoh tidak pernah
cukup. Perbedaan ongkos itu — satu contoh melawan bukti umum — layak dikenali sejak awal,
sebab ia menentukan bentuk seluruh jawabanmu.

### Satu pengecualian yang layak diketahui

S-S-Sd menjadi sah kalau sudut yang diketahui **siku-siku atau tumpul**. Alasannya terbaca di
contoh ini: kedua kemungkinan segitiga muncul karena kaki $D$ bisa jatuh di dua sisi berbeda
terhadap $M$, dan itu hanya mungkin ketika sudutnya lancip. Karena itu pada segitiga
siku-siku, "sisi miring dan satu sisi siku-siku" memang cukup untuk kekongruenan.

## Rubrik

- Menyusun sepasang segitiga yang konkret beserta seluruh ukurannya, bukan sekadar menjelaskan bahwa aturannya salah
- Menyebut dua pasang sisi yang sama panjang, termasuk alasan sisi yang dipakai bersama
- Menyebut sepasang sudut yang sama besar beserta alasannya
- Menunjukkan kedua segitiga tidak kongruen dengan membandingkan sisi ketiganya, atau unsur lain yang jelas berbeda
- Menjelaskan bahwa sudut yang dipakai tidak diapit kedua sisi yang diketahui, sehingga susunannya S-S-Sd
