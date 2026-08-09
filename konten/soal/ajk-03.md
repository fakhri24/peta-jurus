---
id: ajk-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [aturan-pencacahan]
bentuk: isian
kesulitan: 3
jawaban: "3168"
---

## Soal

Ada berapa bilangan empat angka yang memuat **paling sedikit satu** angka $7$?

(Bilangan empat angka adalah bilangan dari $1000$ sampai $9999$.)

## Petunjuk

- Menghitung "paling sedikit satu" secara langsung memaksa memecah kasus tepat satu, tepat dua, tepat tiga, dan tepat empat. Cari jalan yang lebih pendek.
- Kebalikan dari "memuat paling sedikit satu angka $7$" adalah "tidak memuat angka $7$ sama sekali" — dan yang kedua jauh lebih mudah dihitung.
- Hitung seluruh bilangan empat angka, lalu kurangi yang sama sekali tanpa angka $7$. Ingat angka pertama tidak boleh $0$.

## Pembahasan

Kata **"paling sedikit satu"** hampir selalu menandakan hitungan lewat kebalikannya.
Menghitungnya langsung menuntut empat kasus terpisah yang saling tumpang tindih kalau
tidak hati-hati; kebalikannya cuma satu hitungan.

**Seluruhnya.** Bilangan empat angka berjalan dari $1000$ sampai $9999$:

$$9999 - 1000 + 1 = 9000$$

**Yang tidak memuat angka $7$ sama sekali.** Kerjakan tempat demi tempat:

- Angka ribuan tidak boleh $0$ dan tidak boleh $7$, jadi tersisa $\{1,\dots,9\}
  \setminus \{7\}$, yaitu $8$ pilihan.
- Tiga tempat lainnya boleh $0$ tapi tidak boleh $7$, jadi masing-masing $9$ pilihan.

$$8 \times 9 \times 9 \times 9 = 8 \times 729 = 5832$$

**Kurangkan.**

$$9000 - 5832 = \boxed{3168}$$

**Mengapa kedua tempat itu berbeda banyak pilihannya.** Angka ribuan menanggung dua
larangan sekaligus — bukan $0$ karena bilangannya harus empat angka, dan bukan $7$ karena
kita sedang menghindarinya. Tempat yang lain hanya menanggung satu larangan. Kelalaian
menyamakan keduanya adalah kekeliruan yang paling sering pada soal jenis ini.

Periksa kewajarannya: kira-kira sepertiga dari $9000$ memuat angka $7$, dan $3168$ memang
sedikit di atas sepertiga. Angkanya masuk akal.
