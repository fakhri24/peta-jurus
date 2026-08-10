---
id: pyt-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [pythagoras]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Segitiga $ABC$ siku-siku di $C$. Dari $C$ ditarik garis tinggi ke sisi miring $AB$, memotongnya
di titik $D$.

![Segitiga ABC siku-siku di C dengan sisi miring AB mendatar. Dari C ditarik garis tinggi yang memotong sisi miring tegak lurus di titik D, membagi AB menjadi potongan AD yang pendek dan DB yang lebih panjang](siku-siku-garis-tinggi.svg)

Diketahui $AD = 4$ dan $DB = 9$.

Tentukan panjang $CD$.

## Petunjuk

- Sisi miringnya kini terbagi dua, jadi panjang $AB$ sudah kamu ketahui. Cari besaran lain yang bisa dihitung dari situ.
- Namai $CD = h$, $CA = b$, dan $CB = a$. Ada tiga segitiga siku-siku di gambar itu, dan tiap satu memberi satu persamaan.
- Tuliskan Pythagoras pada ketiganya, lalu jumlahkan dua yang kecil dan bandingkan dengan yang besar.

## Pembahasan

**Kumpulkan yang diketahui.**

$$AB = AD + DB = 4 + 9 = 13$$

Namai $CD = h$, $CA = b$, $CB = a$.

**Tuliskan Pythagoras pada ketiga segitiga siku-siku di gambar.**

$$\triangle ADC: \quad b^2 = h^2 + 4^2$$

$$\triangle BDC: \quad a^2 = h^2 + 9^2$$

$$\triangle ACB: \quad a^2 + b^2 = 13^2$$

**Gabungkan.** Masukkan dua yang pertama ke yang ketiga:

$$\left(h^2 + 81\right) + \left(h^2 + 16\right) = 169$$

$$2h^2 + 97 = 169 \quad \Longrightarrow \quad 2h^2 = 72 \quad \Longrightarrow \quad h^2 = 36$$

$$h = \boxed{6}$$

**Periksa.** Dengan $h = 6$: $b^2 = 36 + 16 = 52$ dan $a^2 = 36 + 81 = 117$. Jumlahnya
$52 + 117 = 169 = 13^2$ ✓.

Perhatikan bahwa $a$ dan $b$ sendiri tidak bulat — $b = 2\sqrt{13}$ dan $a = 3\sqrt{13}$ —
tetapi $h$ bulat. Kalau kamu berhenti karena merasa "angkanya jadi jelek", kamu berhenti tepat
satu langkah sebelum jawabannya.

### Hubungan yang baru saja kamu turunkan

Yang tersisa dari perhitungan di atas adalah

$$h^2 = AD \times DB = 4 \times 9 = 36$$

Ini salah satu dari tiga hubungan pada segitiga siku-siku bergaris tinggi:

$$h^2 = pq, \qquad a^2 = cp, \qquad b^2 = cq$$

dengan $p$ dan $q$ potongan sisi miringnya dan $c = p + q$. Periksa dua yang lain pada soal
ini: $b^2 = 13 \times 4 = 52$ ✓ dan $a^2 = 13 \times 9 = 117$ ✓.

Menghafalnya menghemat waktu, tetapi menurunkannya ulang — seperti yang baru saja dikerjakan —
tidak lebih dari tiga baris, dan itu jaring pengaman kalau ingatanmu tertukar antara $pq$ dan
$cp$.

### Cara ketiga: lewat luas

Luas $\triangle ACB$ bisa dihitung dua kali. Dengan kedua sisi siku-siku sebagai alas dan
tinggi, luasnya $\tfrac{1}{2}ab$; dengan sisi miring sebagai alas, luasnya
$\tfrac{1}{2} \times 13 \times h$. Menyamakan keduanya memberi

$$ab = 13h$$

Cek: $ab = 2\sqrt{13} \times 3\sqrt{13} = 6 \times 13 = 78$, dan $13h = 78$ ✓. Menghitung satu
besaran dengan dua cara berbeda adalah salah satu sumber persamaan paling murah di seluruh
geometri.
