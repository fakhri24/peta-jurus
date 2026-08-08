---
id: fkl-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [fermat-kecil]
bentuk: isian
kesulitan: 2
jawaban: "1"
---

## Soal

Tentukan sisa pembagian $2^{100}$ oleh $101$.

## Petunjuk

- Periksa dulu apakah modulusnya prima. Itu menentukan alat mana yang boleh dipakai.
- $101$ prima dan $101 \nmid 2$, jadi Fermat Kecil berlaku dengan eksponen $p - 1$.
- Bandingkan eksponen yang diminta dengan $p - 1$. Kadang keduanya persis sama.

## Pembahasan

Periksa keprimaan $101$: cukup diuji pembagi sampai $\sqrt{101} \approx 10{,}05$, yaitu
$2, 3, 5, 7$. Tidak satu pun membaginya, jadi $101$ prima.

Karena $101$ prima dan $101 \nmid 2$, Teorema Fermat Kecil memberi

$$2^{101 - 1} = 2^{100} \equiv 1 \pmod{101}$$

Eksponen yang diminta persis $p - 1$, jadi tidak ada yang perlu dipotong sama sekali.

Sisanya adalah $\boxed{1}$.

Soal seperti ini menguji satu hal saja: apakah kamu memeriksa keprimaan modulusnya sebelum
mulai menghitung. Kalau $101$ diganti $100$, Fermat Kecil tidak berlaku dan jawabannya
sama sekali berbeda — di sana yang dipakai Teorema Euler dengan $\varphi(100) = 40$.

Perhatikan juga syarat kedua, $p \nmid a$. Untuk $a = 101$ misalnya, $101^{100} \equiv 0$,
bukan $1$.
