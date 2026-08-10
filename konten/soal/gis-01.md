---
id: gis-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [garis-istimewa]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 8$, $AC = 12$, dan $BC = 15$. Garis bagi sudut $A$
memotong sisi $BC$ di titik $D$.

Tentukan panjang $BD$.

## Petunjuk

- Yang dibagi sama besar oleh garis itu adalah sudutnya. Apakah sisi seberangnya ikut terbagi sama panjang?
- Garis bagi membagi sisi seberangnya menurut perbandingan kedua sisi yang mengapit sudut itu.
- $\dfrac{BD}{DC} = \dfrac{AB}{AC}$, dan $BD + DC = 15$.

## Pembahasan

**Pakai teorema garis bagi.**

$$\frac{BD}{DC} = \frac{AB}{AC} = \frac{8}{12} = \frac{2}{3}$$

**Bagi $BC$ menurut perbandingan itu.** Karena $BD : DC = 2 : 3$, seluruh $BC$ terbagi
menjadi $2 + 3 = 5$ bagian:

$$BD = \frac{2}{5} \times 15 = \boxed{6}, \qquad DC = \frac{3}{5} \times 15 = 9$$

### Periksa

$$\frac{BD}{DC} = \frac{6}{9} = \frac{2}{3} = \frac{8}{12} \quad ✓$$

dan $6 + 9 = 15$ ✓. Kedua syarat terpenuhi sekaligus, dan itu memang cara memeriksa yang
paling cepat: satu perbandingan, satu jumlah.

### Jebakan yang disiapkan soal ini

Angka $15$ ganjil, jadi membaginya dua sama panjang memberi $7{,}5$ — bilangan yang
"kelihatan seperti jawaban soal". Kalau kamu menulis $7{,}5$, yang terjadi bukan salah
hitung melainkan salah jurus: **kamu memperlakukan garis bagi sebagai garis berat.**

Keduanya berimpit hanya kalau $AB = AC$. Di sini $8 \ne 12$, jadi $D$ pasti lebih dekat ke
$B$ — sisi yang lebih pendek menarik titiknya. Itu pemeriksaan kasar yang bisa dilakukan
sebelum menghitung: $BD = 6 < 7{,}5$ ✓.

### Kenapa perbandingannya begitu

Tarik garis lewat $C$ sejajar $AD$, memotong perpanjangan $BA$ di $E$. Karena $AD \parallel
EC$, sudut $\angle DAC = \angle ACE$ (dalam berseberangan) dan $\angle BAD = \angle AEC$
(sehadap). Kedua sudut di $A$ sama besar, maka $\angle ACE = \angle AEC$, sehingga
$\triangle ACE$ sama kaki dan $AE = AC$.

Dari kesebangunan $\triangle BAD \sim \triangle BEC$:

$$\frac{BD}{DC} = \frac{BA}{AE} = \frac{AB}{AC}$$

Bukti ini yang membuat rumusnya bisa dibangun ulang saat lupa — dan modalnya cuma
kesebangunan, bukan hafalan.

### Bentuk yang sering menyusul

Kalau soal berikutnya menanyakan panjang $AD$-nya sendiri, yang dipakai bukan lagi
perbandingan ini melainkan

$$AD^2 = AB \cdot AC - BD \cdot DC$$

Di sini nilainya $96 - 54 = 42$, jadi $AD = \sqrt{42}$. Dua pertanyaan yang terlihat mirip,
dua alat yang berbeda.
