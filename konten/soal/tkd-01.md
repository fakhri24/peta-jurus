---
id: tkd-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [tempat-kedudukan]
bentuk: isian
kesulitan: 4
jawaban: "20"
---

## Soal

Ruas $AB$ tetap dengan $AB = 16$. Titik $C$ bergerak sedemikian sehingga luas segitiga
$ABC$ selalu $48$.

![Sebuah ruas mendatar AB sepanjang 16 di bagian bawah, dengan A di kiri dan B di kanan. Di atasnya, sejajar AB dan berjarak 6 darinya, digambar sebuah garis putus-putus yang memanjang melewati kedua ujung AB. Titik C berada pada garis itu dan dihubungkan ke A dan ke B sehingga terbentuk segitiga ABC. Dua letak lain untuk C ditandai sebagai titik kosong pada garis yang sama, menunjukkan bahwa C boleh bergeser sepanjang garis itu tanpa mengubah luas segitiganya. Jarak antara kedua garis sejajar itu, yaitu tinggi segitiga, diberi keterangan 6](alas-tetap-puncak-bergerak.svg)

Tentukan nilai terkecil dari $AC + CB$.

## Petunjuk

- Sebelum mencari nilai terkecil apa pun, tentukan dulu $C$ boleh berada di mana. Alasnya tetap dan luasnya tetap — apa yang menjadi tetap sebagai akibatnya?
- Tempat kedudukan $C$ adalah dua garis sejajar $AB$. Cari jaraknya dari $AB$, dan jangan lupa garis yang kedua.
- Setelah $C$ terkurung pada sebuah garis, soalnya berubah menjadi soal lintasan terpendek: cerminkan $A$ pada garis itu.

## Pembahasan

**Langkah pertama: kurung $C$.** Luas segitiga dengan alas $AB$ adalah

$$L = \frac12 \cdot AB \cdot t$$

dengan $t$ jarak $C$ ke garis $AB$. Karena $AB$ dan $L$ keduanya tetap, $t$ ikut tetap:

$$48 = \frac12 \cdot 16 \cdot t \quad \Longrightarrow \quad t = 6$$

Jadi tempat kedudukan $C$ adalah himpunan titik berjarak $6$ dari garis $AB$ — yaitu
**dua garis sejajar** $AB$, satu di tiap sisinya. Gambar di atas hanya menunjukkan yang
sebelah atas.

**Langkah kedua: lintasan terpendek.** Ambil $C$ pada garis atas. Beri koordinat:

$$A = (0, 0), \qquad B = (16, 0), \qquad C = (u, 6)$$

Cerminkan $A$ terhadap garis $y = 6$, menghasilkan

$$A' = (0, 12)$$

Karena pencerminan menjaga jarak dan $C$ ada pada sumbu cerminnya, $AC = A'C$. Maka

$$AC + CB = A'C + CB \ \ge\ A'B$$

dengan kesamaan tepat ketika $C$ terletak pada ruas $A'B$. Panjangnya:

$$A'B = \sqrt{16^2 + 12^2} = \sqrt{256 + 144} = \sqrt{400} = \boxed{20}$$

**Kesamaannya tercapai.** Ruas $A'B$ dari $(0,12)$ ke $(16,0)$ memotong garis $y = 6$
di titik dengan

$$u = 16 \cdot \frac{12 - 6}{12} = 8$$

jadi $C = (8, 6)$ — tepat di atas titik tengah $AB$. Periksa:

$$AC = \sqrt{64 + 36} = 10, \qquad CB = \sqrt{64 + 36} = 10, \qquad AC + CB = 20 \quad ✓$$

Garis yang di bawah memberi jawaban yang sama karena seluruh gambarnya bercermin pada
$AB$.

### Kenapa $C$ jatuh di tengah

Jawabannya sama kaki, dan itu bukan kebetulan. Setelah $C$ terkurung pada satu garis
sejajar $AB$, jumlah $AC + CB$ adalah jumlah jarak ke dua titik tetap — dan tempat
kedudukan titik dengan $AC + CB$ tetap adalah **elips** berfokus $A$ dan $B$.

Bayangkan elips itu digelembungkan pelan-pelan dari ruas $AB$. Elips terkecil yang masih
menyentuh garis $y = 6$ menyentuhnya di satu titik saja, dan karena elipsnya bersumbu
simetri tegak lurus $AB$ di tengah, titik singgungnya jatuh di tengah.

Cara cermin di atas lebih pendek, tetapi gambaran elips ini menjelaskan **mengapa**
jawabannya simetris — dan sekaligus memberi cara memeriksa: nilai $20$ adalah panjang
sumbu panjang elips yang menyinggung garis itu.

### Apa yang tidak berubah, dan apa yang berubah

Sepanjang $C$ berjalan di garis $y=6$:

| Besaran | Berubah? |
|---|---|
| luas $ABC$ | tidak — memang itu syaratnya |
| tinggi dari $C$ | tidak |
| $AC + CB$ | ya, terkecil $20$, tanpa batas atas |
| $AC \cdot CB$ | ya |
| $\angle ACB$ | ya, terbesar saat $C$ di tengah |

Membedakan kolom itu adalah inti jurus ini. Soal biasanya menyebut yang **tidak**
berubah sebagai syarat, lalu menanyakan salah satu yang berubah.

### Jebakan: lupa garis yang kedua

Pertanyaan soal ini kebetulan tidak terpengaruh — kedua garis memberi $20$ yang sama.
Tetapi kalau pertanyaannya "ada berapa titik $C$ yang membuat $AC + CB = 20$", jawabannya
**dua**, bukan satu.

Aturan yang aman: tuliskan tempat kedudukannya **selengkapnya** dulu, baru jawab
pertanyaannya. Menyingkat langkah itu adalah cara paling umum kehilangan separuh
jawaban di jurus ini.
