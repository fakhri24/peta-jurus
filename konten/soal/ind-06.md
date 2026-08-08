---
id: ind-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [induksi, barisan-deret]
bentuk: isian
kesulitan: 3
jawaban: "63"
---

## Soal

Barisan $a_1, a_2, a_3, \ldots$ didefinisikan oleh

$$a_1 = 1, \qquad a_{n+1} = 2a_n + 1$$

Tentukan nilai $a_6$.

## Petunjuk

- Barisan seperti ini didefinisikan bertahap: tiap suku dibangun dari suku sebelumnya.
- Hitung suku demi suku dari $a_1$ sampai $a_6$.
- Perhatikan pola yang muncul — tiap suku ternyata satu kurang dari pangkat $2$.

## Pembahasan

Hitung berurutan dari $a_1$:

$$a_1 = 1$$
$$a_2 = 2(1) + 1 = 3$$
$$a_3 = 2(3) + 1 = 7$$
$$a_4 = 2(7) + 1 = 15$$
$$a_5 = 2(15) + 1 = 31$$
$$a_6 = 2(31) + 1 = \boxed{63}$$

**Polanya terlihat:** $1, 3, 7, 15, 31, 63$ — masing-masing satu kurang dari
$2, 4, 8, 16, 32, 64$. Jadi dugaannya

$$a_n = 2^n - 1$$

Dugaan itu bisa dibuktikan dengan induksi. Basisnya $a_1 = 2^1 - 1 = 1$, cocok. Untuk
langkah induksi, andaikan $a_k = 2^k - 1$; maka

$$a_{k+1} = 2a_k + 1 = 2\left(2^k - 1\right) + 1 = 2^{k+1} - 2 + 1 = 2^{k+1} - 1$$

persis bentuk yang diminta. Jadi $a_n = 2^n - 1$ untuk setiap $n$, dan $a_6 = 64 - 1 = 63$
— cocok dengan perhitungan langsung.

**Inilah pasangan kerja yang khas.** Menghitung beberapa suku memberi **dugaan**; induksi
memberi **bukti**. Keduanya diperlukan: pola dari enam suku pertama bukan jaminan, dan
induksi tidak bisa dimulai tanpa rumus yang ditebak lebih dulu.

Untuk soal yang hanya menanyakan $a_6$, menghitung langsung sudah cukup. Tetapi kalau yang
ditanya $a_{100}$, rumus tertutupnya wajib — dan di situlah pola serta induksi menjadi
satu-satunya jalan.
