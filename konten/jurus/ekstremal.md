---
id: ekstremal
nama: Prinsip Ekstremal
pilar: kombinatorika
tahap: osn
prasyarat: [sarang-merpati, graf-dasar]
contoh: [eks-contoh-1]
latihan: [eks-01, eks-02, eks-03, eks-04, eks-05, eks-06]
---

## Kapan dipakai

Soal meminta membuktikan sesuatu **ada** atau **tidak mungkin** pada susunan berhingga,
dan tidak ada titik masuk yang jelas — tidak ada rumus untuk dipakai, tidak ada yang bisa
dihitung langsung. Pemicunya justru ketiadaan itu: soal memberi konfigurasi tanpa struktur
apa pun, lalu meminta kesimpulan.

Kalau kamu terjebak pada soal semacam itu, pertanyaan yang hampir selalu membuka jalan
adalah: objek mana yang paling?

## Intinya

Pilih objek yang **paling** — terbesar, terkecil, terpanjang, berderajat tertinggi, paling
kiri. Lalu tunjukkan bahwa objek terpilih itu harus punya sifat tertentu, biasanya dengan
mengandaikan sebaliknya dan membangun objek yang **lebih ekstrem lagi**. Itu mustahil,
karena objek yang paling sudah dipilih.

Yang membuat langkah itu sah adalah **kehinggaan**: himpunan berhingga yang tidak kosong
selalu punya anggota terbesar dan terkecil. Pada himpunan tak berhingga, jaminan itu
hilang.

Penerapan bakunya pada graf: ambil lintasan **terpanjang**, lalu perhatikan titik
ujungnya. Semua tetangga titik itu harus berada di dalam lintasan — sebab kalau ada
tetangga di luar, lintasannya bisa diperpanjang, dan itu bertentangan dengan pemilihan
tadi. Dari satu pengamatan itu banyak soal langsung selesai.

Kembarannya di teori bilangan adalah turun tak hingga: keduanya bersandar pada kenyataan
bahwa tidak ada barisan bilangan asli yang turun selamanya.

## Jebakan umum

- **Memakainya pada himpunan tak berhingga.** Tanpa alasan bahwa maksimumnya benar-benar
  ada, seluruh buktinya runtuh.
- **Memilih besaran ekstrem yang tidak dipakai lagi.** Kalau setelah memilih "yang
  terbesar" sifat itu tidak pernah dipakai untuk menyimpulkan apa pun, pilihannya keliru —
  ganti besarannya.
- **Mengira objek terekstrem itu tunggal.** Boleh ada beberapa yang sama-sama terbesar;
  buktinya harus tetap jalan untuk salah satu di antaranya.
