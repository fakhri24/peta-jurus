---
id: am-gm
nama: Ketaksamaan AM-GM
pilar: aljabar
tahap: osn-p
prasyarat: [ketaksamaan-dasar]
contoh: [ag-contoh-1]
latihan: [ag-01, ag-02, ag-03, ag-04, ag-05, ag-06]
---

## Kapan dipakai

Semua peubahnya **positif**, dan soal meminta nilai terbesar atau terkecil dari jumlah
atau hasil kali. Ciri paling terang: satu di antara jumlah dan hasil kali diketahui tetap,
lalu yang lain ditanyakan.

## Intinya

Untuk bilangan positif $a_1, \dots, a_n$:

$$\frac{a_1 + a_2 + \cdots + a_n}{n} \ \ge\ \sqrt[n]{a_1 a_2 \cdots a_n}$$

dengan kesamaan **tepat ketika semuanya sama**.

Bentuk dua peubah yang paling sering dipakai:

$$a + b \ge 2\sqrt{ab}, \qquad a, b > 0$$

Cara membacanya: kalau hasil kali tetap, jumlahnya paling kecil saat kedua bilangan sama;
kalau jumlahnya tetap, hasil kalinya paling besar saat keduanya sama.

**Syarat kesamaan itu bagian dari jawaban, bukan pelengkap.** Soal "tentukan nilai
minimum" belum selesai sebelum ditunjukkan nilai itu benar-benar tercapai — yaitu ada
pilihan peubah yang membuat semuanya sama sekaligus memenuhi kendala soal.

Kalau penerapan langsung tidak memberi batas yang tetap, biasanya pemecahannya
**memecah suku**: tulis satu suku menjadi beberapa bagian yang sama supaya kesamaannya
bisa tercapai. Contohnya pada $x + \frac{4}{x^2}$, pecah $\frac{4}{x^2}$ jadi dua bagian
$\frac{2}{x^2}$ lalu terapkan AM-GM pada tiga suku.

## Jebakan umum

- **Memakainya pada bilangan yang bisa negatif.** AM-GM menuntut semua suku positif.
- **Berhenti sebelum memeriksa kesamaan.** Batas yang tidak pernah tercapai bukan nilai
  minimum; ia hanya batas bawah.
- **Menerapkannya pada suku yang salah** sehingga yang keluar bukan bilangan tetap. Kalau
  hasilnya masih memuat peubah, penerapannya belum berguna.
