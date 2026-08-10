---
id: pyt-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [pythagoras]
bentuk: uraian
kesulitan: 3
---

## Soal

Segitiga $ABC$ siku-siku di $C$. Dari $C$ ditarik garis tinggi ke sisi miring $AB$, memotongnya
di titik $D$. Tulis

$$p = AD, \qquad q = DB, \qquad h = CD, \qquad c = AB = p + q$$

![Segitiga ABC siku-siku di C dengan sisi miring AB mendatar. Dari C ditarik garis tinggi yang memotong sisi miring tegak lurus di titik D, membagi AB menjadi potongan AD dan DB yang tidak sama panjang](siku-siku-garis-tinggi.svg)

Buktikan bahwa

$$h^2 = pq \qquad \text{dan} \qquad CA^2 = c\,p$$

## Petunjuk

- Gambar itu memuat lebih dari satu segitiga siku-siku. Tuliskan apa yang kamu ketahui tentang masing-masing sebelum menggabungkannya.
- Ada tiga segitiga siku-siku: $\triangle ADC$, $\triangle BDC$, dan $\triangle ACB$. Tuliskan Pythagoras pada ketiganya.
- Jumlahkan dua persamaan yang pertama, lalu bandingkan hasilnya dengan yang ketiga setelah $c$ diganti $p+q$.

## Pembahasan

**Namai kedua sisi siku-sikunya.** Tulis $b = CA$ dan $a = CB$.

**Tuliskan Pythagoras pada ketiga segitiga siku-siku.** Garis tinggi $CD$ tegak lurus $AB$,
jadi $\triangle ADC$ dan $\triangle BDC$ dua-duanya siku-siku di $D$; sedangkan
$\triangle ACB$ siku-siku di $C$ menurut soal.

$$b^2 = h^2 + p^2 \tag{1}$$

$$a^2 = h^2 + q^2 \tag{2}$$

$$a^2 + b^2 = c^2 \tag{3}$$

**Bukti bagian pertama.** Jumlahkan $(1)$ dan $(2)$:

$$a^2 + b^2 = 2h^2 + p^2 + q^2$$

Menurut $(3)$ ruas kirinya sama dengan $c^2$, dan $c = p + q$, sehingga

$$(p+q)^2 = 2h^2 + p^2 + q^2$$

$$p^2 + 2pq + q^2 = 2h^2 + p^2 + q^2$$

$$2pq = 2h^2 \quad \Longrightarrow \quad h^2 = pq$$

**Bukti bagian kedua.** Masukkan hasil itu kembali ke $(1)$:

$$b^2 = h^2 + p^2 = pq + p^2 = p(q + p) = p\,c$$

Jadi $CA^2 = c\,p$. $\blacksquare$

### Yang dipakai dan yang tidak

Seluruh bukti di atas memakai **hanya Pythagoras**, tiga kali, ditambah satu penjabaran
$(p+q)^2$. Tidak ada kesebangunan, tidak ada perbandingan sisi, tidak ada sudut yang dikejar.

Itu layak diperhatikan, sebab hubungan $h^2 = pq$ biasanya diperkenalkan sebagai akibat
kesebangunan ketiga segitiga di gambar itu. Bukti lewat kesebangunan memang lebih pendek —
tetapi bukti di atas menunjukkan hubungan itu **tidak memerlukan** kesebangunan sama sekali,
dan itu keterangan yang berguna: ia berarti hubungannya tetap berlaku di setiap keadaan di
mana ketiga persamaan Pythagoras di atas berlaku.

### Bagian ketiga yang ikut gratis

Dengan cara yang persis sama, dari $(2)$:

$$a^2 = h^2 + q^2 = pq + q^2 = q(p+q) = q\,c$$

sehingga $CB^2 = c\,q$. Ketiga hubungannya kini lengkap:

$$h^2 = pq, \qquad b^2 = cp, \qquad a^2 = cq$$

Cara mengingat tanpa tertukar: **$h$ berpasangan dengan kedua potongan, tiap sisi siku-siku
berpasangan dengan potongan yang menempel padanya.** Sisi $CA$ menempel pada potongan $AD = p$,
jadi $b^2 = cp$ — bukan $cq$.

### Periksa dengan angka

Ambil $p = 4$ dan $q = 9$. Maka $c = 13$, $h^2 = 36$ sehingga $h = 6$, lalu $b^2 = 52$ dan
$a^2 = 117$. Periksa dengan $(3)$: $52 + 117 = 169 = 13^2$ ✓.

Menguji rumus yang baru diturunkan pada satu contoh berangka adalah cara termurah menangkap
$p$ dan $q$ yang tertukar — kekeliruan yang hasilnya tetap terlihat masuk akal.

## Rubrik

- Menyebut ketiga segitiga siku-siku beserta letak sudut siku-sikunya
- Menuliskan Pythagoras pada $\triangle ADC$ dan $\triangle BDC$ dengan benar
- Menuliskan Pythagoras pada $\triangle ACB$, yaitu $a^2 + b^2 = c^2$
- Menjumlahkan dua persamaan pertama dan mengganti $c$ dengan $p + q$
- Menjabarkan $(p+q)^2$ lalu menyimpulkan $h^2 = pq$
- Memasukkan $h^2 = pq$ kembali ke salah satu persamaan untuk mendapat $CA^2 = cp$
