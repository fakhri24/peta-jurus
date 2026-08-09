---
id: inv-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [invarian]
bentuk: uraian
kesulitan: 3
---

## Soal

Di sebuah papan tertulis bilangan $1, 2, 3, \dots, 10$. Sebuah langkah terdiri atas:
menghapus dua bilangan $a$ dan $b$, lalu menuliskan $|a-b|$ sebagai gantinya.

Setelah $9$ langkah hanya tersisa satu bilangan. Buktikan bilangan itu pasti **ganjil**.

## Petunjuk

- Soal tidak menanyakan bilangan mana yang tersisa, melainkan sifat yang selalu berlaku. Cari besaran yang tidak pernah berubah oleh langkah apa pun.
- Coba jumlah seluruh bilangan di papan. Ia jelas berubah — tetapi periksa apakah **sifat ganjil-genapnya** ikut berubah.
- Hitung selisih jumlah sebelum dan sesudah satu langkah, lalu tunjukkan selisih itu selalu genap.

## Pembahasan

**Tebak besarannya.** Jumlah seluruh bilangan di papan adalah calon yang wajar, sebab
langkahnya menyentuh dua bilangan sekaligus. Jumlah itu memang berubah — jadi ia bukan
invarian. Tetapi **paritasnya** mungkin kekal, dan itu yang diperiksa.

**Buktikan paritasnya tidak berubah.** Misalkan sebelum sebuah langkah jumlah seluruh
bilangan adalah $S$. Langkah itu membuang $a$ dan $b$, lalu menambahkan $|a-b|$. Jumlah yang
baru:

$$S' = S - a - b + |a-b|$$

Selisihnya:

$$S - S' = a + b - |a-b|$$

Andaikan $a \ge b$ — kalau tidak, tukar namanya, sebab $|a-b|$ tidak peduli urutannya. Maka
$|a-b| = a-b$ dan

$$S - S' = a + b - (a-b) = 2b$$

Bilangan $2b$ selalu **genap**. Jadi tiap langkah mengubah jumlahnya sebesar bilangan genap,
sehingga

$$S' \equiv S \pmod 2$$

**Paritas jumlah adalah invariannya.**

**Hitung nilai awalnya.**

$$S_0 = 1 + 2 + \cdots + 10 = \frac{10 \times 11}{2} = 55$$

yang **ganjil**.

**Simpulkan.** Karena paritasnya tidak pernah berubah, jumlah seluruh bilangan di papan
selalu ganjil — pada setiap tahap, termasuk di akhir. Di akhir hanya tersisa satu bilangan,
sehingga jumlahnya adalah bilangan itu sendiri.

Maka bilangan terakhir ganjil. $\blacksquare$

### Yang dibuktikan dan yang tidak

Bukti ini menunjukkan bilangan terakhir **pasti ganjil**. Ia tidak menyebut bilangan mana —
dan memang tidak bisa, sebab hasilnya bergantung pada urutan langkah. Dengan mencoba
berbagai urutan, hasil yang bisa muncul adalah $1, 3, 5, 7, 9$; seluruhnya ganjil,
sebagaimana dijamin.

Perhatikan juga arah kesimpulannya. Invarian membuktikan sesuatu **tidak mungkin** — di sini,
tidak mungkin berakhir genap. Ia tidak pernah membuktikan sesuatu mungkin. Untuk menunjukkan
bahwa $7$ benar-benar dapat dicapai, satu-satunya cara adalah memberikan urutan langkahnya.

### Langkah yang paling sering dilewati

Bagian tersulit bukan menebak besarannya, melainkan **membuktikan tiap langkah tidak
mengubahnya**. Banyak jawaban berhenti pada "jumlahnya ganjil, jadi hasilnya ganjil" tanpa
menghitung $S - S' = 2b$ — dan tanpa perhitungan itu, tidak ada alasan apa pun bahwa
paritasnya kekal.

Kalau langkahnya diganti menjadi "tulis $a+b$", paritas jumlahnya juga kekal, tetapi kalau
diganti menjadi "tulis $ab$", ia **tidak** kekal. Perbedaannya hanya terlihat lewat
perhitungan.

## Rubrik

- Menyatakan bahwa yang dicari adalah besaran yang tidak berubah oleh langkah apa pun
- Memilih jumlah seluruh bilangan, dan menyadari yang kekal adalah paritasnya, bukan jumlahnya
- Menghitung $S - S' = a + b - |a-b|$
- Menangani nilai mutlaknya, misalnya dengan memisalkan $a \ge b$, lalu menyimpulkan selisihnya $2b$
- Menyimpulkan selisih itu genap, sehingga paritas jumlah kekal pada setiap langkah
- Menghitung jumlah awal $55$ dan menyebutnya ganjil
- Menyimpulkan bilangan terakhir sama dengan jumlah akhir, sehingga ganjil
