---
id: fkl-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [fermat-kecil]
bentuk: isian
kesulitan: 2
jawaban: "8"
---

## Soal

Tentukan sisa pembagian $2^{2019}$ oleh $13$.

## Petunjuk

- Coba hitung beberapa pangkat $2$ modulo $13$ — atau langsung pakai teorema.
- $13$ prima dan $13 \nmid 2$, jadi Teorema Fermat Kecil berlaku: $2^{12} \equiv 1 \pmod{13}$.
- Sekarang bagi eksponen $2019$ dengan $12$ — bukan dengan $13$.

## Pembahasan

Karena $13$ prima dan $13 \nmid 2$, Teorema Fermat Kecil memberi

$$2^{12} \equiv 1 \pmod{13}$$

Sekarang potong eksponennya modulo $12$:

$$2019 = 12 \times 168 + 3$$

sehingga

$$2^{2019} = \left(2^{12}\right)^{168} \cdot 2^3 \equiv 1^{168} \cdot 8 = 8 \pmod{13}$$

Sisanya $\boxed{8}$.

Perhatikan pergantian modulusnya, karena di sinilah orang paling sering tergelincir:
**bilangan pokok dihitung modulo $13$, tetapi eksponen dihitung modulo $12$.** Membagi
$2019$ dengan $13$ akan memberi jawaban yang salah dan tetap terlihat masuk akal.
