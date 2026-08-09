---
id: inv-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [invarian]
bentuk: uraian
kesulitan: 4
---

## Soal

Beberapa bilangan asli ditulis di papan. Sebuah langkah terdiri atas: memilih dua bilangan
$a$ dan $b$ dengan $a > b$, lalu **mengganti** $a$ dengan $a - b$. Bilangan $b$ dibiarkan.

Buktikan bahwa proses ini **pasti berhenti** — yaitu setelah sejumlah berhingga langkah,
tidak ada lagi dua bilangan yang bisa dipilih.

## Petunjuk

- Yang diminta bukan invarian, melainkan besaran yang selalu berubah ke satu arah saja.
- Perhatikan jumlah seluruh bilangan di papan. Apakah ia bisa naik?
- Sebuah besaran yang selalu turun belum cukup untuk menjamin berhenti. Sifat apa lagi yang dibutuhkan?

## Pembahasan

**Yang dicari adalah monovarian, bukan invarian.** Invarian membuktikan sesuatu tidak
mungkin; untuk membuktikan sebuah proses berakhir, yang dibutuhkan adalah besaran yang
selalu bergerak ke satu arah dan tidak bisa bergerak selamanya.

**Pilih besarannya.** Ambil jumlah seluruh bilangan di papan:

$$S = \sum_{x \text{ di papan}} x$$

**Buktikan $S$ selalu turun.** Sebuah langkah mengganti $a$ dengan $a-b$, sedangkan bilangan
lain tidak disentuh. Maka

$$S' = S - a + (a - b) = S - b$$

Karena $b$ bilangan asli, $b \ge 1$, sehingga

$$S' \le S - 1$$

Jadi tiap langkah menurunkan $S$ sedikitnya satu. **$S$ tidak pernah naik dan tidak pernah
tetap.**

**Buktikan $S$ tidak bisa turun selamanya.** Di sinilah bagian yang paling sering dilewati.
Besaran yang selalu turun belum menjamin apa-apa — bilangan real bisa turun tanpa henti,
misalnya $1, \frac12, \frac14, \dots$.

Yang menutup celah itu adalah dua hal:

1. **$S$ selalu bilangan bulat.** Setiap bilangan di papan tetap bilangan asli: kalau
   $a > b$ dan keduanya asli, maka $a - b$ juga asli.
2. **$S$ terbatas di bawah.** Karena seluruh bilangan di papan paling sedikit $1$, dan
   banyaknya bilangan tidak pernah berubah — langkah itu mengganti, bukan menghapus —
   maka $S \ge n$ dengan $n$ banyaknya bilangan di papan.

Sebuah barisan bilangan bulat yang turun dan terbatas di bawah pasti berhingga. Kalau
prosesnya berjalan $k$ langkah, maka $S$ turun sedikitnya $k$, sehingga

$$S_0 - k \ \ge\ n \quad\Longrightarrow\quad k \ \le\ S_0 - n$$

Jadi banyaknya langkah tidak mungkin melebihi $S_0 - n$, yang berhingga. Prosesnya pasti
berhenti. $\blacksquare$

### Keadaan saat berhenti

Proses berhenti tepat ketika tidak ada dua bilangan dengan $a > b$ — yaitu ketika seluruh
bilangan di papan **sama besar**. Bilangan itu adalah faktor persekutuan terbesar dari
bilangan-bilangan awalnya, dan alasannya juga sebuah invarian: langkah $a \mapsto a-b$
tidak mengubah FPB seluruh bilangan di papan.

Jadi soal ini sebenarnya memuat keduanya sekaligus — monovarian yang menjamin berhenti, dan
invarian yang menentukan berhenti di mana. Prosesnya sendiri tidak lain algoritma Euklid
yang dijalankan pada banyak bilangan.

### Mengapa syarat "bilangan bulat" tidak boleh dilewati

Kalau bilangan di papan boleh bernilai real positif, prosesnya bisa berjalan selamanya.
Ambil $a = \sqrt2$ dan $b = 1$: langkah demi langkah menghasilkan $\sqrt2 - 1$, lalu
$\sqrt2 - 1$ dan $1$ berganti peran, dan seterusnya tanpa pernah bertemu dua bilangan yang
sama.

Perbedaan itu bukan kehalusan teknis — ia justru seluruh alasan mengapa monovarian bekerja.

## Rubrik

- Menyatakan bahwa yang dicari besaran yang selalu berubah satu arah, bukan yang kekal
- Memilih jumlah seluruh bilangan sebagai monovarian
- Menghitung $S' = S - b$ dan menyimpulkan penurunannya sedikitnya $1$
- Menyatakan $S$ selalu bilangan bulat, dengan alasan $a-b$ tetap bilangan asli
- Menyatakan $S$ terbatas di bawah, dengan alasan tiap bilangan paling sedikit $1$ dan banyaknya bilangan tetap
- Menyimpulkan barisan bulat yang turun dan terbatas di bawah pasti berhingga, sehingga proses berhenti
- Menyebut bahwa besaran yang turun saja belum cukup, misalnya lewat contoh bilangan real
