---
id: teori-permainan
nama: Teori Permainan
pilar: kombinatorika
tahap: osn
prasyarat: [invarian, rekursi]
contoh: []
latihan: []
---

## Kapan dipakai

Dua pemain bergantian melangkah, keduanya melihat seluruh keadaan, tidak ada unsur
peluang, dan permainannya pasti berakhir. Soal menanyakan **siapa yang punya strategi
menang** — bukan bagaimana bermain baik, melainkan siapa yang pasti menang kalau
keduanya bermain sempurna.

Pemicunya: mengambil batu dari tumpukan bergantian, menulis bilangan bergantian, mewarnai
petak bergantian, dan yang tidak bisa melangkah dinyatakan kalah.

## Intinya

Tandai tiap keadaan dengan salah satu dari dua huruf:

- **N** — pemain yang mendapat giliran di keadaan itu menang.
- **P** — pemain sebelumnya yang menang, artinya yang mendapat giliran kalah.

Aturannya menurunkan diri sendiri, dan di situlah rekursinya:

- Keadaan yang tidak punya langkah sama sekali adalah **P**.
- Sebuah keadaan adalah **N** kalau ada **satu** langkah menuju keadaan P.
- Sebuah keadaan adalah **P** kalau **semua** langkahnya menuju keadaan N.

Kerjakan mundur dari keadaan terkecil. Pola keadaan P biasanya muncul setelah beberapa
suku, dan bentuknya sering berupa keterbagian — misalnya sisa tertentu modulo suatu
bilangan.

**Strategi pencerminan.** Kalau kamu bisa selalu mengembalikan permainan ke keadaan
simetris setelah langkah lawan, kamu tidak pernah kehabisan langkah lebih dulu. Ini cara
tercepat menyelesaikan banyak soal permainan.

Menemukan pola P bukan akhir pekerjaan: **buktikan** bahwa dari keadaan P setiap langkah
menuju N, dan dari N ada langkah menuju P.

## Jebakan umum

- **Menemukan satu langkah bagus lalu berhenti.** Strategi menang harus punya jawaban
  untuk **setiap** langkah lawan, bukan untuk satu langkah yang kamu bayangkan.
- **Salah menetapkan siapa yang kalah.** "Yang tidak bisa melangkah kalah" dan "yang
  mengambil batu terakhir kalah" menghasilkan pola P yang berbeda.
- **Menebak pola dari terlalu sedikit keadaan.** Empat suku pertama sering menyesatkan;
  hitung sampai polanya berulang meyakinkan, lalu buktikan.
