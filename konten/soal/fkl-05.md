---
id: fkl-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [fermat-kecil]
bentuk: isian
kesulitan: 3
jawaban: "8"
---

## Soal

Tentukan sisa pembagian $3^{2026}$ oleh $17$.

## Petunjuk

- Eksponennya terlalu besar untuk dihitung langsung. Periksa dulu sifat modulusnya — itu menentukan panjang siklus yang boleh kamu pakai.
- $17$ prima, jadi Fermat Kecil memberi $3^{16} \equiv 1 \pmod{17}$. Potong eksponennya modulo $16$.
- Setelah tersisa $3^{10}$, hitung dengan mengkuadratkan berulang — dan perhatikan bahwa $3^8$ memberi nilai yang sangat mudah dipakai.

## Pembahasan

Karena $17$ prima dan $17 \nmid 3$, Teorema Fermat Kecil memberi

$$3^{16} \equiv 1 \pmod{17}$$

**Potong eksponennya.** Bagi $2026$ oleh $16$:

$$2026 = 16 \times 126 + 10$$

sehingga

$$3^{2026} = \left(3^{16}\right)^{126} \times 3^{10} \equiv 3^{10} \pmod{17}$$

**Hitung $3^{10}$ modulo $17$** dengan mengkuadratkan berulang:

$$3^2 = 9$$
$$3^4 = 81 = 4 \times 17 + 13 \equiv 13 \equiv -4$$
$$3^8 \equiv (-4)^2 = 16 \equiv -1$$

Nilai $-1$ itu yang membuat sisanya mudah. Karena $10 = 8 + 2$:

$$3^{10} = 3^8 \times 3^2 \equiv (-1) \times 9 = -9 \equiv 17 - 9 = \boxed{8} \pmod{17}$$

Periksa arah lain: dari $3^8 \equiv -1$ diperoleh $3^{16} \equiv 1$, cocok dengan Fermat
Kecil. Angka $8$ di sini adalah **orde** $3$ modulo $17$ yang setengah jalan — pangkat
terkecil yang memberi $-1$.

Memakai wakil negatif seperti $-4$ dan $-1$ alih-alih $13$ dan $16$ memangkas banyak
perhitungan. Setiap kali sebuah sisa melewati separuh modulus, menggantinya dengan wakil
negatif hampir selalu menguntungkan.
