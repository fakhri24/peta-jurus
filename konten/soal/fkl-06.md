---
id: fkl-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [fermat-kecil]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa $a^{13} \equiv a \pmod{2730}$ untuk setiap bilangan bulat $a$.

## Petunjuk

- Modulusnya besar dan komposit. Pecah dulu atas faktor primanya, lalu tangani satu per satu.
- $2730 = 2 \times 3 \times 5 \times 7 \times 13$ — lima prima berbeda, semuanya berpangkat satu.
- Untuk tiap prima $p$, periksa apakah $p - 1$ membagi $12$. Kalau ya, Fermat Kecil langsung memberi hasilnya.

## Pembahasan

Faktorkan modulusnya:

$$2730 = 2 \times 3 \times 5 \times 7 \times 13$$

Kelima primanya berbeda dan berpangkat satu. Karena itu, cukup dibuktikan

$$a^{13} \equiv a \pmod p$$

untuk masing-masing $p \in \{2, 3, 5, 7, 13\}$ — bilangan yang habis dibagi kelima prima
itu otomatis habis dibagi hasil kalinya, sebab kelimanya saling asing.

**Kunci perhitungannya.** Daftar $p - 1$ untuk kelima prima:

$$2 - 1 = 1, \quad 3 - 1 = 2, \quad 5 - 1 = 4, \quad 7 - 1 = 6, \quad 13 - 1 = 12$$

Kelimanya membagi $12$. Itu bukan kebetulan — modulusnya memang disusun demikian.

**Buktikan untuk satu prima $p$.** Ada dua kasus.

*Kasus $p \mid a$.* Maka $a \equiv 0 \pmod p$, sehingga $a^{13} \equiv 0 \equiv a$.
Terpenuhi.

*Kasus $p \nmid a$.* Fermat Kecil memberi $a^{p-1} \equiv 1 \pmod p$. Karena
$(p-1) \mid 12$, tulis $12 = (p-1)k$ untuk suatu bilangan asli $k$. Maka

$$a^{12} = \left(a^{p-1}\right)^{k} \equiv 1^{k} = 1 \pmod p$$

Kalikan kedua ruas dengan $a$:

$$a^{13} \equiv a \pmod p$$

Kedua kasus memberi kesimpulan yang sama, jadi $a^{13} \equiv a \pmod p$ berlaku untuk
**setiap** bilangan bulat $a$ dan setiap $p$ di daftar itu.

**Gabungkan.** Kelima prima itu berbeda, jadi saling asing berpasangan. Karena masing-
masing membagi $a^{13} - a$, hasil kalinya juga membagi:

$$2730 \mid a^{13} - a \quad\Longrightarrow\quad a^{13} \equiv a \pmod{2730}$$

$\blacksquare$

Perhatikan bahwa kasus $p \mid a$ tidak boleh dilewati. Fermat Kecil mensyaratkan
$p \nmid a$; tanpa memisahkan kasusnya, pembuktian ini hanya berlaku untuk sebagian
bilangan bulat.

Konstruksi yang sama menghasilkan keluarga pernyataan serupa. Untuk eksponen $n$, ambil
modulus berupa hasil kali seluruh prima $p$ dengan $(p-1) \mid (n-1)$ — misalnya
$a^7 \equiv a \pmod{42}$, sebab $42 = 2 \times 3 \times 7$ dan $1, 2, 6$ semuanya membagi
$6$.

## Rubrik

- Memfaktorkan $2730$ menjadi lima prima berbeda berpangkat satu
- Menyatakan bahwa cukup dibuktikan modulo tiap prima, **dengan alasan** kelimanya saling asing
- Memeriksa bahwa $p - 1$ membagi $12$ untuk kelima prima
- Menangani kasus $p \mid a$ secara terpisah
- Menerapkan Fermat Kecil pada kasus $p \nmid a$, memakai $12 = (p-1)k$ untuk memperoleh $a^{12} \equiv 1$
- Menggabungkan kelima keterbagian menjadi $2730 \mid a^{13} - a$
