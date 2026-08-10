---
id: gis-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [garis-istimewa]
bentuk: isian
kesulitan: 3
jawaban: "12"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 21$, $AC = 14$, dan $BC = 25$. Garis bagi sudut $A$
memotong sisi $BC$ di titik $D$.

Tentukan panjang $AD$.

## Petunjuk

- Sebelum panjang $AD$ bisa dihitung, letak $D$ harus diketahui dulu. Apa yang menentukan letaknya?
- Bagi $BC$ menurut perbandingan $AB : AC$, lalu pakai rumus panjang garis bagi.
- $AD^2 = AB \cdot AC - BD \cdot DC$.

## Pembahasan

**Tentukan letak $D$ lebih dulu.** Teorema garis bagi memberi

$$\frac{BD}{DC} = \frac{AB}{AC} = \frac{21}{14} = \frac{3}{2}$$

Karena $BD + DC = 25$ terbagi menjadi $3 + 2 = 5$ bagian:

$$BD = \frac{3}{5} \times 25 = 15, \qquad DC = \frac{2}{5} \times 25 = 10$$

**Pakai rumus panjang garis bagi.**

$$AD^2 = AB \cdot AC - BD \cdot DC = 21 \times 14 - 15 \times 10 = 294 - 150 = 144$$

$$AD = \sqrt{144} = \boxed{12}$$

### Turunkan sendiri lewat Stewart

Rumus di atas bukan hafalan terpisah. Dengan $m = BD = 15$, $n = DC = 10$, $a = 25$,
$b = AC = 14$, $c = AB = 21$, teorema Stewart berbunyi

$$b^2 m + c^2 n = a\left(AD^2 + mn\right)$$

$$14^2 \cdot 15 + 21^2 \cdot 10 = 25\left(AD^2 + 150\right)$$

$$2940 + 4410 = 7350 = 25\,AD^2 + 3750$$

$$25\,AD^2 = 3600 \quad \Longrightarrow \quad AD^2 = 144 \quad \Longrightarrow \quad AD = 12$$

Sama persis, dan dengan rumus yang juga memberi garis berat pada soal sebelumnya.

### Periksa dengan segitiga yang terbentuk

Pada $\triangle ABD$ berlaku aturan kosinus di $D$; pada $\triangle ACD$ juga, dengan sudut
yang **berpelurus**. Karena $\cos \angle ADC = -\cos \angle ADB$, kedua persamaannya bisa
dijumlahkan dengan bobot yang tepat dan suku kosinusnya lenyap — dan yang tersisa persis
teorema Stewart. Jadi Stewart bukan rumus baru, melainkan aturan kosinus yang dipakai dua
kali lalu dijumlahkan.

Sebagai pemeriksaan angka:

$$\cos \angle ADB = \frac{AD^2 + BD^2 - AB^2}{2 \cdot AD \cdot BD}
= \frac{144 + 225 - 441}{2 \cdot 12 \cdot 15} = \frac{-72}{360} = -\frac{1}{5}$$

$$\cos \angle ADC = \frac{AD^2 + DC^2 - AC^2}{2 \cdot AD \cdot DC}
= \frac{144 + 100 - 196}{2 \cdot 12 \cdot 10} = \frac{48}{240} = \frac{1}{5}$$

Keduanya berjumlah nol ✓ — persis yang harus terjadi kalau $B$, $D$, $C$ segaris.

### Jebakan: memakai rumus garis bagi luar

Rumus $AD^2 = bc - BD \cdot DC$ berlaku untuk garis bagi **dalam**. Untuk garis bagi luar,
yang memotong **perpanjangan** $BC$, hubungannya menjadi $AD'^2 = BD' \cdot D'C - bc$, dan
titiknya membagi dengan perbandingan yang sama tetapi ke arah luar.

Cara mengingat mana yang mana tanpa menghafal: kuadrat panjang harus **positif**. Untuk
garis bagi dalam $BD \cdot DC$ selalu lebih kecil dari $bc$; untuk yang luar selalu lebih
besar. Bentuk yang salah akan memberi bilangan negatif, dan itu tanda paling cepat bahwa
rumusnya tertukar.
