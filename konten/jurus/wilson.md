---
id: wilson
nama: Teorema Wilson
pilar: teori-bilangan
tahap: osn
prasyarat: [fermat-kecil]
contoh: [wl-contoh-1]
latihan: [wl-01, wl-02, wl-03, wl-04, wl-05, wl-06]
---

## Kapan dipakai

Soal memuat **faktorial $(p-1)!$ atau $(p-2)!$** berdampingan dengan **modulus prima $p$**. Ini adalah satu-satunya teorema utama yang menghubungkan faktorial dengan keterbagian prima.

Pemicu kedua: membuktikan bahwa $p$ adalah **bilangan prima** lewat kesetaraan penuh dua arah — $n$ prima jika dan hanya jika $(n-1)! \equiv -1 \pmod n$. Untuk $n > 4$ komposit, $(n-1)! \equiv 0 \pmod n$.

Pemicu ketiga: penyederhanaan bentuk faktorial parsial modulo $p = 4k+1$ atau $p = 4k+3$, seperti menghitung nilai $\left(\frac{p-1}{2}\right)! \pmod p$.

Pemicu keempat: soal menanyakan sisa pembagian faktorial berukuran besar seperti $96! \pmod{97}$ atau $95! \pmod{97}$, di mana sifat pasang-pasangan invers modulo $p$ menyisakan $-1$ atau $1$.

## Intinya

$p$ prima **tepat ketika**

$$(p-1)! \equiv -1 \pmod p$$

Ini satu-satunya uji keprimaan yang berupa kesetaraan penuh — berlaku dua arah, tidak
seperti Fermat Kecil.

Alasannya elegan: kalikan seluruh $1, 2, \dots, p-1$. Setiap unsur berpasangan dengan
inversnya, dan hasil kali tiap pasangan adalah $1$. Yang tersisa hanya unsur yang menjadi
invers dirinya sendiri, yaitu $x^2 \equiv 1$, yaitu $x = 1$ dan $x = p-1$. Hasil kalinya
$1 \cdot (p-1) \equiv -1$.

Secara praktis Wilson jarang dipakai untuk menguji prima — untuk itu ia terlalu lambat.
Gunanya adalah **menyederhanakan faktorial dalam kongruensi**.

## Jebakan umum

- **Memakainya pada modulus komposit.** Untuk $n$ komposit dan $n > 4$, justru
  $(n-1)! \equiv 0 \pmod n$.
- **Salah mengingat ruas kanannya.** $-1$, bukan $1$. Modulo $p$, nilai $-1$ sama dengan
  $p - 1$.
- **Lupa kasus $p = 2$.** Di situ $(p-1)! = 1$ dan $-1 \equiv 1 \pmod 2$, jadi tetap
  benar — tapi patut dicek terpisah kalau soalnya rewel.
