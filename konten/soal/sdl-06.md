---
id: sdl-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [sudut-lingkaran]
bentuk: isian
kesulitan: 3
jawaban: "150"
---

## Soal

Ruas $AB$ adalah diameter lingkaran berpusat $O$. Titik $C$ terletak pada keliling lingkaran di
satu sisi $AB$, dan titik $D$ pada keliling di sisi yang berlawanan.

![Lingkaran berpusat O dengan AB sebagai diameter mendatar, A di kiri dan B di kanan. Titik C di keliling di atas AB dan titik D di keliling di bawah AB. Tali busur AC dan BD digambar, begitu pula jari-jari OC dan OD. Sudut CAB besarnya 25 derajat, sudut DBA besarnya 40 derajat, dan sudut COD ditanyakan](lingkaran-dua-sisi-diameter.svg)

Diketahui $\angle CAB = 25^\circ$ dan $\angle DBA = 40^\circ$.

Tentukan besar $\angle COD$ dalam derajat, yakni sudut yang bukan refleks.

## Petunjuk

- Kedua sudut yang diketahui bertitik sudut di keliling, sedangkan yang ditanyakan bertitik sudut di pusat. Ubah dulu keduanya menjadi besaran yang sejenis.
- Ubah tiap sudut keliling menjadi sudut pusat yang menghadap busur yang sama, lalu perhatikan bahwa ketiga sudut di sepanjang satu sisi diameter berjumlah $180^\circ$.
- $\angle COB = 50^\circ$ dan $\angle AOD = 80^\circ$. Sekarang telusuri dari $C$ ke $D$ lewat sisi yang memuat $B$.

## Pembahasan

**Ubah kedua sudut keliling menjadi sudut pusat.**

Sudut $\angle CAB$ menghadap busur $CB$, dan sudut pusat yang menghadap busur yang sama adalah
$\angle COB$:

$$\angle COB = 2 \times 25^\circ = 50^\circ$$

Sudut $\angle DBA$ menghadap busur $DA$, dan sudut pusat yang menghadapnya adalah $\angle AOD$:

$$\angle AOD = 2 \times 40^\circ = 80^\circ$$

**Telusuri sepanjang garis $AB$.** Karena $A$, $O$, $B$ segaris, sudut-sudut di $O$ pada tiap
sisi diameter berjumlah $180^\circ$.

Di sisi atas hanya ada $C$, dan di sisi bawah hanya ada $D$. Ambil jalur dari sinar $OC$
memutar lewat sinar $OB$ lalu ke sinar $OD$:

$$\angle COD = \angle COB + \angle BOD$$

Sudut $\angle BOD$ belum diketahui, tetapi ia pelurus $\angle AOD$ sebab $A$, $O$, $B$
segaris:

$$\angle BOD = 180^\circ - 80^\circ = 100^\circ$$

**Jumlahkan.**

$$\angle COD = 50^\circ + 100^\circ = \boxed{150^\circ}$$

### Periksa lewat jalur yang berlawanan

Jalur yang lain, dari $OC$ memutar lewat $OA$ ke $OD$:

$$\angle COA + \angle AOD = \left(180^\circ - 50^\circ\right) + 80^\circ = 130^\circ + 80^\circ = 210^\circ$$

Kedua jalur berjumlah $150^\circ + 210^\circ = 360^\circ$ ✓ — satu putaran penuh, seperti
seharusnya. Yang $150^\circ$ adalah sudut biasa, yang $210^\circ$ sudut refleksnya.

Itu sebabnya soal menyebut "yang bukan refleks": tanpa keterangan itu, dua jawaban sama-sama
bisa dipertahankan.

### Mengapa sisi C dan D harus disebut

Andaikan $D$ dipindahkan ke sisi **yang sama** dengan $C$, dengan sudut $\angle DBA$ tetap
$40^\circ$. Maka $\angle AOD = 80^\circ$ diukur pada sisi atas, sehingga $\angle DOB = 100^\circ$
juga di sisi atas, dan

$$\angle COD = \left|100^\circ - 50^\circ\right| = 50^\circ$$

Jawabannya berubah dari $150^\circ$ menjadi $50^\circ$ hanya karena satu titik pindah sisi,
padahal seluruh angka yang diberikan sama persis. Kalimat "di sisi yang berlawanan" pada soal
karena itu bukan hiasan — ia salah satu **data**.

### Kebiasaan yang membuat soal semacam ini pendek

Ubah semua sudut menjadi satu jenis lebih dulu — di sini, semuanya menjadi sudut pusat — baru
kemudian dijumlahkan atau dikurangkan. Mencampur sudut keliling dan sudut pusat dalam satu
persamaan adalah sumber kekeliruan faktor dua yang paling sering, dan faktor dua tidak pernah
terlihat mencurigakan pada hasil akhirnya.
