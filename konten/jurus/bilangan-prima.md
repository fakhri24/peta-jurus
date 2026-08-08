---
id: bilangan-prima
nama: Bilangan Prima & Faktorisasi
pilar: teori-bilangan
tahap: osn-k
prasyarat: [keterbagian]
contoh: [bp-contoh-1]
latihan: [bp-01, bp-02, bp-03, bp-04, bp-05, bp-06]
---

## Kapan dipakai

Soal menyebut prima, atau meminta sesuatu tentang **struktur** sebuah bilangan:
banyaknya faktor, kuadrat sempurna, pangkat tiga sempurna, atau kapan dua bilangan tidak
berbagi faktor.

## Intinya

Setiap bilangan bulat $n > 1$ punya penulisan tunggal

$$n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$$

dengan $p_i$ prima berbeda. Ini **Teorema Dasar Aritmetika**, dan ketunggalannya itulah
seluruh kekuatannya: dua penulisan yang tampak berbeda untuk bilangan yang sama harus
punya pangkat prima yang identik. Menyamakan pangkat di kedua ruas adalah langkah yang
sering menyelesaikan soal dalam satu tarikan.

Dua sifat turunan yang paling sering dipakai:

1. **Lema Euclid.** Kalau $p$ prima dan $p \mid ab$, maka $p \mid a$ atau $p \mid b$.
   Sifat ini khas prima — untuk komposit tidak berlaku ($6 \mid 4 \cdot 9$ tapi $6$ tidak
   membagi $4$ maupun $9$).
2. $n$ adalah **kuadrat sempurna** tepat ketika semua pangkat $a_i$ genap. Pangkat tiga
   sempurna: semua $a_i$ kelipatan tiga.

Untuk menguji keprimaan $n$, cukup coba bagi dengan prima sampai $\sqrt{n}$ — kalau tidak
ada yang membagi, $n$ prima.

## Jebakan umum

- **Menganggap $1$ prima.** Bukan. Kalau $1$ dihitung prima, ketunggalan faktorisasi
  runtuh — dan bersamanya hampir seluruh teori bilangan.
- **Melupakan $2$.** Satu-satunya prima genap. Hampir semua soal bergaya "buktikan semua
  prima berbentuk…" punya $2$ sebagai kekecualian yang harus diperiksa terpisah.
- **Memakai lema Euclid pada bilangan komposit.** Itu langkah yang tampak sah tapi salah.
