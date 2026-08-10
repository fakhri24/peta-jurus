---
id: hmt-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [homoteti]
bentuk: isian
kesulitan: 4
jawaban: "4"
---

## Soal

Pada segitiga $ABC$, panjang alas $BC = 12$ dan tinggi dari $A$ ke $BC$ adalah $6$. Sebuah
persegi digambar di dalam segitiga sehingga satu sisinya terletak pada $BC$, satu titik
sudutnya pada $AB$, dan satu titik sudutnya pada $AC$.

![Segitiga ABC dengan alas BC mendatar sepanjang 12, B di kiri bawah dan C di kanan bawah, serta puncak A di atas agak ke kiri sehingga tingginya 6. Sebuah persegi digambar di dalam segitiga: sisi bawahnya terletak pada alas BC, sudut kiri atasnya menyentuh sisi AB, dan sudut kanan atasnya menyentuh sisi AC. Panjang sisi persegi itu belum diketahui. Tinggi segitiga dari A ke alas digambar putus-putus](segitiga-persegi-dalam.svg)

Tentukan panjang sisi persegi itu.

## Petunjuk

- Sisi atas persegi sejajar $BC$, jadi ia memotong segitiga pada sebuah ruas yang sejajar alasnya. Berapa panjang ruas itu pada ketinggian $y$?
- Segitiga kecil di atas ruas itu sebangun dengan $\triangle ABC$, dengan faktor $\dfrac{6-y}{6}$.
- Sisi atas persegi panjangnya $s$, dan ia berada pada ketinggian $s$. Samakan keduanya.

## Pembahasan

**Nyatakan lebar segitiga pada ketinggian $y$.** Potongan segitiga di atas ketinggian $y$
adalah segitiga yang sebangun dengan $\triangle ABC$ — homoteti berpusat $A$ dengan faktor
$\dfrac{6-y}{6}$ memetakan $\triangle ABC$ ke sana.

Karena homoteti mengalikan semua panjang dengan faktornya, lebar segitiga pada ketinggian $y$
adalah

$$\ell(y) = 12 \cdot \frac{6-y}{6} = 2\left(6-y\right)$$

**Pasang syarat perseginya.** Sisi atas persegi berada pada ketinggian $s$ dan panjangnya
juga $s$, sedangkan lebar segitiga di situ $\ell(s)$. Kedua ujung sisi atas menyentuh $AB$
dan $AC$, jadi keduanya sama:

$$s = 2(6 - s)$$

$$s = 12 - 2s \quad \Longrightarrow \quad 3s = 12 \quad \Longrightarrow \quad s = \boxed{4}$$

### Periksa

Pada ketinggian $4$, lebar segitiganya $2(6-4) = 4$ ✓ — sama dengan sisi perseginya, jadi
kedua sudut atasnya tepat menyentuh $AB$ dan $AC$.

Periksa pula bahwa $s < 6$, sebab persegi harus muat di bawah puncaknya ✓.

### Rumus umumnya

Dengan alas $a$ dan tinggi $h$, langkah yang sama memberi

$$s = a \cdot \frac{h-s}{h} \quad \Longrightarrow \quad sh = ah - as
\quad \Longrightarrow \quad s = \frac{ah}{a+h}$$

Periksa: $\dfrac{12 \times 6}{12+6} = \dfrac{72}{18} = 4$ ✓

Bentuk $\dfrac{ah}{a+h}$ itu **setengah rata-rata harmonik** dari $a$ dan $h$ — dan itu bukan
kebetulan: pola $\dfrac{1}{s} = \dfrac{1}{a} + \dfrac{1}{h}$ muncul di setiap soal yang dua
kendalanya bersaing secara linear seperti ini.

Akibat yang layak dicatat: $s$ **selalu lebih kecil** dari $a$ maupun $h$, dan hasilnya sama
kalau alas dan tinggi ditukar. Segitiga beralas $6$ dengan tinggi $12$ memberi persegi
bersisi $4$ juga.

### Cara kedua: bangun perseginya dulu, baru diperbesar

Ini cara yang murni homoteti, dan berguna karena ia bekerja bahkan ketika perhitungan
langsungnya berantakan.

Gambar **sembarang** persegi $PQRS$ dengan sisi $PQ$ pada $BC$ dan sudut $S$ pada sinar $AB$
— ukurannya bebas, jadi sudut $R$ umumnya **tidak** pada $AC$. Sekarang lakukan homoteti
berpusat $B$: ia menggeser $S$ sepanjang $AB$ dan tetap membuat $PQ$ pada $BC$, jadi
bayangannya tetap persegi yang memenuhi dua syarat pertama.

Perbesar sampai $R$ jatuh pada $AC$. Faktornya adalah nisbah yang membuat $R$ bertemu $AC$,
dan hasilnya persegi yang dicari.

Cara ini menjawab sekaligus pertanyaan yang perhitungan langsung tidak sentuh: **perseginya
ada dan tunggal**, sebab garis $BR$ memotong $AC$ tepat sekali.

### Kenapa puncaknya tidak perlu di tengah

Perhatikan bahwa perhitungannya tidak pernah memakai letak $A$ secara mendatar — hanya
tingginya. Jadi jawabannya sama untuk segitiga sama kaki maupun yang miring, selama alas dan
tingginya sama.

Yang berubah cuma letak perseginya, bukan ukurannya. Rajah di atas sengaja memakai puncak
yang tidak di tengah supaya kemandirian itu terlihat.
