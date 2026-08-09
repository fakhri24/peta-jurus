---
id: psk-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-siklik]
bentuk: isian
kesulitan: 3
jawaban: "2520"
---

## Soal

Delapan manik yang seluruhnya berbeda dirangkai menjadi sebuah **gelang**. Gelang itu boleh
diputar dan boleh **dibalik**, dan dua rangkaian dianggap sama kalau yang satu dapat
diperoleh dari yang lain lewat pemutaran atau pembalikan.

Ada berapa gelang yang berbeda?

## Petunjuk

- Kerjakan dulu seolah-olah gelangnya tidak boleh dibalik. Itu soal melingkar biasa.
- Sekarang perhatikan apa yang terjadi kalau gelangnya dibalik: urutan maniknya berbalik arah.
- Tiap gelang karena itu terhitung dua kali pada hitungan pertama — sekali untuk tiap arah pembacaan.

## Pembahasan

**Langkah 1 — anggap dulu tidak boleh dibalik.** Delapan manik berbeda disusun melingkar:

$$(8-1)! = 7! = 5040$$

**Langkah 2 — perhitungkan pembalikan.** Kalau gelangnya dibalik, urutan maniknya terbaca
dari arah yang berlawanan. Rangkaian yang searah jarum jam berbunyi

$$m_1 \to m_2 \to m_3 \to \cdots \to m_8$$

setelah dibalik terbaca

$$m_1 \to m_8 \to m_7 \to \cdots \to m_2$$

Keduanya dihitung sebagai dua hal berbeda pada langkah 1, padahal keduanya **gelang yang
sama** — cukup dibalik.

Jadi tiap gelang terhitung tepat dua kali:

$$\frac{7!}{2} = \frac{5040}{2} = \boxed{2520}$$

**Mengapa pembaginya tepat $2$ dan tidak kurang.** Pembagian ini hanya sah kalau tidak ada
rangkaian yang **sama dengan bayangan cerminnya sendiri** — sebab rangkaian semacam itu
akan terhitung sekali, bukan dua kali. Untuk manik yang seluruhnya berbeda, hal itu tidak
mungkin terjadi: pembalikan menukar tetangga kiri dengan tetangga kanan tiap manik, dan
dengan manik yang semuanya berlainan, susunan tetangganya pasti berubah.

**Kapan pembagi $2$ dipakai dan kapan tidak.** Yang menentukan adalah bendanya, bukan
bentuknya:

| Keadaan | Rumus |
|---|---|
| Orang duduk mengelilingi meja | $(n-1)!$ |
| Gelang atau kalung yang boleh dibalik | $\dfrac{(n-1)!}{2}$, untuk $n \ge 3$ |
| Kursi bernomor | $n!$ |

Orang yang duduk membedakan tetangga kiri dari tetangga kanan, jadi membalik meja tidak
masuk akal. Gelang yang tergeletak di meja bisa diambil dan dibalik, jadi masuk akal.

**Batas $n \ge 3$ bukan kelengkapan tanpa guna.** Untuk $n = 2$, rumusnya memberi
$\frac{1!}{2} = \frac12$ — bukan bilangan bulat, jadi jelas tidak berlaku. Sebabnya untuk
dua manik, membalik tidak menghasilkan apa pun yang baru untuk dihilangkan.
