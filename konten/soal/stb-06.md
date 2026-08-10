---
id: stb-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [segiempat-talibusur]
bentuk: uraian
kesulitan: 3
---

## Soal

Segiempat $ABCD$ mempunyai keempat titik sudut pada satu lingkaran berpusat $O$.

Buktikan bahwa

$$\angle DAB + \angle BCD = 180^\circ$$

## Petunjuk

- Kedua sudut itu bertitik sudut di keliling. Untuk tiap sudut, tentukan busur mana yang dihadapinya.
- Sudut $\angle DAB$ menghadap busur $BCD$, dan $\angle BCD$ menghadap busur $DAB$. Kedua busur itu bersama-sama menutupi apa?
- Pakai hubungan sudut keliling dengan sudut pusat, lalu jumlahkan kedua persamaannya.

## Pembahasan

**Tentukan busur yang dihadapi masing-masing.**

Sudut $\angle DAB$ bertitik sudut di $A$, dengan kaki menuju $D$ dan $B$. Busur yang
dihadapinya adalah busur $BD$ yang **tidak memuat $A$** — yaitu busur yang melewati $C$. Sebut
besar sudut pusatnya $\theta_1 = \angle BOD$ yang diukur pada sisi $C$.

Sudut $\angle BCD$ bertitik sudut di $C$, dengan kaki menuju $B$ dan $D$. Busur yang
dihadapinya adalah busur $BD$ yang **tidak memuat $C$** — yaitu yang melewati $A$. Sebut sudut
pusatnya $\theta_2$.

**Kedua busur itu menutupi seluruh lingkaran.** Busur $BD$ lewat $C$ dan busur $BD$ lewat $A$
bersama-sama membentuk lingkaran penuh tanpa bertindihan, sehingga

$$\theta_1 + \theta_2 = 360^\circ$$

**Pakai hubungan pusat–keliling.** Sudut keliling setengah sudut pusat yang menghadap busur
yang sama:

$$\angle DAB = \tfrac{1}{2}\theta_1, \qquad \angle BCD = \tfrac{1}{2}\theta_2$$

**Jumlahkan.**

$$\angle DAB + \angle BCD = \tfrac{1}{2}\theta_1 + \tfrac{1}{2}\theta_2
= \tfrac{1}{2}\left(\theta_1 + \theta_2\right) = \tfrac{1}{2} \times 360^\circ = 180^\circ$$

Jadi $\angle DAB + \angle BCD = 180^\circ$. $\blacksquare$

### Sudut pusat refleks harus ikut dihitung

Satu titik yang sering dilewati: salah satu dari $\theta_1$ dan $\theta_2$ pasti **lebih besar
daripada $180^\circ$** — sudut refleks — kecuali kalau keduanya tepat $180^\circ$.

Hubungan "sudut keliling setengah sudut pusat" tetap berlaku untuk sudut refleks, asalkan yang
dipakai memang sudut pusat yang menghadap busur yang benar. Kalau yang dipakai selalu sudut
pusat yang bukan refleks, jumlahnya tidak akan pernah $360^\circ$, dan buktinya gagal tanpa
sebab yang terlihat.

Karena itu langkah "tentukan busur yang dihadapi" tidak boleh dipersingkat menjadi "tentukan
sudut pusatnya".

### Pasangan yang lain, tanpa pekerjaan tambahan

Karena keempat sudut segiempat mana pun berjumlah $360^\circ$,

$$\angle ABC + \angle CDA = 360^\circ - 180^\circ = 180^\circ$$

Jadi begitu satu pasangan terbukti, pasangan yang lain ikut secara gratis. Menuliskannya
sebagai akibat lebih baik daripada mengulang seluruh bukti untuk pasangan kedua.

### Kebalikannya, dan mengapa ia perlu bukti sendiri

Kebalikannya juga benar: kalau pada segiempat $ABCD$ berlaku $\angle DAB + \angle BCD =
180^\circ$, maka keempat titiknya terletak pada satu lingkaran. Justru arah inilah yang paling
banyak dipakai di soal olimpiade.

Tetapi ia **tidak otomatis** ikut dari bukti di atas — bukti tadi berangkat dari lingkaran yang
sudah ada. Arah sebaliknya dibuktikan tersendiri, biasanya dengan menggambar lingkaran lewat
tiga titik, lalu menunjukkan titik keempat tidak mungkin berada di luar maupun di dalamnya.

Membedakan pernyataan dari kebalikannya adalah kebiasaan yang menyelamatkan banyak bukti dari
berputar.

## Rubrik

- Menyebut busur yang dihadapi $\angle DAB$ dan busur yang dihadapi $\angle BCD$, masing-masing dengan jelas titik mana yang dilewatinya
- Menyatakan kedua busur itu bersama-sama menutupi lingkaran penuh, sehingga kedua sudut pusatnya berjumlah $360^\circ$
- Menerapkan hubungan sudut keliling setengah sudut pusat pada kedua sudut
- Menjumlahkan kedua persamaan dan menyimpulkan $180^\circ$
- Menangani sudut pusat refleks dengan benar, atau menyebut secara eksplisit bahwa salah satunya refleks
