---
id: smp-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [sarang-merpati]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Beberapa bilangan dipilih dari himpunan $\{1, 2, 3, \dots, 10\}$.

Paling sedikit berapa bilangan harus dipilih supaya **pasti** ada dua di antaranya yang
jumlahnya $11$?

## Petunjuk

- Sarangnya bukan bilangan itu sendiri. Kelompokkan kesepuluh bilangan menurut sesuatu yang berhubungan dengan syarat soal.
- Pasangkan tiap bilangan dengan bilangan yang melengkapinya menjadi $11$. Ada berapa pasangan seperti itu?
- Kalau dua bilangan berasal dari pasangan yang sama, jumlahnya pasti $11$.

## Pembahasan

**Susun sarangnya.** Kelompokkan $\{1,\dots,10\}$ menjadi pasangan yang jumlahnya $11$:

$$\{1,10\},\quad \{2,9\},\quad \{3,8\},\quad \{4,7\},\quad \{5,6\}$$

Ada $5$ pasangan, dan tiap bilangan dari $1$ sampai $10$ masuk tepat satu pasangan. Inilah
sarangnya:

$$k = 5$$

**Keadaan terburuk.** Kalau dipilih $5$ bilangan, masih mungkin tidak ada dua yang berjumlah
$11$ — ambil satu wakil dari tiap pasangan, misalnya

$$\{1, 2, 3, 4, 5\}$$

Tidak ada dua di antaranya yang berjumlah $11$. Jadi $5$ belum cukup.

**Bilangan keenam.** Ia harus masuk salah satu dari kelima pasangan, dan tiap pasangan sudah
punya satu wakil. Maka ada pasangan yang kedua anggotanya terpilih, dan jumlahnya $11$.

$$\boxed{6}$$

**Inilah bagian tersulit dari jurus ini: memilih sarangnya.** Sarang di soal ini tidak
disebutkan sama sekali oleh soalnya — ia harus dikarang, dan yang mengarahkannya adalah
**syarat yang diminta**. Karena syaratnya "berjumlah $11$", sarang yang berguna adalah
pengelompokan menurut pasangan berjumlah $11$.

Kalau syaratnya diganti "selisihnya $5$", sarangnya juga berganti: $\{1,6\}, \{2,7\},
\{3,8\}, \{4,9\}, \{5,10\}$ — kebetulan juga $5$ pasangan, jadi jawabannya juga $6$.

Kalau syaratnya "jumlahnya $11$" tetapi himpunannya $\{1,\dots,12\}$, bilangan $11$ dan
$12$ tidak punya pasangan di dalam himpunan. Keduanya menjadi sarang sendiri-sendiri, jadi
$k = 5 + 2 = 7$ dan jawabannya $8$. Memeriksa apakah ada anggota yang tidak berpasangan
adalah langkah yang tidak boleh dilewati.
