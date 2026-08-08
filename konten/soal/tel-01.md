---
id: tel-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [deret-teleskopik]
bentuk: isian
kesulitan: 1
jawaban: "99"
---

## Soal

Tentukan nilai dari

$$\left(2^2 - 1^2\right) + \left(3^2 - 2^2\right) + \left(4^2 - 3^2\right) + \cdots
+ \left(10^2 - 9^2\right)$$

## Petunjuk

- Jangan menghitung tiap kurung. Tulis semuanya berderet tanpa kurung dan perhatikan polanya.
- Tiap suku positif pada satu kurung punya pasangan negatif di kurung berikutnya.
- Yang tersisa hanya suku paling awal dan paling akhir.

## Pembahasan

Buka seluruh kurungnya dan tuliskan berderet:

$$-1^2 + 2^2 - 2^2 + 3^2 - 3^2 + 4^2 - \cdots - 9^2 + 10^2$$

Setiap $k^2$ untuk $k = 2, 3, \ldots, 9$ muncul **dua kali** dengan tanda berlawanan —
sekali sebagai suku positif di satu kurung, sekali sebagai suku negatif di kurung
berikutnya. Semuanya saling menghapus.

Yang tersisa hanya dua ujung:

$$10^2 - 1^2 = 100 - 1 = \boxed{99}$$

Bentuk umumnya sangat sederhana:

$$\sum_{k=1}^{n} \left[(k+1)^2 - k^2\right] = (n+1)^2 - 1^2$$

Deret ini adalah wujud teleskop yang paling telanjang — selisihnya sudah tertulis di soal,
jadi tidak ada yang perlu dipecah lebih dulu.

Ada bacaan lain yang menarik. Karena $(k+1)^2 - k^2 = 2k+1$, deret di atas sebenarnya
sama dengan $3 + 5 + 7 + \cdots + 19$ — jumlah bilangan ganjil dari $3$ sampai $19$. Dan
memang jumlahnya $99$, yaitu $10^2 - 1^2$.
