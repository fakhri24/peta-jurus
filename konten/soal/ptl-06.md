---
id: ptl-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ptolemy]
bentuk: uraian
kesulitan: 4
---

## Soal

Diberikan segi lima beraturan $ABCDE$ dengan panjang sisi $s$ dan panjang diagonal $d$.

**(a)** Buktikan bahwa $d^2 = s^2 + sd$.

**(b)** Simpulkan bahwa $\dfrac{d}{s} = \dfrac{1+\sqrt5}{2}$.

## Petunjuk

- Segi lima beraturan punya lingkaran luar, jadi setiap empat titik sudutnya membentuk segiempat talibusur.
- Ambil empat titik sudut yang **berurutan**, misalnya $A$, $B$, $C$, $D$. Mana yang menjadi sisi segi lima, mana yang menjadi diagonalnya?
- Pada segiempat $ABCD$: $AB$, $BC$, $CD$ semuanya sisi segi lima; sedangkan $AD$, $AC$, $BD$ semuanya diagonal.

## Pembahasan

### Bagian (a)

**Pastikan Ptolemy boleh dipakai.** Segi lima beraturan punya lingkaran luar yang melalui
kelima titik sudutnya, jadi setiap empat di antaranya setalibusur.

**Pilih empat titik yang berurutan.** Ambil $A$, $B$, $C$, $D$ — berurutan mengelilingi
lingkaran, jadi $ABCD$ segiempat talibusur dengan urutan yang sah.

**Kenali mana sisi, mana diagonal.**

| Ruas | Melompati | Jenisnya | Panjang |
|---|---|---|---|
| $AB$ | — | sisi segi lima | $s$ |
| $BC$ | — | sisi segi lima | $s$ |
| $CD$ | — | sisi segi lima | $s$ |
| $AD$ | $B$, $C$ | diagonal segi lima | $d$ |
| $AC$ | $B$ | diagonal segi lima | $d$ |
| $BD$ | $C$ | diagonal segi lima | $d$ |

Perhatikan bahwa $AD$ adalah **sisi** segiempat $ABCD$ tetapi **diagonal** segi limanya. Dua
kata "sisi" yang berbeda inilah tempat kekeliruan paling sering masuk.

**Terapkan Ptolemy pada $ABCD$.**

$$AC \cdot BD = AB \cdot CD + BC \cdot AD$$

$$d \cdot d = s \cdot s + s \cdot d$$

$$d^2 = s^2 + sd \qquad \blacksquare$$

### Bagian (b)

Bagi kedua ruas dengan $s^2$, yang boleh karena $s > 0$. Tulis $\varphi = \dfrac{d}{s}$:

$$\varphi^2 = 1 + \varphi \quad \Longrightarrow \quad \varphi^2 - \varphi - 1 = 0$$

$$\varphi = \frac{1 \pm \sqrt{1+4}}{2} = \frac{1 \pm \sqrt5}{2}$$

Akar yang bertanda minus bernilai $\dfrac{1-\sqrt5}{2} \approx -0{,}618$, dan itu negatif —
mustahil sebagai nisbah dua panjang. Maka

$$\frac{d}{s} = \frac{1+\sqrt5}{2} \approx 1{,}618 \qquad \blacksquare$$

Bilangan ini disebut **nisbah emas**, dan biasanya ditulis $\varphi$.

### Periksa dengan trigonometri

Untuk segi lima beraturan berjari-jari luar $R$, sisi dan diagonalnya adalah talibusur yang
sudut pusatnya $72^\circ$ dan $144^\circ$:

$$s = 2R \sin 36^\circ, \qquad d = 2R \sin 72^\circ$$

$$\frac{d}{s} = \frac{\sin 72^\circ}{\sin 36^\circ} = \frac{2 \sin 36^\circ \cos 36^\circ}{\sin 36^\circ}
= 2\cos 36^\circ$$

Dengan $R = 1$ dan menghitung koordinat kelima titik sudutnya secara langsung, diperoleh
$s \approx 1{,}17557$ dan $d \approx 1{,}90211$, sehingga
$\dfrac{d}{s} \approx 1{,}61803$ ✓

Jadi sebagai hasil sampingan, buktinya menetapkan $\cos 36^\circ = \dfrac{1+\sqrt5}{4}$ —
nilai kosinus istimewa yang tidak ada di tabel sekolah, diperoleh tanpa satu pun rumus sudut
rangkap.

### Kenapa harus empat titik yang berurutan

Kalau yang diambil $A$, $B$, $C$, $E$, urutan kelilingnya menjadi $A$, $B$, $C$, $E$ — masih
sah — tetapi sisinya kini $AB = s$, $BC = s$, $CE = d$, $EA = s$, dan diagonalnya $AC = d$,
$BE = d$. Ptolemy memberi

$$d \cdot d = s \cdot d + s \cdot s$$

yaitu persamaan yang **sama persis**. Jadi pilihan itu juga bekerja — kebetulan yang tidak
akan terjadi pada segi banyak beraturan bersisi lebih.

Yang benar-benar harus dijaga adalah urutan kelilingnya. Kalau ditulis $ABEC$ misalnya,
"diagonal" yang dimaksud bukan diagonal lagi, dan kesamaannya gagal.

### Kegunaannya di luar segi lima

Nisbah emas muncul lagi pada segitiga emas — segitiga sama kaki bersudut puncak $36^\circ$,
yang tak lain segitiga $ABC$ pada segi lima ini. Nisbah kaki terhadap alasnya juga $\varphi$.

Yang layak dibawa dari soal ini bukan angkanya, melainkan caranya: **pada segi banyak
beraturan, Ptolemy mengubah hubungan panjang menjadi persamaan aljabar dalam satu peubah.**
Cara yang sama pada segi tujuh beraturan memberi hubungan
$\dfrac{1}{s} = \dfrac{1}{d_1} + \dfrac{1}{d_2}$ antara sisi dan kedua diagonalnya.

## Rubrik

- **(a)** Menyebut bahwa segi lima beraturan punya lingkaran luar, sehingga empat titik
  sudutnya setalibusur
- **(a)** Memilih empat titik sudut yang berurutan dan menyebut urutan kelilingnya
- **(a)** Mengenali dengan benar mana ruas yang panjangnya $s$ dan mana yang $d$, termasuk
  bahwa $AD$ adalah diagonal segi lima meski menjadi sisi segiempatnya
- **(a)** Menerapkan Ptolemy dengan pasangan sisi berhadapan yang benar dan menyimpulkan
  $d^2 = s^2 + sd$
- **(b)** Membagi dengan $s^2$ dan menyusun persamaan kuadrat dalam $\varphi = d/s$
- **(b)** Menyelesaikannya dan **membuang akar negatifnya** dengan alasan nisbah panjang
  bernilai positif

Menyebut hasilnya "nisbah emas" tidak menambah nilai; yang dinilai penurunannya. Sebaliknya,
melewatkan pembuangan akar negatif mengurangi nilai, sebab di situlah satu-satunya keterangan
geometris dipakai pada bagian (b).
