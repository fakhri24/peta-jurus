---
id: ktg-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [ketaksamaan-geometri, transformasi]
bentuk: uraian
kesulitan: 5
---

## Soal

Diberikan segitiga $ABC$ yang ketiga sudutnya kurang dari $120^\circ$, dan titik $P$
di dalamnya.

![Segitiga ABC dengan A di kiri bawah, B di kanan bawah, dan C di atas agak ke kiri; ketiga sudutnya lancip. Sebuah titik P berada di dalam segitiga itu, di bawah dan sedikit ke kiri dari pusatnya, dan dihubungkan dengan ruas tebal ke ketiga titik sudut sehingga terbentuk ruas PA, PB, dan PC. Ketiga sudut di P jelas tidak sama besar](segitiga-titik-dalam-tiga-ruas.svg)

**(a)** Buktikan bahwa nilai terkecil dari $PA + PB + PC$ tercapai pada titik $P$ yang
memenuhi

$$\angle APB = \angle BPC = \angle CPA = 120^\circ$$

**(b)** Jelaskan mengapa syarat "ketiga sudut segitiganya kurang dari $120^\circ$" tidak
boleh dihapus, dan sebutkan letak titik minimumnya kalau syarat itu dilanggar.

## Petunjuk

- Ketiga ruas $PA$, $PB$, $PC$ bertemu di satu titik, jadi jumlahnya belum berbentuk lintasan. Yang menolong adalah memindahkan salah satunya sehingga ketiganya bersambung ujung ke ujung.
- Putar segitiga $APB$ sebesar $60^\circ$ mengelilingi $A$, ke arah luar segitiga. Perhatikan apa yang terjadi pada ruas $AP$ sendiri.
- Setelah diputar, $PA + PB + PC$ menjadi panjang lintasan patah dari $C$ ke satu titik tetap. Lintasan patah menjadi terpendek ketika ia lurus.

## Pembahasan

### Bagian (a)

**Susun ulang ketiga ruasnya jadi satu lintasan.** Selama $PA$, $PB$, $PC$ semuanya
berpangkal di $P$, jumlahnya bukan panjang lintasan apa pun, dan ketaksamaan segitiga
tidak bisa dipakai. Langkah pembukanya adalah membuat ketiganya bersambung.

Putar seluruh bidang sebesar $60^\circ$ mengelilingi $A$, ke arah yang menjauhi
segitiga. Sebut

$$B \mapsto B', \qquad P \mapsto P'$$

Tiga akibat langsung, semuanya karena putaran menjaga jarak:

1. $AP' = AP$, dan $\angle PAP' = 60^\circ$. Segitiga $APP'$ punya dua sisi sama dengan
   sudut apit $60^\circ$, jadi ia **sama sisi**, sehingga

   $$PP' = AP$$

2. $P'B' = PB$, sebab $P'B'$ bayangan $PB$.

3. $AB' = AB$, jadi $B'$ titik tetap yang tidak bergantung pada $P$ — dan segitiga
   $ABB'$ sama sisi.

Sekarang gantikan:

$$PA + PB + PC = PP' + P'B' + PC = CP + PP' + P'B'$$

Ruas kanan adalah panjang lintasan patah $C \to P \to P' \to B'$.

**Turunkan batasnya.** Lintasan patah tidak pernah lebih pendek daripada ruas lurus
antara kedua ujungnya:

$$CP + PP' + P'B' \ \ge\ CB'$$

Panjang $CB'$ sama sekali tidak memuat $P$: $C$ dan $B'$ keduanya tetap. Jadi

$$PA + PB + PC \ \ge\ CB' \qquad \text{untuk setiap } P$$

**Kapan kesamaannya berlaku.** Tepat ketika $C$, $P$, $P'$, $B'$ segaris, dalam urutan
itu. Dua akibatnya:

- Di titik $P$: $\angle CPP' = 180^\circ$. Karena $\triangle APP'$ sama sisi,
  $\angle APP' = 60^\circ$, sehingga

  $$\angle APC = 180^\circ - 60^\circ = 120^\circ$$

- Di titik $P'$: $\angle PP'B' = 180^\circ$, dan $\angle AP'P = 60^\circ$, sehingga
  $\angle AP'B' = 120^\circ$. Tetapi $\angle AP'B'$ adalah bayangan $\angle APB$, dan
  putaran menjaga besar sudut, jadi

  $$\angle APB = 120^\circ$$

Sudut ketiganya tinggal sisa satu putaran penuh di sekeliling $P$:

$$\angle BPC = 360^\circ - 120^\circ - 120^\circ = 120^\circ$$

Ketiganya $120^\circ$ ✓ $\blacksquare$

**Titik itu ada.** Karena ketiga sudut segitiganya kurang dari $120^\circ$, ruas $CB'$
memotong bagian dalam segitiga dan memberikan titik $P$ yang dimaksud. Titik itu disebut
**titik Fermat** segitiga $ABC$.

### Bagian (b)

Andaikan $\angle A \ge 120^\circ$. Titik yang melihat ketiga sisi dengan sudut
$120^\circ$ tidak lagi ada di dalam segitiga: sudut $\angle BPC$ selalu lebih besar
daripada $\angle BAC \ge 120^\circ$ untuk $P$ di dalam segitiga, sehingga ketiga sudut
di $P$ tidak bisa sama-sama $120^\circ$.

Dalam hal itu nilai terkecilnya tercapai **di titik sudut yang tumpul itu sendiri**,
yaitu $P = A$, dengan nilai

$$PA + PB + PC = AB + AC$$

Alasannya: konstruksi putaran tadi tetap memberi batas $CB'$, tetapi ruas $CB'$ kini
tidak lagi memotong bagian dalam segitiga, sehingga kesamaannya tidak bisa dicapai oleh
$P$ mana pun di dalam. Yang paling mendekat adalah $P$ yang jatuh di $A$.

**Pemeriksaan angka.** Untuk $A = (0,0)$, $B = (5,0)$, $C = (-3;\ 1{,}2)$ — di sini
$\angle A \approx 158^\circ$ — pencarian numerik memberi minimum $\approx 8{,}2311$,
sedangkan

$$AB + AC = 5 + \sqrt{9 + 1{,}44} = 5 + 3{,}2311 = 8{,}2311 \quad ✓$$

Jadi minimumnya memang jatuh tepat di $A$.

### Rumus panjangnya, sebagai pemeriksaan

Untuk segitiga yang ketiga sudutnya kurang dari $120^\circ$, panjang $CB'$ bisa
dihitung dan hasilnya

$$PA + PB + PC \ \ge\ \sqrt{\frac{a^2+b^2+c^2}{2} + 2\sqrt3\, L}$$

dengan $L$ luas segitiganya. Untuk $A=(0,0)$, $B=(5,0)$, $C=(1{,}5;\ 4)$, rumus itu
memberi $\approx 8{,}3899$, dan pencarian numerik langsung memberi angka yang sama
dengan ketiga sudut di titik minimumnya terukur $120{,}000^\circ$ ✓

Rumus itu tidak perlu dihafal. Yang perlu diingat adalah **letaknya** — sudut
$120^\circ$ — sebab itu yang dipakai soal.

### Kenapa putaran $60^\circ$, dan kenapa mengelilingi titik sudut

Dua hal harus terjadi sekaligus, dan hanya putaran $60^\circ$ memberi keduanya:

- **$PP' = AP$.** Ini yang mengubah $AP$ — ruas yang tadinya menjuntai dari $P$ —
  menjadi mata rantai dalam lintasan. Itu hanya terjadi kalau $\triangle APP'$ sama
  sisi, dan itu menuntut sudut putarnya tepat $60^\circ$.
- **$B'$ tetap.** Pusat putarannya harus titik tetap segitiganya, jadi salah satu titik
  sudut. Kalau diputar mengelilingi $P$, tidak ada yang tetap dan tidak ada yang bisa
  dibandingkan.

Karena itu jangan menghafalnya sebagai "putar $60^\circ$". Yang berlaku umum adalah:
**cari gerakan yang menyambung ketiga ruas menjadi satu lintasan dengan kedua ujungnya
tetap.** Sudut $60^\circ$ cuma jawaban gerakan itu untuk kasus ini.

### Hubungannya dengan latihan pertama jurus ini

Pola pikirnya sama persis dengan soal $P$ di dalam sudut $30^\circ$: jumlah beberapa
jarak diubah menjadi **satu lintasan** dengan kedua ujung tetap, lalu diluruskan.
Bedanya cuma alat yang dipakai — di sana pencerminan, di sini putaran.

Yang berulang di keduanya, dan layak dibawa ke soal berikutnya:

1. jumlah jarak yang berpangkal di satu titik tidak bisa ditaksir apa adanya;
2. carilah transformasi yang menjadikannya lintasan bersambung;
3. batasnya adalah jarak lurus antara kedua ujung tetapnya;
4. kesamaannya menuntut kesegarisan — dan kesegarisan itulah yang memberi sudutnya.

## Rubrik

- **(a)** Menyatakan putaran $60^\circ$ mengelilingi salah satu titik sudut, dengan
  arah putar yang jelas (keluar dari segitiga)
- **(a)** Menunjukkan $\triangle APP'$ sama sisi **beserta alasannya** (dua sisi sama,
  sudut apit $60^\circ$), sehingga $PP' = AP$
- **(a)** Menyatakan $P'B' = PB$ karena putaran menjaga jarak, dan bahwa $B'$ tidak
  bergantung pada $P$
- **(a)** Menuliskan $PA+PB+PC$ sebagai panjang lintasan $C \to P \to P' \to B'$ dan
  menerapkan ketaksamaan segitiga untuk memperoleh batas $CB'$
- **(a)** Menurunkan ketiga sudut $120^\circ$ **dari syarat kesegarisan**, bukan
  menyatakannya sebagai hasil yang sudah diketahui
- **(b)** Menjelaskan bahwa titik bersudut $120^\circ$ tidak ada di dalam segitiga
  ketika salah satu sudutnya $\ge 120^\circ$
- **(b)** Menyebut bahwa minimumnya jatuh di titik sudut yang tumpul, dengan nilai
  $AB + AC$

Bukti yang memakai putaran mengelilingi $B$ atau $C$ dinilai sama penuh. Menyebut hasil
"titik Fermat melihat ketiga sisi dengan sudut $120^\circ$" tanpa menurunkannya tidak
memperoleh angka untuk bagian (a) — yang diminta buktinya, dan konstruksi putaran itulah
isinya.
