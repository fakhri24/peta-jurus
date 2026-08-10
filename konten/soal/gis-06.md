---
id: gis-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [garis-istimewa]
bentuk: uraian
kesulitan: 4
---

## Soal

Misalkan $m_a$, $m_b$, $m_c$ berturut-turut panjang garis berat segitiga $ABC$ dari titik
sudut $A$, $B$, dan $C$, sedangkan $a$, $b$, $c$ panjang sisi di hadapan ketiga titik sudut
itu.

**(a)** Buktikan bahwa

$$m_a^2 + m_b^2 + m_c^2 = \frac{3}{4}\left(a^2 + b^2 + c^2\right)$$

**(b)** Buktikan bahwa jika $m_b = m_c$ maka $b = c$.

## Petunjuk

- Panjang tiap garis berat sudah bisa dinyatakan hanya dengan ketiga sisi. Tulis ketiganya, jangan cuma satu.
- Rumusnya $4m_a^2 = 2b^2 + 2c^2 - a^2$. Ketiga bentuknya diperoleh dengan memutar peran huruf, dan bagian (a) tinggal menjumlahkan.
- Untuk (b), tulis $4m_b^2$ dan $4m_c^2$ lalu samakan. Suku yang memuat $a$ akan lenyap dengan sendirinya.

## Pembahasan

**Modal tunggal untuk kedua bagian.** Panjang garis berat dari $A$ ke titik tengah $BC$:

$$4 m_a^2 = 2b^2 + 2c^2 - a^2$$

Rumus ini simetris terhadap $b$ dan $c$ — dan memang harus, karena menukar $B$ dengan $C$
tidak mengubah garis beratnya. Dua bentuk lainnya diperoleh dengan memutar peran hurufnya:

$$4 m_b^2 = 2c^2 + 2a^2 - b^2, \qquad 4 m_c^2 = 2a^2 + 2b^2 - c^2$$

### Bagian (a)

Jumlahkan ketiganya:

$$4\left(m_a^2 + m_b^2 + m_c^2\right)
= \left(2b^2 + 2c^2 - a^2\right) + \left(2c^2 + 2a^2 - b^2\right) + \left(2a^2 + 2b^2 - c^2\right)$$

Kumpulkan menurut hurufnya. Suku $a^2$ muncul sebagai $-a^2 + 2a^2 + 2a^2 = 3a^2$, dan
karena bentuknya simetris hal yang sama terjadi pada $b^2$ dan $c^2$:

$$4\left(m_a^2 + m_b^2 + m_c^2\right) = 3a^2 + 3b^2 + 3c^2$$

$$m_a^2 + m_b^2 + m_c^2 = \frac{3}{4}\left(a^2 + b^2 + c^2\right) \qquad \blacksquare$$

### Bagian (b)

Andaikan $m_b = m_c$. Kuadratkan dan kalikan $4$:

$$2c^2 + 2a^2 - b^2 = 2a^2 + 2b^2 - c^2$$

Suku $2a^2$ ada di kedua ruas dan lenyap — dan itu bukan kebetulan, melainkan tanda bahwa
sisi $BC$ tidak berperan apa-apa dalam perbandingan kedua garis berat ini:

$$2c^2 - b^2 = 2b^2 - c^2 \quad \Longrightarrow \quad 3c^2 = 3b^2 \quad \Longrightarrow \quad b^2 = c^2$$

Karena $b$ dan $c$ panjang, keduanya positif, sehingga $b = c$ $\blacksquare$

Panjang sisi selalu positif, jadi dari $b^2 = c^2$ boleh langsung disimpulkan $b = c$ —
kemungkinan $b = -c$ tidak ada. Langkah kecil ini tetap perlu ditulis; menghilangkannya
adalah bentuk paling umum dari lompatan yang dipotong nilainya.

### Periksa bagian (a) pada segitiga 13-14-15

Dengan $a = 14$, $b = 13$, $c = 15$:

$$4m_a^2 = 2(169) + 2(225) - 196 = 592, \qquad m_a^2 = 148$$

$$4m_b^2 = 2(225) + 2(196) - 169 = 673, \qquad m_b^2 = 168{,}25$$

$$4m_c^2 = 2(196) + 2(169) - 225 = 505, \qquad m_c^2 = 126{,}25$$

$$m_a^2 + m_b^2 + m_c^2 = 148 + 168{,}25 + 126{,}25 = 442{,}5$$

Sedangkan $\tfrac{3}{4}(169 + 196 + 225) = \tfrac{3}{4}(590) = 442{,}5$ ✓

### Apa yang sebenarnya dikatakan bagian (a)

Ruas kanannya tidak memuat sudut sama sekali. Jadi identitas ini berlaku untuk segitiga apa
pun — lancip, siku-siku, tumpul — dan jumlah kuadrat garis beratnya **selalu** tepat tiga
perempat jumlah kuadrat sisinya. Nisbah itu tetap, tidak peduli bentuknya.

Akibat yang sering dipakai: ketiga garis berat tidak pernah bisa dibuat sekaligus sangat
panjang, karena jumlah kuadratnya terkunci pada sisinya.

### Bagian (b) dibaca terbalik

Yang dibuktikan: **dua garis berat sama panjang memaksa segitiganya sama kaki.** Arah
sebaliknya jelas dari kesetangkupan — pada segitiga sama kaki dengan $b = c$, mencerminkan
gambar menukar $m_b$ dengan $m_c$.

Bandingkan dengan garis bagi: pernyataan yang serupa untuk garis bagi ("dua garis bagi sama
panjang berakibat sama kaki") juga benar, tetapi itu **teorema Steiner–Lehmus** yang
buktinya jauh lebih sulit dan tidak punya jalan aljabar sependek ini. Kemiripan bunyi tidak
menjamin kemiripan ongkos.

## Rubrik

- Menuliskan rumus panjang garis berat $4m_a^2 = 2b^2 + 2c^2 - a^2$ beserta kedua bentuk
  lainnya dengan peran huruf yang diputar benar
- **(a)** Menjumlahkan ketiganya dan mengumpulkan sukunya sampai memperoleh $3(a^2+b^2+c^2)$
- **(a)** Membagi $4$ dan menuliskan kesimpulannya dalam bentuk yang diminta
- **(b)** Menyamakan $4m_b^2$ dengan $4m_c^2$ dan menunjukkan suku $2a^2$ lenyap
- **(b)** Menyederhanakan sampai $b^2 = c^2$
- **(b)** Menyebut bahwa panjang sisi positif sebagai alasan sahnya menyimpulkan $b = c$
