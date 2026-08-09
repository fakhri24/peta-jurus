---
id: rek-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [rekursi]
bentuk: isian
kesulitan: 4
jawaban: "3281"
---

## Soal

Barisan $a_0, a_1, a_2, \dots$ memenuhi

$$a_0 = 1, \qquad a_1 = 1, \qquad a_n = 2a_{n-1} + 3a_{n-2} \quad (n \ge 2)$$

Tentukan $a_8$.

## Petunjuk

- Menghitung suku demi suku sudah cukup untuk menjawab, tetapi rumus tertutupnya membuat pemeriksaan jauh lebih mudah.
- Untuk rekurens berbentuk $a_n = p\,a_{n-1} + q\,a_{n-2}$, susun persamaan karakteristik $x^2 = px + q$.
- Setelah akar-akarnya diperoleh, tentukan kedua tetapannya dari $a_0$ dan $a_1$ — dan periksa rumusnya pada suku yang sudah kamu hitung.

## Pembahasan

**Cara pertama — hitung suku demi suku.**

$$a_2 = 2(1) + 3(1) = 5$$
$$a_3 = 2(5) + 3(1) = 13$$
$$a_4 = 2(13) + 3(5) = 41$$
$$a_5 = 2(41) + 3(13) = 121$$
$$a_6 = 2(121) + 3(41) = 365$$
$$a_7 = 2(365) + 3(121) = 1093$$
$$a_8 = 2(1093) + 3(365) = 2186 + 1095 = \boxed{3281}$$

**Cara kedua — rumus tertutup.** Susun persamaan karakteristiknya:

$$x^2 = 2x + 3 \quad\Longrightarrow\quad x^2 - 2x - 3 = 0 \quad\Longrightarrow\quad (x-3)(x+1) = 0$$

Akarnya $r_1 = 3$ dan $r_2 = -1$, keduanya berbeda, sehingga

$$a_n = A \cdot 3^{\,n} + B \cdot (-1)^{\,n}$$

**Tentukan $A$ dan $B$ dari kasus dasarnya.**

$$n = 0: \quad A + B = 1$$
$$n = 1: \quad 3A - B = 1$$

Jumlahkan kedua persamaan: $4A = 2$, sehingga $A = \frac12$ dan $B = \frac12$.

$$a_n = \frac{3^{\,n} + (-1)^{\,n}}{2}$$

**Periksa rumusnya sebelum dipakai.** Untuk $n = 2$: $\frac{9+1}{2} = 5$ ✓. Untuk $n = 3$:
$\frac{27-1}{2} = 13$ ✓. Untuk $n = 4$: $\frac{81+1}{2} = 41$ ✓.

**Hitung $a_8$.**

$$a_8 = \frac{3^8 + (-1)^8}{2} = \frac{6561 + 1}{2} = \frac{6562}{2} = 3281$$

Cocok dengan cara pertama.

**Memeriksa rumus tertutup pada suku yang sudah diketahui bukan kelengkapan yang bisa
dilewati.** Kekeliruan tanda saat menyelesaikan $A$ dan $B$ tidak akan terlihat di langkah
mana pun berikutnya; ia baru muncul sebagai jawaban akhir yang salah. Mencocokkan dengan
dua atau tiga suku pertama menangkapnya dengan segera.

**Bentuk rumusnya juga bisa dibaca.** Suku $(-1)^n$ berayun antara $+1$ dan $-1$, sehingga

$$a_n = \frac{3^n \pm 1}{2}$$

dengan tanda $+$ untuk $n$ genap dan $-$ untuk $n$ ganjil. Periksa daftarnya: $1, 1, 5, 13,
41, 121, 365, 1093, 3281$ — memang selalu bilangan bulat, sebab $3^n$ selalu ganjil sehingga
$3^n \pm 1$ selalu genap.

**Kalau akar karakteristiknya kembar,** bentuk $A r^n + B r^n$ tidak lagi cukup — ia hanya
punya satu tetapan yang berdiri sendiri, sedangkan dua kasus dasar menuntut dua. Bentuk yang
benar di situ adalah $(A + Bn)r^n$.
