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

Semua peubah bernilai **real positif** ($a, b, c > 0$), dan soal meminta nilai **maksimum** atau **minimum** dari jumlah atau hasil kali peubah-peubah tersebut.

Pemicu kedua: satu di antara jumlah $\sum a_i$ atau hasil kali $\prod a_i$ bernilai **tetap (konstan)**, lalu yang lain ditanyakan ekstremumnya. AM-GM adalah jembatan paling alami antara penjumlahan dan perkalian.

Pemicu ketiga: bentuk perkalian pecahan atau suku-suku yang **saling mengeliminasi (resiprokal)**, seperti $x + \frac{1}{x} \ge 2$ untuk $x > 0$, atau $\frac{a}{b} + \frac{b}{c} + \frac{c}{a} \ge 3$.

Pemicu keempat: pertaksamaan yang menuntut syarat kesamaan tercapai ketika semua peubah **sama besar** ($a = b = c$).

Pemicu kelima: teknik pembobotan suku (weighted AM-GM) atau pemecahan suku untuk menyesuaikan koefisien agar syarat kesamaan dapat dipenuhi serentak.

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
