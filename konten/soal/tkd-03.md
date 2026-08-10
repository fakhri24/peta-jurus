---
id: tkd-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [tempat-kedudukan, sudut-lingkaran]
bentuk: isian
kesulitan: 4
jawaban: "8"
---

## Soal

Ruas $AB$ tetap dengan $AB = 8$. Titik $P$ bergerak sehingga $\angle APB = 150^\circ$.

Tempat kedudukan $P$ terdiri atas dua busur lingkaran yang saling bercermin pada $AB$.
Tentukan jari-jari lingkarannya.

![Sebuah ruas mendatar AB dengan A di kiri dan B di kanan. Melalui A dan B digambar dua busur lingkaran yang dangkal dan sama bentuknya: satu melengkung ke atas AB, satu lagi melengkung ke bawah, saling bercermin pada AB sehingga bersama-sama membentuk bangun seperti lensa. Titik P berada di puncak busur atas dan dihubungkan ke A dan ke B; sudut di P besarnya 150 derajat dan tampak sangat tumpul. Titik Q berada pada busur bawah, tidak di titik terendahnya melainkan agak ke kiri, dan juga dihubungkan ke A dan ke B dengan ruas putus-putus. Sudut di Q sama tumpulnya dengan sudut di P](busur-sudut-tetap.svg)

## Petunjuk

- $A$, $B$, dan $P$ ketiganya ada pada satu lingkaran, dan $AB$ menjadi tali busurnya. Ada satu rumus yang menghubungkan panjang tali busur, sudut kelilingnya, dan jari-jari.
- Aturan sinus pada segitiga $APB$: $\dfrac{AB}{\sin \angle APB} = 2R$.
- $\sin 150^\circ = \sin 30^\circ = \dfrac12$.

## Pembahasan

**Aturan sinus.** Segitiga $APB$ punya lingkaran luar, dan $P$ bergerak pada lingkaran
itu. Aturan sinus dalam bentuk yang memuat jari-jari lingkaran luar berbunyi

$$\frac{AB}{\sin \angle APB} = 2R$$

Masukkan angkanya, dengan $\sin 150^\circ = \tfrac12$:

$$\frac{8}{\tfrac12} = 2R \quad \Longrightarrow \quad 16 = 2R \quad \Longrightarrow \quad
R = \boxed{8}$$

**Periksa lewat sudut pusat.** Jari-jari $8$ dan tali busur $8$ berarti segitiga $AOB$
punya ketiga sisi $8$ — jadi ia sama sisi, dan

$$\angle AOB = 60^\circ$$

Sudut keliling dari busur **kecil** adalah setengah sudut pusat busur besarnya:

$$\angle APB = \frac{360^\circ - 60^\circ}{2} = 150^\circ \quad ✓$$

Jarak pusatnya ke $AB$:

$$\sqrt{8^2 - 4^2} = \sqrt{48} = 4\sqrt3 \approx 6{,}93$$

Karena $4\sqrt3 > 0$ dan busurnya di sisi berlawanan dari pusat, busurnya hanya
menonjol $8 - 4\sqrt3 \approx 1{,}07$ dari $AB$ — dangkal, seperti pada gambar ✓

### Busur yang mana

Ini bagian yang paling mudah keliru. Satu lingkaran memberi **dua** busur pada tali
busur $AB$, dan sudut kelilingnya berbeda di masing-masing:

| Busur | Sudut keliling |
|---|---|
| busur kecil (dekat $AB$) | $150^\circ$ |
| busur besar | $30^\circ$ |

Keduanya berjumlah $180^\circ$ — memang begitu seharusnya, sebab $APBQ$ pada busur yang
berlawanan membentuk segiempat tali busur, dan sudut yang berhadapan pada segiempat tali
busur berjumlah $180^\circ$.

Jadi **lingkaran yang sama** melayani dua soal sekaligus: $\angle APB = 150^\circ$ pada
busur kecilnya, dan $\angle APB = 30^\circ$ pada busur besarnya. Aturan sinus tidak
membedakan keduanya, sebab $\sin 150^\circ = \sin 30^\circ$ — dan itu bukan cacat
rumusnya, melainkan pernyataan bahwa jari-jarinya memang sama.

Yang membedakan cuma **busur mana** yang menjadi jawaban. Untuk sudut tumpul, busurnya
yang kecil dan dangkal; untuk sudut lancip, busurnya yang besar dan hampir melingkari
seluruh lingkaran.

### Jawaban lengkapnya, kalau diminta

Soal ini hanya menanyakan jari-jarinya. Kalau yang diminta tempat kedudukannya sendiri,
jawabannya:

> Dua busur berjari-jari $8$, masing-masing busur kecil dari lingkaran yang berpusat
> berjarak $4\sqrt3$ dari $AB$ di sisi yang berlawanan dengan busurnya — **tanpa** kedua
> titik ujungnya $A$ dan $B$.

Dua hal yang wajib ikut ditulis:

- **dua busur, bukan satu.** Sudut $\angle APB$ tidak membedakan $P$ di atas atau di
  bawah $AB$;
- **titik $A$ dan $B$ dibuang.** Di sana $\angle APB$ tidak terdefinisi, sebab
  segitiganya merosot menjadi ruas garis.

Membuang titik yang tidak sah adalah salah satu jebakan yang ditulis di halaman jurus
ini, dan ia hampir selalu muncul pada tempat kedudukan berbentuk busur.

### Kalau sudutnya $90^\circ$

Sebagai pemeriksaan atas rumusnya, coba $\angle APB = 90^\circ$:

$$2R = \frac{8}{\sin 90^\circ} = 8 \quad \Longrightarrow \quad R = 4$$

Pusatnya berjarak $\sqrt{16-16} = 0$ dari $AB$ — jadi pusatnya **pada** $AB$, di titik
tengahnya, dan kedua busurnya menyatu menjadi satu lingkaran berdiameter $AB$. Itu persis
teorema Thales ✓

Jadi sudut $90^\circ$ adalah satu-satunya kasus yang tempat kedudukannya berupa lingkaran
utuh, bukan sepasang busur.
