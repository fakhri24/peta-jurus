---
id: pencacahan-ganda
nama: Pencacahan Ganda
pilar: kombinatorika
tahap: osn-p
prasyarat: [kombinasi]
contoh: []
latihan: []
---

## Kapan dipakai

Soal meminta membuktikan sebuah **identitas** pencacahan, atau menghitung sesuatu yang
sukar didekati langsung tetapi mudah kalau dilihat dari sisi lain. Pemicu yang khas: ada
dua kelompok objek dan sebuah hubungan di antara keduanya — siswa dan klub, titik dan
garis, orang dan jabat tangan.

Kalau soal berbentuk "buktikan $A = B$" dengan kedua sisi berupa jumlah pencacahan, hampir
selalu ada satu himpunan yang dihitung dua kali.

## Intinya

Hitung anggota **satu himpunan yang sama** dengan dua cara berbeda. Kedua hasilnya wajib
sama, dan persamaan itulah yang dicari.

Bentuk yang paling sering dipakai adalah tabel berisi $0$ dan $1$: jumlah seluruh isinya
bisa dihitung baris demi baris atau kolom demi kolom.

$$\sum_{i} r_i = \sum_{j} c_j$$

Contoh yang paling dikenal adalah lema jabat tangan pada graf: menjumlahkan derajat semua
titik berarti menghitung tiap ruas dua kali, sekali dari tiap ujungnya.

$$\sum_{v} \deg(v) = 2|E|$$

**Kuncinya menyebutkan dengan jelas apa yang sedang dicacah** — biasanya berupa pasangan
$(a, b)$ yang memenuhi suatu hubungan. Kalau himpunannya sudah dinyatakan tepat, kedua cara
menghitungnya biasanya muncul sendiri.

## Jebakan umum

- **Dua cara yang sebenarnya satu.** Kalau cara kedua cuma menyusun ulang cara pertama,
  persamaan yang keluar sepele dan tidak membuktikan apa-apa.
- **Himpunannya tidak sama persis.** Kedua hitungan harus mencacah objek yang sama,
  bukan dua himpunan yang mirip.
- **Tidak menyatakan apa yang dicacah.** Tanpa itu, bukti jadi rangkaian rumus yang tidak
  bisa diperiksa — dan biasanya di situlah kekeliruannya bersembunyi.
