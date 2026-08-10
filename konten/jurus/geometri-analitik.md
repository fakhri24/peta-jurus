---
id: geometri-analitik
nama: Geometri Analitik
pilar: geometri
tahap: osn-k
prasyarat: [pythagoras, persamaan-kuadrat]
contoh: []
latihan: []
---

## Kapan dipakai

Soal geometri yang **sarat perhitungan panjang dan tegak lurus** tetapi miskin sudut, dan
tidak ada kesebangunan yang jelas. Memberi koordinat mengubahnya jadi soal aljabar yang
pasti selesai, meski kadang panjang.

Pemicu paling terang: gambar memuat **persegi, persegi panjang, atau sudut siku-siku** yang
bisa dijadikan sumbu. Menaruh titik asal di tempat yang tepat menghapus separuh
perhitungannya.

Pemicu kedua: yang ditanyakan **tempat kedudukan** atau titik potong beberapa garis
sekaligus. Menyelesaikan sistem persamaan lebih dapat diandalkan daripada mengejar sudut.

Sebaliknya, jangan pakai kalau soalnya penuh lingkaran dan sudut — di situ jurus sintetik
biasanya jauh lebih pendek.

## Intinya

**Jarak dan titik tengah.** Untuk $A(x_1,y_1)$ dan $B(x_2,y_2)$:

$$AB = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}, \qquad
M = \left( \frac{x_1+x_2}{2}, \frac{y_1+y_2}{2} \right)$$

Yang pertama Pythagoras, hanya ditulis lain.

**Titik yang membagi ruas** dengan perbandingan $AP : PB = m : n$:

$$P = \left( \frac{n x_1 + m x_2}{m+n}, \frac{n y_1 + m y_2}{m+n} \right)$$

**Garis.** Gradien $m = \dfrac{y_2-y_1}{x_2-x_1}$; dua garis sejajar kalau gradiennya sama
dan tegak lurus kalau $m_1 m_2 = -1$. Jarak titik $(x_0,y_0)$ ke garis $ax+by+c=0$:

$$d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2+b^2}}$$

**Lingkaran** berpusat $(a,b)$ berjari-jari $r$:

$$(x-a)^2 + (y-b)^2 = r^2$$

Memotongkannya dengan garis menghasilkan persamaan kuadrat, dan **diskriminannya**
menjawab langsung: dua titik potong, menyinggung, atau tidak memotong sama sekali.

**Luas segitiga dari koordinat:**

$$L = \tfrac{1}{2} \left| x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2) \right|$$

Bentuk ini juga menguji kesegarisan: hasilnya nol tepat ketika ketiga titiknya segaris.

## Jebakan umum

- **Menaruh sumbu di tempat yang menyulitkan.** Titik asal dan sumbu boleh dipilih bebas;
  memilihnya di titik sudut siku-siku atau di titik tengah bangun sering memangkas
  perhitungan sampai separuh.
- **Memberi koordinat pada terlalu banyak titik bebas.** Bangun sembarang cukup diberi
  beberapa peubah; menaruh enam huruf di tempat yang bisa tiga membuat aljabarnya tak
  terkendali.
- **Lupa nilai mutlak pada rumus jarak ke garis dan luas.** Tanpa itu jawabannya bisa
  negatif, dan panjang negatif berarti langkahnya salah, bukan jawabannya unik.
- **Gradien tak terdefinisi diabaikan.** Garis tegak tidak punya gradien; syarat
  $m_1 m_2 = -1$ tidak bisa dipakai kalau salah satunya tegak.
- **Mengira koordinat selalu jalan tercepat.** Untuk soal yang penuh sudut keliling,
  koordinat justru bentuk terpanjang dari jawaban yang sama.
