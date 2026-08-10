---
id: ksb-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kesebangunan]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Pada segitiga $ABC$, titik $D$ terletak pada sisi $AB$ dan titik $E$ pada sisi $AC$, dengan
$DE$ sejajar $BC$.

![Segitiga ABC dengan alas BC mendatar dan puncak A di atas. Titik D pada sisi AB dan titik E pada sisi AC, dengan ruas DE sejajar alas BC. Ruas AD panjangnya 6, DB panjangnya 4, AE panjangnya 9, dan EC ditanyakan](segitiga-garis-sejajar.svg)

Diketahui $AD = 6$, $DB = 4$, dan $AE = 9$.

Tentukan panjang $EC$.

## Petunjuk

- Kesejajaran $DE$ dengan $BC$ menghasilkan pasangan sudut yang sama besar. Sudut mana saja, dan pada segitiga mana?
- Sudut $\angle ADE$ dan $\angle ABC$ sehadap, begitu pula $\angle AED$ dan $\angle ACB$. Ditambah sudut di $A$ yang dipakai bersama, $\triangle ADE$ sebangun dengan $\triangle ABC$.
- Susun perbandingannya dengan hati-hati: $\dfrac{AD}{DB} = \dfrac{AE}{EC}$, bukan $\dfrac{AD}{AB} = \dfrac{AE}{EC}$.

## Pembahasan

**Dari sejajar ke sebangun.** Karena $DE \parallel BC$ dipotong garis $AB$, sudut
$\angle ADE$ dan $\angle ABC$ **sehadap**, sehingga sama besar. Dengan alasan yang sama pada
garis $AC$, $\angle AED = \angle ACB$. Ditambah $\angle A$ yang dipakai bersama:

$$\triangle ADE \sim \triangle ABC \quad (\text{Sd-Sd})$$

**Susun perbandingannya.** Dari kesebangunan itu,

$$\frac{AD}{AB} = \frac{AE}{AC}$$

Dengan $AB = AD + DB = 6 + 4 = 10$ dan $AC = 9 + EC$:

$$\frac{6}{10} = \frac{9}{9 + EC}$$

$$6(9 + EC) = 90 \quad \Longrightarrow \quad 54 + 6\,EC = 90 \quad \Longrightarrow \quad EC = \boxed{6}$$

**Cara yang lebih pendek: pakai bentuk potongannya langsung.** Teorema garis sejajar
menyatakan

$$\frac{AD}{DB} = \frac{AE}{EC} \quad \Longrightarrow \quad \frac{6}{4} = \frac{9}{EC}
\quad \Longrightarrow \quad EC = \frac{4 \times 9}{6} = 6$$

Hasil yang sama, satu baris.

### Dua perbandingan yang benar, dan satu yang salah

Ini sumber kekeliruan paling sering di jurus ini, jadi layak ditulis lengkap:

| Bentuk | Benar? | Keterangan |
|---|---|---|
| $\dfrac{AD}{AB} = \dfrac{AE}{AC}$ | ✓ | potongan atas berbanding sisi **penuh** |
| $\dfrac{AD}{DB} = \dfrac{AE}{EC}$ | ✓ | potongan atas berbanding potongan bawah |
| $\dfrac{AD}{AB} = \dfrac{AE}{EC}$ | ✗ | ruas kiri memakai sisi penuh, ruas kanan memakai potongan |

Kedua bentuk yang benar itu setara, tetapi **tidak boleh dicampur**. Kebiasaan yang
menyelamatkan: tuliskan pasangan yang bersesuaian lebih dulu — $A \leftrightarrow A$,
$D \leftrightarrow B$, $E \leftrightarrow C$ — lalu susun pecahannya mengikuti pasangan itu.

### Hitung juga panjang $DE$

Kalau diberikan $BC = 15$, maka dengan nisbah kesebangunan $k = \dfrac{AD}{AB} = \dfrac{6}{10}
= \dfrac{3}{5}$,

$$DE = k \times BC = \tfrac{3}{5} \times 15 = 9$$

Perhatikan bahwa $DE$ dibandingkan dengan **sisi penuh** $BC$, jadi nisbah yang dipakai
$\dfrac{AD}{AB}$, bukan $\dfrac{AD}{DB}$. Memakai $\dfrac{6}{4}$ di sini memberi $22{,}5$ —
lebih panjang daripada $BC$ sendiri, yang mustahil untuk ruas di dalam segitiga.

Pemeriksaan kewajaran semacam itu murah dan menangkap persis kekeliruan yang paling mahal.

### Kebalikannya juga terpakai

Kalau yang **diketahui** justru $\dfrac{AD}{DB} = \dfrac{AE}{EC}$ dan yang diminta membuktikan
$DE \parallel BC$, jalannya dibalik: dari perbandingan sisi didapat $\triangle ADE \sim
\triangle ABC$ menurut S-Sd-S, lalu $\angle ADE = \angle ABC$ memberikan kesejajarannya
sebagai sudut sehadap.

Arah kedua ini justru yang lebih sering muncul di soal pembuktian.
