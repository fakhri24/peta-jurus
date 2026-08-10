---
id: tkd-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [tempat-kedudukan]
bentuk: uraian
kesulitan: 4
---

## Soal

Diberikan lingkaran $\omega$ berpusat $O$ berjari-jari $R$, dan sebuah titik tetap $A$
di dalam $\omega$ dengan $A \ne O$.

![Sebuah lingkaran berpusat O. Di dalamnya ada titik tetap A yang letaknya jelas bukan di pusat, melainkan di kanan atas O. Tiga tali busur digambar, ketiganya melalui A dengan arah yang berbeda-beda, sehingga A menjadi satu-satunya titik yang dilalui ketiganya. Titik tengah masing-masing tali busur ditandai dan diberi nama M, N, dan K. Ketiga titik tengah itu tidak segaris dan letaknya berkumpul di daerah antara O dan A](talibusur-lewat-titik-tetap.svg)

Tentukan tempat kedudukan titik tengah semua tali busur $\omega$ yang melalui $A$, dan
**buktikan kedua arahnya**.

## Petunjuk

- Sebut $M$ titik tengah sebuah tali busur. Ada satu hubungan baku antara pusat lingkaran dan titik tengah tali busur — dan hubungan itu memberi sebuah sudut.
- $OM$ tegak lurus tali busurnya. Karena $A$ juga terletak pada tali busur itu, sudut $\angle OMA$ diketahui besarnya.
- Titik yang melihat ruas $OA$ dengan sudut siku-siku membentuk lingkaran berdiameter $OA$. Setelah itu, arah sebaliknya masih harus dikerjakan: ambil sembarang titik pada lingkaran itu, dan tunjukkan ia memang titik tengah suatu tali busur lewat $A$.

## Pembahasan

**Jawabannya.** Tempat kedudukannya adalah **lingkaran berdiameter $OA$** — seluruhnya,
tanpa titik yang dibuang.

Sebut lingkaran itu $\gamma$: berpusat di titik tengah $OA$, berjari-jari $\dfrac{OA}{2}$.

### Arah pertama: setiap titik tengah ada pada $\gamma$

Ambil sembarang tali busur $PQ$ dari $\omega$ yang melalui $A$, dan sebut $M$ titik
tengahnya. Ada dua kemungkinan.

**Kasus $M \ne O$.** Segitiga $OPQ$ sama kaki, sebab $OP = OQ = R$. Pada segitiga sama
kaki, garis dari puncak ke titik tengah alas sekaligus tegak lurus alasnya, jadi

$$OM \perp PQ$$

Titik $A$ terletak pada tali busur $PQ$, dan $M$ juga. Kalau $M \ne A$, maka $MA$
sepanjang garis $PQ$, sehingga

$$\angle OMA = 90^\circ$$

Menurut teorema Thales, $M$ ada pada lingkaran berdiameter $OA$, yaitu $\gamma$ ✓

Kalau $M = A$, titik itu salah satu ujung diameter $\gamma$, jadi ia ada pada $\gamma$ ✓

**Kasus $M = O$.** Terjadi ketika tali busurnya diameter, yaitu tali busur yang melalui
$O$ dan $A$ sekaligus. Titik $O$ adalah ujung diameter $\gamma$ yang lain, jadi ia ada
pada $\gamma$ ✓

### Arah kedua: setiap titik $\gamma$ adalah titik tengah suatu tali busur lewat $A$

Ini arah yang paling sering dilewatkan, dan tanpanya jawabannya belum lengkap — sejauh
ini yang terbukti hanya bahwa tempat kedudukannya **termuat** di $\gamma$, belum bahwa ia
seluruh $\gamma$.

Ambil sembarang $M$ pada $\gamma$.

**Kalau $M = O$:** ambil tali busur yang melalui $O$ dan $A$. Ia diameter, dan titik
tengah diameter adalah $O$ ✓

**Kalau $M = A$:** ambil tali busur yang melalui $A$ dan tegak lurus $OA$. Kaki tegak
lurus dari $O$ ke tali busur itu adalah $A$ sendiri, dan kaki tegak lurus dari pusat ke
tali busur selalu titik tengahnya ✓

**Selain itu:** karena $M$ pada $\gamma$ dan $OA$ diameternya, teorema Thales memberi

$$\angle OMA = 90^\circ$$

Tarik garis $g$ yang melalui $M$ dan $A$. Dari $\angle OMA = 90^\circ$ diperoleh
$OM \perp g$.

Garis $g$ memang memotong $\omega$ pada dua titik, sebab jaraknya dari $O$ adalah
$OM \le OA < R$ — jadi $g$ sungguh-sungguh sebuah tali busur. Ia melalui $A$ menurut
pembuatannya, dan titik tengahnya adalah kaki tegak lurus dari $O$, yaitu $M$ ✓

Kedua arah terbukti, jadi tempat kedudukannya **tepat** $\gamma$ $\blacksquare$

### Tidak ada yang dibuang, dan itu perlu diperiksa

Banyak tempat kedudukan berbentuk "bangun baku dikurangi beberapa titik". Di sini
tidak — dan alasannya baru terlihat setelah arah kedua dikerjakan: kedua titik yang
biasanya bermasalah, $O$ dan $A$, keduanya tercapai oleh tali busur yang sah.

Kalau $A$ diletakkan **pada** $\omega$, ceritanya berubah: lingkaran $\gamma$ tetap
terbentuk, tetapi titik $A$ sendiri hanya dicapai oleh "tali busur" yang merosot menjadi
satu titik. Jadi letak $A$ di dalam $\omega$ bukan syarat hiasan.

### Kasus merosot $A = O$

Kalau $A = O$, setiap tali busur lewat $A$ adalah diameter, dan semua titik tengahnya
jatuh di $O$. Tempat kedudukannya menyusut menjadi **satu titik**.

Rumusnya tetap benar kalau dibaca dengan benar: lingkaran berdiameter $OA$ dengan
$OA = 0$ adalah titik $O$ itu sendiri. Soal ini menyebut $A \ne O$ justru supaya
jawabannya berupa lingkaran sungguhan, tetapi menyebutkan kasus merosotnya menunjukkan
jawabannya dipahami, bukan dihafal.

### Cara analitik, sebagai pemeriksaan

Taruh $O = (0,0)$ dan $A = (p, q)$. Tali busur berarah satuan $\vec{u}$ melalui $A$
terdiri atas titik $A + t\vec{u}$, dan berpotongan dengan $\omega$ pada akar-akar

$$t^2 + 2t\,(A \cdot \vec u) + \left(|A|^2 - R^2\right) = 0$$

Jumlah kedua akarnya $-2(A \cdot \vec u)$, jadi titik tengahnya ada di
$t = -(A \cdot \vec u)$:

$$M = A - (A \cdot \vec u)\,\vec u$$

Hitung jaraknya ke titik tengah $OA$:

$$\left|M - \tfrac{A}{2}\right|^2
= \left|\tfrac{A}{2} - (A\cdot\vec u)\vec u\right|^2
= \frac{|A|^2}{4} - (A\cdot\vec u)^2 + (A\cdot\vec u)^2 = \frac{|A|^2}{4}$$

Jadi $\left|M - \tfrac{A}{2}\right| = \dfrac{|A|}{2} = \dfrac{OA}{2}$ untuk setiap arah
$\vec u$ ✓ — persis lingkaran berdiameter $OA$.

Perhatikan bahwa cara ini membuktikan **kedua arah sekaligus**, sebab tiap titik $\gamma$
diperoleh dari suatu $\vec u$. Itu keunggulan jalur analitik pada soal tempat kedudukan;
ongkosnya, ia tidak memperlihatkan sudut siku-siku yang menjadi sebabnya.

## Rubrik

- Menyatakan jawabannya: lingkaran berdiameter $OA$
- **Arah pertama:** menurunkan $OM \perp PQ$ dengan alasan (segitiga sama kaki $OPQ$,
  atau sifat baku garis dari pusat ke titik tengah tali busur)
- **Arah pertama:** menyimpulkan $\angle OMA = 90^\circ$ dan memakai Thales
- **Arah kedua:** mengambil sembarang $M \in \gamma$ dan **membangun** tali busur yang
  titik tengahnya $M$ — bukan sekadar menyatakan bahwa arah kedua "jelas"
- **Arah kedua:** memeriksa bahwa garis yang dibangun memang memotong $\omega$, yaitu
  $OM < R$
- Menangani kasus $M = O$ dan $M = A$ pada kedua arah, atau menyatakan mengapa keduanya
  tidak perlu dipisah
- Menyatakan bahwa tidak ada titik $\gamma$ yang harus dibuang

Bukti analitik penuh dinilai sama penuh, asalkan disebutkan secara eksplisit bahwa
setiap titik lingkarannya tercapai oleh suatu arah $\vec u$ — tanpa kalimat itu, yang
terbukti baru satu arah, sama seperti pada bukti sintetiknya.
