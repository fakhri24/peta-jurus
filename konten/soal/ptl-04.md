---
id: ptl-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ptolemy]
bentuk: isian
kesulitan: 3
jawaban: "9"
---

## Soal

Diberikan segitiga sama sisi $ABC$ dan sebuah titik $P$ di bidang yang sama dengan
$PB = 4$ dan $PC = 5$. Titik $P$ boleh berada di mana saja — di dalam segitiga, di luarnya,
atau pada lingkaran luarnya.

Tentukan nilai terbesar yang mungkin bagi $PA$.

## Petunjuk

- Yang diminta nilai **terbesar**, bukan nilai tertentu, dan $P$ boleh di mana saja. Itu tanda alatnya bukan kesamaan melainkan batas — batas yang berubah menjadi kesamaan tepat ketika keempat titiknya setalibusur.
- Bentuk itu pemicu ketaksamaan Ptolemy: untuk **empat titik sembarang**, $AP \cdot BC \le AB \cdot PC + BP \cdot CA$.
- Segitiganya sama sisi, jadi ketiga sisinya bisa dicoret. Kapan kesamaannya tercapai?

## Pembahasan

**Pakai ketaksamaan Ptolemy.** Untuk empat titik sembarang $A$, $B$, $P$, $C$ pada bidang:

$$AP \cdot BC \ \le\ AB \cdot PC + BP \cdot CA$$

**Coret sisinya.** Karena $AB = BC = CA = s$ dengan $s > 0$:

$$AP \cdot s \ \le\ s \cdot PC + BP \cdot s \quad \Longrightarrow \quad AP \ \le\ PB + PC = 4 + 5 = 9$$

**Periksa bahwa batas itu tercapai.** Kesamaan pada ketaksamaan Ptolemy berlaku tepat ketika
$ABPC$ segiempat talibusur dengan urutan itu — yaitu ketika $P$ berada pada busur $BC$ yang
tidak memuat $A$.

Titik seperti itu ada: ambil segitiga sama sisi dengan sisi

$$s^2 = 4^2 + 5^2 - 2 \cdot 4 \cdot 5 \cos 120^\circ = 16 + 25 + 20 = 61$$

yaitu $s = \sqrt{61} \approx 7{,}81$, lalu tempatkan $P$ pada busur $BC$ dengan $PB = 4$.
Sudut $\angle BPC$ otomatis $120^\circ$ karena berpelurus dengan $\angle BAC = 60^\circ$,
sehingga $PC$ keluar tepat $5$.

Jadi nilai terbesarnya benar-benar dicapai:

$$PA_{\max} = \boxed{9}$$

### Kenapa "periksa tercapai" tidak boleh dilewati

Ketaksamaan hanya memberi **batas atas**. Batas atas yang tidak pernah dicapai bukan nilai
terbesar — ia cuma bilangan yang lebih besar dari semuanya.

Contohnya soal yang sama tetapi segitiganya **ditetapkan** bersisi $6$. Di situ
$PB + PC = 9 > 6 = BC$ masih memenuhi ketaksamaan segitiga, jadi $P$ ada; tetapi apakah $P$
bisa berada pada busur $BC$ dengan $PB = 4$ dan $PC = 5$ sekaligus? Untuk itu diperlukan
$s = \sqrt{61} \ne 6$, jadi **tidak bisa** — dan nilai terbesar $PA$ menjadi lebih kecil
dari $9$.

Karena itu soal ini sengaja **tidak** menyebutkan panjang sisi segitiganya: kebebasan itulah
yang membuat kesamaannya bisa dicapai.

### Tidak ada bentuk Ptolemy untuk batas bawah

Ketaksamaan Ptolemy hanya berjalan satu arah: ia membatasi $AP \cdot BC$ **dari atas**. Tidak
ada bentuk kembarannya yang membatasi dari bawah, sebab kesamaannya menandai keadaan yang
paling "terentang" — keempat titik pada satu lingkaran dengan urutan tertentu — dan tidak ada
keadaan ekstrem yang berlawanan dengan itu.

Akibat praktisnya: kalau soal menanyakan nilai **terkecil**, Ptolemy bukan alatnya. Yang
biasanya dipakai di sana ketaksamaan segitiga langsung, atau pencerminan seperti pada jurus
transformasi.

### Pemicu yang perlu dikenali

Ketaksamaan Ptolemy pantas dicoba saat soal memuat **empat titik dan sebuah hasil kali
panjang, tanpa jaminan keempatnya setalibusur**. Kata "sembarang", "di mana saja", atau
"nilai terbesar" hampir selalu penandanya.

Yang membedakannya dari teorema Ptolemy biasa cuma satu: teoremanya butuh keempat titik pada
satu lingkaran, ketaksamaannya tidak butuh apa-apa.

### Kalau titiknya di dalam segitiga

Sekadar gambaran seberapa jauh batasnya dari kasus lain: untuk $P$ di **dalam** segitiga sama
sisi, ketiga jaraknya justru memenuhi ketaksamaan yang berlawanan arah,

$$PA \ <\ PB + PC$$

tetap, tetapi tidak pernah mencapai kesamaan — sebab kesamaan menuntut $P$ pada lingkaran
luarnya, dan lingkaran luar tidak melewati bagian dalam segitiga. Jadi seluruh bagian dalam
segitiga otomatis tersingkir dari kandidat nilai terbesar.
