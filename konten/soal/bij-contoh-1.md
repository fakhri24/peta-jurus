---
id: bij-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [bijeksi]
bentuk: isian
kesulitan: 3
jawaban: "256"
---

## Soal

Ada berapa himpunan bagian dari $\{1, 2, 3, \dots, 8\}$?

Kerjakan dengan membangun padanan satu-satu ke sebuah himpunan yang sudah kamu tahu cara
menghitungnya.

## Petunjuk

- Membentuk himpunan bagian sama artinya dengan mengambil keputusan untuk tiap unsur. Bagaimana keputusan itu bisa dicatat?
- Catat keputusannya sebagai barisan $0$ dan $1$ sepanjang delapan — satu tempat untuk tiap unsur.
- Untuk memastikan padanannya sah, tunjukkan cara membacanya kembali dari barisan menjadi himpunan.

## Pembahasan

**Bangun padanannya.** Untuk tiap himpunan bagian $A \subseteq \{1,\dots,8\}$, tuliskan
barisan $\left(b_1, b_2, \dots, b_8\right)$ dengan

$$b_i = \begin{cases} 1 & \text{kalau } i \in A \\ 0 & \text{kalau } i \notin A\end{cases}$$

Contohnya $A = \{1,3,8\}$ menjadi $10100001$, dan $A = \varnothing$ menjadi $00000000$.

**Periksa arah sebaliknya.** Dari sebarang barisan $0$ dan $1$ sepanjang $8$, bacalah
kembali himpunannya: masukkan $i$ ke dalam $A$ tepat ketika $b_i = 1$. Cara ini selalu
memberi sebuah himpunan bagian yang sah.

**Kedua arah saling meniadakan.** Menulis himpunan menjadi barisan lalu membacanya kembali
mengembalikan himpunan yang sama, dan sebaliknya. Karena itu padanannya **satu-satu dan
pada**, sehingga kedua himpunan sama banyaknya.

**Cacah barisannya.** Tiap tempat punya $2$ pilihan, dan ada $8$ tempat:

$$2^8 = \boxed{256}$$

**Mengapa arah sebaliknya perlu diperiksa.** Padanan satu arah saja hanya menunjukkan
himpunan bagiannya **tidak lebih banyak** daripada barisannya. Untuk menyimpulkan sama
banyaknya, harus ditunjukkan tidak ada barisan yang terlewat — dan itu yang dikerjakan oleh
cara pembacaan tadi.

Kelalaian ini bukan kehalusan tanpa akibat. Kalau padanannya diubah menjadi "tulis unsur
$A$ berurutan lalu isi sisanya dengan nol", maka $\{1,2\}$ dan $\{2,1\}$ memberi barisan
yang sama, sementara sebagian barisan tidak pernah tercapai — dan pencacahannya salah.

**Cara pandang ini terpakai jauh lebih luas.** Begitu sebuah objek berhasil ditulis sebagai
**barisan keputusan**, mencacahnya berubah menjadi mengalikan banyaknya pilihan tiap
keputusan. Soal jalur pada kisi, susunan bintang dan sekat, serta himpunan bagian tanpa dua
unsur berurutan semuanya diselesaikan dengan cara yang sama — yang berbeda hanya barisan
apa yang dipilih.
