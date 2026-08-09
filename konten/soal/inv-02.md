---
id: inv-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [invarian]
bentuk: isian
kesulitan: 3
jawaban: "1"
---

## Soal

Di sebuah papan tertulis $10$ tanda $+$ dan $15$ tanda $-$. Sebuah langkah terdiri atas
menghapus **dua** tanda sembarang, lalu menuliskan satu tanda baru menurut aturan:

- kalau kedua tanda yang dihapus **sama**, tulis $+$;
- kalau **berbeda**, tulis $-$.

Setelah $24$ langkah tersisa satu tanda. Ada berapa tanda $-$ yang tersisa?

## Petunjuk

- Perhatikan hanya banyaknya tanda $-$, dan periksa bagaimana angka itu berubah pada tiap jenis langkah.
- Ada tiga jenis langkah: dua $+$, dua $-$, atau satu masing-masing. Periksa ketiganya satu per satu.
- Banyaknya tanda $-$ memang berubah, tetapi ada sifatnya yang tidak pernah berubah.

## Pembahasan

**Periksa tiap jenis langkah.** Sebut $m$ banyaknya tanda $-$ di papan.

| Yang dihapus | Yang ditulis | Perubahan $m$ |
|---|---|---|
| $+$ dan $+$ | $+$ | $0$ |
| $-$ dan $-$ | $+$ | $-2$ |
| $+$ dan $-$ | $-$ | $0$ |

Baris kedua: dua tanda $-$ hilang dan yang ditulis $+$, sehingga $m$ berkurang $2$. Baris
ketiga: satu $-$ hilang tetapi satu $-$ ditulis, sehingga $m$ tidak berubah.

**Simpulkan invariannya.** Pada ketiga jenis langkah, $m$ berubah sebesar $0$ atau $-2$ —
selalu bilangan **genap**. Maka

$$m \bmod 2 \text{ tidak pernah berubah}$$

**Hitung nilai awalnya.** Mula-mula $m = 15$, yang **ganjil**.

**Simpulkan.** Paritas $m$ tetap ganjil sampai akhir. Di akhir hanya tersisa satu tanda,
sehingga $m$ bernilai $0$ atau $1$. Karena harus ganjil, satu-satunya kemungkinan

$$m = \boxed{1}$$

Jadi tanda yang tersisa adalah $-$.

**Banyaknya tanda $+$ sama sekali tidak berpengaruh.** Angka $10$ pada soal boleh diganti
berapa pun — jawabannya tetap ditentukan oleh paritas banyaknya tanda $-$. Mengenali data
mana yang tidak menentukan adalah bagian dari mengerjakan soal invarian.

**Cara memandang yang lebih ringkas.** Ganti $+$ dengan $1$ dan $-$ dengan $-1$. Aturannya
persis aturan perkalian:

$$(+1)(+1) = +1, \qquad (-1)(-1) = +1, \qquad (+1)(-1) = -1$$

Jadi tiap langkah mengganti dua bilangan dengan hasil kalinya, sehingga **hasil kali seluruh
bilangan di papan** tidak pernah berubah. Nilai awalnya

$$1^{10} \times (-1)^{15} = -1$$

Di akhir tersisa satu bilangan, dan ia harus sama dengan $-1$. Cara ini mengubah invarian
paritas menjadi invarian hasil kali — bentuk yang sering lebih mudah diperiksa.
