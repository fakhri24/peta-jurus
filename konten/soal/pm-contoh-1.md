---
id: pm-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi]
bentuk: isian
kesulitan: 2
jawaban: "1440"
---

## Soal

Tujuh orang berfoto berjajar dalam satu baris. Dua orang di antaranya, Ani dan Budi, ingin
berdiri **berdampingan**.

Ada berapa susunan yang mungkin?

## Petunjuk

- Selama Ani dan Budi tidak boleh terpisah, mereka selalu bergerak bersama. Perlakukan keduanya sebagai satu kesatuan.
- Setelah keduanya disatukan, berapa benda yang tersisa untuk disusun?
- Jangan lupa Ani dan Budi masih bisa bertukar tempat di dalam kesatuan itu.

## Pembahasan

**Ikat keduanya menjadi satu blok.** Karena Ani dan Budi harus selalu berdampingan, mereka
tidak pernah terpisah — jadi anggap saja keduanya satu benda.

Sekarang yang disusun adalah:

$$\underbrace{[\text{Ani–Budi}]}_{1 \text{ blok}}, \ \text{C}, \ \text{D}, \ \text{E}, \ \text{F}, \ \text{G}$$

yaitu $6$ benda. Menyusunnya berjajar:

$$6! = 720$$

**Susunan di dalam blok.** Blok itu sendiri bisa berisi Ani–Budi atau Budi–Ani:

$$2! = 2$$

**Gabungkan.** Tiap susunan blok bisa dipasangkan dengan tiap susunan di dalamnya:

$$720 \times 2 = \boxed{1440}$$

**Mengapa dikalikan $2$ dan bukan ditambah.** Menentukan letak blok dan menentukan urutan
di dalam blok adalah dua keputusan berurutan pada satu susunan yang sama, bukan dua jenis
susunan yang berbeda. Melupakan faktor $2$ adalah kekeliruan yang paling sering pada soal
berdampingan — dan hasilnya persis setengah dari yang benar.

**Cara memeriksa kewajarannya.** Tanpa syarat apa pun ada $7! = 5040$ susunan. Kalau dua
orang diambil acak, peluang keduanya berdampingan pada susunan tujuh orang adalah
$\frac{2}{7}$, sehingga perkiraannya $5040 \times \frac27 = 1440$. Cocok.

**Soal kebalikannya** — Ani dan Budi tidak boleh berdampingan — dikerjakan dengan
mengurangkan: $5040 - 1440 = 3600$. Pola "hitung yang berdampingan lalu kurangkan" itu
akan muncul lagi berkali-kali.
