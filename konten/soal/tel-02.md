---
id: tel-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [deret-teleskopik]
bentuk: isian
kesulitan: 2
jawaban: "10/21"
---

## Soal

Tentukan nilai dari

$$\frac{1}{1 \cdot 3} + \frac{1}{3 \cdot 5} + \frac{1}{5 \cdot 7} + \cdots + \frac{1}{19 \cdot 21}$$

Tulis jawabanmu sebagai pecahan paling sederhana.

## Petunjuk

- Polanya sama seperti sebelumnya, tetapi kedua penyebutnya kini berjarak $2$, bukan $1$.
- Pecahan parsialnya: $\frac{1}{k(k+2)} = \frac12\left(\frac1k - \frac{1}{k+2}\right)$ — perhatikan faktor $\frac12$ di depan.
- Jangan lupa faktor itu saat menjumlahkan.

## Pembahasan

Penyebutnya berbentuk $k(k+2)$ dengan $k = 1, 3, 5, \ldots, 19$. Pecahan parsialnya:

$$\frac{1}{k(k+2)} = \frac{1}{2}\left(\frac{1}{k} - \frac{1}{k+2}\right)$$

Periksa: ruas kanan bernilai
$\frac12 \cdot \frac{(k+2)-k}{k(k+2)} = \frac12 \cdot \frac{2}{k(k+2)} = \frac{1}{k(k+2)}$.
Cocok.

**Faktor $\frac12$ itu yang paling sering terlupa.** Ia muncul karena selisih kedua
penyebutnya $2$, bukan $1$. Untuk jarak $d$, faktornya $\frac1d$.

Tuliskan deretnya:

$$\frac{1}{2}\left[\left(\frac11 - \frac13\right) + \left(\frac13 - \frac15\right)
+ \cdots + \left(\frac{1}{19} - \frac{1}{21}\right)\right]$$

Bagian tengahnya saling menghapus, menyisakan

$$\frac{1}{2}\left(1 - \frac{1}{21}\right) = \frac{1}{2} \cdot \frac{20}{21}
= \boxed{\frac{10}{21}}$$

Perhatikan bahwa di sini yang tersisa tetap **dua** suku, bukan empat — sebab $k$ hanya
menjelajahi bilangan ganjil, sehingga tiap $\frac{1}{k+2}$ selalu bertemu pasangannya.
Kalau $k$ menjelajahi **semua** bilangan dari $1$ sampai $19$, yang tersisa akan menjadi
empat suku: dua di awal dan dua di akhir.

Itu sebabnya menuliskan beberapa suku secara nyata lebih dapat diandalkan daripada
menerapkan rumus dari ingatan.
