---
id: tfm-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [transformasi]
bentuk: isian
kesulitan: 3
jawaban: "10"
---

## Soal

Titik $A$ dan $B$ terletak pada sisi yang sama dari sebuah garis $\ell$. Jarak $A$ ke $\ell$
adalah $2$, jarak $B$ ke $\ell$ adalah $4$, dan kedua kaki tegak lurusnya pada $\ell$
berjarak $8$ satu sama lain.

![Sebuah garis lurus mendatar bernama l. Di atasnya ada titik A di kiri, berjarak 2 dari garis itu, dan titik B di kanan, berjarak 4 dari garis itu. Kedua kaki tegak lurusnya pada garis l berjarak 8 satu sama lain. Sebuah titik P berada pada garis l di antara kedua kaki itu, dan lintasan patah dari A ke P lalu ke B digambar putus-putus](cermin-lintasan-terpendek.svg)

Titik $P$ bergerak sepanjang $\ell$. Tentukan nilai terkecil dari $AP + PB$.

## Petunjuk

- Lintasan $A \to P \to B$ patah karena $P$ harus menyentuh $\ell$. Kalau kedua titik berada di sisi yang **berlawanan**, lintasan terpendeknya jelas — garis lurus.
- Cerminkan salah satu titik terhadap $\ell$. Panjang lintasan tidak berubah, tetapi bentuknya berubah.
- Kalau $A'$ cerminan $A$, maka $AP = A'P$ untuk setiap $P$ pada $\ell$, sehingga $AP + PB = A'P + PB$.

## Pembahasan

**Kenali pemicunya.** Yang diminta jumlah dua panjang yang tersebar, dengan satu titik bebas
di garis. Itu pemicu baku pencerminan.

**Cerminkan $A$ terhadap $\ell$.** Sebut hasilnya $A'$. Karena $\ell$ sumbu cerminnya, setiap
titik $P$ pada $\ell$ berjarak sama ke $A$ dan ke $A'$:

$$AP = A'P \quad \text{untuk setiap } P \text{ pada } \ell$$

Maka

$$AP + PB = A'P + PB$$

**Sekarang soalnya jadi soal garis lurus.** Titik $A'$ dan $B$ berada di sisi yang
**berlawanan** dari $\ell$, jadi ruas $A'B$ pasti memotong $\ell$. Untuk sembarang $P$ pada
$\ell$ berlaku ketaksamaan segitiga:

$$A'P + PB \ \ge\ A'B$$

dengan kesamaan tepat ketika $P$ berada pada ruas $A'B$ — yaitu ketika $P$ titik potong $A'B$
dengan $\ell$.

**Hitung $A'B$.** Ambil sumbu dengan $\ell$ sebagai sumbu $x$ dan kaki $A$ sebagai titik asal:

$$A(0, 2), \qquad B(8, 4), \qquad A'(0, -2)$$

$$A'B = \sqrt{(8-0)^2 + \left(4-(-2)\right)^2} = \sqrt{64 + 36} = \sqrt{100} = \boxed{10}$$

### Di mana letak $P$ yang terbaik

Garis $A'B$ memotong sumbu $x$ ketika ordinatnya nol. Dari $A'(0,-2)$ ke $B(8,4)$, ordinatnya
naik $6$ sepanjang absis $8$, jadi ia mencapai nol setelah naik $2$, yaitu setelah menempuh
$\tfrac{2}{6}$ bagian:

$$P = \left(\tfrac{8}{3},\ 0\right) \approx (2{,}67,\ 0)$$

Periksa: $AP = \sqrt{\left(\tfrac83\right)^2 + 4} = \sqrt{\tfrac{64}{9} + \tfrac{36}{9}}
= \tfrac{10}{3}$, dan $PB = \sqrt{\left(\tfrac{16}{3}\right)^2 + 16}
= \sqrt{\tfrac{256}{9} + \tfrac{144}{9}} = \tfrac{20}{3}$. Jumlahnya
$\tfrac{10}{3} + \tfrac{20}{3} = 10$ ✓

Bandingkan dengan pilihan lain: $P = (2,0)$ memberi $\approx 10{,}04$; $P = (3,0)$ memberi
$\approx 10{,}01$; $P = (4,0)$ memberi $\approx 10{,}13$. Semuanya lebih besar ✓

### Sudut datang sama dengan sudut pantul

Perhatikan bahwa $A$, $P$, dan $B$ pada penyelesaian terbaik membentuk lintasan yang mematuhi
hukum pemantulan: sudut antara $AP$ dan $\ell$ sama dengan sudut antara $PB$ dan $\ell$.
Alasannya langsung dari gambarnya — $A'$, $P$, $B$ segaris, dan sudut $A'P$ terhadap $\ell$
adalah cerminan sudut $AP$ terhadap $\ell$.

Jadi soal "lintasan terpendek yang menyentuh garis" dan soal "lintasan sinar yang memantul"
adalah soal yang sama. Kalau nanti bertemu soal bola biliar memantul di sisi meja,
pencerminan tetap alatnya.

### Jebakan: mencerminkan pada saat yang salah

Kalau $A$ dan $B$ berada di sisi yang **berlawanan** dari $\ell$, tidak ada yang perlu
dicerminkan: ruas $AB$ sendiri sudah memotong $\ell$, dan lintasan terpendeknya $AB$ langsung.
Mencerminkan di situ justru memanjangkan hasilnya.

Aturannya: **cerminkan supaya kedua titik berakhir di sisi yang berlawanan.** Kalau sudah
berlawanan sejak awal, pencerminan tidak diperlukan.

### Bentuk sebaliknya: selisih terbesar

Soal kembarannya menanyakan nilai **terbesar** dari $\left|AP - PB\right|$. Di situ yang
dicerminkan tetap satu titik, tetapi tujuannya berbalik: kita ingin ketiganya segaris dengan
$P$ di **luar** ruasnya, sehingga

$$\left|AP - PB\right| \le AB$$

dan kesamaannya tercapai saat $P$ titik potong perpanjangan $AB$ dengan $\ell$. Perhatikan
bahwa di sini yang dipakai $AB$, bukan $A'B$ — untuk selisih, justru **tidak** perlu
mencerminkan. Membedakan keduanya jauh lebih penting daripada menghafal salah satunya.
