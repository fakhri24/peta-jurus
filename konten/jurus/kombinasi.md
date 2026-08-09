---
id: kombinasi
nama: Kombinasi
pilar: kombinatorika
tahap: osn-k
prasyarat: [permutasi]
contoh: [kb-contoh-1]
latihan: [kb-01, kb-02, kb-03, kb-04, kb-05, kb-06]
---

## Kapan dipakai

Memilih $k$ objek dari $n$ objek berbeda, **urutan tidak penting**. Uji cepatnya kebalikan
dari permutasi: kalau menukar dua objek terpilih menghasilkan pilihan yang dianggap
**sama**, ini kombinasi.

Kata yang biasa muncul: dipilih, diambil, dibentuk tim, dibentuk himpunan bagian, ditarik
dari kotak sekaligus.

## Intinya

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!} = \frac{P(n,k)}{k!}$$

Bentuk kedua yang menjelaskan asalnya: hitung dulu susunannya seolah urutan penting, lalu
bagi $k!$ — karena tiap kumpulan yang sama terhitung $k!$ kali, sekali untuk tiap cara
mengurutkannya. Membagi seperti ini adalah cara berpikir yang dipakai lagi di banyak jurus
lain.

Sifat yang paling sering memendekkan hitungan:

$$\binom{n}{k} = \binom{n}{n-k}$$

Memilih $k$ yang masuk sama saja dengan memilih $n-k$ yang keluar. Kalau $k$ besar, hitung
lewat sisi satunya.

Nilai tepinya $\binom{n}{0} = \binom{n}{n} = 1$.

**Memilih sekaligus versus berurutan.** "Diambil 3 bola sekaligus" adalah kombinasi;
"diambil satu per satu tanpa dikembalikan lalu dicatat urutannya" adalah permutasi. Soal
biasanya menyatakan ini dengan satu kata saja, dan kata itu menentukan seluruh jawabannya.

## Jebakan umum

- **Urutan ternyata berarti.** Jabatan ketua–sekretaris–bendahara bukan sekadar memilih tiga
  orang; ketiganya bisa ditukar dan hasilnya berbeda.
- **Objek yang boleh diambil berulang.** Rumus ini menganggap tiap objek terpilih paling
  banyak sekali.
- **Objeknya ternyata tidak berbeda.** Kalau bolanya sewarna dan tidak bisa dibedakan, yang
  dicacah bukan lagi pilihan objek melainkan pembagian jumlah.
