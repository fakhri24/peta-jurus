---
id: sarang-merpati
nama: Prinsip Sarang Merpati
pilar: kombinatorika
tahap: osn-k
prasyarat: [aturan-pencacahan]
contoh: [smp-contoh-1]
latihan: [smp-01, smp-02, smp-03, smp-04, smp-05, smp-06]
---

## Kapan dipakai

Soal meminta **membuktikan ada** sesuatu, tanpa menyuruh menemukannya: "tunjukkan pasti ada
dua orang yang…", "buktikan di antara bilangan itu ada yang…". Kalau soal menanyakan
*berapa banyak*, ini bukan jurusnya.

Pemicu lain yang sering: ada bilangan yang terasa aneh besarnya — "di antara 13 orang",
"dari 101 bilangan". Angka seperti itu biasanya satu lebih banyak dari sesuatu, dan
tugasmu menemukan sesuatu itu.

## Intinya

Kalau $n$ objek dimasukkan ke $k$ kotak dan $n > k$, ada kotak yang berisi paling sedikit
dua objek.

Bentuk yang lebih berguna di olimpiade:

$$\left\lceil \frac{n}{k} \right\rceil$$

yaitu ada kotak yang berisi paling sedikit sebanyak itu.

**Menerapkan prinsipnya cuma satu baris; pekerjaan sesungguhnya memilih kotaknya.** Soal
hampir tidak pernah memberi tahu apa yang jadi merpati dan apa yang jadi sarang — itu yang
harus kamu karang. Sarang yang sering menolong: sisa pembagian, selang bilangan, pasangan
yang jumlahnya tetap, dan petak papan.

Prinsip ini menjamin **ada**; ia tidak pernah menunjukkan yang mana.

## Jebakan umum

- **Terbalik arah.** Merpatinya yang harus lebih banyak dari sarangnya, bukan sebaliknya.
- **Sarang terlalu banyak.** Kalau kotaknya sebanyak objeknya, kesimpulannya kosong. Sarang
  harus dibuat cukup sedikit supaya ada yang terpaksa berbagi.
- **Menuntut prinsipnya menunjuk.** Kesimpulannya "ada", dan soal yang bertanya "yang mana"
  memang meminta jurus lain.
