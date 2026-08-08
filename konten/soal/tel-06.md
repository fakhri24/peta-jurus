---
id: tel-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [deret-teleskopik, induksi]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa untuk setiap bilangan asli $n$,

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = \frac{n}{n+1}$$

## Petunjuk

- Ada dua jalur yang sama sahnya: mengubah tiap suku jadi selisih lalu menjumlahkan, atau membuktikan rumusnya bertahap dari $n$ ke $n+1$.
- Jalur teleskop: buktikan dulu $\frac{1}{k(k+1)} = \frac1k - \frac{1}{k+1}$, lalu jumlahkan dan tunjukkan apa yang menghapus apa.
- Jalur induksi: pada langkah $k \to k+1$, tambahkan suku $\frac{1}{(k+1)(k+2)}$ ke hipotesis lalu sederhanakan.

## Pembahasan

### Cara pertama: teleskop

**Buktikan pecahan parsialnya lebih dulu.**

$$\frac{1}{k} - \frac{1}{k+1} = \frac{(k+1) - k}{k(k+1)} = \frac{1}{k(k+1)}$$

**Jumlahkan.** Substitusikan bentuk itu ke seluruh deret:

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = \sum_{k=1}^{n}\left(\frac{1}{k} - \frac{1}{k+1}\right)$$

Tuliskan sukunya secara nyata:

$$\left(\frac11 - \frac12\right) + \left(\frac12 - \frac13\right) + \cdots
+ \left(\frac1n - \frac{1}{n+1}\right)$$

Untuk setiap $j$ dengan $2 \le j \le n$, suku $-\frac1j$ muncul pada kurung ke-$(j-1)$ dan
suku $+\frac1j$ muncul pada kurung ke-$j$. Keduanya saling menghapus. Yang tidak punya
pasangan hanya $+\frac11$ pada kurung pertama dan $-\frac{1}{n+1}$ pada kurung terakhir.

Maka

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = 1 - \frac{1}{n+1} = \frac{n+1-1}{n+1} = \frac{n}{n+1}$$

### Cara kedua: induksi matematika

**Basis.** Untuk $n = 1$: ruas kiri $= \frac{1}{1 \cdot 2} = \frac12$, dan ruas kanan
$= \frac{1}{2}$. Cocok.

**Langkah induksi.** Andaikan benar untuk $n = m$, yaitu

$$\sum_{k=1}^{m} \frac{1}{k(k+1)} = \frac{m}{m+1}$$

Tinjau $n = m+1$. Tambahkan suku berikutnya ke kedua ruas hipotesis:

$$\sum_{k=1}^{m+1} \frac{1}{k(k+1)} = \frac{m}{m+1} + \frac{1}{(m+1)(m+2)}$$

Satukan dengan penyebut $(m+1)(m+2)$:

$$= \frac{m(m+2) + 1}{(m+1)(m+2)} = \frac{m^2+2m+1}{(m+1)(m+2)} = \frac{(m+1)^2}{(m+1)(m+2)}
= \frac{m+1}{m+2}$$

Itu persis bentuk yang diminta untuk $n = m+1$.

Kedua langkah terpenuhi, jadi pernyataannya berlaku untuk setiap bilangan asli $n$.
$\blacksquare$

Perbedaan keduanya layak diperhatikan. **Induksi hanya bisa memeriksa rumus yang sudah
kamu punya**; ia tidak menemukannya. Teleskop justru **menghasilkan** rumusnya — dan itu
yang kamu butuhkan di ruang ujian, ketika tidak ada yang memberitahu jawabannya lebih dulu.

## Rubrik

- Jalur teleskop: membuktikan $\frac{1}{k(k+1)} = \frac1k - \frac{1}{k+1}$, bukan sekadar memakainya
- Jalur teleskop: menuliskan deretnya secara nyata dan menjelaskan suku mana yang berpasangan
- Jalur teleskop: menyatakan hanya dua ujung yang tersisa, lalu menyederhanakan menjadi $\frac{n}{n+1}$
- **Atau**, jalur induksi: memeriksa basis $n = 1$
- Jalur induksi: menuliskan hipotesis dan menambahkan suku ke-$(m+1)$ padanya
- Jalur induksi: menyederhanakan sampai berbentuk $\frac{m+1}{m+2}$, dengan pemfaktoran $m^2+2m+1 = (m+1)^2$ ditulis eksplisit
