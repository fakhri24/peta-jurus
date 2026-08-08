---
id: tel-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [deret-teleskopik]
bentuk: isian
kesulitan: 2
jawaban: "9/10"
jawaban_alt: ["0,9", "0.9"]
---

## Soal

Tentukan nilai dari

$$\frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \frac{1}{3 \cdot 4} + \cdots + \frac{1}{9 \cdot 10}$$

Tulis jawabanmu sebagai pecahan paling sederhana.

## Petunjuk

- Menjumlahkan sembilan pecahan satu per satu bisa, tetapi susunan penyebutnya terlalu teratur untuk kebetulan.
- Tiap suku bisa ditulis sebagai **selisih** dua pecahan: $\frac{1}{k(k+1)} = \frac1k - \frac{1}{k+1}$.
- Tulis beberapa suku pertama dalam bentuk selisih itu dan lihat apa yang saling menghapus.

## Pembahasan

Pecah tiap suku menjadi selisih:

$$\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$$

Periksa: ruas kanan bernilai $\frac{(k+1) - k}{k(k+1)} = \frac{1}{k(k+1)}$. Cocok.

Tuliskan seluruh deretnya dalam bentuk itu:

$$\left(\frac11 - \frac12\right) + \left(\frac12 - \frac13\right) + \left(\frac13 - \frac14\right)
+ \cdots + \left(\frac19 - \frac{1}{10}\right)$$

Sekarang perhatikan apa yang terjadi. Suku $-\frac12$ pada kurung pertama menghapus
$+\frac12$ pada kurung kedua; $-\frac13$ menghapus $+\frac13$; dan seterusnya. **Seluruh
bagian tengahnya lenyap**, menyisakan hanya dua ujung:

$$\frac{1}{1} - \frac{1}{10} = \frac{10 - 1}{10} = \boxed{\frac{9}{10}}$$

Itulah yang disebut deret teleskopik — seperti teleskop lipat yang menyusut menjadi dua
ujungnya saja.

Bentuk umumnya:

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$

Untuk $n = 9$ memang $\frac{9}{10}$.

**Kebiasaan yang menyelamatkan:** tulis tiga suku pertama dan dua suku terakhir secara
nyata sebelum menyimpulkan apa yang menghapus apa. Pada deret yang selisihnya berjarak
lebih dari satu, yang tersisa bukan dua suku melainkan lebih — dan menebaknya tanpa
menuliskan hampir selalu meleset.
