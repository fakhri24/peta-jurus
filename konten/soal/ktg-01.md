---
id: ktg-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [ketaksamaan-geometri, transformasi]
bentuk: isian
kesulitan: 4
jawaban: "10"
---

## Soal

Diberikan sudut $\angle XOY = 30^\circ$ dan sebuah titik tetap $P$ di dalam sudut itu
dengan $OP = 10$. Titik $A$ bergerak pada sinar $OX$ dan titik $B$ bergerak pada sinar
$OY$.

![Dua sinar yang keduanya berpangkal di titik O dan mengapit sudut 30 derajat: sinar OX mendatar ke kanan, dan sinar OY miring ke atas. Sebuah titik P berada di dalam sudut itu, agak jauh dari O dan lebih dekat ke sinar OX daripada ke sinar OY. Titik A terletak pada sinar OX, lebih dekat ke O daripada P, dan titik B pada sinar OY, sedikit lebih jauh dari O daripada P. Ketiganya dihubungkan menjadi segitiga PAB, yang sisi-sisinya digambar tebal, dan segitiga itu terlihat jelas tidak simetris](titik-dalam-sudut-dua-sinar.svg)

Tentukan nilai terkecil dari keliling segitiga $PAB$.

## Petunjuk

- Kelilingnya adalah panjang lintasan $P \to A \to B \to P$. Lintasan patah menjadi terpendek kalau ia bisa diluruskan — dan yang meluruskannya bukan menggeser $A$ atau $B$, melainkan memindahkan $P$.
- Cerminkan $P$ pada sinar $OX$ menjadi $P_1$, dan pada sinar $OY$ menjadi $P_2$. Pencerminan menjaga panjang: $PA = P_1A$ dan $PB = P_2B$.
- Kelilingnya sama dengan $P_1A + AB + BP_2$, yaitu panjang lintasan dari $P_1$ ke $P_2$. Sekarang cari besar $\angle P_1OP_2$.

## Pembahasan

**Ubah kelilingnya jadi satu lintasan.** Keliling segitiga $PAB$ adalah

$$PA + AB + BP$$

Ketiga ruas itu tersebar, dan tidak ada yang bisa dikerjakan selama bentuknya masih
begitu. Yang mengubah keadaan adalah **pencerminan**.

Sebut $P_1$ cerminan $P$ terhadap garis $OX$, dan $P_2$ cerminan $P$ terhadap garis
$OY$. Karena $A$ ada pada $OX$, pencerminan itu tidak memindahkan $A$, sehingga

$$PA = P_1 A$$

dan dengan alasan yang sama $PB = P_2 B$. Jadi

$$PA + AB + BP = P_1A + AB + BP_2$$

Ruas kanannya adalah panjang lintasan patah dari $P_1$ ke $P_2$ yang singgah di $A$
lalu $B$. Menurut ketaksamaan segitiga, lintasan patah tidak pernah lebih pendek
daripada ruas lurus yang menghubungkan kedua ujungnya:

$$P_1A + AB + BP_2 \ \ge\ P_1P_2$$

**Hitung $P_1P_2$.** Pencerminan menjaga jarak ke $O$, sebab $O$ ada pada kedua sumbu
cerminnya:

$$OP_1 = OP_2 = OP = 10$$

Sudutnya: pencerminan terhadap $OX$ memantulkan $P$ ke seberang $OX$, jadi $\angle
P_1OX = \angle XOP$. Begitu pula $\angle P_2OY = \angle YOP$. Maka

$$\angle P_1OP_2 = \angle P_1OX + \angle XOP + \angle POY + \angle YOP_2
= 2\left(\angle XOP + \angle POY\right) = 2 \angle XOY = 60^\circ$$

Perhatikan bahwa letak $P$ **tidak ikut** dalam hitungan itu — yang tersisa cuma $2$
kali sudut $XOY$.

Segitiga $OP_1P_2$ punya dua sisi sama panjang $10$ dengan sudut apit $60^\circ$, jadi
ia sama sisi:

$$P_1P_2 = 10$$

**Kesamaannya tercapai.** Batas $P_1P_2$ dicapai tepat ketika $A$ dan $B$ terletak pada
ruas $P_1P_2$. Karena $\angle P_1OP_2 = 60^\circ < 180^\circ$, ruas $P_1P_2$ memang
memotong kedua sinar $OX$ dan $OY$ — jadi $A$ dan $B$ yang dimaksud sungguh-sungguh
ada, bukan hanya kedudukan khayal.

$$\text{keliling minimum} = \boxed{10}$$

### Nilainya tidak bergantung pada letak $P$

Yang keluar hanyalah $OP$ dan besar sudutnya. Jadi setiap titik pada busur berjari-jari
$10$ di dalam sudut itu memberi keliling minimum yang sama, $10$.

Itu bisa dipakai sebagai pemeriksaan cepat: kalau jawabanmu memuat jarak $P$ ke salah
satu sinar, hampir pasti ada langkah yang salah.

### Kapan cara ini gagal

Kesamaan tadi menuntut ruas $P_1P_2$ memotong kedua sinar, dan itu menuntut

$$2 \angle XOY < 180^\circ \quad \Longleftrightarrow \quad \angle XOY < 90^\circ$$

Kalau $\angle XOY \ge 90^\circ$, titik $P_1$ dan $P_2$ jatuh sedemikian rupa sehingga
ruas $P_1P_2$ tidak lagi melewati kedua sinar, dan kelilingnya tidak punya nilai
terkecil yang tercapai — ia hanya bisa didekati dengan menarik $A$ dan $B$ ke $O$.

Di sini $\angle XOY = 30^\circ$, jadi syaratnya aman. Tetapi memeriksanya adalah bagian
dari jawabannya, bukan tambahan.

### Angkanya, untuk yang ingin melihat

Dengan $O$ di pangkal, $OX$ pada sumbu-$x$, dan $P$ pada sudut $11^\circ$:

$$P \approx (9{,}82;\ 1{,}91), \qquad P_1 \approx (9{,}82;\ -1{,}91), \qquad
P_2 \approx (6{,}56;\ 7{,}55)$$

$$P_1P_2 \approx \sqrt{3{,}26^2 + 9{,}46^2} = \sqrt{10{,}6 + 89{,}4} = \sqrt{100} = 10 \quad ✓$$

Titik terbaiknya jatuh di $OA \approx 9{,}16$ dan $OB \approx 8{,}83$ — dua bilangan yang
tidak rapi sama sekali, padahal jawabannya bulat. Itu ciri khas soal pencerminan:
**yang ditanyakan panjang lintasannya, bukan letak titik singgahnya**, dan hanya yang
pertama yang rapi.

### Pola yang berulang

Ketiga soal jarak terpendek berikut dikerjakan dengan gerakan yang sama:

| Soal | Yang dicerminkan |
|---|---|
| $A$, $B$ sesisi, $P$ pada garis $\ell$ | salah satu titik, sekali |
| $P$ di dalam sudut, $A$ dan $B$ pada kedua kakinya | titik $P$, dua kali |
| lintasan memantul beberapa kali | sekali untuk tiap pantulan |

Yang dicerminkan selalu **titik tetapnya**, dan yang dicerminkan padanya selalu **garis
tempat titik bebasnya berjalan**.
