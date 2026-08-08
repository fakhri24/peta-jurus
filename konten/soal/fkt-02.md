---
id: fkt-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [faktorisasi]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Tentukan akar terbesar dari persamaan

$$x^3 - 6x^2 + 11x - 6 = 0$$

## Petunjuk

- Untuk polinomial berkoefisien bulat, akar bulatnya pasti membagi suku konstanta. Di sini konstantanya $-6$.
- Coba $x = 1$. Kalau bernilai nol, maka $(x-1)$ faktornya.
- Setelah $(x-1)$ dikeluarkan, sisanya kuadrat yang bisa difaktorkan biasa.

## Pembahasan

**Cari satu akar.** Kalau ada akar bulat, ia harus membagi konstanta $-6$, jadi
kandidatnya $\pm 1, \pm 2, \pm 3, \pm 6$.

Coba $x = 1$:

$$1 - 6 + 11 - 6 = 0$$

Berhasil, jadi $(x-1)$ merupakan faktor.

**Bagi.** Membagi $x^3-6x^2+11x-6$ oleh $(x-1)$ memberi

$$x^3 - 6x^2 + 11x - 6 = (x-1)\left(x^2 - 5x + 6\right)$$

**Faktorkan sisanya.** Cari dua bilangan berjumlah $-5$ dan berhasil kali $6$: yaitu
$-2$ dan $-3$.

$$x^2 - 5x + 6 = (x-2)(x-3)$$

Sehingga

$$(x-1)(x-2)(x-3) = 0$$

Akarnya $1$, $2$, dan $3$; yang terbesar adalah $\boxed{3}$.

Pemeriksaan cepat lewat Vieta: jumlah akarnya harus $-\frac{-6}{1} = 6$, dan memang
$1+2+3 = 6$. Hasil kalinya harus $-\frac{-6}{1} = 6$, dan memang $1 \times 2 \times 3 = 6$.

Aturan "akar bulat membagi konstanta" itu menyaring kandidat dari tak hingga menjadi
delapan. Tanpa itu, mencari akar kubik dengan tangan hampir mustahil.
