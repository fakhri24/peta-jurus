---
id: aturan-pencacahan
nama: Aturan Jumlah dan Aturan Kali
pilar: kombinatorika
tahap: osn-k
prasyarat: []
contoh: []
latihan: []
---

## Kapan dipakai

Setiap soal pencacahan dimulai di sini, dan pertanyaan pembukanya selalu sama: pilihannya
disusun **bertahap** atau dipecah menjadi **kasus**? "Ini lalu itu" berarti kali; "ini atau
itu" berarti jumlah.

Kalau yang diminta memuat "paling sedikit satu", biasanya lebih pendek menghitung
kebalikannya lalu mengurangkannya dari seluruhnya.

## Intinya

**Aturan kali.** Kalau langkah pertama bisa dikerjakan $m$ cara dan — untuk setiap hasil
langkah pertama — langkah kedua bisa dikerjakan $n$ cara, maka seluruhnya

$$m \times n$$

Syarat yang paling sering dilupakan ada di kata "untuk setiap": banyaknya pilihan langkah
kedua harus **sama** apa pun hasil langkah pertama. Kalau tidak sama, pecah dulu jadi
kasus.

**Aturan jumlah.** Kalau kejadian $A$ bisa terjadi $m$ cara, $B$ bisa $n$ cara, dan tidak
ada satu cara pun yang termasuk keduanya, maka

$$|A \cup B| = |A| + |B| \qquad (A \cap B = \varnothing)$$

Syaratnya juga sering dilupakan: kasusnya harus **lepas**. Kalau beririsan, jumlahnya
kelebihan — dan memperbaikinya adalah jurus tersendiri.

**Aturan komplemen.** Kalau yang diminta susah dihitung langsung tapi kebalikannya mudah:

$$|A| = |S| - |A^{c}|$$

## Jebakan umum

- **Menjumlahkan kasus yang beririsan.** Anggota yang masuk dua kasus terhitung dua kali.
- **Mengalikan padahal banyak pilihannya berubah.** Kalau langkah kedua punya 5 pilihan
  untuk sebagian hasil langkah pertama dan 4 untuk sisanya, aturan kali belum bisa dipakai
  apa adanya.
- **Kasus yang tidak menutupi semuanya.** Setelah memecah jadi kasus, periksa dua hal
  sekaligus: tidak ada yang tumpang tindih, dan tidak ada yang terlewat.
