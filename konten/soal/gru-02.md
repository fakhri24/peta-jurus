---
id: gru-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-ruang]
bentuk: isian
kesulitan: 2
jawaban: "216"
---

## Soal

Sebuah kubus mempunyai diagonal ruang sepanjang $6\sqrt{3}$.

Tentukan volume kubus itu.

## Petunjuk

- Volume kubus ditentukan seluruhnya oleh panjang rusuknya, jadi carilah rusuknya lebih dulu.
- Untuk kubus berusuk $a$, diagonal ruangnya $a\sqrt{3}$.
- Bandingkan $a\sqrt3$ dengan $6\sqrt3$.

## Pembahasan

**Diagonal ruang kubus.** Untuk kubus berusuk $a$, rumus diagonal ruang balok memberi

$$d = \sqrt{a^2 + a^2 + a^2} = \sqrt{3a^2} = a\sqrt{3}$$

**Cari rusuknya.**

$$a\sqrt3 = 6\sqrt3 \quad \Longrightarrow \quad a = 6$$

**Hitung volumenya.**

$$V = a^3 = 6^3 = \boxed{216}$$

### Bentuk $\sqrt3$ itu isyarat, bukan hiasan

Soal menuliskan diagonalnya sebagai $6\sqrt3$, bukan $10{,}39$. Bentuk berakar seperti itu
hampir selalu isyarat bahwa jawabannya dirancang bulat — dan pada kubus, $\sqrt3$ khususnya
menandai diagonal **ruang**, sedangkan $\sqrt2$ menandai diagonal **bidang**.

| Ruas pada kubus berusuk $a$ | Panjangnya |
|---|---|
| Rusuk | $a$ |
| Diagonal bidang (pada satu sisi) | $a\sqrt2$ |
| Diagonal ruang | $a\sqrt3$ |

Kalau soal memberi $6\sqrt2$ alih-alih $6\sqrt3$, yang dimaksud diagonal sisinya, rusuknya
tetap $6$ — tetapi kalau kamu memakai rumus yang salah, rusuknya keluar $\sqrt6$ dan seluruh
jawabannya melenceng.

### Periksa dengan angka

Rusuk $6$ memberi diagonal ruang $\sqrt{36+36+36} = \sqrt{108}$. Dan
$\sqrt{108} = \sqrt{36 \times 3} = 6\sqrt3$ ✓.

Kebiasaan menyederhanakan $\sqrt{108}$ menjadi $6\sqrt3$ — bukan membiarkannya sebagai
$\sqrt{108}$ — memudahkan pemeriksaan seperti ini, dan soal isian biasanya memang menuntut
bentuk yang sudah sederhana.

### Bandingkan ketiga besarannya

Untuk kubus ini: rusuk $6$, luas permukaan $6 \times 36 = 216$, dan volume $216$. Keduanya
kebetulan sama — kebetulan yang **hanya** terjadi pada kubus berusuk $6$, sebab
$6a^2 = a^3$ tepat ketika $a = 6$.

Soal olimpiade kadang memakai kebetulan seperti ini sebagai jebakan halus: angka yang sama
muncul dua kali, dan siswa tergoda menyimpulkan hubungan yang sebenarnya tidak umum.
