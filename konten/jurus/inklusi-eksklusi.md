---
id: inklusi-eksklusi
nama: Inklusi–Eksklusi
pilar: kombinatorika
tahap: osn-k
prasyarat: [aturan-pencacahan]
contoh: []
latihan: []
---

## Kapan dipakai

Kamu menjumlahkan beberapa kelompok, tapi kelompoknya **beririsan** — ada anggota yang
kena hitung lebih dari sekali. Pemicu paling terang: kata "atau", "habis dibagi 3 atau 5",
"paling sedikit satu di antaranya", dan soal yang memberi data "yang ikut keduanya
sebanyak …".

## Intinya

Ini aturan jumlah yang diperbaiki. Aturan jumlah hanya sah kalau kelompoknya lepas; kalau
tidak, kelebihannya dikurangi — lalu yang terlanjur terlalu banyak dikurangi dikembalikan.

$$|A \cup B| = |A| + |B| - |A \cap B|$$

$$|A \cup B \cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|$$

Polanya berselang-seling, dan bentuk umumnya:

$$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{k=1}^{n} (-1)^{k-1} \sum_{|S|=k} \left|\bigcap_{i \in S} A_i\right|$$

Bacaannya sederhana: irisan berjumlah ganjil ditambah, berjumlah genap dikurangi. Dengan
begitu setiap anggota gabungan terhitung tepat sekali, berapa pun kelompok yang memuatnya.

Sering lebih pendek dipakai lewat komplemen: "tidak memenuhi satu pun syarat" adalah
seluruhnya dikurangi gabungannya.

## Jebakan umum

- **Berhenti di pengurangan pertama.** Untuk tiga himpunan, mengurangi ketiga irisan
  berpasangan membuat anggota yang ada di ketiganya hilang sama sekali — ia harus
  dikembalikan.
- **Salah tanda di suku terakhir.** Untuk $n$ himpunan, tandanya $(-1)^{n-1}$, jadi
  bergantung pada ganjil-genapnya $n$.
- **Mengarang $|A \cap B|$.** Ukuran irisan adalah data atau hasil hitungan, bukan
  $|A|\cdot|B|$ — itu keliru kecuali ada alasan tersendiri.
