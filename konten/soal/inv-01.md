---
id: inv-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [invarian]
bentuk: isian
kesulitan: 3
jawaban: "0"
---

## Soal

Di sebuah papan tertulis bilangan $1, 2, 3, \dots, 20$. Sebuah langkah terdiri atas
menghapus dua bilangan $a$ dan $b$, lalu menuliskan $|a-b|$.

Setelah $19$ langkah tersisa satu bilangan. Berapa nilai **terkecil** yang mungkin untuk
bilangan itu?

## Petunjuk

- Cari lebih dulu besaran yang tidak berubah oleh langkah apa pun. Jumlah seluruh bilangan berubah, tetapi ada sifatnya yang tidak.
- Sifat itu membatasi nilai akhir yang mungkin. Tentukan batas itu sebelum mencari nilai terkecilnya.
- Setelah batasnya diketahui, tunjukkan nilai terkecil itu memang bisa dicapai dengan memberi urutan langkahnya.

## Pembahasan

**Cari invariannya.** Satu langkah mengubah jumlah seluruh bilangan dari $S$ menjadi

$$S' = S - a - b + |a-b|$$

Dengan memisalkan $a \ge b$, selisihnya

$$S - S' = a + b - (a - b) = 2b$$

yang selalu genap. Jadi **paritas jumlah tidak pernah berubah**.

**Hitung paritas awalnya.**

$$S_0 = 1 + 2 + \cdots + 20 = \frac{20 \times 21}{2} = 210$$

yang **genap**.

**Batasi nilai akhirnya.** Karena paritasnya kekal, bilangan terakhir harus genap. Nilai
mutlak tidak pernah negatif, sehingga nilai terkecil yang mungkin **secara paritas** adalah
$0$.

**Tunjukkan $0$ benar-benar tercapai.** Batas saja belum menjawab — harus ada urutan langkah
yang mencapainya.

Pasangkan bilangan berurutan:

$$(1,2) \to 1, \quad (3,4) \to 1, \quad (5,6) \to 1, \quad \dots, \quad (19,20) \to 1$$

Sepuluh pasangan menghasilkan sepuluh angka $1$. Sekarang pasangkan angka-angka $1$ itu:

$$(1,1) \to 0$$

lima kali, menghasilkan lima angka $0$. Terakhir, gabungkan kelima nol:

$$(0,0) \to 0, \quad (0,0) \to 0, \quad (0,0) \to 0, \quad (0,0) \to 0$$

Tersisa $\boxed{0}$.

**Dua bagian itu keduanya perlu.** Invarian memberi batas — hasilnya tidak mungkin ganjil,
jadi tidak mungkin $1$. Konstruksi menunjukkan batas itu tercapai. Menjawab $0$ hanya
dengan invarian belum lengkap; menjawab dengan konstruksi saja tidak membuktikan tidak ada
yang lebih kecil.

**Bandingkan dengan soal $1$ sampai $10$.** Di sana jumlahnya $55$ yang ganjil, sehingga
$0$ **mustahil** dan nilai terkecilnya $1$. Satu angka pada soal mengubah seluruh
jawabannya — dan itu ditentukan sepenuhnya oleh paritas $\frac{n(n+1)}{2}$.
