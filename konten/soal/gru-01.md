---
id: gru-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-ruang]
bentuk: isian
kesulitan: 1
jawaban: "13"
---

## Soal

Sebuah balok berukuran $3 \times 4 \times 12$.

Tentukan panjang diagonal ruangnya.

## Petunjuk

- Diagonal ruang menghubungkan dua titik sudut yang tidak sebidang. Pecah perjalanannya menjadi dua langkah yang masing-masing bisa kamu hitung.
- Cari dulu diagonal alasnya, lalu pakai diagonal itu bersama tingginya.
- Pythagoras dipakai dua kali berturut-turut.

## Pembahasan

**Langkah pertama: diagonal alasnya.** Alasnya persegi panjang $3 \times 4$, sehingga

$$d_{\text{alas}}^2 = 3^2 + 4^2 = 25 \quad \Longrightarrow \quad d_{\text{alas}} = 5$$

**Langkah kedua: diagonal ruangnya.** Diagonal alas, rusuk tegak, dan diagonal ruang membentuk
segitiga siku-siku — sebab rusuk tegak tegak lurus **seluruh** bidang alas, termasuk diagonal
alas yang baru dihitung.

$$d^2 = 5^2 + 12^2 = 25 + 144 = 169 \quad \Longrightarrow \quad d = \boxed{13}$$

**Dengan rumus langsungnya.**

$$d = \sqrt{p^2 + l^2 + t^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$$

Rumus itu tidak lain kedua langkah tadi yang digabung — dan menurunkannya ulang lebih aman
daripada menghafalnya, sebab penurunannya sekaligus mengingatkan **mengapa** ketiganya boleh
dijumlahkan begitu saja.

### Yang membuat langkah kedua sah

Kunci penurunannya adalah kalimat "rusuk tegak tegak lurus seluruh bidang alas". Dari situ ia
tegak lurus **setiap** garis pada bidang itu — termasuk diagonal alas, yang arahnya tidak
sejajar rusuk mana pun.

Sifat itu yang membedakan bangun ruang dari bidang datar, dan ia dipakai di hampir setiap soal
ruang. Menyebutnya sekali di jawabanmu jauh lebih baik daripada menganggapnya jelas.

### Dua tripel yang bekerja berurutan

$(3,4,5)$ menghasilkan $5$, lalu $(5,12,13)$ menghasilkan $13$. Ukuran balok pada soal ini
dipilih supaya keduanya bulat — isyarat yang bisa kamu baca dari soalnya sendiri.

Balok lain dengan sifat serupa: $1 \times 2 \times 2$ (diagonal $3$), $2 \times 3 \times 6$
(diagonal $7$), dan $4 \times 4 \times 7$ (diagonal $9$). Balok yang ketiga rusuk **dan**
keempat diagonalnya semuanya bulat jauh lebih jarang, dan mencarinya adalah soal teori bilangan,
bukan soal geometri.

### Semua diagonal ruangnya sama panjang

Balok punya **empat** diagonal ruang, dan keempatnya sama panjang — masing-masing $13$ pada
soal ini — sebab rumusnya tidak membedakan dari titik sudut mana ia ditarik. Keempatnya juga
berpotongan di satu titik, yaitu pusat baloknya, dan saling membagi dua sama panjang.
