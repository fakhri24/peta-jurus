---
id: bij-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [bijeksi]
bentuk: isian
kesulitan: 3
jawaban: "512"
---

## Soal

Ada berapa himpunan bagian dari $\{1, 2, 3, \dots, 10\}$ yang **banyak anggotanya genap**?
(Himpunan kosong ikut terhitung.)

## Petunjuk

- Menjumlahkan $\binom{10}{0} + \binom{10}{2} + \cdots$ bisa, tetapi ada padanan yang menyelesaikannya tanpa menghitung satu koefisien pun.
- Pasangkan tiap himpunan berukuran genap dengan sebuah himpunan berukuran ganjil, lewat aturan yang membalik satu unsur tertentu.
- Kalau padanannya sah, kedua kelompok sama banyaknya — dan jumlah keduanya sudah diketahui.

## Pembahasan

**Bangun padanannya.** Sebut $G$ kumpulan himpunan bagian berukuran genap dan $J$ yang
berukuran ganjil. Tetapkan sebuah unsur, misalnya $1$, lalu tentukan aturan:

$$f(A) = \begin{cases} A \cup \{1\} & \text{kalau } 1 \notin A \\ A \setminus \{1\} & \text{kalau } 1 \in A\end{cases}$$

yaitu **balikkan keanggotaan unsur $1$**.

**Aturan ini selalu mengubah paritas ukuran.** Menambahkan $1$ menaikkan ukurannya satu;
membuangnya menurunkannya satu. Jadi $f$ memetakan $G$ ke $J$ dan sebaliknya.

**Periksa padanannya sah.** Menerapkan $f$ dua kali mengembalikan himpunan semula:

$$f\bigl(f(A)\bigr) = A$$

sebab membalik dua kali sama dengan tidak membalik. Karena $f$ adalah kebalikan dari dirinya
sendiri, ia satu-satu dan pada.

**Simpulkan.** Padanan itu menunjukkan

$$|G| = |J|$$

Sementara keduanya bersama-sama adalah seluruh himpunan bagian:

$$|G| + |J| = 2^{10} = 1024$$

Maka

$$|G| = \frac{1024}{2} = \boxed{512}$$

**Periksa dengan menjumlahkan langsung.**

$$\binom{10}{0} + \binom{10}{2} + \binom{10}{4} + \binom{10}{6} + \binom{10}{8} + \binom{10}{10}$$

$$= 1 + 45 + 210 + 210 + 45 + 1 = 512$$

Cocok — tetapi menuntut enam koefisien, sedangkan padanan tadi tidak menuntut satu pun.

**Perhatikan padanan ini tidak peduli pada angka $10$.** Untuk sebarang $n \ge 1$, aturan
yang sama membuktikan himpunan bagian berukuran genap dan ganjil sama banyaknya, yaitu
$2^{\,n-1}$ masing-masing. Ini setara dengan identitas

$$\sum_{k} (-1)^k \binom{n}{k} = 0 \qquad (n \ge 1)$$

yang biasanya dibuktikan dengan mensubstitusi $x = -1$ ke $(1+x)^n$. Padanan tadi
membuktikannya tanpa aljabar sama sekali.

**Syarat $n \ge 1$ tidak boleh dilupakan.** Untuk $n = 0$ hanya ada satu himpunan bagian,
yaitu himpunan kosong, dan ukurannya genap — sehingga $|G| = 1$ dan $|J| = 0$. Padanannya
gagal karena tidak ada unsur yang bisa dibalik, dan justru di situ terlihat bahwa
keberadaan unsur tetap seperti $1$ adalah syarat yang sungguh dipakai.
