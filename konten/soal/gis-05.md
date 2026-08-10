---
id: gis-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [garis-istimewa]
bentuk: uraian
kesulitan: 3
---

## Soal

Pada segitiga $ABC$, garis bagi sudut $A$ memotong sisi $BC$ di titik $D$.

Buktikan bahwa

$$\frac{BD}{DC} = \frac{AB}{AC}$$

## Petunjuk

- Kedua bagian yang dibandingkan, $BD$ dan $DC$, adalah alas dari dua segitiga yang berbagi puncak. Apa yang sama pada keduanya?
- Bandingkan luas $\triangle ABD$ dan $\triangle ACD$. Luas itu bisa ditulis dua cara: dengan alas pada $BC$, dan dengan sudut di $A$.
- Dengan alas pada $BC$ perbandingannya $BD : DC$; dengan sudut di $A$ perbandingannya $AB : AC$ karena kedua sudutnya sama besar.

## Pembahasan

Kuncinya menghitung **satu besaran dengan dua cara**. Besaran itu adalah perbandingan luas
$[ABD] : [ACD]$.

**Cara pertama: alas pada $BC$.** Kedua segitiga punya puncak yang sama, yaitu $A$, dan
alasnya terletak pada satu garis yang sama, yaitu $BC$. Jadi tingginya — jarak dari $A$ ke
garis $BC$ — sama, sebutlah $h$:

$$[ABD] = \tfrac{1}{2} \cdot BD \cdot h, \qquad [ACD] = \tfrac{1}{2} \cdot DC \cdot h$$

$$\frac{[ABD]}{[ACD]} = \frac{BD}{DC}$$

**Cara kedua: sudut di $A$.** Pakai rumus luas dengan sudut apit. Pada $\triangle ABD$ sudut
apitnya $\angle BAD$ di antara sisi $AB$ dan $AD$; pada $\triangle ACD$ sudut apitnya
$\angle DAC$ di antara $AC$ dan $AD$:

$$[ABD] = \tfrac{1}{2} \cdot AB \cdot AD \cdot \sin \angle BAD$$

$$[ACD] = \tfrac{1}{2} \cdot AC \cdot AD \cdot \sin \angle DAC$$

Karena $AD$ garis bagi, $\angle BAD = \angle DAC$, sehingga $\sin \angle BAD = \sin \angle DAC$.
Faktor itu dan faktor $AD$ sama-sama muncul di pembilang dan penyebut, lalu lenyap:

$$\frac{[ABD]}{[ACD]} = \frac{AB}{AC}$$

**Samakan keduanya.** Satu bilangan yang sama dihitung dua cara, maka

$$\frac{BD}{DC} = \frac{[ABD]}{[ACD]} = \frac{AB}{AC} \qquad \blacksquare$$

### Cara kedua: tarik garis sejajar

Bukti tanpa luas sama sekali. Tarik garis lewat $C$ sejajar $AD$; ia memotong perpanjangan
$BA$ di titik $E$.

Karena $AD \parallel EC$ dipotong garis $BE$, sudut $\angle BAD = \angle AEC$ (sehadap).
Karena $AD \parallel EC$ dipotong garis $AC$, sudut $\angle DAC = \angle ACE$ (dalam
berseberangan). Padahal $\angle BAD = \angle DAC$, maka

$$\angle AEC = \angle ACE$$

sehingga $\triangle ACE$ sama kaki dengan $AE = AC$.

Sekarang $\triangle BAD \sim \triangle BEC$ karena $AD \parallel EC$, jadi

$$\frac{BD}{BC} = \frac{BA}{BE} \quad \Longrightarrow \quad
\frac{BD}{DC} = \frac{BA}{AE} = \frac{AB}{AC}$$

Kedua bukti memakai fakta yang berbeda — satu memakai luas, satu memakai kesejajaran — dan
sampai ke kesimpulan yang sama. Yang pertama lebih pendek; yang kedua lebih mudah diingat
ulang saat rumus luas dengan sinus belum boleh dipakai.

### Yang wajib disebut di lembar jawaban

Yang membuat bukti ini sah bukan rumusnya, melainkan **alasan tiap penyederhanaan**:

- pada cara pertama, alasan tingginya sama adalah $B$, $D$, $C$ segaris — kalau itu tidak
  disebut, langkah pertamanya menggantung;
- pada cara kedua, alasan sinusnya sama adalah sifat garis bagi — itu satu-satunya tempat
  keterangan soal dipakai, jadi menghilangkannya membuat "buktinya" berlaku untuk sembarang
  ruas $AD$, yang jelas salah.

### Kebalikannya juga berlaku

Kalau $D$ pada $BC$ memenuhi $\dfrac{BD}{DC} = \dfrac{AB}{AC}$, maka $AD$ pasti garis bagi
sudut $A$. Alasannya: hanya ada **satu** titik pada ruas $BC$ yang membaginya menurut
perbandingan tertentu, dan garis bagi sudah menghasilkan titik dengan perbandingan itu.
Arah kebalikan inilah yang dipakai untuk **membuktikan** suatu ruas adalah garis bagi, dan
di lembar jawaban ia perlu disebut eksplisit.

## Rubrik

- Menyatakan besaran yang akan dihitung dua cara, yaitu perbandingan luas $[ABD] : [ACD]$
- Menyebut bahwa $\triangle ABD$ dan $\triangle ACD$ punya tinggi yang sama dari $A$, dengan
  alasan $B$, $D$, $C$ segaris, lalu menyimpulkan perbandingannya $BD : DC$
- Menulis kedua luas dengan rumus sudut apit di $A$
- Memakai $\angle BAD = \angle DAC$ — sifat garis bagi — untuk melenyapkan faktor sinusnya,
  dan menyimpulkan perbandingannya $AB : AC$
- Menyamakan kedua hasil dan menuliskan kesimpulannya

Bukti dengan garis sejajar lewat $C$ dinilai penuh asalkan kesamaan sudut sehadap dan dalam
berseberangan disebut, $\triangle ACE$ ditunjukkan sama kaki, dan kesebangunan
$\triangle BAD \sim \triangle BEC$ dinyatakan beserta alasannya.
