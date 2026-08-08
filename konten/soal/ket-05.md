---
id: ket-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [keterbagian]
bentuk: isian
kesulitan: 2
jawaban: "30"
---

## Soal

Bilangan bulat positif $n$ habis dibagi $6$, dan $n^2$ habis dibagi $45$. Tentukan nilai
terkecil $n$ yang mungkin.

## Petunjuk

- Ada dua syarat sekaligus. Pecah keduanya menjadi syarat atas faktor-faktor prima.
- $45 = 3^2 \times 5$. Kalau $5$ membagi $n^2$, apa yang bisa kamu simpulkan tentang $n$ sendiri?
- Karena $5$ prima, $5 \mid n^2$ memaksa $5 \mid n$. Sekarang gabungkan dengan $6 \mid n$.

## Pembahasan

Terjemahkan kedua syarat ke dalam faktor prima.

Syarat pertama: $6 = 2 \times 3$, jadi $2 \mid n$ dan $3 \mid n$.

Syarat kedua: $45 = 3^2 \times 5$, jadi $9 \mid n^2$ dan $5 \mid n^2$.

Bagian $5 \mid n^2$ itu yang menentukan. Karena $5$ prima, kalau $5$ membagi hasil kali
$n \times n$ maka $5$ harus membagi salah satu faktornya — dan kedua faktornya sama, jadi
$5 \mid n$.

Bagian $9 \mid n^2$ tidak menambah apa pun: dari $3 \mid n$ sudah otomatis $9 \mid n^2$.

Jadi $n$ habis dibagi $2$, $3$, dan $5$ sekaligus, sehingga $30 \mid n$. Nilai terkecilnya

$$n = \boxed{30}$$

Periksa: $30$ habis dibagi $6$, dan $30^2 = 900 = 45 \times 20$.

Langkah $5 \mid n^2 \Rightarrow 5 \mid n$ bertumpu pada $5$ yang prima. Untuk modulus yang
bukan prima langkah itu tidak sah — misalnya $4 \mid 6^2$ padahal $4 \nmid 6$.
