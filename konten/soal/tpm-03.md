---
id: tpm-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [teori-permainan]
bentuk: uraian
kesulitan: 4
---

## Soal

Dua pemain bergantian meletakkan sebuah koin bundar di atas meja bundar. Koin tidak boleh
bertumpuk dengan koin yang sudah ada, dan harus seluruhnya berada di atas meja. Pemain yang
**tidak bisa** meletakkan koin lagi dinyatakan kalah.

Buktikan bahwa **pemain pertama** punya strategi menang.

## Petunjuk

- Permainan ini tidak bisa dianalisis dengan tabel P/N — keadaannya tak terhingga banyaknya. Cari gagasan lain.
- Meja bundar punya sifat yang bisa dimanfaatkan: ia simetris terhadap titik pusatnya.
- Kalau pemain pertama bisa menjaga susunan koin selalu simetris **setelah langkahnya**, apa akibatnya bagi lawan?

## Pembahasan

**Mengapa tabel P/N tidak dipakai.** Keadaan permainan ini adalah susunan koin di atas meja,
dan banyaknya tak terhingga. Tidak ada tabel yang bisa dikerjakan mundur. Yang dipakai adalah
**strategi pencerminan**.

### Strateginya

**Langkah pertama.** Pemain pertama meletakkan koin **tepat di pusat meja**.

**Langkah berikutnya.** Setiap kali lawan meletakkan koin di suatu tempat, pemain pertama
meletakkan koinnya di **titik pencerminan tempat itu terhadap pusat meja** — yaitu titik
yang berjarak sama dari pusat, pada arah yang berlawanan.

### Mengapa langkah balasan itu selalu bisa dilakukan

Ini bagian yang harus dibuktikan, bukan dianggap jelas. Tiga hal diperiksa.

**Tempatnya berada di atas meja.** Meja berbentuk bundar dan simetris terhadap pusatnya.
Kalau koin lawan seluruhnya berada di atas meja, maka bayangan cerminnya terhadap pusat juga
seluruhnya di atas meja.

**Tempatnya tidak bertumpuk dengan koin lain.** Setelah tiap langkah pemain pertama, susunan
koin di meja **simetris terhadap pusat** — kecuali koin pusat, yang bayangannya adalah
dirinya sendiri. Andaikan bayangan koin lawan bertumpuk dengan sebuah koin $C$ yang sudah
ada. Menurut kesimetrian, bayangan $C$ juga sudah ada di meja — dan bayangan $C$ akan
bertumpuk dengan koin lawan yang barusan diletakkan. Itu mustahil, sebab langkah lawan sah.

**Tempatnya bukan pusat meja.** Pusat sudah terisi sejak langkah pertama, sehingga koin
lawan tidak mungkin diletakkan di sana. Karena itu bayangannya juga bukan pusat, dan tidak
bertabrakan dengan koin pertama.

Jadi langkah balasan **selalu sah**.

### Mengapa pemain pertama menang

Setelah setiap langkah pemain pertama, susunan koin kembali simetris. Akibatnya pemain
pertama tidak pernah kehabisan langkah: setiap kali lawan berhasil melangkah, pemain pertama
punya jawabannya.

Permainan ini pasti berakhir, sebab meja punya luas berhingga dan tiap koin memakai luas
yang tetap, sehingga banyaknya koin tidak bisa bertambah selamanya.

Karena pemain pertama selalu punya jawaban, pihak yang lebih dulu kehabisan langkah pasti
**lawan**. Maka pemain pertama menang. $\blacksquare$

### Mengapa langkah pertama harus di pusat

Titik pusat adalah **satu-satunya** titik yang bayangannya adalah dirinya sendiri. Kalau
langkah pertama tidak di pusat, lawan bisa mengambil pusat itu, dan mulai saat itu justru
lawan yang bisa menjalankan strategi pencerminan.

Merebut titik istimewa itu lebih dulu adalah seluruh isi strategi ini.

### Pola yang lebih luas

Strategi pencerminan bekerja setiap kali papan permainan punya kesimetrian dan ada cara
"menetralkan" titik tetapnya. Ia muncul lagi pada permainan dua tumpukan sama besar — cukup
tirukan langkah lawan pada tumpukan yang lain — dan pada permainan di papan persegi panjang.

Yang harus selalu dibuktikan sama: **langkah balasannya selalu sah**. Tanpa itu, strategi
pencerminan hanya terdengar meyakinkan.

## Rubrik

- Menyatakan langkah pertama di pusat meja
- Menyatakan aturan balasan sebagai pencerminan terhadap pusat
- Membuktikan bayangan koin lawan tetap berada di atas meja, dengan alasan meja simetris
- Membuktikan bayangan itu tidak bertumpuk, lewat pengandaian dan kesimetrian susunan
- Menangani kasus pusat meja secara khusus
- Menyatakan permainan pasti berakhir, dengan alasan luas meja berhingga
- Menyimpulkan pemain pertama tidak pernah kehabisan langkah, sehingga lawan yang kalah
- Menjelaskan mengapa langkah pertama harus di pusat
