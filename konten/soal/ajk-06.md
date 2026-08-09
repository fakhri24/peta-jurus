---
id: ajk-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [aturan-pencacahan]
bentuk: uraian
kesulitan: 3
---

## Soal

Tinjau bilangan lima angka yang **seluruh angkanya ganjil** dan **tidak ada dua angka
bertetangga yang sama**.

Buktikan bahwa banyaknya bilangan seperti itu adalah $5 \cdot 4^{4}$, dan jelaskan mengapa
aturan kali boleh dipakai di sini padahal pilihan tiap tempat bergantung pada tempat
sebelumnya.

## Petunjuk

- Isi bilangannya dari kiri ke kanan, satu tempat pada satu waktu, dan catat berapa pilihan yang tersedia di tiap langkah.
- Syarat yang mengikat sebuah tempat hanya menyangkut tetangga kirinya — bukan seluruh angka yang sudah ditulis sebelumnya.
- Yang dituntut aturan kali bukan "pilihannya sama", melainkan "**banyaknya** pilihan sama". Bedakan keduanya dengan hati-hati dalam tulisanmu.

## Pembahasan

Isi bilangannya dari kiri ke kanan.

**Tempat pertama.** Angkanya ganjil, jadi dari $\{1, 3, 5, 7, 9\}$:

$$5 \text{ pilihan}$$

**Tempat kedua sampai kelima.** Tiap tempat harus ganjil dan harus berbeda dari tetangga
kirinya. Dari lima angka ganjil, tepat satu terlarang — yaitu angka di sebelah kirinya —
sehingga tersisa

$$4 \text{ pilihan}$$

Karena ada empat tempat semacam itu:

$$5 \times 4 \times 4 \times 4 \times 4 = 5 \cdot 4^{4} = 1280 \qquad \blacksquare$$

### Mengapa aturan kali tetap sah

Di sinilah inti soalnya. Sekilas aturan kali seperti tidak berlaku, sebab **pilihan** untuk
tempat ke-$k$ jelas bergantung pada apa yang ditulis di tempat ke-$(k-1)$: kalau tetangga
kirinya $3$, angka yang boleh dipakai adalah $\{1,5,7,9\}$; kalau tetangga kirinya $7$,
angka yang boleh adalah $\{1,3,5,9\}$. Kedua himpunan itu **berbeda**.

Tetapi yang dituntut aturan kali bukan itu. Yang dituntutnya adalah **banyaknya** pilihan
sama, bukan pilihannya sendiri yang sama. Dan di sini banyaknya selalu $4$, apa pun angka
di sebelah kiri — karena berapa pun nilainya, ia menyingkirkan tepat satu dari lima angka
ganjil.

Perbedaan itu yang membuat aturan kali jauh lebih luas pemakaiannya daripada yang terlihat.

### Contoh tandingan yang menunjukkan syaratnya sungguh perlu

Ganti syaratnya menjadi "tiap angka harus **lebih besar** dari tetangga kirinya". Sekarang
banyaknya pilihan ikut berubah: setelah $1$ tersisa $4$ pilihan, tetapi setelah $7$ hanya
tersisa $1$. Jawabannya bukan lagi hasil kali sederhana, dan hitungannya harus dipecah
menurut kasus.

Jadi syarat "banyaknya sama" bukan formalitas — ia benar-benar bisa gagal.

## Rubrik

- Menyatakan bahwa bilangannya diisi tempat demi tempat, dan menyebut urutan pengisiannya
- Menghitung $5$ pilihan untuk tempat pertama dengan alasan angkanya ganjil
- Menghitung $4$ pilihan untuk tiap tempat berikutnya, dengan alasan tepat satu angka ganjil terlarang
- Menyimpulkan hasil kalinya $5 \cdot 4^4$
- Menyatakan syarat aturan kali dengan tepat: yang harus sama adalah **banyaknya** pilihan, bukan himpunan pilihannya
- Menunjukkan syarat itu terpenuhi di soal ini, dengan menyebut bahwa tetangga kiri mana pun menyingkirkan tepat satu angka
- Memberi contoh tandingan atau penjelasan yang menunjukkan syarat itu bisa gagal pada soal lain
