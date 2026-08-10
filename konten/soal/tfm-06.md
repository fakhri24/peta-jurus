---
id: tfm-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [transformasi, kekongruenan]
bentuk: uraian
kesulitan: 4
---

## Soal

Di luar segitiga $ABC$ dibuat segitiga sama sisi $ABD$ pada sisi $AB$, dan segitiga sama sisi
$ACE$ pada sisi $AC$.

Buktikan bahwa $CD = BE$.

## Petunjuk

- Kedua ruas yang dibandingkan, $CD$ dan $BE$, punya satu titik yang sama-sama dekat: $A$. Apa yang menghubungkan $D$ dengan $B$, dan $C$ dengan $E$, lewat $A$?
- Kedua segitiga sama sisi berbagi titik sudut $A$, jadi memutar $60^\circ$ terhadap $A$ memetakan $D$ ke $B$ dan $C$ ke $E$ — kalau arahnya benar.
- Putaran memetakan ruas ke ruas dengan panjang yang sama. Kalau $D \mapsto B$ dan $C \mapsto E$, maka ruas $DC$ dipetakan ke ruas $BE$.

## Pembahasan

**Pilih putarannya.** Perhatikan putaran $\rho$ terhadap titik $A$ sebesar $60^\circ$, dengan
arah yang memetakan $D$ ke $B$.

**Periksa bahwa putaran itu memetakan $D$ ke $B$.** Segitiga $ABD$ sama sisi, sehingga
$AD = AB$ dan $\angle DAB = 60^\circ$. Jadi $B$ memang diperoleh dari $D$ dengan memutar
$60^\circ$ terhadap $A$:

$$\rho(D) = B$$

**Periksa bahwa putaran yang sama memetakan $C$ ke $E$.** Segitiga $ACE$ juga sama sisi,
sehingga $AC = AE$ dan $\angle CAE = 60^\circ$. Yang perlu diperiksa hanya **arahnya**.

Karena kedua segitiga sama sisi dibuat di **luar** segitiga $ABC$, keduanya berada di sisi
yang berlawanan terhadap $ABC$ — dan akibatnya putaran $D \to B$ dan putaran $C \to E$ punya
arah yang sama. Maka

$$\rho(C) = E$$

**Simpulkan.** Putaran memetakan ruas ke ruas: karena $\rho(D) = B$ dan $\rho(C) = E$,

$$\rho(\text{ruas } DC) = \text{ruas } BE$$

Putaran adalah isometri — ia menjaga panjang. Maka

$$CD = BE \qquad \blacksquare$$

### Yang wajib disebut di lembar jawaban

Bukti dengan transformasi hanya sah kalau **peta tiap titik disebut jelas**. Menulis "putar
$60^\circ$, selesai" tidak cukup; yang harus muncul:

1. pusat putarannya ($A$) dan besarnya ($60^\circ$);
2. alasan $\rho(D) = B$ — yaitu $AD = AB$ **dan** $\angle DAB = 60^\circ$;
3. alasan $\rho(C) = E$ dengan putaran yang **sama**, termasuk arahnya;
4. pernyataan bahwa putaran menjaga panjang.

Butir 3 yang paling sering hilang, dan justru di situlah keterangan "di luar segitiga"
dipakai. Tanpa keterangan itu, satu segitiga sama sisi bisa dibuat ke dalam, arah putarannya
berbeda, dan kesimpulannya gagal.

### Bukti kedua: kekongruenan sisi–sudut–sisi

Tanpa transformasi sama sekali. Bandingkan $\triangle DAC$ dengan $\triangle BAE$:

- $AD = AB$ karena $\triangle ABD$ sama sisi;
- $AC = AE$ karena $\triangle ACE$ sama sisi;
- sudut apitnya:
  $$\angle DAC = \angle DAB + \angle BAC = 60^\circ + \angle BAC$$
  $$\angle BAE = \angle BAC + \angle CAE = \angle BAC + 60^\circ$$
  jadi $\angle DAC = \angle BAE$.

Menurut sisi–sudut–sisi, $\triangle DAC \cong \triangle BAE$, sehingga $DC = BE$ ✓

Kedua bukti mengatakan hal yang sama: putaran $60^\circ$ terhadap $A$ **adalah** kekongruenan
itu, ditulis dengan bahasa yang berbeda. Yang membuat bahasa transformasi berharga adalah
apa yang ikut terbawa cuma-cuma — lihat bagian berikutnya.

### Yang ikut terbawa cuma-cuma

Karena $CD$ diperoleh dari $BE$ lewat putaran $60^\circ$, kedua ruas itu **membentuk sudut
$60^\circ$** satu sama lain. Bukti kekongruenan di atas memberi panjangnya saja; putaran
memberi sudutnya sekaligus, tanpa pekerjaan tambahan.

Kalau ditambahkan segitiga sama sisi ketiga pada sisi $BC$, ketiga ruas semacam ini
berpotongan di satu titik — yaitu **titik Fermat** segitiga $ABC$, titik yang meminimumkan
$PA + PB + PC$. Soal ini langkah pertama menuju ke sana.

### Kalau segitiganya dibuat ke dalam

Pernyataannya tetap benar asalkan **kedua** segitiga sama sisi dibuat ke arah yang sama —
dua-duanya keluar, atau dua-duanya ke dalam. Yang gagal adalah campuran: satu ke luar, satu
ke dalam. Di situ sudut apitnya menjadi $60^\circ + \angle BAC$ lawan
$\angle BAC - 60^\circ$, yang umumnya tidak sama.

Memeriksa hal semacam ini murah dan patut jadi kebiasaan: **ganti satu keterangan soal, lalu
periksa di langkah mana buktinya patah.** Kalau tidak ada langkah yang patah, kemungkinan
besar ada keterangan yang belum kamu pakai.

## Rubrik

- Menyebut putaran terhadap $A$ sebesar $60^\circ$, beserta arahnya
- Menyatakan $\rho(D) = B$ dengan alasan $AD = AB$ dan $\angle DAB = 60^\circ$
- Menyatakan $\rho(C) = E$ dengan putaran yang sama, dan memakai keterangan "di luar
  segitiga" sebagai alasan arahnya cocok
- Menyimpulkan ruas $DC$ terpetakan ke ruas $BE$
- Menyebut bahwa putaran menjaga panjang, lalu menuliskan kesimpulannya

Bukti dengan kekongruenan $\triangle DAC \cong \triangle BAE$ dinilai penuh, asalkan kedua
pasangan sisi disebut beserta alasannya dan kesamaan sudut apitnya diturunkan lewat
$\angle DAB = \angle CAE = 60^\circ$, bukan sekadar dinyatakan.
