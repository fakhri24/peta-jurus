---
id: ajk-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [aturan-pencacahan]
bentuk: isian
kesulitan: 2
jawaban: "24"
---

## Soal

Dari angka $1, 2, 3, 4, 5$ dibentuk bilangan tiga angka yang **angka-angkanya berbeda**.

Ada berapa bilangan seperti itu yang bernilai genap?

## Petunjuk

- Ada satu tempat yang paling terkekang oleh syarat soal. Isi tempat itu lebih dulu, bukan dari kiri.
- Bilangan genap ditentukan oleh angka terakhirnya, dan dari kelima angka itu hanya dua yang membuatnya genap.
- Setelah angka terakhir ditetapkan, dua tempat sisanya diisi dari empat angka yang belum terpakai.

## Pembahasan

**Dahulukan tempat yang paling terkekang.** Syarat "genap" hanya menyentuh angka satuan,
jadi isi tempat itu lebih dulu. Kalau dikerjakan dari kiri, syaratnya baru muncul di
langkah terakhir dan banyaknya pilihan jadi bergantung pada apa yang sudah terpakai —
tepat keadaan yang membuat aturan kali tidak bisa dipakai langsung.

**Langkah 1 — angka satuan.** Harus genap, jadi $2$ atau $4$:

$$2 \text{ pilihan}$$

**Langkah 2 — dua tempat sisanya.** Satu angka sudah terpakai, tersisa $4$ angka untuk $2$
tempat, dan urutannya berarti:

$$4 \times 3 = 12$$

Banyaknya pilihan ini **sama** apa pun angka satuan yang terpilih — baik $2$ maupun $4$
sama-sama menyisakan empat angka. Karena itu aturan kali sah:

$$2 \times 12 = \boxed{24}$$

**Periksa ulang lewat jalan lain.** Seluruh bilangan tiga angka berbeda dari lima angka itu
ada $5 \times 4 \times 3 = 60$. Menurut simetri, tiap angka muncul di tempat satuan
sebanyak $60 / 5 = 12$ kali. Karena dua di antara lima angka itu genap, banyaknya bilangan
genap adalah $2 \times 12 = 24$. Cocok.

Kebiasaan mendahulukan tempat yang paling terkekang akan dipakai terus, dan pada soal
susunan dengan banyak syarat ia sering satu-satunya yang membuat hitungannya tetap rapi.
