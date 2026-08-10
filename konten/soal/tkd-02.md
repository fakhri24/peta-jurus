---
id: tkd-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [tempat-kedudukan, kuasa-titik]
bentuk: isian
kesulitan: 4
jawaban: "9"
---

## Soal

Lingkaran $\omega_1$ berpusat $O_1$ dengan jari-jari $12$, dan lingkaran $\omega_2$
berpusat $O_2$ dengan jari-jari $8$. Jarak $O_1O_2 = 10$.

Tempat kedudukan titik yang kuasanya terhadap $\omega_1$ sama dengan kuasanya terhadap
$\omega_2$ adalah sebuah garis. Tentukan jarak garis itu dari $O_1$.

## Petunjuk

- Kuasa titik $P$ terhadap lingkaran berpusat $O$ berjari-jari $R$ adalah $PO^2 - R^2$. Tuliskan syaratnya sebagai persamaan.
- Beri koordinat: $O_1 = (0,0)$ dan $O_2 = (10, 0)$. Suku $x^2$ dan $y^2$ akan saling menghapus — itu sebabnya jawabannya garis, bukan lingkaran.
- Setelah $x$ ketemu, ingat bahwa garisnya tegak lurus $O_1O_2$, sehingga jarak yang ditanya adalah $|x|$ itu sendiri.

## Pembahasan

**Tulis syaratnya.** Kuasa titik $P$ terhadap lingkaran berpusat $O$ berjari-jari $R$
adalah

$$\text{kuasa}(P) = PO^2 - R^2$$

Taruh $O_1 = (0,0)$ dan $O_2 = (10, 0)$. Untuk $P = (x,y)$, syarat soalnya berbunyi

$$x^2 + y^2 - 12^2 \;=\; (x-10)^2 + y^2 - 8^2$$

**Sederhanakan.** Suku $x^2$ dan $y^2$ muncul di kedua ruas dan saling menghapus:

$$-144 = -20x + 100 - 64$$

$$-144 = -20x + 36$$

$$20x = 180 \quad \Longrightarrow \quad x = 9$$

Jadi tempat kedudukannya adalah garis $x = 9$ — tegak lurus $O_1O_2$, dan jaraknya dari
$O_1$ adalah

$$\boxed{9}$$

### Kenapa jawabannya pasti garis

Yang menentukan bukan angka-angkanya, melainkan bentuk persamaannya. Kedua sisi memuat
$x^2 + y^2$ dengan koefisien $1$ yang sama, sehingga keduanya lenyap saat dikurangkan.
Yang tersisa persamaan derajat satu — dan itu selalu garis.

Bandingkan dengan soal lingkaran Apollonius, yang syaratnya $PA = 2\,PB$: di sana
pengkuadratannya memberi koefisien $1$ dan $4$ untuk $x^2+y^2$, jadi sukunya **tidak**
saling menghapus dan hasilnya lingkaran. Perbedaan satu koefisien itu yang memisahkan
kedua jawaban.

Garis ini disebut **garis kuasa** kedua lingkaran.

### Kedua lingkaran ini berpotongan

Periksa: $|12 - 8| = 4 < 10 < 20 = 12 + 8$, jadi $\omega_1$ dan $\omega_2$ berpotongan
di dua titik. Titik potongnya ada pada $x = 9$, dengan

$$y^2 = 144 - 81 = 63 \quad \Longrightarrow \quad y = \pm\sqrt{63}$$

Periksa pada $\omega_2$: $(9-10)^2 + 63 = 1 + 63 = 64 = 8^2$ ✓

Jadi untuk dua lingkaran yang berpotongan, garis kuasanya adalah **garis yang memuat
tali busur persekutuannya**. Itu masuk akal: di titik potongnya, kuasa terhadap kedua
lingkaran sama-sama nol.

Kalau kedua lingkaran tidak berpotongan, garis kuasanya tetap ada dan tetap tegak lurus
$O_1O_2$ — hanya saja ia tidak lagi menyentuh lingkaran mana pun.

### Rumus umumnya

Dengan $d = O_1O_2$, jarak garis kuasa dari $O_1$ adalah

$$x = \frac{d^2 + R_1^2 - R_2^2}{2d}$$

Di sini $\dfrac{100 + 144 - 64}{20} = \dfrac{180}{20} = 9$ ✓

Rumus itu tidak perlu dihafal — menurunkannya ulang butuh tiga baris, seperti di atas.
Yang perlu diingat cuma **bentuk jawabannya**: selalu garis, dan selalu tegak lurus garis
pusat.

### Ke arah mana garisnya bergeser

Perhatikan bahwa $9 < 10$, jadi garisnya berada di antara kedua pusat, tetapi lebih dekat
ke $O_2$ — lingkaran yang **lebih kecil**. Itu berlaku umum: garis kuasa selalu condong
ke lingkaran yang lebih kecil, sebab kuasa tumbuh lebih cepat di sekitar lingkaran kecil.

Kalau $R_1 = R_2$, rumusnya memberi $x = \tfrac{d}{2}$ — sumbu ruas $O_1O_2$, tepat di
tengah, seperti seharusnya.

Pemeriksaan arah itu murah dan sering menangkap salah tanda.
