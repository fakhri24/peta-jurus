---
id: trg-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [trigonometri-segitiga]
bentuk: isian
kesulitan: 3
jawaban: "60"
---

## Soal

Pada segitiga $ABC$ diketahui $BC = 7$, $CA = 5$, dan $AB = 8$.

Tentukan besar sudut $A$ dalam derajat.

## Petunjuk

- Yang diketahui ketiga sisinya, yang ditanyakan sebuah sudut. Aturan mana yang menghubungkan keempatnya sekaligus?
- Aturan kosinus. Pastikan sisi yang berdiri sendiri di ruas kiri adalah sisi yang **berhadapan** dengan sudut yang dicari.
- $\cos A = \dfrac{b^2 + c^2 - a^2}{2bc}$ dengan $a = BC$, sisi di hadapan $A$.

## Pembahasan

**Pasangkan hurufnya dengan benar.** Penamaan bakunya: $a$ sisi di hadapan $A$, $b$ di
hadapan $B$, $c$ di hadapan $C$. Jadi

$$a = BC = 7, \qquad b = CA = 5, \qquad c = AB = 8$$

Langkah ini terlihat sepele dan justru di sinilah kekeliruan paling sering masuk. Sudut $A$
berhadapan dengan $BC$, bukan dengan $AB$.

**Pakai aturan kosinus.**

$$\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{5^2 + 8^2 - 7^2}{2 \cdot 5 \cdot 8}
= \frac{25 + 64 - 49}{80} = \frac{40}{80} = \frac{1}{2}$$

$$A = \boxed{60^\circ}$$

### Periksa: jumlah ketiga sudutnya

$$\cos B = \frac{a^2+c^2-b^2}{2ac} = \frac{49+64-25}{112} = \frac{88}{112} = \frac{11}{14}
\ \Longrightarrow\ B \approx 38{,}21^\circ$$

$$\cos C = \frac{a^2+b^2-c^2}{2ab} = \frac{49+25-64}{70} = \frac{10}{70} = \frac{1}{7}
\ \Longrightarrow\ C \approx 81{,}79^\circ$$

$$60 + 38{,}21 + 81{,}79 = 180 \quad ✓$$

Menghitung ketiganya lalu menjumlahkan adalah pemeriksaan termurah pada soal aturan
kosinus, dan ia menangkap hampir semua kesalahan pemasangan huruf.

### Apa yang dibuka oleh $A = 60^\circ$

Begitu satu sudutnya diketahui, dua besaran lain jatuh dengan sendirinya.

**Luas**, lewat rumus sudut apit:

$$L = \tfrac{1}{2} bc \sin A = \tfrac{1}{2} \cdot 5 \cdot 8 \cdot \frac{\sqrt3}{2} = 10\sqrt3$$

Bandingkan dengan Heron, $s = 10$:

$$L = \sqrt{10 \cdot 3 \cdot 5 \cdot 2} = \sqrt{300} = 10\sqrt3 \quad ✓$$

**Jari-jari lingkaran luar**, lewat bentuk lengkap aturan sinus:

$$\frac{a}{\sin A} = 2R \quad \Longrightarrow \quad
2R = \frac{7}{\sqrt3/2} = \frac{14}{\sqrt3} \quad \Longrightarrow \quad R = \frac{7\sqrt3}{3} \approx 4{,}04$$

Periksa dengan rumus lain, $R = \dfrac{abc}{4L} = \dfrac{7 \cdot 5 \cdot 8}{4 \cdot 10\sqrt3}
= \dfrac{280}{40\sqrt3} = \dfrac{7}{\sqrt3}$ ✓

Bagian $2R$ itu yang paling sering tidak diajarkan, dan justru yang paling sering
menyelesaikan soal olimpiade — ia satu-satunya jembatan langsung antara sudut segitiga dan
lingkaran luarnya.

### Mengapa aturan kosinus, bukan aturan sinus

Aturan sinus menghubungkan **sisi dengan sudut di hadapannya**. Kalau yang diketahui hanya
sisi-sisi, tidak ada satu pun pasangan lengkap untuk memulainya — setiap persamaan memuat
dua hal yang belum diketahui.

Aturan kosinus tidak punya masalah itu: ia memuat tiga sisi dan satu sudut, jadi kalau
ketiga sisinya ada, sudutnya langsung keluar. Aturan praktisnya:

- **tiga sisi**, atau **dua sisi dan sudut apitnya** → kosinus;
- **dua sudut dan satu sisi**, atau **dua sisi dan sudut di hadapan salah satunya** → sinus.

### Segitiga 5-7-8, dan kenapa angkanya begitu

Sudut $60^\circ$ keluar bulat bukan kebetulan: soalnya disusun mundur dari $\cos A =
\tfrac12$, yaitu $b^2 + c^2 - a^2 = bc$. Dengan $b = 5$ dan $c = 8$ itu memberi
$a^2 = 25 + 64 - 40 = 49$.

Cara yang sama memberi seluruh keluarga segitiga bersudut $60^\circ$ dengan sisi bulat:
$3,7,8$ dan $7,13,15$ termasuk di dalamnya, karena $9 + 64 - 24 = 49$ dan
$49 + 225 - 105 = 169$.

Keluarga kembarannya memakai $\cos = -\tfrac12$, yaitu $a^2 = b^2 + c^2 + bc$, dan memberi
segitiga bersudut $120^\circ$ — di situ $3,5,7$ yang paling terkenal. Mengenali keduanya
berguna: soal yang sisinya salah satu dari daftar itu hampir pasti ingin kamu menemukan
sudut istimewanya, bukan menghitung kosinus berkoma.
