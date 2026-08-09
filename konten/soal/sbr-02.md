---
id: sbr-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [stars-and-bars]
bentuk: isian
kesulitan: 2
jawaban: "165"
---

## Soal

Ada berapa penyelesaian bilangan bulat **positif** dari persamaan

$$x_1 + x_2 + x_3 + x_4 = 12\ ?$$

(Bilangan bulat positif berarti $x_i \ge 1$.)

## Petunjuk

- Bedakan syarat ini dari yang biasa: tiap peubah sekarang harus paling sedikit $1$, bukan boleh $0$.
- Sisihkan dulu satu untuk tiap peubah, lalu bagikan sisanya tanpa syarat apa pun.
- Setelah disisihkan, berapa yang tersisa untuk dibagikan bebas?

## Pembahasan

**Sisihkan dulu jatah wajibnya.** Karena tiap peubah harus paling sedikit $1$, berikan lebih
dulu satu untuk masing-masing. Terpakai $4$, dan yang tersisa

$$12 - 4 = 8$$

**Ubah menjadi soal tanpa syarat.** Tulis $y_i = x_i - 1$. Syarat $x_i \ge 1$ berubah
menjadi $y_i \ge 0$, dan persamaannya menjadi

$$y_1 + y_2 + y_3 + y_4 = 8, \qquad y_i \ge 0$$

Padanan $x_i \leftrightarrow y_i$ ini satu-satu: tiap penyelesaian yang lama memberi tepat
satu yang baru, dan sebaliknya. Jadi kedua persoalan punya jawaban yang sama banyaknya.

**Terapkan rumusnya** dengan $n = 8$ dan $k = 4$:

$$\binom{8+4-1}{4-1} = \binom{11}{3} = \frac{11 \times 10 \times 9}{3 \times 2 \times 1} = \boxed{165}$$

**Cara langsung lewat gambar.** Bayangkan $12$ bintang berjajar. Untuk memecahnya menjadi
$4$ kelompok yang **semuanya tak kosong**, sekatnya harus diletakkan di **celah antar
bintang** — bukan di ujung dan tidak dua sekat pada celah yang sama.

$$\star\ \_\ \star\ \_\ \star\ \_\ \cdots\ \_\ \star$$

Ada $12 - 1 = 11$ celah, dan dipilih $3$ untuk sekat:

$$\binom{11}{3} = 165$$

Cocok. Dari sini terbaca rumus umumnya untuk penyelesaian positif:

$$\binom{n-1}{k-1}$$

**Membedakan kedua rumus.** Keduanya sering tertukar, padahal bedanya cuma satu kata di
soal:

| Syarat | Rumus | Gambaran |
|---|---|---|
| $x_i \ge 0$ | $\dbinom{n+k-1}{k-1}$ | sekat boleh di mana saja, termasuk berdempetan |
| $x_i \ge 1$ | $\dbinom{n-1}{k-1}$ | sekat hanya di celah antar bintang, satu celah satu sekat |

**Periksa kewajarannya.** Untuk $n = 12$ dan $k = 4$, syarat tak negatif memberi
$\binom{15}{3} = 455$ — jauh lebih besar dari $165$, sebagaimana seharusnya, sebab
syaratnya lebih longgar.
