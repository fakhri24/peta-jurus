---
id: pewarnaan
nama: Pewarnaan
pilar: kombinatorika
tahap: osn
prasyarat: [invarian]
contoh: [pwn-contoh-1]
latihan: [pwn-01, pwn-02, pwn-03, pwn-04, pwn-05, pwn-06]
---

## Kapan dipakai

Sebuah papan atau bidang harus ditutup ubin, dan soal menanyakan **mungkin atau tidak** —
bukan berapa banyak caranya. Pemicu paling khas: papan catur yang beberapa petaknya
dibuang, penutupan dengan domino atau trimino, dan bidak yang bergerak menurut aturan
tetap.

Kalau kamu sudah mencoba menutup papannya berkali-kali dan selalu tersisa dua petak yang
tidak bertetangga, itu tandanya.

## Intinya

Warnai petaknya sedemikian rupa sehingga tiap ubin — di mana pun diletakkan dan bagaimana
pun diputar — menutup **sejumlah warna yang tetap**. Setelah itu hitung persediaan warna di
papan. Kalau angkanya tidak cocok, penutupannya mustahil.

Pewarnaan adalah invarian yang dipilih dengan sengaja: yang tidak berubah adalah selisih
antara warna yang tertutup dan warna yang tersedia.

Beberapa pewarnaan baku:

- **Dua warna papan catur.** Domino selalu menutup tepat satu petak hitam dan satu putih,
  jadi papan yang jumlah hitam dan putihnya tidak sama tidak bisa ditutup domino.
- **Pewarnaan bergaris**, mewarnai kolom berselang-seling atau bergantian tiga warna,
  dipakai untuk ubin yang panjangnya tiga.
- **Pewarnaan modulo**, memberi petak $(i,j)$ warna menurut $i + j$ atau $i - j$ modulo
  suatu bilangan.

Kalau satu pewarnaan tidak memberi kesimpulan, biasanya bukan jurusnya yang salah —
melainkan warnanya yang perlu diganti.

## Jebakan umum

- **Pewarnaan yang tidak memberi jumlah tetap.** Kalau sebuah ubin bisa menutup dua hitam
  pada satu peletakan dan satu hitam pada peletakan lain, hitungan warnanya tidak
  menyimpulkan apa-apa.
- **Menyimpulkan "mungkin" karena warnanya cocok.** Cocok cuma berarti belum tertutup
  kemungkinannya; untuk menunjukkan bisa, gambarkan penutupannya.
- **Berhenti pada dua warna.** Banyak soal ubin tiga petak baru terpecahkan dengan tiga
  warna atau dengan pewarnaan diagonal.
