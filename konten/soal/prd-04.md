---
id: prd-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [probabilitas-diskret]
bentuk: isian
kesulitan: 3
jawaban: "5/9"
jawaban_alt: ["20/36"]
---

## Soal

Dua dadu setimbang dilempar bersamaan.

Berapa peluang jumlah kedua mata dadu **genap atau lebih dari $9$**? (Tulis sebagai pecahan
paling sederhana.)

## Petunjuk

- Kata "atau" menandakan gabungan dua kejadian, dan kedua kejadian di sini bisa terjadi bersamaan.
- Hitung masing-masing kejadian sendiri, lalu cari hasil yang memenuhi keduanya sekaligus.
- Menjumlahkan begitu saja akan menghitung sebagian hasil dua kali.

## Pembahasan

**Ruang sampelnya** adalah $36$ pasangan terurut, seluruhnya sama mungkin.

Sebut $A$ kejadian "jumlahnya genap" dan $B$ kejadian "jumlahnya lebih dari $9$".

**Hitung $|A|$.** Jumlahnya genap tepat ketika kedua mata sama paritasnya — keduanya ganjil
atau keduanya genap:

$$3 \times 3 + 3 \times 3 = 18$$

**Hitung $|B|$.** Jumlah lebih dari $9$ berarti $10$, $11$, atau $12$. Dari tabel sebaran:

$$3 + 2 + 1 = 6$$

**Hitung $|A \cap B|$.** Jumlah yang genap **dan** lebih dari $9$ adalah $10$ dan $12$:

$$3 + 1 = 4$$

**Rangkai.**

$$|A \cup B| = 18 + 6 - 4 = 20$$

$$P(A \cup B) = \frac{20}{36} = \boxed{\frac59}$$

**Mengapa pengurangan itu perlu.** Pasangan seperti $(4,6)$ berjumlah $10$ — genap sekaligus
lebih dari $9$. Ia terhitung sekali di $|A|$ dan sekali lagi di $|B|$. Menjumlahkan tanpa
koreksi memberi $\frac{24}{36} = \frac23$, yang keliru.

**Aturan yang berlaku umum:**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Menjumlahkan begitu saja hanya sah kalau kedua kejadian **tidak mungkin terjadi bersamaan**.
Memeriksa hal itu adalah langkah yang tidak boleh dilewati, dan di soal ini pemeriksaannya
langsung gagal — ada jumlah yang genap sekaligus melebihi $9$.

**Perhatikan bahwa $11$ tidak masuk irisan.** Ia lebih dari $9$ tetapi ganjil. Mendaftar
$10$, $11$, $12$ lalu menandai mana yang genap adalah cara paling aman menghitung irisannya
— jauh lebih aman daripada menduganya.
