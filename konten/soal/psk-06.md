---
id: psk-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-siklik]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa banyaknya cara menyusun $n$ benda berbeda secara melingkar adalah $(n-1)!$,
dengan ketentuan dua susunan dianggap sama kalau yang satu dapat diperoleh dari yang lain
lewat pemutaran.

Buktikan dengan **dua cara**: lewat pemakuan satu benda, dan lewat pembagian susunan
berjajar. Untuk cara kedua, jelaskan mengapa pembaginya tepat $n$.

## Petunjuk

- Cara pertama: tetapkan satu benda di satu tempat. Jelaskan mengapa hal itu boleh dilakukan tanpa kehilangan susunan mana pun.
- Cara kedua: hitung susunan berjajar, lalu tentukan berapa susunan berjajar yang berasal dari satu susunan melingkar yang sama.
- Untuk cara kedua, pembagian hanya sah kalau tiap susunan melingkar punya jumlah salinan yang **sama**. Buktikan itu, jangan hanya menyatakannya.

## Pembahasan

### Cara pertama — paku satu benda

Pilih satu benda tertentu, sebut $b_1$, lalu tetapkan ia di satu tempat pada lingkaran.

**Langkah ini tidak menghilangkan susunan apa pun.** Ambil sebarang susunan melingkar.
Karena memutar tidak mengubahnya, ia dapat diputar sehingga $b_1$ berada di tempat yang
sudah ditetapkan. Jadi tiap susunan melingkar punya wakil dengan $b_1$ di sana.

**Langkah ini juga tidak menghitung apa pun dua kali.** Kalau dua susunan sama-sama
menempatkan $b_1$ di tempat itu dan keduanya sama sebagai susunan melingkar, maka
pemutarannya harus memindahkan $b_1$ ke dirinya sendiri — yaitu pemutaran sejauh nol.
Karena itu keduanya susunan yang sama persis.

Setelah $b_1$ dipaku, lingkarannya punya titik acuan. Sisa $n-1$ benda tinggal disusun
searah jarum jam mulai dari sebelah $b_1$, dan itu susunan berjajar biasa:

$$(n-1)! \qquad \blacksquare$$

### Cara kedua — bagi susunan berjajar

Susunan berjajar dari $n$ benda berbeda ada $n!$.

Tiap susunan berjajar dapat dibaca sebagai susunan melingkar, dengan menyambungkan ujung
kanan ke ujung kiri. Pertanyaannya: **berapa susunan berjajar yang menghasilkan susunan
melingkar yang sama?**

Ambil sebuah susunan melingkar. Untuk menuliskannya sebagai barisan, harus dipilih dari
benda mana pembacaan dimulai. Ada $n$ pilihan, dan tiap pilihan memberi barisan yang
berbeda — sebab barisan yang berbeda titik awalnya punya benda pertama yang berbeda, dan
seluruh bendanya berlainan.

Jadi **setiap** susunan melingkar berasal dari tepat $n$ susunan berjajar. Karena jumlah
salinannya sama untuk semua, pembagiannya sah:

$$\frac{n!}{n} = (n-1)! \qquad \blacksquare$$

### Mengapa syarat "jumlah salinan sama" perlu dinyatakan

Pembagian hanya boleh dipakai ketika tiap hasil terhitung dengan kelipatan yang sama. Kalau
sebagian susunan punya $n$ salinan dan sebagian punya lebih sedikit, membagi dengan $n$
akan salah.

Di sini syarat itu terpenuhi **karena seluruh bendanya berbeda**. Kalau ada benda yang
kembar, sebagian susunan bisa berimpit dengan hasil pemutarannya sendiri, salinannya
menjadi kurang dari $n$, dan rumus $(n-1)!$ tidak lagi berlaku.

Contoh terkecilnya: susunan melingkar dari benda $A, A, B, B$. Rumus $(4-1)! = 6$ jelas
salah — susunannya hanya ada dua, yaitu $AABB$ dan $ABAB$ dibaca melingkar. Sebabnya
$ABAB$ berimpit dengan dirinya sendiri setelah diputar dua langkah, sehingga salinannya
hanya $2$, bukan $4$.

Menangani keadaan seperti itu memerlukan alat yang lebih berat daripada pembagian
sederhana. Untuk soal-soal di tahap ini, syarat "benda berbeda semua" selalu terpenuhi dan
$(n-1)!$ aman dipakai.

## Rubrik

- Cara pertama: menyatakan pemakuan satu benda di satu tempat
- Cara pertama: menjelaskan mengapa pemakuan tidak menghilangkan susunan apa pun
- Cara pertama: menjelaskan mengapa pemakuan tidak menghitung susunan dua kali
- Cara pertama: menyimpulkan sisanya disusun berjajar, memberi $(n-1)!$
- Cara kedua: menyatakan ada $n!$ susunan berjajar
- Cara kedua: menunjukkan tiap susunan melingkar berasal dari tepat $n$ susunan berjajar, dengan alasan pemilihan titik awal
- Menyebut bahwa jumlah salinan yang sama itulah yang membuat pembagian sah, dan mengaitkannya dengan syarat benda berbeda semua
