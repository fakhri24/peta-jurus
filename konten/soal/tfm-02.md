---
id: tfm-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [transformasi]
bentuk: isian
kesulitan: 4
jawaban: "135"
---

## Soal

Titik $P$ terletak di dalam persegi $ABCD$ dengan $PA = 1$, $PB = 2$, dan $PC = 3$.

Tentukan besar sudut $\angle APB$ dalam derajat.

## Petunjuk

- Bangunnya persegi, jadi sudut putar yang memetakan sisi ke sisi bukan $60^\circ$ melainkan $90^\circ$.
- Putar $P$ terhadap $B$ sebesar $90^\circ$, dengan arah yang memetakan $C$ ke $A$.
- Setelah itu $\triangle BPP'$ menjadi siku-siku sama kaki, dan segitiga $APP'$ punya ketiga sisinya diketahui.

## Pembahasan

**Putar $P$ terhadap $B$ sebesar $90^\circ$**, dengan arah yang memetakan $C$ ke $A$. Sebut
bayangannya $P'$.

**Baca ketiga panjangnya.**

- $BP' = BP = 2$, karena putaran menjaga jarak ke pusatnya;
- $\angle PBP' = 90^\circ$, sehingga $\triangle BPP'$ siku-siku **sama kaki** dan
  $$PP' = 2\sqrt2$$
- $AP' = CP = 3$, karena putaran memetakan ruas $CP$ ke ruas $AP'$.

**Periksa segitiga $APP'$.**

$$AP = 1, \qquad PP' = 2\sqrt2, \qquad AP' = 3$$

$$1^2 + \left(2\sqrt2\right)^2 = 1 + 8 = 9 = 3^2$$

Jadi $\triangle APP'$ siku-siku di $P$ — sudut siku-sikunya di hadapan sisi terpanjang, $AP'$.

$$\angle APP' = 90^\circ$$

**Rakit sudut yang ditanya.** Karena $\triangle BPP'$ siku-siku sama kaki, kedua sudut alasnya
$45^\circ$, khususnya

$$\angle BPP' = 45^\circ$$

$$\angle APB = \angle APP' + \angle P'PB = 90^\circ + 45^\circ = \boxed{135^\circ}$$

### Periksa dengan menghitung sisi perseginya

Dari $\triangle APB$ dengan aturan kosinus:

$$AB^2 = 1^2 + 2^2 - 2 \cdot 1 \cdot 2 \cos 135^\circ = 5 + 4 \cdot \frac{\sqrt2}{2}
= 5 + 2\sqrt2 \approx 7{,}828$$

Jadi sisi perseginya $\approx 2{,}798$. Sekarang periksa apakah $P$ dengan jarak $1$, $2$, $3$
muat: dengan $A(0,0)$, $B(2{,}798, 0)$, $C(2{,}798,\ 2{,}798)$,

$$x = \frac{1 - 4 + 7{,}828}{2 \cdot 2{,}798} = 0{,}863, \qquad y = \sqrt{1 - 0{,}863^2} = 0{,}505$$

dan jarak dari $P(0{,}863,\ 0{,}505)$ ke $C$ adalah $3{,}000$ ✓

Ketiga jarak cocok sekaligus, jadi $135^\circ$ benar.

### Hubungan yang berlaku tanpa memutar sama sekali

Untuk sembarang titik $P$ di bidang dan persegi $ABCD$ berlaku

$$PA^2 + PC^2 = PB^2 + PD^2$$

Buktinya cukup koordinat: dengan $A(0,0)$, $B(s,0)$, $C(s,s)$, $D(0,s)$ dan $P(x,y)$, kedua
ruas sama-sama bernilai $2x^2 + 2y^2 - 2sx - 2sy + 2s^2$.

Di sini itu memberi $1 + 9 = 4 + PD^2$, sehingga $PD = \sqrt6 \approx 2{,}449$ — panjang
keempat yang didapat cuma-cuma. Perhatikan bahwa hubungan ini **tidak** menjawab soalnya:
ia memberi panjang, bukan sudut. Untuk sudut, putaran tetap alat yang diperlukan.

### Bandingkan dengan bangun sama sisi

Pola kerjanya sama persis, hanya angkanya berubah mengikuti bangunnya:

| | Segitiga sama sisi | Persegi |
|---|---|---|
| Sudut putar | $60^\circ$ | $90^\circ$ |
| Bentuk $\triangle BPP'$ | sama sisi | siku-siku sama kaki |
| $PP'$ | $BP$ | $BP\sqrt2$ |
| $\angle BPP'$ | $60^\circ$ | $45^\circ$ |

Yang dihafal cukup satu kalimat: **putar terhadap titik sudut yang sudutnya ditanya, sebesar
sudut yang memetakan sisi ke sisi.** Sisanya keluar sendiri dari gambarnya.

### Kalau ketiga panjangnya bukan tripel yang rapi

Soal ini keluar rapi karena $1$, $2\sqrt2$, $3$ kebetulan siku-siku. Kalau tidak, langkah
terakhirnya memakai aturan kosinus pada $\triangle APP'$:

$$\cos \angle APP' = \frac{AP^2 + PP'^2 - AP'^2}{2 \cdot AP \cdot PP'}$$

lalu ditambah $45^\circ$ (atau $60^\circ$) seperti biasa. Jadi metodenya tidak bergantung
pada kebetulan angkanya — yang bergantung cuma kerapian jawabannya.
