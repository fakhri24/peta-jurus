---
id: trg-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [trigonometri-segitiga, pythagoras]
bentuk: uraian
kesulitan: 3
---

## Soal

Pada segitiga $ABC$, tulis $a = BC$, $b = CA$, dan $c = AB$.

**(a)** Dengan menarik garis tinggi dari $A$ ke sisi $BC$, buktikan bahwa

$$c^2 = a^2 + b^2 - 2ab \cos C$$

untuk segitiga yang ketiga sudutnya lancip.

![Segitiga ABC dengan ketiga sudutnya lancip. Sisi BC mendatar sebagai alas, dengan B di kiri bawah dan C di kanan bawah; panjangnya diberi nama a. Sisi CA di sebelah kanan diberi nama b, dan sisi AB di sebelah kiri diberi nama c. Puncak A berada di atas, agak ke kiri. Dari A ditarik garis tinggi putus-putus tegak lurus alas, memotongnya di titik D yang terletak di antara B dan C. Sudut di titik sudut C ditandai busur kecil, karena sudut itulah yang muncul dalam rumusnya](segitiga-lancip-kaki-tinggi.svg)

**(b)** Tunjukkan bahwa rumus yang sama tetap berlaku ketika $\angle C$ tumpul.

## Petunjuk

- Garis tinggi memecah segitiga jadi dua segitiga siku-siku, dan pada segitiga siku-siku kamu boleh memakai Pythagoras.
- Namai kaki garis tingginya $D$. Nyatakan $CD$ dan $AD$ dengan $b$ dan $\angle C$, lalu nyatakan $BD$ dengan $a$ dan $CD$.
- Untuk (b), yang berubah hanya letak $D$: ia keluar dari ruas $BC$. Perhatikan bahwa $\cos C$ juga berubah tanda, dan periksa apakah kedua perubahan itu saling meniadakan.

## Pembahasan

### Bagian (a) — segitiga lancip

**Tarik garis tinggi dan namai kakinya.** Misalkan $D$ kaki garis tinggi dari $A$ pada $BC$.
Karena $\angle B$ dan $\angle C$ keduanya lancip, $D$ terletak **di antara** $B$ dan $C$.

**Nyatakan dua ruas dengan $b$ dan $\angle C$.** Segitiga $ADC$ siku-siku di $D$, dengan
sisi miring $AC = b$ dan sudut $\angle ACD = \angle C$:

$$CD = b \cos C, \qquad AD = b \sin C$$

**Nyatakan $BD$.** Karena $D$ di antara $B$ dan $C$:

$$BD = BC - CD = a - b \cos C$$

**Pakai Pythagoras pada segitiga $ABD$**, yang siku-siku di $D$ dengan sisi miring $AB = c$:

$$c^2 = AD^2 + BD^2 = \left(b \sin C\right)^2 + \left(a - b\cos C\right)^2$$

**Jabarkan dan rapikan.**

$$c^2 = b^2 \sin^2 C + a^2 - 2ab \cos C + b^2 \cos^2 C$$

$$= a^2 - 2ab\cos C + b^2\left(\sin^2 C + \cos^2 C\right)$$

Karena $\sin^2 C + \cos^2 C = 1$:

$$c^2 = a^2 + b^2 - 2ab\cos C \qquad \blacksquare$$

### Bagian (b) — $\angle C$ tumpul

Yang berubah hanya satu: karena $\angle C > 90^\circ$, kaki garis tinggi $D$ jatuh di
**perpanjangan** $BC$ melewati $C$, bukan di dalam ruasnya.

Tulis $\theta = 180^\circ - \angle C$, sudut pelurusnya, yang lancip. Pada segitiga siku-siku
$ADC$ sudut di $C$ adalah $\theta$, sehingga

$$CD = b \cos\theta = -b\cos C, \qquad AD = b\sin\theta = b \sin C$$

Sekarang $C$ berada di antara $B$ dan $D$, jadi panjangnya **dijumlahkan**, bukan
dikurangkan:

$$BD = BC + CD = a - b\cos C$$

Ruas kanannya **sama persis** dengan bagian (a). Dua perubahan itu — letak $D$ yang membalik
tanda operasinya, dan $\cos C$ yang membalik tandanya sendiri — saling meniadakan. Sisa
perhitungannya identik:

$$c^2 = AD^2 + BD^2 = b^2\sin^2 C + \left(a - b\cos C\right)^2 = a^2 + b^2 - 2ab\cos C \qquad \blacksquare$$

### Kasus yang tersisa

Untuk kelengkapan, $\angle C = 90^\circ$ memberi $\cos C = 0$ dan rumusnya menyusut menjadi
$c^2 = a^2 + b^2$ — teorema Pythagoras. Jadi Pythagoras bukan teorema yang berbeda dari
aturan kosinus, melainkan kasus khususnya.

Masih ada satu bentuk lagi yang belum tersentuh: $\angle B$ tumpul, sementara $\angle C$
tetap lancip. Di situ $D$ jatuh di perpanjangan $BC$ di seberang $B$, sehingga
$b\cos C > a$ dan $BD = b\cos C - a$. Karena yang dipakai selanjutnya cuma $BD^2$, dan
$\left(b\cos C - a\right)^2 = \left(a - b\cos C\right)^2$, hasilnya tetap sama.

### Mengapa dua kasus itu perlu dipisahkan

Godaan terbesarnya adalah menulis bagian (a) saja lalu berkata "kasus lain serupa". Itu
tidak cukup, karena **langkah $BD = a - b\cos C$ memakai letak $D$ secara sungguhan** —
tanpa memeriksa ulang letaknya, langkah itu tidak punya alasan pada segitiga tumpul.

Yang menarik justru kesimpulannya: kedua kasus memberi ungkapan yang sama, dan itu sebabnya
rumus aturan kosinus tidak pernah membawa syarat "hanya untuk segitiga lancip". Sifat itu
harus **dibuktikan**, bukan diandaikan.

### Cara yang tidak butuh kasus sama sekali

Dengan vektor, seluruh pembagian kasus lenyap. Tulis $\vec{u} = \overrightarrow{CB}$ dan
$\vec{v} = \overrightarrow{CA}$, maka $\overrightarrow{AB} = \vec u - \vec v$ dan

$$c^2 = \left|\vec u - \vec v\right|^2 = \left|\vec u\right|^2 + \left|\vec v\right|^2
- 2\,\vec u \cdot \vec v = a^2 + b^2 - 2ab\cos C$$

karena $\vec u \cdot \vec v = ab \cos C$ menurut definisi hasil kali titik. Bukti ini lebih
pendek, tetapi ia memindahkan pekerjaannya ke definisi hasil kali titik — dan definisi itu
sendiri biasanya dibangun dari aturan kosinus. Untuk lembar jawaban olimpiade, keduanya sah.

## Rubrik

- **(a)** Menarik garis tinggi dari $A$, menamai kakinya, dan menyebut alasan $D$ terletak
  di antara $B$ dan $C$ pada segitiga lancip
- **(a)** Menyatakan $CD = b\cos C$ dan $AD = b\sin C$ dari segitiga siku-siku $ADC$
- **(a)** Menyatakan $BD = a - b\cos C$ dengan alasan letak $D$
- **(a)** Memakai Pythagoras pada $\triangle ABD$, menjabarkannya, dan memakai
  $\sin^2 C + \cos^2 C = 1$ untuk sampai ke bentuk yang diminta
- **(b)** Menyebut bahwa $D$ jatuh di perpanjangan $BC$ melewati $C$ ketika $\angle C$ tumpul
- **(b)** Menyatakan $CD = -b\cos C$ dengan alasan $\cos C < 0$, atau lewat sudut pelurusnya
- **(b)** Menunjukkan $BD = BC + CD$ menghasilkan ungkapan yang sama, $a - b\cos C$, lalu
  menyimpulkan sisa perhitungannya identik

Bukti vektor dinilai penuh untuk kedua bagian sekaligus, asalkan
$\vec u \cdot \vec v = ab\cos C$ dinyatakan dan penjabaran $\left|\vec u - \vec v\right|^2$
ditulis lengkap.
