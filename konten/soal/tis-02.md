---
id: tis-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [titik-istimewa]
bentuk: isian
kesulitan: 2
jawaban: "70"
---

## Soal

Pada segitiga $ABC$, titik $I$ adalah pusat lingkaran dalamnya. Diketahui
$\angle BIC = 125^\circ$.

Tentukan besar $\angle BAC$ dalam derajat.

## Petunjuk

- Titik $I$ adalah perpotongan ketiga garis bagi, jadi $\angle IBC = \tfrac12\angle B$ dan $\angle ICB = \tfrac12\angle C$.
- Pada $\triangle IBC$, ketiga sudutnya berjumlah $180^\circ$. Tulis itu, lalu ganti $\tfrac12(B+C)$ dengan sesuatu yang memuat $A$.
- $\angle BIC = 90^\circ + \tfrac12 \angle A$.

## Pembahasan

**Turunkan hubungannya, jangan cuma memakainya.** Karena $BI$ garis bagi sudut $B$ dan $CI$
garis bagi sudut $C$:

$$\angle IBC = \tfrac12 B, \qquad \angle ICB = \tfrac12 C$$

Jumlah sudut $\triangle IBC$:

$$\angle BIC = 180^\circ - \tfrac12 B - \tfrac12 C = 180^\circ - \tfrac12 (B + C)$$

Karena $A + B + C = 180^\circ$, berlaku $B + C = 180^\circ - A$, sehingga

$$\angle BIC = 180^\circ - \tfrac12\left(180^\circ - A\right) = 90^\circ + \tfrac12 A$$

**Selesaikan.**

$$125^\circ = 90^\circ + \tfrac12 A \quad \Longrightarrow \quad \tfrac12 A = 35^\circ
\quad \Longrightarrow \quad A = \boxed{70^\circ}$$

### Periksa

Dengan $A = 70^\circ$, berlaku $B + C = 110^\circ$, sehingga
$\tfrac12 B + \tfrac12 C = 55^\circ$ dan

$$\angle BIC = 180^\circ - 55^\circ = 125^\circ \quad ✓$$

Perhatikan bahwa $B$ dan $C$ masing-masing tidak tertentu — hanya jumlahnya yang terkunci.
Jadi soal ini punya jawaban tunggal meski segitiganya tidak tunggal, dan itu memang ciri
hubungan $\angle BIC = 90^\circ + \tfrac12 A$: ia cuma bergantung pada $A$.

### Batas nilainya

Karena $0^\circ < A < 180^\circ$, berlaku

$$90^\circ < \angle BIC < 180^\circ$$

Jadi $\angle BIC$ **selalu tumpul**, berapa pun bentuk segitiganya. Kalau perhitunganmu
memberi $\angle BIC$ lancip, ada yang salah sebelum langkah terakhir.

Nilai $125^\circ$ di soal memenuhi batas itu ✓.

### Tiga hubungan bersaudara yang sering tertukar

Untuk ketiga titik istimewa, sudut yang dilihat dari sisi $BC$:

| Titik | Sudut $\angle B\cdot C$ | Untuk $A = 70^\circ$ |
|---|---|---|
| Pusat dalam $I$ | $90^\circ + \tfrac12 A$ | $125^\circ$ |
| Pusat luar $O$ | $2A$ | $140^\circ$ |
| Titik tinggi $H$ | $180^\circ - A$ | $110^\circ$ |

Ketiganya berbeda, dan ketiganya sering muncul di soal yang bunyinya nyaris sama. Yang
membedakan cuma titik mana yang disebut — jadi bacalah namanya, bukan gambarnya.

Catatan untuk $O$: rumus $\angle BOC = 2A$ berlaku saat $\angle A$ lancip. Kalau $\angle A$
tumpul, $O$ berada di seberang $BC$ dan sudut yang terukur $360^\circ - 2A$.

### Sifat lain yang sering menyusul

Titik $I$ juga punya sifat yang tidak terlihat dari rumus di atas: kalau garis $AI$
diperpanjang sampai memotong lingkaran luar di $M$, maka

$$MB = MC = MI$$

Titik $M$ karena itu disebut **titik tengah busur** $BC$, dan sifat "$M$ pusat lingkaran yang
melalui $B$, $I$, $C$" sering jadi kunci soal OSN. Buktinya memakai sudut keliling, dan bahan
pertamanya justru $\angle BIC = 90^\circ + \tfrac12 A$ yang baru saja diturunkan.
