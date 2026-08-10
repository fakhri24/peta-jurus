---
id: kut-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [kuasa-titik, sudut-lingkaran]
bentuk: uraian
kesulitan: 3
---

## Soal

Dua talibusur $AB$ dan $CD$ pada sebuah lingkaran berpotongan di titik $P$ di dalam
lingkaran.

Buktikan bahwa $PA \cdot PB = PC \cdot PD$.

## Petunjuk

- Hasil kali dua panjang sama dengan hasil kali dua panjang lain — bentuk itu adalah perbandingan yang ditulis ulang. Perbandingan biasanya datang dari mana?
- Cari dua segitiga yang sebangun di antara keempat titik itu, dengan $P$ sebagai titik sudut bersama.
- Sudut di $P$ bertolak belakang. Sudut kedua diperoleh dari dua sudut keliling yang menghadap busur yang sama.

## Pembahasan

**Pilih dua segitiganya.** Hubungkan $A$ dengan $C$, dan $D$ dengan $B$. Terbentuk
$\triangle APC$ dan $\triangle DPB$.

**Sudut pertama: bertolak belakang.** Karena $A$, $P$, $B$ segaris dan $C$, $P$, $D$ segaris,

$$\angle APC = \angle DPB$$

**Sudut kedua: sudut keliling pada busur yang sama.** Sudut $\angle CAP$ tak lain
$\angle CAB$, dan sudut $\angle BDP$ tak lain $\angle BDC$. Keduanya sudut keliling yang
menghadap **busur $CB$ yang sama**, sehingga

$$\angle CAP = \angle BDP$$

**Simpulkan kesebangunannya.** Dua pasang sudut yang bersesuaian sama besar, maka

$$\triangle APC \sim \triangle DPB$$

dengan padanan $A \leftrightarrow D$, $P \leftrightarrow P$, $C \leftrightarrow B$.

**Tulis perbandingan sisinya.** Sisi-sisi yang bersesuaian sebanding:

$$\frac{PA}{PD} = \frac{PC}{PB}$$

**Kalikan silang.**

$$PA \cdot PB = PC \cdot PD \qquad \blacksquare$$

### Yang paling mudah salah: urutan padanannya

Kesebangunannya **menyilang**: $A$ berpasangan dengan $D$, dan $C$ dengan $B$ — bukan $A$
dengan $B$ dan $C$ dengan $D$. Padanan yang salah menghasilkan
$\dfrac{PA}{PB} = \dfrac{PC}{PD}$, yang berarti $PA \cdot PD = PB \cdot PC$, sebuah
pernyataan yang umumnya **tidak benar**.

Cara memastikannya: tuliskan kesebangunan dengan huruf berurut, $\triangle APC \sim
\triangle DPB$, lalu baca sisi-sisinya menurut urutan huruf itu. $AP$ berpasangan dengan
$DP$; $PC$ berpasangan dengan $PB$; $AC$ berpasangan dengan $DB$.

### Kenapa dua busur itu benar-benar sama

Langkah yang paling sering dilewati adalah menyebut **busur mana** yang dihadapi. Sudut
$\angle CAB$ berpuncak di $A$ dengan kaki melalui $C$ dan $B$, jadi ia menghadap busur $CB$
yang tidak memuat $A$. Sudut $\angle BDC$ berpuncak di $D$ dengan kaki melalui $B$ dan $C$,
jadi ia menghadap busur $CB$ yang tidak memuat $D$.

Karena $A$ dan $D$ berada pada busur yang sama relatif terhadap talibusur $CB$ — keduanya di
sisi yang sama — kedua sudut itu menghadap busur yang persis sama. Tanpa keterangan itu,
kesamaan sudutnya belum beralasan.

### Bentuk kedua: dari titik luar

Bukti yang sama berlaku hampir kata demi kata ketika $P$ di luar lingkaran, dengan satu
penyesuaian: sudut di $P$ bukan lagi bertolak belakang melainkan **sudut yang sama**, dipakai
bersama oleh kedua segitiga. Sudut keliling yang kedua tetap datang dari busur yang sama.

Jadi teorema talibusur berpotongan dan teorema dua garis potong bukan dua teorema, melainkan
satu teorema dengan dua gambar.

### Kaitannya dengan rumus kuasa

Setelah teorema ini berdiri, terapkan pada talibusur yang **melalui pusat**. Kedua bagiannya
$r - OP$ dan $r + OP$, sehingga untuk sembarang talibusur lewat $P$

$$PA \cdot PB = (r-OP)(r+OP) = r^2 - OP^2$$

Itulah asal rumus kuasa titik. Perhatikan urutan kerjanya: teoremanya dulu, rumusnya
kemudian — bukan sebaliknya.

## Rubrik

- Menarik ruas bantu $AC$ dan $DB$, dan menyebut dua segitiga yang akan dipakai
- Menyatakan $\angle APC = \angle DPB$ dengan alasan bertolak belakang, disertai keterangan
  bahwa $A$, $P$, $B$ segaris dan $C$, $P$, $D$ segaris
- Menyatakan $\angle CAP = \angle BDP$ dengan alasan sudut keliling yang menghadap busur
  yang sama, **dan menyebut busur mana**
- Menyimpulkan $\triangle APC \sim \triangle DPB$ dengan padanan huruf yang benar
- Menuliskan perbandingan sisi yang bersesuaian sesuai padanan itu
- Mengalikan silang dan menuliskan kesimpulannya

Bukti yang memakai padanan huruf terbalik dinilai tidak lengkap meski hasil akhirnya
kebetulan tertulis benar, karena perbandingan sisi yang ditulisnya tidak mengikuti
kesebangunan yang dinyatakan.
