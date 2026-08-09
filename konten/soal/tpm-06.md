---
id: tpm-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [teori-permainan]
bentuk: uraian
kesulitan: 4
---

## Soal

Dua tumpukan batu berisi $a$ dan $b$ batu. Dua pemain bergantian mengambil **sejumlah batu
sebanyak apa pun** (paling sedikit satu) dari **salah satu** tumpukan. Pemain yang tidak
bisa melangkah dinyatakan kalah.

Buktikan bahwa pemain yang mendapat giliran **kalah tepat ketika $a = b$**.

## Petunjuk

- Buktikan dua hal terpisah: dari keadaan $a = b$ setiap langkah menuju keadaan tak sama, dan dari keadaan tak sama ada langkah menuju keadaan sama.
- Untuk arah kedua, langkahnya jelas: ambil dari tumpukan yang lebih banyak sampai keduanya sama.
- Jangan lupa menunjukkan permainan pasti berakhir, sebab tanpa itu "kalah" belum berarti apa-apa.

## Pembahasan

Sebut keadaan $(a,b)$ **P** kalau pemain yang mendapat giliran kalah, dan **N** kalau ia
menang. Yang harus dibuktikan:

$$(a,b) \text{ adalah P} \quad\Longleftrightarrow\quad a = b$$

### Langkah 1 — permainan pasti berakhir

Jumlah seluruh batu, $a+b$, berkurang sedikitnya satu pada tiap langkah, dan ia bilangan
bulat tak negatif. Barisan bilangan bulat yang turun dan terbatas di bawah pasti berhingga,
sehingga permainan berakhir setelah paling banyak $a+b$ langkah.

Tanpa langkah ini, pernyataan "seseorang kalah" belum tentu bermakna.

### Langkah 2 — dari $a = b$, setiap langkah menuju keadaan tak sama

Andaikan $a = b$. Sebuah langkah mengambil batu dari **satu** tumpukan saja, sehingga
salah satu bilangan berkurang dan yang lain tetap. Karena yang berkurang sedikitnya satu,
keduanya tidak lagi sama.

Jadi seluruh langkah dari keadaan sama menuju keadaan tak sama.

### Langkah 3 — dari $a \ne b$, ada langkah menuju keadaan sama

Andaikan $a \ne b$, misalkan $a > b$. Ambil $a - b$ batu dari tumpukan pertama. Karena
$a - b \ge 1$, langkah itu sah, dan hasilnya

$$(b, b)$$

yaitu keadaan sama.

### Langkah 4 — rangkai

Keadaan akhir permainan adalah $(0,0)$, yang tidak punya langkah sama sekali — jadi ia P, dan
memang memenuhi $a = b$.

Sekarang tinjau sebarang keadaan, dan kerjakan dengan induksi pada $a+b$:

- Kalau $a = b$, menurut Langkah 2 seluruh langkahnya menuju keadaan tak sama. Menurut
  hipotesis induksi keadaan-keadaan itu N, sehingga $(a,b)$ adalah **P**.
- Kalau $a \ne b$, menurut Langkah 3 ada langkah menuju keadaan sama, yang menurut hipotesis
  induksi adalah P. Karena ada satu langkah menuju P, keadaan $(a,b)$ adalah **N**.

Induksinya sah karena tiap langkah memperkecil $a+b$, dan basisnya $(0,0)$ sudah diperiksa.

Maka $(a,b)$ adalah P tepat ketika $a = b$. $\blacksquare$

### Bacaan strateginya

Untuk pemain yang menghadapi $a \ne b$: **samakan kedua tumpukan**, lalu setelah itu
**tirukan setiap langkah lawan pada tumpukan yang lain**. Kesamaan selalu pulih setelah
langkahmu, dan menurut Langkah 2 lawan tidak pernah bisa mempertahankannya.

Ini bentuk lain dari strategi pencerminan: yang dijaga bukan kesimetrian ruang, melainkan
kesamaan dua bilangan.

### Mengapa kedua arah perlu dibuktikan

Menunjukkan "dari $a=b$ semua langkah merusak kesamaan" saja belum cukup — itu baru
menjelaskan mengapa keadaan sama sulit dipertahankan, bukan mengapa ia kalah. Yang
melengkapinya adalah arah sebaliknya: dari keadaan tak sama **selalu ada** jalan kembali ke
keadaan sama.

Dua arah itu yang membuat penandaan P dan N konsisten pada seluruh keadaan sekaligus.

## Rubrik

- Membuktikan permainan pasti berakhir, dengan alasan $a+b$ turun dan terbatas di bawah
- Membuktikan dari $a=b$ setiap langkah menghasilkan $a \ne b$, dengan alasan hanya satu tumpukan yang berubah
- Membuktikan dari $a \ne b$ ada langkah menuju $a=b$, dengan menyebut langkahnya secara nyata
- Menyebut keadaan akhir $(0,0)$ sebagai keadaan P
- Merangkai kedua arah menjadi kesimpulan menyeluruh, misalnya dengan induksi pada $a+b$
- Menyatakan strategi praktisnya: samakan lalu tirukan
