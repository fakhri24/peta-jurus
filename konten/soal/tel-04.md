---
id: tel-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [deret-teleskopik]
bentuk: isian
kesulitan: 3
jawaban: "9"
---

## Soal

Tentukan nilai dari

$$\frac{1}{\sqrt1+\sqrt2} + \frac{1}{\sqrt2+\sqrt3} + \cdots + \frac{1}{\sqrt{99}+\sqrt{100}}$$

## Petunjuk

- Bentuknya bukan pecahan biasa, tetapi gagasannya sama: ubah tiap suku menjadi selisih.
- Rasionalkan penyebutnya — kalikan dengan sekawannya, $\sqrt{k+1} - \sqrt{k}$.
- Penyebutnya akan menjadi $1$, dan yang tersisa persis selisih dua akar.

## Pembahasan

Rasionalkan tiap suku dengan mengalikan pembilang dan penyebut dengan sekawan penyebutnya:

$$\frac{1}{\sqrt{k}+\sqrt{k+1}} \cdot \frac{\sqrt{k+1}-\sqrt{k}}{\sqrt{k+1}-\sqrt{k}}
= \frac{\sqrt{k+1}-\sqrt{k}}{\left(\sqrt{k+1}\right)^2 - \left(\sqrt{k}\right)^2}$$

Penyebutnya menjadi selisih kuadrat:

$$= \frac{\sqrt{k+1}-\sqrt{k}}{(k+1) - k} = \sqrt{k+1} - \sqrt{k}$$

Penyebutnya lenyap seluruhnya — dan yang tersisa persis bentuk selisih yang dibutuhkan
teleskop.

Tuliskan deretnya:

$$\left(\sqrt2 - \sqrt1\right) + \left(\sqrt3 - \sqrt2\right) + \cdots
+ \left(\sqrt{100} - \sqrt{99}\right)$$

Bagian tengahnya saling menghapus, menyisakan

$$\sqrt{100} - \sqrt{1} = 10 - 1 = \boxed{9}$$

Bahwa hasilnya bilangan bulat memang disusun begitu: kedua ujungnya sengaja dipilih
kuadrat sempurna.

**Merasionalkan penyebut di sini bukan sekadar merapikan bentuk** — ia yang mengubah
pecahan menjadi selisih, dan tanpa itu tidak ada yang bisa diteleskopkan. Pola yang sama
bekerja pada bentuk lain berpenyebut akar:

$$\frac{1}{\sqrt{k+2}+\sqrt{k}} = \frac{\sqrt{k+2}-\sqrt{k}}{2}$$

dengan faktor $\frac12$ muncul karena selisih di dalam akarnya $2$ — persis seperti faktor
$\frac1d$ pada pecahan parsial.
