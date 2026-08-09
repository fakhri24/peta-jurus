---
id: permutasi-siklik
nama: Permutasi Siklik
pilar: kombinatorika
tahap: osn-k
prasyarat: [permutasi]
contoh: [psk-contoh-1]
latihan: [psk-01, psk-02, psk-03, psk-04, psk-05, psk-06]
---

## Kapan dipakai

Menyusun objek **melingkar**: duduk mengelilingi meja bundar, manik pada gelang, orang
membentuk lingkaran. Yang membedakannya dari permutasi biasa adalah tidak adanya posisi
pertama — susunan yang bisa diputar menjadi satu sama lain dianggap **sama**.

Bacalah soalnya sekali lagi untuk satu hal: apakah kursinya bernomor? Kalau bernomor,
lingkarannya cuma gambar, dan yang berlaku permutasi biasa.

## Intinya

Menyusun $n$ objek berbeda melingkar:

$$(n-1)!$$

Alasannya bukan hafalan: patok satu objek di satu tempat — boleh, karena memutar tidak
membuat susunan baru — lalu susun $n-1$ sisanya berjajar searah jarum jam.

Cara lain sampai ke sana: ada $n!$ susunan berjajar, dan tiap susunan melingkar
bersesuaian dengan tepat $n$ di antaranya, sekali untuk tiap kemungkinan pemutaran. Jadi
$n!/n = (n-1)!$.

**Kalau pantulan juga tidak membedakan** — kalung yang boleh dibalik, atau lingkaran yang
dilihat dari dua sisi — bagi dua lagi:

$$\frac{(n-1)!}{2} \qquad (n \ge 3)$$

Untuk $n = 1$ dan $n = 2$ pembagian itu tidak berlaku, karena membalik tidak menghasilkan
apa pun yang baru untuk dihilangkan.

## Jebakan umum

- **Memakai $n!$ untuk susunan melingkar,** sehingga tiap susunan terhitung $n$ kali.
- **Membagi dua padahal soal tidak menyamakan pantulan.** Orang yang duduk mengelilingi
  meja punya kiri dan kanan; kalung yang tergeletak boleh dibalik. Keduanya berbeda.
- **Meja bernomor dianggap melingkar.** Begitu tempatnya bisa dibedakan, memutar
  menghasilkan susunan yang lain, dan jawabannya kembali $n!$.
