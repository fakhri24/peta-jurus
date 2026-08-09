---
id: pcg-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [pencacahan-ganda]
bentuk: isian
kesulitan: 2
jawaban: "12"
---

## Soal

Di sebuah sekolah terdapat $30$ siswa dan beberapa klub. Setiap siswa mengikuti **tepat
$2$** klub, dan setiap klub beranggotakan **tepat $5$** siswa.

Ada berapa klub di sekolah itu?

## Petunjuk

- Cacah pasangan (siswa, klub yang ia ikuti). Himpunan itu bisa dihitung dari dua sisi.
- Dari sisi siswa: tiap siswa menyumbang dua pasangan.
- Dari sisi klub: tiap klub menyumbang sebanyak anggotanya.

## Pembahasan

**Nyatakan apa yang dicacah.**

$$T = \{(s, k) : \text{siswa } s \text{ mengikuti klub } k\}$$

**Cara A — dari sisi siswa.** Tiap siswa mengikuti tepat $2$ klub, dan ada $30$ siswa:

$$|T| = 30 \times 2 = 60$$

**Cara B — dari sisi klub.** Tiap klub beranggotakan tepat $5$ siswa. Kalau banyaknya klub
adalah $K$:

$$|T| = 5K$$

**Samakan.**

$$5K = 60 \quad\Longrightarrow\quad K = \boxed{12}$$

**Bentuk yang layak dikenali.** Kalau ada dua kelompok objek dan sebuah hubungan di
antaranya, lalu diketahui berapa hubungan yang dimiliki tiap anggota di kedua sisi, maka

$$(\text{banyak sisi kiri}) \times (\text{hubungan per objek kiri}) = (\text{banyak sisi kanan}) \times (\text{hubungan per objek kanan})$$

Persamaan itu langsung memberi besaran yang belum diketahui. Soal yang bunyinya bermacam-
macam — siswa dan klub, titik dan garis, buku dan rak, pemain dan pertandingan — semuanya
persoalan yang sama.

**Periksa kesahihannya.** Hasilnya harus bilangan bulat, dan di sini $60 / 5 = 12$ memang
bulat. Kalau tidak bulat, keadaan yang digambarkan soal mustahil. Misalnya kalau tiap klub
beranggotakan $7$ siswa, maka $K = \frac{60}{7}$ bukan bilangan bulat, sehingga tidak ada
susunan yang memenuhi.

Pemeriksaan itu murah dan sering menjadi seluruh isi soal olimpiade jenis ini: yang
ditanyakan bukan berapa banyak, melainkan **apakah mungkin**.
