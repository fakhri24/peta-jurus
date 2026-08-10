---
id: gis-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [garis-istimewa]
bentuk: isian
kesulitan: 3
jawaban: "3"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 8$, $BC = 9$, dan $CA = 7$. Garis sumbu sisi $AB$
memotong sisi $BC$ di titik $P$.

Tentukan panjang $PC$.

## Petunjuk

- Apa yang membuat sebuah titik berada pada garis sumbu suatu ruas? Terjemahkan itu menjadi persamaan tentang $P$.
- Setiap titik pada garis sumbu $AB$ berjarak sama ke $A$ dan ke $B$, jadi $PA = PB$.
- Tarik ruas dari $P$ ke titik tengah $AB$. Segitiga apa yang terbentuk, dan sudut mana yang bisa kamu hitung dengan aturan kosinus?

## Pembahasan

**Terjemahkan "garis sumbu" jadi persamaan.** Titik $P$ ada pada garis sumbu $AB$, jadi

$$PA = PB$$

Itu satu-satunya keterangan yang diberikan tentang $P$, dan itu cukup.

**Pakai segitiga siku-siku yang terbentuk.** Misalkan $M$ titik tengah $AB$, jadi
$BM = 4$ dan $PM \perp AB$. Pada segitiga siku-siku $BMP$:

$$\cos \angle MBP = \frac{BM}{BP} = \frac{4}{BP}$$

Sudut $\angle MBP$ tidak lain $\angle ABC$, karena $M$ ada pada $BA$ dan $P$ ada pada $BC$.
Aturan kosinus memberi

$$\cos \angle ABC = \frac{AB^2 + BC^2 - CA^2}{2 \cdot AB \cdot BC}
= \frac{64 + 81 - 49}{2 \cdot 8 \cdot 9} = \frac{96}{144} = \frac{2}{3}$$

Maka

$$\frac{4}{BP} = \frac{2}{3} \quad \Longrightarrow \quad BP = 6$$

$$PC = BC - BP = 9 - 6 = \boxed{3}$$

### Periksa lewat definisinya

Hitung $PA$ langsung dengan aturan kosinus pada $\triangle ABP$, memakai $BP = 6$:

$$PA^2 = AB^2 + BP^2 - 2 \cdot AB \cdot BP \cos \angle ABC
= 64 + 36 - 2 \cdot 8 \cdot 6 \cdot \tfrac{2}{3} = 100 - 64 = 36$$

$$PA = 6 = PB \quad ✓$$

Pemeriksaan ini memakai sifat yang **mendefinisikan** garis sumbu, bukan langkah-langkah
yang tadi dipakai — jadi ia benar-benar menguji.

### Cara kedua: Stewart pada ruas $AP$

Kalau aturan kosinus belum ingin dipakai, perlakukan $AP$ sebagai ruas dari $A$ ke titik
$P$ pada $BC$. Dengan $BP = x$, $PC = 9 - x$, dan $AP = PB = x$:

$$AB^2 \cdot PC + AC^2 \cdot BP = BC\left(AP^2 + BP \cdot PC\right)$$

$$64(9-x) + 49x = 9\left(x^2 + x(9-x)\right) = 9 \cdot 9x = 81x$$

$$576 - 15x = 81x \quad \Longrightarrow \quad 96x = 576 \quad \Longrightarrow \quad x = 6$$

Suku $x^2$ lenyap dengan sendirinya, dan persamaannya jadi linear. Itu pola yang berulang
tiap kali dua jarak disamakan.

### Kapan garis sumbunya tidak memotong sisi $BC$

Rumus yang tadi dipakai, $BP = \dfrac{AB/2}{\cos \angle B}$, sekaligus memberitahu kapan
soalnya tidak punya jawaban seperti yang dibayangkan:

- $\angle B$ **siku-siku** — maka $\cos \angle B = 0$ dan $BP$ tidak terdefinisi. Memang:
  garis sumbu $AB$ tegak lurus $AB$, dan $BC$ juga tegak lurus $AB$, jadi keduanya
  **sejajar** dan tidak pernah bertemu.
- $\angle B$ **tumpul** — maka $\cos \angle B < 0$ dan $BP$ keluar negatif. Tandanya
  perpotongannya ada di perpanjangan $CB$ di seberang $B$, bukan di dalam ruasnya.
- $BP > BC$ — perpotongannya di perpanjangan $BC$ melewati $C$.

Di sini $\cos \angle B = \tfrac{2}{3} > 0$ dan $BP = 6 < 9$, jadi $P$ benar-benar di dalam
ruas $BC$. Periksa keduanya sebelum menuliskan jawaban: soal yang sama dengan $CA$
diperbesar sedikit saja sudah bisa melempar $P$ keluar dari gambar.
