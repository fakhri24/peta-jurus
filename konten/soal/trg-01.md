---
id: trg-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [trigonometri-segitiga]
bentuk: isian
kesulitan: 2
jawaban: "14"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 6$, $AC = 10$, dan $\angle BAC = 120^\circ$.

Tentukan panjang $BC$.

## Petunjuk

- Yang diketahui dua sisi beserta sudut yang **diapit** keduanya. Pythagoras tidak berlaku karena sudutnya bukan siku-siku.
- Aturan kosinus adalah Pythagoras yang diperluas ke sudut sembarang.
- $BC^2 = AB^2 + AC^2 - 2 \cdot AB \cdot AC \cos \angle BAC$, dan $\cos 120^\circ = -\tfrac12$.

## Pembahasan

**Pakai aturan kosinus dengan sudut apitnya.**

$$BC^2 = AB^2 + AC^2 - 2 \cdot AB \cdot AC \cdot \cos 120^\circ$$

$$= 36 + 100 - 2 \cdot 6 \cdot 10 \cdot \left(-\tfrac12\right)$$

Perhatikan dua tanda minus yang bertemu:

$$= 136 + 60 = 196$$

$$BC = \sqrt{196} = \boxed{14}$$

### Jebakan yang disiapkan soal ini

Untuk sudut tumpul, $\cos$ bernilai **negatif**. Tanda minus di rumus tetap ditulis minus,
lalu bertemu dengan negatifnya kosinus dan berubah jadi tambah. Yang lupa akan memperoleh

$$136 - 60 = 76 \quad \Longrightarrow \quad BC \approx 8{,}72$$

Angka itu bukan sekadar salah, ia **tidak masuk akal**: sisi di hadapan sudut tumpul wajib
menjadi sisi terpanjang, padahal $8{,}72 < 10$. Pemeriksaan sekilas itu menangkap
kekeliruan tanda tanpa menghitung ulang apa pun.

Dengan jawaban yang benar, $14 > 10 > 6$ ✓.

### Periksa dari arah sebaliknya

Balik aturan kosinus memakai ketiga sisi $6$, $10$, $14$:

$$\cos \angle BAC = \frac{6^2 + 10^2 - 14^2}{2 \cdot 6 \cdot 10} = \frac{36 + 100 - 196}{120}
= \frac{-60}{120} = -\frac12 \quad ✓$$

Kembali ke $120^\circ$, jadi perhitungannya konsisten.

### Kapan sudutnya lancip, siku-siku, atau tumpul

Aturan kosinus sekaligus alat pemeriksa jenis segitiga, karena tanda suku terakhirnya
mengikuti tanda kosinusnya:

$$a^2 < b^2 + c^2 \iff A \text{ lancip}, \qquad
a^2 = b^2 + c^2 \iff A \text{ siku-siku}, \qquad
a^2 > b^2 + c^2 \iff A \text{ tumpul}$$

Di sini $196 > 136$, jadi $\angle A$ tumpul ✓ — cocok dengan yang diketahui.

### Segitiga $120^\circ$ bersisi bulat

Sisi $6$, $10$, $14$ semuanya bulat, dan itu bukan kebetulan. Untuk $\angle A = 120^\circ$
rumusnya menjadi

$$a^2 = b^2 + c^2 + bc$$

Dengan $b = 6$, $c = 10$: $36 + 100 + 60 = 196$. Semuanya kelipatan $2$ dari segitiga
$3, 5, 7$ — segitiga $120^\circ$ terkecil yang sisinya bulat. Soal olimpiade suka memakai
kelipatan $3,5,7$ persis karena angkanya tetap bulat sampai akhir.
