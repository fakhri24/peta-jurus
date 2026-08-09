---
id: psk-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-siklik]
bentuk: isian
kesulitan: 3
jawaban: "72"
---

## Soal

Enam orang duduk mengelilingi meja bundar tanpa nomor kursi. Dua orang di antaranya, Ani
dan Budi, sedang bertengkar dan **tidak mau** duduk berdampingan.

Ada berapa susunan tempat duduk yang berbeda?

## Petunjuk

- Syarat "tidak mau" biasanya lebih pendek dikerjakan lewat kebalikannya.
- Hitung seluruh susunan melingkar, lalu hitung yang justru menempatkan keduanya berdampingan.
- Untuk yang berdampingan, satukan keduanya menjadi satu blok — dan ingat isi blok itu masih bisa ditukar.

## Pembahasan

**Seluruh susunan.** Enam orang melingkar tanpa syarat:

$$(6-1)! = 5! = 120$$

**Susunan yang melanggar.** Ani dan Budi berdampingan. Ikat keduanya menjadi satu blok,
sehingga yang duduk melingkar tinggal $5$ benda:

$$(5-1)! = 4! = 24$$

Di dalam blok, Ani bisa di kiri atau di kanan Budi, dan pada meja bundar kedua keadaan itu
berbeda:

$$24 \times 2 = 48$$

**Kurangkan.**

$$120 - 48 = \boxed{72}$$

**Periksa dengan cara celah.** Dudukkan dulu keempat orang lain melingkar:
$(4-1)! = 3! = 6$ cara. Susunan itu membentuk $4$ celah. Tempatkan Ani dan Budi pada dua
celah **berbeda**, dan urutannya berarti karena keduanya orang yang berlainan:

$$4 \times 3 = 12$$

Menempatkan keduanya pada celah berbeda menjamin ada orang lain di antaranya.

$$6 \times 12 = 72$$

Cocok.

**Perhatikan mengapa cara celah di sini memakai $4$ celah, bukan $5$.** Pada susunan
berjajar, $4$ orang membentuk $5$ celah karena kedua ujungnya ikut terhitung. Pada susunan
melingkar tidak ada ujung — celahnya sebanyak orangnya. Perbedaan ini kecil tetapi mengubah
jawaban, dan ia berlaku di setiap soal meja bundar yang memakai cara celah.

**Periksa kewajarannya sekali lagi.** Bagian susunan yang Ani dan Budi-nya berdampingan:

$$\frac{48}{120} = \frac25$$

Masuk akal — pada meja bundar berisi enam orang, Ani punya $5$ orang lain yang mungkin dan
$2$ di antaranya duduk bersebelahan dengannya.
