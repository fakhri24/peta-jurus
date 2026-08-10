---
id: gan-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-analitik]
bentuk: uraian
kesulitan: 3
---

## Soal

Segitiga $ABC$ mempunyai titik sudut $A(x_1, y_1)$, $B(x_2, y_2)$, dan $C(x_3, y_3)$.

Buktikan bahwa ketiga garis beratnya — yaitu ruas dari tiap titik sudut ke titik tengah sisi
seberangnya — berpotongan di satu titik, dan tentukan koordinat titik itu.

## Petunjuk

- Membuktikan tiga garis berpotongan di satu titik bisa dikerjakan dengan mencari titik potong dua di antaranya lalu memeriksa yang ketiga — tetapi ada jalan yang jauh lebih pendek.
- Tebak dulu titiknya, lalu buktikan ia terletak pada ketiga garis berat sekaligus.
- Tulis titik yang membagi garis berat dari $A$ dengan perbandingan $2 : 1$ dari $A$, lalu perhatikan bentuk hasilnya.

## Pembahasan

**Ambil satu garis berat dan tandai satu titik padanya.** Titik tengah sisi $BC$ adalah

$$M_A = \left(\frac{x_2+x_3}{2}, \frac{y_2+y_3}{2}\right)$$

Pada ruas $AM_A$, ambil titik $G$ yang membaginya dengan $AG : GM_A = 2 : 1$, yaitu

$$G = A + \tfrac{2}{3}\left(M_A - A\right)$$

**Hitung koordinatnya.** Untuk absisnya,

$$x_G = x_1 + \tfrac{2}{3}\left(\frac{x_2+x_3}{2} - x_1\right)
= x_1 + \frac{x_2+x_3}{3} - \frac{2x_1}{3} = \frac{x_1 + x_2 + x_3}{3}$$

Dengan hitungan yang sama untuk ordinatnya,

$$G = \left(\frac{x_1+x_2+x_3}{3},\ \frac{y_1+y_2+y_3}{3}\right)$$

**Perhatikan bentuknya.** Hasil itu **setangkup** terhadap $A$, $B$, dan $C$: menukar nama
ketiga titiknya tidak mengubahnya sama sekali.

**Ulangi untuk garis berat dari $B$.** Titik tengah $CA$ adalah
$M_B = \left(\frac{x_3+x_1}{2}, \frac{y_3+y_1}{2}\right)$, dan titik yang membagi $BM_B$ dengan
$BG : GM_B = 2 : 1$ adalah

$$B + \tfrac{2}{3}\left(M_B - B\right)
= \left(\frac{x_1+x_2+x_3}{3},\ \frac{y_1+y_2+y_3}{3}\right)$$

yakni **titik yang sama**. Hal yang sama berlaku untuk garis berat dari $C$.

**Simpulkan.** Titik $G$ terletak pada ketiga garis berat sekaligus, sehingga ketiganya
berpotongan di satu titik, yaitu

$$G = \left(\frac{x_1+x_2+x_3}{3},\ \frac{y_1+y_2+y_3}{3}\right) \qquad \blacksquare$$

### Mengapa cara ini jauh lebih pendek

Jalan yang biasa terpikir adalah: cari persamaan dua garis berat, selesaikan sistemnya, lalu
periksa titik itu memenuhi persamaan garis berat ketiga. Itu bekerja, tetapi memerlukan tiga
persamaan garis dengan gradien berupa pecahan bertingkat — dan gagal seluruhnya kalau salah
satu garis beratnya kebetulan tegak.

Cara di atas membalik urutannya: **tebak titiknya, lalu buktikan ia ada di ketiganya.** Yang
membuatnya bekerja adalah kesetangkupan hasilnya — begitu $x_G$ keluar berbentuk
$\frac{x_1+x_2+x_3}{3}$, tidak ada lagi yang perlu dihitung untuk kedua garis lainnya, sebab
perhitungannya persis sama dengan nama yang dipertukarkan.

### Sekaligus terbukti: perbandingan $2 : 1$

Karena $G$ didefinisikan sebagai pembagi $2 : 1$ pada tiap garis berat, ikut terbukti bahwa
titik potongnya membagi **setiap** garis berat dengan perbandingan $2 : 1$ dihitung dari titik
sudutnya. Itu sifat yang dipakai berulang kali, antara lain pada garis Euler.

### Uji dengan angka

Untuk $A(1,2)$, $B(7,4)$, $C(3,8)$: titik beratnya
$G = \left(\tfrac{11}{3}, \tfrac{14}{3}\right)$.

Periksa lewat garis berat dari $C$: titik tengah $AB$ adalah $(4,3)$, dan

$$C + \tfrac{2}{3}\left((4,3) - (3,8)\right) = \left(3 + \tfrac{2}{3},\ 8 - \tfrac{10}{3}\right)
= \left(\tfrac{11}{3}, \tfrac{14}{3}\right) \quad ✓$$

Menguji rumus umum pada satu contoh berangka adalah cara termurah menangkap kekeliruan
aljabar, dan layak dikerjakan **sebelum** menuliskan buktinya rapi-rapi.

## Rubrik

- Menuliskan koordinat titik tengah salah satu sisi dengan benar
- Menuliskan titik yang membagi garis berat dengan perbandingan $2:1$ dari titik sudutnya
- Menyederhanakan koordinatnya sampai berbentuk rata-rata ketiga koordinat titik sudut
- Menyebut bahwa hasilnya setangkup terhadap $A$, $B$, $C$, atau mengulang perhitungannya untuk garis berat kedua
- Menyimpulkan ketiga garis berat melalui titik yang sama, dan menuliskan koordinatnya
