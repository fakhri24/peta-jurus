---
id: ketaksamaan-geometri
nama: Ketaksamaan Geometri
pilar: geometri
tahap: osn
prasyarat: [trigonometri-segitiga, am-gm]
contoh: [ktg-contoh-1]
latihan: [ktg-01, ktg-02, ktg-03, ktg-04, ktg-05, ktg-06]
---

## Kapan dipakai

Soal meminta membuktikan sebuah **ketaksamaan** yang peubahnya panjang sisi, sudut, luas,
atau jari-jari — bukan bilangan bebas. Bedanya dengan ketaksamaan aljabar terletak pada
satu hal: peubahnya **tidak bebas**, karena ketiga sisi harus membentuk segitiga.

Pemicu kedua: soal meminta nilai **maksimum atau minimum** suatu besaran geometri, dan
tidak ada turunan yang wajar dipakai. Ketaksamaan baku beserta syarat kesamaannya menjawab
sekaligus nilainya dan kapan tercapai.

Pemicu ketiga: soal mencari **lintasan terpendek** atau jumlah jarak terkecil. Di situ
yang bekerja ketaksamaan segitiga, biasanya bersama pencerminan.

## Intinya

**Ketaksamaan segitiga.** Untuk ketiga sisi segitiga,

$$|b - c| < a < b + c$$

Bentuk sebagai jarak, yang lebih sering berguna: $AB + BC \ge AC$, dengan kesamaan tepat
ketika $B$ terletak pada ruas $AC$.

**Substitusi Ravi.** Ini teknik terpenting di jurus ini. Setiap segitiga bersisi $a,b,c$
bisa ditulis

$$a = y+z, \qquad b = z+x, \qquad c = x+y$$

dengan $x,y,z > 0$. Substitusi itu **menghapus** kendala ketaksamaan segitiga: setelah
diganti, $x,y,z$ menjadi peubah positif yang bebas, dan seluruh senjata ketaksamaan
aljabar — AM-GM, Cauchy-Schwarz — bisa dipakai apa adanya.

**Ketaksamaan baku yang layak dikenali:**

$$R \ge 2r \quad \text{(Euler)}, \qquad L \le \frac{\sqrt{3}}{4}\left(\frac{a+b+c}{3}\right)^2 \cdot 3$$

Kesamaan pada keduanya tercapai tepat ketika segitiganya **sama sisi** — dan itu pola
umumnya: di antara semua segitiga dengan keliling tetap, yang sama sisi punya luas
terbesar.

**Ketaksamaan Erdős–Mordell.** Untuk titik $P$ di dalam segitiga, jumlah jarak ke ketiga
titik sudut paling sedikit dua kali jumlah jarak ke ketiga sisinya.

**Titik Fermat.** Titik yang meminimumkan $PA + PB + PC$ melihat ketiga sisi dengan sudut
$120^\circ$ — asalkan semua sudut segitiganya kurang dari $120^\circ$.

## Jebakan umum

- **Memperlakukan $a, b, c$ sebagai peubah bebas.** Tanpa Ravi, ketaksamaan aljabar yang
  dipakai bisa memberi hasil yang benar untuk bilangan positif sembarang tetapi tidak
  memakai syarat segitiganya — dan soal biasanya justru bergantung pada syarat itu.
- **Lupa memeriksa syarat kesamaan.** Soal maksimum-minimum belum selesai sebelum
  ditunjukkan nilainya **tercapai**; ketaksamaan saja hanya memberi batas.
- **Membalik arah saat mengalikan dengan besaran negatif**, atau saat mengambil
  kebalikannya. Pada besaran geometri semuanya positif, jadi kekeliruan ini biasanya masuk
  lewat langkah aljabar di tengah.
- **Memakai titik Fermat pada segitiga bersudut $\ge 120^\circ$.** Di situ titik
  minimumnya justru titik sudut yang tumpul itu sendiri.
