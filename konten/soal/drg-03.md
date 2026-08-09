---
id: drg-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [derangement]
bentuk: isian
kesulitan: 3
jawaban: "135"
---

## Soal

Enam kado ditukar secara acak di antara enam orang, satu kado per orang.

Ada berapa cara pembagian sehingga **tepat $2$ orang** menerima kado miliknya sendiri?

## Petunjuk

- Pecah menjadi dua keputusan: siapa saja yang menerima miliknya sendiri, lalu apa yang terjadi pada sisanya.
- Kata "tepat" menuntut sisanya **tidak boleh** ada yang menerima miliknya sendiri.
- Sisa itu adalah persoalan yang sama pada objek yang lebih sedikit.

## Pembahasan

**Pecah menjadi dua keputusan.**

**Langkah 1 — pilih siapa yang menerima miliknya sendiri.** Dua orang dari enam, tanpa
urutan:

$$\binom62 = 15$$

**Langkah 2 — pastikan sisanya tidak ada yang benar.** Empat orang tersisa harus menerima
kado yang bukan miliknya — tepat persoalan yang sama pada $4$ objek:

$$D_4 = 9$$

**Gabungkan.**

$$\binom62 \times D_4 = 15 \times 9 = \boxed{135}$$

**Mengapa langkah kedua memakai $D_4$ dan bukan $4!$.** Kata **"tepat"** pada soal
menentukan seluruhnya. Kalau dipakai $4!= 24$, yang terhitung adalah pembagian dengan
**paling sedikit** dua orang benar — sebab di antara $24$ susunan itu ada yang membuat orang
ketiga atau keempat ikut menerima miliknya sendiri. Hasilnya $15 \times 24 = 360$, yang
menghitung banyak pembagian berkali-kali.

**Bentuk umumnya** untuk tepat $m$ objek yang tetap di tempatnya dari $n$ objek:

$$\binom{n}{m} D_{n-m}$$

**Periksa lewat jumlah seluruhnya.** Kalau rumus itu benar, menjumlahkan atas seluruh $m$
harus memberi $6! = 720$:

| $m$ | $\binom6m$ | $D_{6-m}$ | hasil |
|---|---|---|---|
| $0$ | $1$ | $265$ | $265$ |
| $1$ | $6$ | $44$ | $264$ |
| $2$ | $15$ | $9$ | $135$ |
| $3$ | $20$ | $2$ | $40$ |
| $4$ | $15$ | $1$ | $15$ |
| $5$ | $6$ | $0$ | $0$ |
| $6$ | $1$ | $1$ | $1$ |

$$265+264+135+40+15+0+1 = 720$$

Cocok. Pemeriksaan semacam ini murah dan langsung menangkap kekeliruan pada rumusnya.

**Perhatikan baris $m = 5$ bernilai nol.** Memang mustahil tepat lima orang menerima
miliknya sendiri — orang keenam otomatis juga menerima miliknya. Kenyataan itu terbaca
langsung dari $D_1 = 0$, dan itu salah satu alasan mengapa nilai $D_1$ tidak boleh ditulis
keliru.
