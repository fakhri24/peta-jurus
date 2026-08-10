---
id: homoteti
nama: Homoteti
pilar: geometri
tahap: osn
prasyarat: [kesebangunan, transformasi]
contoh: [hmt-contoh-1]
latihan: [hmt-01, hmt-02, hmt-03, hmt-04, hmt-05, hmt-06]
---

## Kapan dipakai

Gambar memuat dua bangun **sebangun dan sejajar** — sisi-sisi bersesuaiannya sejajar, bukan
sekadar sebanding. Begitu ciri itu terlihat, ada satu titik yang memetakan bangun pertama
ke bangun kedua, dan menemukannya sering menyelesaikan seluruh soal.

Pemicu paling produktif: **dua lingkaran yang bersinggungan**. Titik singgungnya adalah
pusat homoteti yang memetakan satu lingkaran ke lingkaran lain, dan setiap garis lewat
titik itu memotong keduanya di pasangan titik yang bersesuaian.

Pemicu ketiga: soal meminta membuktikan **tiga titik segaris**, dan dua di antaranya
adalah pusat dua lingkaran. Pusat homoteti selalu segaris dengan titik yang bersesuaian
dan petanya.

## Intinya

**Homoteti** berpusat $O$ dengan faktor $k \ne 0$ memetakan tiap titik $P$ ke $P'$ dengan

$$\overrightarrow{OP'} = k \cdot \overrightarrow{OP}$$

Yang dijaga: bentuk, sudut, dan **kesejajaran** — setiap garis dipetakan ke garis yang
sejajar dengannya. Yang berubah: panjang menjadi $|k|$ kali, luas menjadi $k^2$ kali.

Tanda $k$ menentukan letaknya: kalau $k > 0$ bangun petanya sepihak dengan aslinya
terhadap $O$; kalau $k < 0$ ia di seberang, terbalik.

**Dua lingkaran punya dua pusat homoteti** — satu dalam dan satu luar. Pusat luar terletak
pada perpanjangan garis pusat dan memetakan dengan $k = r_2/r_1$; pusat dalam terletak di
antara kedua pusat dan memetakan dengan $k = -r_2/r_1$. Untuk lingkaran yang bersinggungan,
salah satunya tepat titik singgungnya.

**Gabungan dua homoteti adalah homoteti lagi** (atau translasi kalau hasil kali faktornya
$1$), dan pusatnya segaris dengan kedua pusat semula. Kenyataan itu — **teorema Monge** —
yang menjadikan homoteti alat pembuktian kesegarisan, bukan sekadar alat menghitung.

**Contoh baku.** Homoteti berpusat titik berat $G$ dengan faktor $-\tfrac{1}{2}$ memetakan
tiap titik sudut ke titik tengah sisi seberangnya. Dari situ lingkaran luar terpetakan ke
lingkaran sembilan titik, dan seluruh garis Euler mengalir keluar.

## Jebakan umum

- **Mengira sebangun berarti homotetik.** Homoteti menuntut sisi bersesuaian **sejajar**.
  Dua segitiga sebangun yang saling terputar tidak dihubungkan homoteti saja, melainkan
  homoteti digabung rotasi.
- **Melupakan pusat homoteti yang satu lagi.** Dua lingkaran punya dua; memakai yang salah
  memberi kesimpulan yang benar bentuknya tetapi salah titiknya.
- **Salah tanda $k$.** Faktor negatif membalik letak; menuliskannya positif membuat titik
  petanya jatuh di sisi yang keliru.
- **Memakai $k$ untuk perbandingan luas.** Luas berbanding $k^2$, dan tandanya hilang
  karena dikuadratkan.
