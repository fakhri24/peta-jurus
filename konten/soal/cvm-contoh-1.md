---
id: cvm-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ceva-menelaus]
bentuk: isian
kesulitan: 3
jawaban: "2"
---

## Soal

Pada segitiga $ABC$, titik $D$ pada sisi $BC$, titik $E$ pada sisi $CA$, dan titik $F$ pada
sisi $AB$. Ruas $AD$, $BE$, dan $CF$ berpotongan di satu titik $P$.

![Segitiga ABC dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, dan puncak A di atas agak ke kiri. Dari A ditarik ruas ke titik D pada sisi BC, dari B ke titik E pada sisi CA, dan dari C ke titik F pada sisi AB. Ketiga ruas itu berpotongan di satu titik P di dalam segitiga](segitiga-tiga-ceva.svg)

Diketahui $\dfrac{BD}{DC} = \dfrac{2}{3}$ dan $\dfrac{CE}{EA} = \dfrac{3}{4}$.

Tentukan nilai $\dfrac{AF}{FB}$.

## Petunjuk

- Ketiga ruas berangkat dari ketiga titik sudut dan bertemu di satu titik. Teorema mana yang bicara tentang keadaan itu?
- Teorema Ceva: hasil kali ketiga perbandingannya bernilai $1$.
- Susun perbandingannya **berkeliling**: $B \to D \to C$, lalu $C \to E \to A$, lalu $A \to F \to B$.

## Pembahasan

**Kenali bentuknya.** Ketiga ruas berangkat dari **ketiga titik sudut** menuju sisi
seberangnya, dan bertemu di satu titik. Itu bentuk Ceva, bukan Menelaus.

**Tulis teorema Ceva dengan urutan yang berkeliling.**

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$

Perhatikan pola hurufnya: tiap pecahan berangkat dari satu titik sudut, lewat titik pada
sisi, lalu berakhir di titik sudut berikutnya — $B \to D \to C$, $C \to E \to A$,
$A \to F \to B$. Ia menutup satu putaran penuh mengelilingi segitiga.

**Masukkan yang diketahui.**

$$\frac{2}{3} \cdot \frac{3}{4} \cdot \frac{AF}{FB} = 1$$

$$\frac{1}{2} \cdot \frac{AF}{FB} = 1 \quad \Longrightarrow \quad \frac{AF}{FB} = \boxed{2}$$

### Periksa lewat luas

Ceva bisa diperiksa tanpa memakai Ceva. Kunci pemeriksanya: dua segitiga yang tingginya sama
punya perbandingan luas sama dengan perbandingan alasnya. Karena $\triangle ABD$ dan
$\triangle ACD$ beralas pada garis yang sama dengan puncak yang sama, dan begitu pula
$\triangle PBD$ dan $\triangle PCD$:

$$\frac{BD}{DC} = \frac{[ABD]}{[ACD]} = \frac{[PBD]}{[PCD]}
= \frac{[ABD] - [PBD]}{[ACD] - [PCD]} = \frac{[ABP]}{[ACP]}$$

Langkah terakhirnya memakai sifat perbandingan: kalau $\tfrac{p}{q} = \tfrac{r}{s}$ maka
keduanya sama dengan $\tfrac{p-r}{q-s}$.

Dengan cara yang sama, $\dfrac{CE}{EA} = \dfrac{[BCP]}{[BAP]}$ dan
$\dfrac{AF}{FB} = \dfrac{[CAP]}{[CBP]}$. Hasil kali ketiganya:

$$\frac{[ABP]}{[ACP]} \cdot \frac{[BCP]}{[BAP]} \cdot \frac{[CAP]}{[CBP]} = 1$$

karena tiap luas muncul sekali di pembilang dan sekali di penyebut. Jadi Ceva bukan rumus
yang harus dihafal — ia bisa dibangun ulang dari perbandingan luas kapan saja.

Sekalian periksa angkanya: dengan $\tfrac{[ABP]}{[ACP]} = \tfrac23$ dan
$\tfrac{[BCP]}{[ABP]} = \tfrac34$, ambil $[ABP] = 6$, maka $[ACP] = 9$ dan $[BCP] = 4{,}5$.
Maka $\dfrac{AF}{FB} = \dfrac{[ACP]}{[BCP]} = \dfrac{9}{4{,}5} = 2$ ✓

### Jebakan: satu suku dibalik

Kalau salah satu pecahan ditulis terbalik — misalnya $\dfrac{DC}{BD}$ alih-alih
$\dfrac{BD}{DC}$ — hasil kalinya menjadi kebalikannya, dan jawabannya keluar $\tfrac12$
alih-alih $2$.

Yang menyelamatkan bukan hafalan melainkan pola berkelilingnya. Tuliskan dulu urutan
hurufnya, $B \to D \to C \to E \to A \to F \to B$, lalu potong-potong jadi tiga pecahan. Kalau
huruf terakhirnya kembali ke huruf pertama, urutannya pasti benar.

### Kapan Ceva, kapan Menelaus

Keduanya berbentuk sama persis, dan salah pilih menghasilkan bukti yang rapi tetapi
membuktikan hal lain. Pembedanya cuma satu:

- ketiga ruas **berangkat dari titik sudut** dan bertemu di satu titik → **Ceva**;
- satu garis lurus **melintasi** segitiga, memotong ketiga sisi atau perpanjangannya →
  **Menelaus**.

Kalau panjangnya dihitung bertanda, hasil kali Ceva bernilai $+1$ sedangkan Menelaus $-1$ —
dan itu satu-satunya beda rumusnya.

### Arah yang lebih sering dipakai di olimpiade

Soal ini memakai Ceva ke arah "diketahui konkuren, hitung perbandingan". Di olimpiade, arah
**kebalikannya** yang lebih sering muncul: hitung hasil kali ketiga perbandingan, tunjukkan
nilainya $1$, lalu simpulkan ketiga ruasnya konkuren.

Kebalikan Ceva memang berlaku, tetapi di lembar jawaban ia harus disebut eksplisit — menulis
"menurut Ceva" saja tidak cukup, karena yang dipakai bukan Ceva melainkan kebalikannya.
