---
id: ptl-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ptolemy, pythagoras]
bentuk: isian
kesulitan: 2
jawaban: "10"
---

## Soal

Persegi panjang $ABCD$ mempunyai $AB = 8$ dan $BC = 6$.

Dengan memakai teorema Ptolemy, tentukan panjang diagonal $AC$.

## Petunjuk

- Ptolemy hanya berlaku untuk segiempat talibusur. Apakah persegi panjang selalu punya lingkaran luar?
- Keempat sudutnya siku-siku, jadi sudut yang berhadapan berjumlah $180^\circ$ — syarat segiempat talibusur.
- Pada persegi panjang, kedua diagonalnya sama panjang. Sebut keduanya $d$, lalu tulis Ptolemy.

## Pembahasan

**Periksa bahwa Ptolemy boleh dipakai.** Persegi panjang punya keempat sudut $90^\circ$,
sehingga tiap pasang sudut berhadapan berjumlah $180^\circ$. Itu tepat syarat sebuah
segiempat punya lingkaran luar, jadi **setiap persegi panjang adalah segiempat talibusur** —
lingkaran luarnya berpusat di titik potong diagonalnya.

**Tulis Ptolemy.** Sisi berhadapan: $AB$ dengan $CD$, dan $BC$ dengan $AD$. Pada persegi
panjang $AB = CD = 8$ dan $BC = AD = 6$. Kedua diagonalnya sama panjang, sebut $d$:

$$AC \cdot BD = AB \cdot CD + BC \cdot AD$$

$$d \cdot d = 8 \times 8 + 6 \times 6$$

$$d^2 = 64 + 36 = 100 \quad \Longrightarrow \quad d = \boxed{10}$$

### Yang barusan terjadi adalah Pythagoras

Tulis ulang langkahnya dengan huruf. Untuk persegi panjang bersisi $p$ dan $q$, Ptolemy
memberi

$$d^2 = p^2 + q^2$$

Itu **teorema Pythagoras**, muncul sebagai kasus khusus Ptolemy — sebab diagonal persegi
panjang memang sisi miring segitiga siku-siku bersisi $p$ dan $q$.

Jadi Ptolemy bukan cuma teorema tentang lingkaran; ia perluasan Pythagoras ke segiempat
talibusur sembarang. Itu sudut pandang yang menjelaskan mengapa bentuknya "hasil kali sama
dengan jumlah hasil kali".

### Periksa dengan cara biasa

Segitiga $ABC$ siku-siku di $B$:

$$AC = \sqrt{8^2 + 6^2} = \sqrt{100} = 10 \quad ✓$$

Segitiga $6$-$8$-$10$ adalah kelipatan dua dari $3$-$4$-$5$.

### Kapan sebuah segiempat punya lingkaran luar

Langkah pertama tadi patut diingat sebagai daftar, sebab Ptolemy tidak boleh dipakai tanpa
memastikannya:

- **sudut berhadapan berjumlah $180^\circ$** — syarat baku;
- semua persegi panjang (termasuk persegi) memenuhinya;
- semua trapesium sama kaki memenuhinya;
- **jajaran genjang yang bukan persegi panjang tidak memenuhinya**, sebab sudut
  berhadapannya sama besar, dan dua sudut sama yang berjumlah $180^\circ$ berarti keduanya
  $90^\circ$;
- belah ketupat yang bukan persegi juga tidak.

Untuk segiempat yang bukan talibusur, yang berlaku hanya **ketaksamaan** Ptolemy — dengan
tanda kurang dari. Coba pada jajaran genjang bersisi $8$ dan $6$ dengan sudut $60^\circ$:
diagonalnya $\sqrt{64+36-48} = \sqrt{52}$ dan $\sqrt{64+36+48} = \sqrt{148}$, hasil kalinya
$\sqrt{7696} \approx 87{,}7 < 100$ ✓ — memang lebih kecil, persis seperti yang dijanjikan
ketaksamaannya.
