---
id: tfm-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [transformasi]
bentuk: isian
kesulitan: 3
jawaban: "6"
---

## Soal

Titik $P$ terletak di dalam sudut $XOY$ yang besarnya $30^\circ$, dengan $OP = 6$. Titik
$P_1$ adalah cerminan $P$ terhadap garis $OX$, dan $P_2$ adalah cerminan $P$ terhadap garis
$OY$.

Tentukan panjang $P_1P_2$.

## Petunjuk

- Pencerminan menjaga jarak ke setiap titik pada sumbu cerminnya. Berapa $OP_1$ dan $OP_2$?
- Soal tidak memberitahu di mana persisnya $P$ di dalam sudut itu. Kalau soalnya punya jawaban tunggal, jawabannya tidak boleh bergantung pada letak itu.
- Hitung $\angle P_1OP_2$ dengan menjumlahkan sudut-sudut kecil di sekitar $O$.

## Pembahasan

**Panjang dari $O$ tidak berubah.** Titik $O$ terletak pada kedua sumbu cermin, jadi jaraknya
ke $P$ dijaga oleh kedua pencerminan:

$$OP_1 = OP = 6, \qquad OP_2 = OP = 6$$

**Hitung sudut $\angle P_1OP_2$.** Misalkan $\angle POX = \alpha$, sehingga
$\angle POY = 30^\circ - \alpha$.

Pencerminan terhadap $OX$ memindahkan $P$ ke seberang $OX$ dengan sudut yang sama, jadi
$\angle P_1OX = \alpha$. Dengan cara yang sama $\angle P_2OY = 30^\circ - \alpha$.

Susun keempat sudut itu berurutan dari $OP_1$ sampai $OP_2$:

$$\angle P_1OP_2 = \underbrace{\alpha}_{P_1 \to OX} + \underbrace{\alpha}_{OX \to P}
+ \underbrace{(30^\circ - \alpha)}_{P \to OY} + \underbrace{(30^\circ - \alpha)}_{OY \to P_2}
= 60^\circ$$

Suku $\alpha$ lenyap seluruhnya — **jawabannya tidak bergantung pada letak $P$ di dalam
sudut itu**, hanya pada $OP$ dan besar sudutnya. Itu yang membuat soalnya punya jawaban
meski letak $P$ tidak disebutkan.

**Selesaikan.** Segitiga $OP_1P_2$ punya $OP_1 = OP_2 = 6$ dan sudut apit $60^\circ$ — segitiga
sama kaki dengan sudut puncak $60^\circ$ adalah **sama sisi**:

$$P_1P_2 = \boxed{6}$$

### Periksa dengan aturan kosinus

$$P_1P_2^2 = 6^2 + 6^2 - 2 \cdot 6 \cdot 6 \cos 60^\circ = 72 - 36 = 36 \quad \Longrightarrow \quad
P_1P_2 = 6 \quad ✓$$

Periksa juga dengan letak $P$ yang dipilih sembarang, misalnya $\alpha = 12^\circ$:
$P_1$ berada pada sudut $-12^\circ$ dan $P_2$ pada sudut $48^\circ$, keduanya berjarak $6$
dari $O$. Selisih sudutnya $60^\circ$ ✓, dan panjangnya $6$. Coba $\alpha = 5^\circ$ atau
$\alpha = 22^\circ$ — hasilnya tetap $6$.

### Aturan umum dua pencerminan berturut-turut

Yang baru saja terjadi kasus khusus dari satu kenyataan penting:

> **Dua pencerminan terhadap dua garis yang berpotongan dengan sudut $\theta$ setara dengan
> satu putaran sebesar $2\theta$ terhadap titik potongnya.**

Di sini $\theta = 30^\circ$, jadi memetakan $P_1$ ke $P_2$ sama saja dengan memutar
$60^\circ$ terhadap $O$ — dan itu langsung memberi $\angle P_1OP_2 = 60^\circ$ tanpa
menjumlahkan empat sudut satu per satu.

Aturan ini juga menjelaskan mengapa $\alpha$ lenyap: putaran tidak peduli titik mana yang
diputar.

### Kegunaannya: keliling segitiga terkecil

Konfigurasi ini muncul pada soal klasik: **cari segitiga berkeliling terkecil yang satu titik
sudutnya $P$ dan dua lainnya pada kedua kaki sudut.**

Untuk sembarang $Q$ pada $OX$ dan $R$ pada $OY$,

$$PQ + QR + RP = P_1Q + QR + RP_2 \ \ge\ P_1P_2$$

karena pencerminan menjaga panjangnya, dan lintasan patah tidak pernah lebih pendek daripada
ruas lurus. Kesamaannya tercapai ketika $Q$ dan $R$ berada pada ruas $P_1P_2$.

Jadi keliling terkecilnya tepat $P_1P_2 = 6$ — dan itulah alasan sesungguhnya soal ini
menanyakan panjang $P_1P_2$.

### Kalau sudutnya tidak lancip

Rumus $\angle P_1OP_2 = 2\theta$ berlaku selama $2\theta \le 180^\circ$. Untuk
$\theta > 90^\circ$, sudut antara $OP_1$ dan $OP_2$ yang terukur adalah $360^\circ - 2\theta$,
dan bangun keliling terkecilnya tidak lagi terbentuk seperti di atas.

Periksa syarat itu sebelum memakai hasilnya: di sini $\theta = 30^\circ$, jadi
$2\theta = 60^\circ \le 180^\circ$ ✓.
