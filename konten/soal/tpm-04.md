---
id: tpm-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [teori-permainan]
bentuk: isian
kesulitan: 4
jawaban: "1"
---

## Soal

Sebuah tumpukan berisi $22$ batu. Dua pemain bergantian mengambil $1$, $2$, atau $3$ batu.
Kali ini pemain yang mengambil **batu terakhir kalah**.

Berapa batu yang harus diambil pemain pertama pada langkah pertamanya supaya ia menang?

## Petunjuk

- Aturan kalahnya berbeda dari yang biasa, jadi jangan memakai pola kelipatan $4$ begitu saja. Tentukan ulang keadaan dasarnya.
- Kalau mengambil batu terakhir berarti kalah, maka meninggalkan **tepat satu** batu untuk lawan berarti menang.
- Kerjakan mundur dari keadaan $1$ batu, bukan dari $0$.

## Pembahasan

**Tetapkan keadaan dasarnya dengan benar.** Di sini yang mengambil batu terakhir kalah.
Karena itu, pemain yang menghadapi **tepat $1$ batu** terpaksa mengambilnya dan kalah.

$$n = 1 \ \Longrightarrow\ \textbf{P} \quad (\text{yang giliran kalah})$$

Perhatikan ini berbeda dari permainan biasa, yang keadaan dasarnya $n = 0$.

**Kerjakan mundur.**

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
|---|---|---|---|---|---|---|---|---|---|
| Tanda | P | N | N | N | P | N | N | N | P |

- $2,3,4$: bisa menyisakan tepat $1$ batu (P) → **N**.
- $5$: langkahnya menyisakan $4, 3, 2$ — seluruhnya N → **P**.
- $6,7,8$: bisa menyisakan $5$ (P) → **N**.

**Polanya.**

$$n \equiv 1 \pmod 4 \ \Longleftrightarrow\ \text{keadaan P}$$

**Terapkan pada $22$.** Karena $22 \equiv 2 \pmod 4$, keadaan awal adalah N — pemain pertama
menang. Ia harus meninggalkan keadaan P, yaitu bilangan berbentuk $4m+1$ terdekat di bawah
$22$, yaitu $21$:

$$22 - 21 = \boxed{1}$$

**Strategi selanjutnya.** Setelah lawan mengambil $k$ batu, ambil $4-k$ batu. Tiap putaran
menghabiskan $4$ batu, sehingga tumpukan berjalan $21 \to 17 \to 13 \to 9 \to 5 \to 1$.
Akhirnya lawan menghadapi $1$ batu dan terpaksa mengambilnya.

**Bandingkan dengan aturan biasa.**

| Aturan kalah | Keadaan P | Untuk $n=22$ |
|---|---|---|
| Tidak bisa melangkah kalah | $n \equiv 0 \pmod 4$ | ambil $2$ |
| Mengambil batu terakhir kalah | $n \equiv 1 \pmod 4$ | ambil $1$ |

Polanya bergeser tepat satu. Sebabnya sederhana: di aturan kedua, batu terakhir menjadi
"beban" yang harus dihindari, sehingga sasaran yang ditinggalkan bagi lawan bergeser dari
$0$ menjadi $1$.

**Kekeliruan yang paling sering** adalah memakai pola kelipatan $4$ tanpa membaca ulang
aturan kalahnya. Untuk $n = 22$ hal itu memberi jawaban $2$, yang justru menyerahkan
kemenangan kepada lawan.

Karena itu langkah pertama pada setiap soal permainan selalu sama: **tentukan keadaan yang
kalah, lalu kerjakan mundur dari sana** — bukan menyalin pola dari soal yang mirip.
