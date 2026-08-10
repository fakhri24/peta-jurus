---
id: gru-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-ruang]
bentuk: isian
kesulitan: 3
jawaban: "384"
---

## Soal

Limas segiempat beraturan $T.ABCD$ mempunyai alas persegi dengan $AB = 12$ dan tinggi $8$.

Tentukan luas permukaan limas itu.

## Petunjuk

- Luas permukaan adalah luas alas ditambah luas keempat sisi tegaknya. Luas alas mudah; yang perlu dicari adalah tinggi tiap segitiga sisi.
- Tinggi segitiga sisi diukur dari $T$ ke **titik tengah** rusuk alas, bukan ke titik sudut.
- Segitiga siku-sikunya dibentuk oleh tinggi limas, jarak dari pusat alas ke titik tengah sisi, dan tinggi segitiga sisi itu.

## Pembahasan

**Luas alasnya.**

$$L_{\text{alas}} = 12 \times 12 = 144$$

**Cari tinggi segitiga sisinya.** Sebut $O$ pusat alas dan $M$ titik tengah rusuk $AB$. Maka:

- $OM$ adalah jarak dari pusat persegi ke titik tengah sisinya, yaitu **setengah sisi**:
  $OM = 6$.
- $TO = 8$, tegak lurus bidang alas, sehingga tegak lurus $OM$.

Pada $\triangle TOM$ yang siku-siku di $O$,

$$TM^2 = 8^2 + 6^2 = 64 + 36 = 100 \quad \Longrightarrow \quad TM = 10$$

Ruas $TM$ inilah tinggi segitiga $TAB$, sebab $TM$ tegak lurus $AB$ — segitiga $TAB$ sama kaki
sehingga garis dari puncaknya ke titik tengah alas juga tegak lurus alas.

**Luas keempat sisi tegaknya.**

$$L_{\text{selimut}} = 4 \times \tfrac{1}{2} \times AB \times TM
= 4 \times \tfrac{1}{2} \times 12 \times 10 = 240$$

**Jumlahkan.**

$$L_{\text{permukaan}} = 144 + 240 = \boxed{384}$$

### Dua "tinggi" yang tidak boleh tertukar

Ini kekeliruan paling sering di soal limas, dan sepadan ditulis lengkap:

| Ruas | Dari $T$ ke | Panjangnya di sini | Dipakai untuk |
|---|---|---|---|
| Tinggi limas $TO$ | pusat alas | $8$ | volume |
| Apotema sisi $TM$ | titik tengah rusuk alas | $10$ | luas sisi tegak |
| Rusuk tegak $TA$ | titik sudut alas | $\sqrt{8^2 + (6\sqrt2)^2} = \sqrt{136}$ | panjang rusuk |

Ketiganya berangkat dari $T$ dan ketiganya sering disebut "tinggi" dalam percakapan sehari-hari,
tetapi hanya satu yang tegak lurus alas. Memakai $TA$ sebagai tinggi segitiga sisi memberi
$4 \times \tfrac12 \times 12 \times \sqrt{136} \approx 280$ — angka yang wajar dan salah.

### Kenapa $TM$ tegak lurus $AB$

Karena $TA = TB$ (limasnya beraturan), $\triangle TAB$ sama kaki, sehingga garis dari $T$ ke
titik tengah $AB$ sekaligus menjadi garis tingginya. Ini persis sifat yang sudah kamu buktikan
lewat kekongruenan pada segitiga sama kaki — dipakai di dalam ruang tanpa perubahan apa pun.

Menyebut alasannya penting: kalau limasnya **tidak** beraturan, $TM$ pada umumnya bukan tinggi
segitiga sisinya, dan seluruh perhitungan selimutnya berubah.

### Volumenya, sekalian

$$V = \tfrac{1}{3} \times 144 \times 8 = 384$$

Angkanya kebetulan sama dengan luas permukaannya. Kebetulan itu tidak bermakna apa-apa —
keduanya besaran berdimensi berbeda — tetapi berguna sebagai pengingat untuk selalu menuliskan
**apa** yang dihitung, bukan hanya angkanya.
