---
id: pyt-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [pythagoras]
bentuk: isian
kesulitan: 2
jawaban: "210"
---

## Soal

Sebuah segitiga mempunyai panjang sisi $20$, $21$, dan $29$.

Tentukan luas segitiga itu.

## Petunjuk

- Untuk menghitung luas kamu perlu alas dan tinggi, dan tinggi tidak diberikan. Sebelum mencarinya, periksa dulu apakah segitiga ini punya bentuk istimewa.
- Bandingkan jumlah kuadrat dua sisi terpendek dengan kuadrat sisi terpanjang.
- Kalau $a^2 + b^2 = c^2$, maka sudut di hadapan $c$ siku-siku — dan kedua sisi lainnya menjadi alas dan tinggi sekaligus.

## Pembahasan

**Periksa jenisnya lebih dulu.** Sisi terpanjang $29$. Bandingkan:

$$20^2 + 21^2 = 400 + 441 = 841 \qquad \text{dan} \qquad 29^2 = 841$$

Keduanya sama. Menurut **kebalikan Pythagoras**, sudut di hadapan sisi $29$ siku-siku.

**Pakai kedua sisi siku-sikunya sebagai alas dan tinggi.** Pada segitiga siku-siku, kedua sisi
siku-sikunya saling tegak lurus — jadi salah satunya boleh dipakai sebagai alas dan yang lain
langsung menjadi tingginya, tanpa perlu menarik garis tinggi apa pun:

$$L = \tfrac{1}{2} \times 20 \times 21 = \boxed{210}$$

### Kebalikan Pythagoras adalah alat pemeriksa bentuk

Yang baru saja dipakai bukan Pythagoras, melainkan **kebalikannya**: dari panjang ke sudut,
bukan dari sudut ke panjang. Perbedaan arah itu penting, sebab arah inilah yang menjawab
pertanyaan "segitiga macam apa ini" tanpa mengukur satu sudut pun.

Perbandingannya bahkan memberi lebih dari sekadar siku-siku:

| Hubungan | Sudut di hadapan sisi terpanjang |
|---|---|
| $a^2 + b^2 > c^2$ | lancip |
| $a^2 + b^2 = c^2$ | siku-siku |
| $a^2 + b^2 < c^2$ | tumpul |

Karena itu, tiap kali soal memberi tiga panjang sisi, satu perkalian singkat sudah memberitahu
bentuk segitiganya.

### Periksa dengan Heron

Setengah kelilingnya $s = \dfrac{20+21+29}{2} = 35$, sehingga

$$L = \sqrt{35 \times 15 \times 14 \times 6} = \sqrt{44100} = 210$$

Cocok. Heron selalu bisa dipakai dan tidak memerlukan pemeriksaan bentuk sama sekali —
tetapi perhatikan ongkosnya: satu akar dari bilangan lima angka, melawan satu perkalian.
Memeriksa bentuknya lebih dulu bukan sekadar rapi, ia benar-benar memangkas pekerjaan.

### Kalau angkanya diubah sedikit

Untuk sisi $20$, $21$, dan $30$: $400 + 441 = 841 < 900$, jadi segitiganya **tumpul**. Untuk
sisi $20$, $21$, dan $28$: $841 > 784$, jadi **lancip**. Ketiganya segitiga yang sah — yang
berubah cuma jenisnya, dan hanya perbandingan itu yang memberitahunya.
