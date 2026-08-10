---
id: gsg-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [garis-singgung]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Lingkaran dalam segitiga $ABC$ menyinggung sisi $BC$ di $X$, sisi $CA$ di $Y$, dan sisi $AB$
di $Z$.

![Segitiga ABC dengan lingkaran dalam berpusat I, menyinggung sisi BC di X, sisi CA di Y, dan sisi AB di Z. Jari-jari IX digambar putus-putus dan tegak lurus sisi BC](segitiga-lingkaran-dalam.svg)

Diketahui $AB = 13$, $BC = 14$, dan $CA = 15$.

Tentukan panjang $BX$.

## Petunjuk

- Dari tiap titik sudut ada **dua** titik singgung yang terdekat. Apa hubungan antara kedua jarak itu?
- Dua garis singgung dari satu titik luar sama panjang. Namai ketiga pasangan itu $x$, $y$, $z$.
- Tiap sisi segitiga terpecah menjadi dua di antara ketiga peubah itu, jadi kamu punya tiga persamaan dengan tiga peubah.

## Pembahasan

**Beri nama pada ketiga pasangan.** Dari titik $A$ ada dua garis singgung ke lingkaran dalam,
menyentuh di $Y$ dan $Z$. Karena dua garis singgung dari satu titik luar sama panjang,

$$AY = AZ$$

Namai ketiganya:

$$x = AY = AZ, \qquad y = BZ = BX, \qquad z = CX = CY$$

Perhatikan bahwa **enam** panjang tadi hanya menyimpan **tiga** bilangan yang berbeda. Itu
seluruh isi jurus ini pada soal semacam ini.

**Susun ketiga persamaannya.** Tiap sisi terbagi dua oleh titik singgungnya:

$$y + z = BC = 14$$

$$z + x = CA = 15$$

$$x + y = AB = 13$$

**Selesaikan.** Jumlahkan ketiganya:

$$2(x + y + z) = 14 + 15 + 13 = 42 \quad \Longrightarrow \quad x + y + z = 21$$

Angka $21$ itu tidak lain **setengah keliling** segitiganya, $s$. Sekarang tiap peubah keluar
dengan satu pengurangan:

$$y = (x+y+z) - (z+x) = 21 - 15 = 6$$

Karena $BX = y$,

$$BX = \boxed{6}$$

**Lengkapnya:** $x = 21 - 14 = 7$ dan $z = 21 - 13 = 8$.

**Periksa.** $y + z = 6 + 8 = 14$ ✓, $z + x = 8 + 7 = 15$ ✓, $x + y = 7 + 6 = 13$ ✓.

### Bentuk umumnya

Perhatikan pola pengurangannya: tiap peubah adalah $s$ dikurangi sisi **di hadapan** titik
sudutnya.

$$x = s - a, \qquad y = s - b, \qquad z = s - c$$

dengan $a = BC$, $b = CA$, $c = AB$. Di sini $y = s - b = 21 - 15 = 6$ ✓.

Hafalannya mudah tertukar antara "sisi di hadapan" dan "sisi yang menempel", jadi periksa
sekali dengan angka: $BX$ berpasangan dengan $B$, dan sisi di hadapan $B$ adalah $CA = 15$,
memberi $21 - 15 = 6$ ✓. Satu pemeriksaan seperti ini lebih cepat daripada mengingat aturannya.

### Kenapa "dua singgung sama panjang" itu benar

Tarik $IA$, dengan $I$ pusat lingkaran dalam. Segitiga $IYA$ dan $IZA$ dua-duanya siku-siku —
di $Y$ dan $Z$, sebab jari-jari tegak lurus garis singgung di titik singgungnya. Keduanya punya
sisi miring $IA$ yang sama dan sisi siku-siku $IY = IZ = r$. Maka menurut Pythagoras,

$$AY^2 = IA^2 - r^2 = AZ^2$$

sehingga $AY = AZ$.

Perhatikan bahwa langkah pertamanya — **menarik jari-jari ke titik singgung** — adalah gerakan
yang disebut halaman jurus sebagai "hampir selalu sama dan sering dilupakan". Tanpa itu tidak
ada sudut siku-siku, dan tanpa sudut siku-siku tidak ada Pythagoras.

### Apa lagi yang terbuka dari ketiga angka ini

Dengan $x = 7$, $y = 6$, $z = 8$ dan $s = 21$, luas segitiganya lewat Heron adalah

$$L = \sqrt{s \cdot x \cdot y \cdot z} = \sqrt{21 \times 7 \times 6 \times 8} = \sqrt{7056} = 84$$

Perhatikan bentuk Heron di situ: $(s-a)(s-b)(s-c)$ **sama dengan** hasil kali ketiga panjang
singgungnya. Jadi ketiga bilangan yang baru kamu cari itu bukan bilangan sembarangan — mereka
tokoh utama pada rumus luas juga.
