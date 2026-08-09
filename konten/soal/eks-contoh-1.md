---
id: eks-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [ekstremal]
bentuk: uraian
kesulitan: 4
---

## Soal

Sebuah graf memiliki $n$ titik, dan setiap titiknya berderajat paling sedikit $k$, dengan
$k \ge 1$.

Buktikan bahwa graf itu memuat sebuah **lintasan** yang melalui paling sedikit $k+1$ titik.

(Lintasan adalah rangkaian titik berbeda yang tiap dua titik berurutannya terhubung ruas.)

## Petunjuk

- Soal meminta membuktikan sesuatu **ada**, tanpa memberi tahu di mana. Tidak ada rumus untuk dipakai, jadi pilih objek yang paling.
- Ambil lintasan **terpanjang** di dalam graf itu, lalu perhatikan salah satu titik ujungnya.
- Ke mana saja tetangga titik ujung itu bisa berada? Kalau ada tetangga di luar lintasan, apa yang bisa dilakukan?

## Pembahasan

**Pilih objek yang paling.** Tinjau seluruh lintasan di dalam graf, dan ambil salah satu
yang **terpanjang**. Sebut lintasan itu

$$P: \ v_1 \to v_2 \to \cdots \to v_m$$

**Pilihan ini sah karena grafnya berhingga.** Banyaknya lintasan berhingga dan tidak nol —
sebuah ruas saja sudah lintasan, dan ruas pasti ada karena tiap titik berderajat paling
sedikit $k \ge 1$. Himpunan berhingga yang tidak kosong selalu punya anggota terpanjang.

**Perhatikan titik ujungnya.** Tinjau $v_1$, dan misalkan $u$ salah satu tetangganya.

**Klaim: $u$ pasti berada di dalam $P$.**

Andaikan tidak — yaitu $u$ berada di luar lintasan. Maka rangkaian

$$u \to v_1 \to v_2 \to \cdots \to v_m$$

juga sebuah lintasan, sebab $u$ terhubung ke $v_1$ dan $u$ berbeda dari seluruh titik yang
sudah ada di $P$. Lintasan baru itu **lebih panjang** daripada $P$.

Itu bertentangan dengan pemilihan $P$ sebagai yang terpanjang. Maka $u$ pasti di dalam $P$.

**Simpulkan.** Seluruh tetangga $v_1$ berada di dalam $P$. Karena $v_1$ punya paling sedikit
$k$ tetangga, dan seluruhnya berbeda dari $v_1$ sendiri, maka $P$ memuat sedikitnya

$$k \ \text{tetangga} \ + \ v_1 \ = \ k+1 \ \text{titik}$$

Jadi $m \ge k+1$. $\blacksquare$

### Mengapa "terpanjang" yang dipilih, bukan yang lain

Seluruh kekuatan bukti ini terletak pada satu langkah: **kalau ada tetangga di luar, lintasan
bisa diperpanjang.** Langkah itu hanya menjadi pertentangan kalau yang dipilih memang
lintasan terpanjang.

Kalau yang dipilih sembarang lintasan, tidak ada yang bertentangan — memang wajar sebuah
lintasan bisa diperpanjang. Sifat "paling" itulah yang diubah menjadi keterangan.

Pola ini berulang: pilih objek yang paling, andaikan sifat yang diinginkan tidak berlaku,
lalu bangun objek yang **lebih ekstrem lagi**. Itu mustahil, dan pertentangannya
menyelesaikan soal.

### Uji dengan menghapus syarat kehinggaan

Kalau grafnya tak berhingga — misalnya garis bilangan bulat dengan tiap bilangan terhubung
ke tetangganya — maka tidak ada lintasan terpanjang, dan seluruh buktinya runtuh. Jaminan
adanya objek terekstrem adalah syarat yang benar-benar dipakai, bukan formalitas.

### Ketajamannya

Batas $k+1$ tidak bisa diperbaiki secara umum. Ambil graf lengkap $K_{k+1}$: tiap titiknya
berderajat tepat $k$, dan lintasan terpanjangnya memuat tepat $k+1$ titik — sebab titiknya
memang hanya sebanyak itu.

Adanya contoh yang mencapai batas adalah tanda bahwa buktinya sudah sepadan dengan soalnya.

## Rubrik

- Memilih lintasan terpanjang, dan menyebut alasan keberadaannya (grafnya berhingga dan lintasan ada)
- Meninjau titik ujung lintasan dan tetangganya
- Mengandaikan ada tetangga di luar lintasan, lalu membangun lintasan yang lebih panjang
- Menyatakan pertentangannya dengan pemilihan lintasan terpanjang
- Menyimpulkan seluruh tetangga titik ujung berada di dalam lintasan
- Menghitung banyaknya titik: paling sedikit $k$ tetangga ditambah titik ujung itu sendiri
