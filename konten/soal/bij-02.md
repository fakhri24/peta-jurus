---
id: bij-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [bijeksi]
bentuk: isian
kesulitan: 3
jawaban: "70"
---

## Soal

Ada berapa barisan **tak turun** $\left(a_1, a_2, a_3, a_4\right)$ yang seluruh sukunya
diambil dari $\{1,2,3,4,5\}$?

(Tak turun berarti $a_1 \le a_2 \le a_3 \le a_4$; suku boleh berulang.)

## Petunjuk

- Urutan sukunya sudah ditentukan oleh syarat tak turun, jadi yang benar-benar bebas hanyalah **berapa kali** tiap nilai muncul.
- Ubah barisannya menjadi catatan banyaknya kemunculan tiap nilai. Berapa jumlah seluruh catatan itu?
- Persoalannya berubah menjadi membagi $4$ satuan ke dalam $5$ wadah.

## Pembahasan

**Amati apa yang sebenarnya bebas.** Sebuah barisan tak turun ditentukan sepenuhnya oleh
**berapa kali** tiap nilai muncul — urutannya tidak menambah kebebasan apa pun, sebab
sukunya wajib terurut naik.

**Bangun padanannya.** Untuk tiap barisan, catat

$$x_j = \text{banyaknya suku yang bernilai } j, \qquad j = 1,\dots,5$$

Karena barisannya punya $4$ suku,

$$x_1 + x_2 + x_3 + x_4 + x_5 = 4, \qquad x_j \ge 0$$

Contohnya barisan $(1,3,3,5)$ menjadi $(1,0,2,0,1)$.

**Periksa arah sebaliknya.** Dari sebarang penyelesaian tak negatif, susun barisannya:
tulis nilai $1$ sebanyak $x_1$ kali, lalu $2$ sebanyak $x_2$ kali, dan seterusnya. Hasilnya
selalu barisan tak turun sepanjang $4$ dengan suku dari $\{1,\dots,5\}$, dan cara
menyusunnya hanya satu.

Kedua arah saling meniadakan, jadi padanannya satu-satu dan pada.

**Cacah penyelesaiannya** dengan $n = 4$ dan $k = 5$:

$$\binom{n+k-1}{k-1} = \binom{8}{4} = \frac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2 \times 1} = \boxed{70}$$

**Yang dilatih di sini adalah mengubah bentuk soalnya.** Soal berbicara tentang barisan;
jawabannya datang dari soal membagi objek identik. Padanan itu yang menghubungkan keduanya,
dan tanpanya rumus yang tepat tidak akan terlihat.

**Bentuk umumnya** — barisan tak turun sepanjang $r$ dari $n$ nilai:

$$\binom{n+r-1}{r}$$

Ini juga banyaknya cara memilih $r$ benda dari $n$ jenis **dengan pengulangan
diperbolehkan** — sebab memilih dengan pengulangan sama saja dengan mencatat berapa kali
tiap jenis terambil.

**Periksa pada kasus kecil.** Barisan tak turun sepanjang $2$ dari $\{1,2,3\}$: rumusnya
memberi $\binom42 = 6$, dan daftarnya memang $(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)$.

**Bandingkan dengan barisan naik tegas** ($a_1 < a_2 < a_3 < a_4$), yang jawabannya
$\binom54 = 5$ — jauh lebih sedikit, sebab pengulangan dilarang. Satu tanda pada syarat
mengubah seluruh rumusnya.
