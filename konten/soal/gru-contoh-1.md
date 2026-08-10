---
id: gru-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-ruang]
bentuk: isian
kesulitan: 2
jawaban: "7"
---

## Soal

Limas segiempat beraturan $T.ABCD$ mempunyai alas persegi dengan $AB = 12$ dan rusuk tegak
$TA = 11$.

![Limas segiempat beraturan dengan alas persegi ABCD dan puncak T tepat di atas titik potong diagonal alas. Titik O adalah perpotongan diagonal AC dan BD, dan ruas TO digambar putus-putus sebagai tinggi limas, tegak lurus alas. Rusuk AD, DC, dan TD tersembunyi di belakang sehingga digambar putus-putus](limas-segiempat.svg)

Tentukan tinggi limas itu.

## Petunjuk

- Tinggi limas adalah ruas tegak lurus dari $T$ ke bidang alas. Pada limas beraturan, di titik mana ruas itu menembus alasnya?
- Kakinya adalah titik potong diagonal alas, sebut $O$. Sekarang $T$, $O$, dan $A$ membentuk satu segitiga siku-siku — gambar segitiga itu sendirian, lepas dari limasnya.
- Untuk memakai Pythagoras pada $\triangle TOA$, kamu perlu $OA$, yaitu setengah diagonal persegi.

## Pembahasan

**Temukan bidang datar yang memuat semuanya.** Ini langkah pertama hampir setiap soal ruang.
Yang dicari — tinggi $TO$ — dan yang diketahui — $TA = 11$ — dua-duanya terletak pada
segitiga $TOA$. Gambar ulang segitiga itu **sendirian**, dan soal ruangnya berubah menjadi soal
bidang yang biasa saja.

**Tentukan letak $O$.** Pada limas segiempat **beraturan**, puncaknya tepat di atas pusat
alasnya, yaitu titik potong diagonal persegi. Jadi $TO \perp$ bidang $ABCD$, dan karena
$OA$ terletak pada bidang alas,

$$\angle TOA = 90^\circ$$

**Cari $OA$.** Diagonal persegi bersisi $12$ adalah

$$AC = 12\sqrt{2}$$

dan $O$ titik tengahnya, sehingga

$$OA = 6\sqrt{2} \quad \Longrightarrow \quad OA^2 = 72$$

Perhatikan: yang diperlukan justru $OA^2$, bukan $OA$. Menyimpan bentuk kuadratnya menghindari
akar sampai baris terakhir.

**Pythagoras pada $\triangle TOA$.**

$$TO^2 = TA^2 - OA^2 = 11^2 - 72 = 121 - 72 = 49$$

$$TO = \boxed{7}$$

### Periksa kewajarannya

Tinggi $7$ harus lebih pendek daripada rusuk tegak $11$ ✓ — rusuk tegak selalu sisi miring
terhadap tinggi. Dan $OA = 6\sqrt2 \approx 8{,}49$, juga lebih pendek daripada $11$ ✓.

Kalau perhitunganmu memberi tinggi yang lebih besar daripada rusuk tegaknya, hampir pasti $TA$
dan $TO$ tertukar peran, atau $OA$ dihitung sebagai diagonal penuh alih-alih setengahnya.

### Kekeliruan yang paling sering

Memakai **setengah sisi** alih-alih setengah diagonal, yakni $OA = 6$ alih-alih $6\sqrt{2}$.
Hasilnya $\sqrt{121-36} = \sqrt{85} \approx 9{,}22$ — angka yang tampak wajar, tanpa isyarat
apa pun bahwa ia salah.

Bedanya: jarak $6$ adalah dari $O$ ke **titik tengah sisi** (apotema alas), sedangkan $6\sqrt2$
dari $O$ ke **titik sudut**. Yang mana yang dipakai bergantung pada apa yang diketahui:

| Yang diketahui | Segitiga siku-sikunya | Sisi mendatarnya |
|---|---|---|
| Rusuk tegak $TA$ | $T$, $O$, titik sudut $A$ | $6\sqrt2$ |
| Apotema sisi (tinggi segitiga sisi) | $T$, $O$, titik tengah sisi | $6$ |

Menuliskan segitiga mana yang dipakai **sebelum** menghitung adalah kebiasaan yang menghapus
seluruh golongan kekeliruan ini.

### Yang terbuka setelah tingginya diketahui

$$V = \tfrac{1}{3} \times L_{\text{alas}} \times t = \tfrac{1}{3} \times 144 \times 7 = 336$$

Apotema sisinya $\sqrt{7^2 + 6^2} = \sqrt{85}$, sehingga luas selimutnya
$4 \times \tfrac12 \times 12 \times \sqrt{85} = 24\sqrt{85}$.

Perhatikan bahwa tingginya bulat tetapi apotema sisinya tidak. Pada soal ruang, satu besaran
yang bulat tidak menjanjikan apa pun tentang besaran lainnya — jadi jangan memaksakan bentuk
bulat pada jawaban yang memang berakar.
