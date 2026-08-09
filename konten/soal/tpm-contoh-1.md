---
id: tpm-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [teori-permainan]
bentuk: isian
kesulitan: 3
jawaban: "1"
---

## Soal

Sebuah tumpukan berisi $21$ batu. Dua pemain bergantian mengambil **$1$, $2$, atau $3$**
batu. Pemain yang **tidak bisa melangkah** — yaitu yang menghadapi tumpukan kosong —
dinyatakan kalah.

Berapa batu yang harus diambil pemain pertama pada langkah pertamanya supaya ia pasti
menang?

## Petunjuk

- Kerjakan mundur dari keadaan terkecil. Tandai tiap banyaknya batu dengan menang atau kalah bagi pemain yang mendapat giliran.
- Keadaan $0$ batu adalah kalah bagi yang mendapat giliran, sebab ia tidak bisa melangkah.
- Sebuah keadaan menang kalau ada satu langkah menuju keadaan kalah bagi lawan.

## Pembahasan

**Tandai tiap keadaan.** Sebut sebuah keadaan **P** kalau pemain yang mendapat giliran di
situ **kalah** (dengan permainan sempurna), dan **N** kalau ia **menang**.

Aturannya menurunkan diri sendiri:

- Keadaan tanpa langkah adalah **P**.
- Sebuah keadaan adalah **N** kalau ada **satu** langkah menuju keadaan P.
- Sebuah keadaan adalah **P** kalau **semua** langkahnya menuju keadaan N.

**Kerjakan mundur.**

| Batu | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|---|---|
| Tanda | P | N | N | N | P | N | N | N | P |

- $0$: tidak bisa melangkah → **P**.
- $1, 2, 3$: bisa mengambil semuanya dan meninggalkan $0$ (P) → **N**.
- $4$: langkahnya menuju $3, 2, 1$ — seluruhnya N → **P**.
- $5,6,7$: bisa menuju $4$ (P) → **N**.
- $8$: menuju $7,6,5$ — seluruhnya N → **P**.

**Polanya.** Keadaan P adalah kelipatan $4$:

$$n \equiv 0 \pmod 4$$

**Terapkan pada $21$.** Karena $21 = 4 \times 5 + 1$, keadaan awal adalah **N** — pemain
pertama menang. Untuk menang, ia harus meninggalkan keadaan P bagi lawannya, yaitu kelipatan
$4$ terdekat di bawah $21$, yaitu $20$. Jadi ia mengambil

$$21 - 20 = \boxed{1}$$

**Strateginya setelah itu.** Setiap kali lawan mengambil $k$ batu, pemain pertama mengambil
$4-k$ batu. Karena $1 \le k \le 3$, maka $1 \le 4-k \le 3$ — jadi langkah balasan itu selalu
sah. Dengan begitu tiap putaran menghabiskan tepat $4$ batu, dan tumpukan berjalan
$20 \to 16 \to 12 \to 8 \to 4 \to 0$. Lawan selalu menghadapi kelipatan $4$, dan akhirnya
menghadapi $0$.

**Membuktikan polanya, bukan sekadar menebaknya.** Dua hal harus ditunjukkan:

1. **Dari keadaan P, setiap langkah menuju N.** Dari $4m$, mengambil $k \in \{1,2,3\}$
   memberi $4m-k$, yang tidak habis dibagi $4$ — jadi N.
2. **Dari keadaan N, ada langkah menuju P.** Kalau $n = 4m + r$ dengan $1 \le r \le 3$,
   ambil $r$ batu dan tersisa $4m$ — yaitu P.

Kedua arah itu yang membuat pola tersebut benar-benar strategi, bukan pengamatan.

**Bentuk umumnya.** Kalau langkah yang boleh diambil adalah $1$ sampai $k$, keadaan P adalah
kelipatan $k+1$, dan strategi menangnya selalu "lengkapi menjadi $k+1$".

**Perhatikan aturan siapa yang kalah menentukan seluruh jawaban.** Kalau soalnya berbunyi
"yang mengambil batu terakhir kalah", pola P-nya bergeser dan jawabannya berbeda. Membaca
aturan itu dengan teliti adalah langkah pertama pada setiap soal permainan.
