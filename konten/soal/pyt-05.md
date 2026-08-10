---
id: pyt-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [pythagoras]
bentuk: isian
kesulitan: 3
jawaban: "15"
---

## Soal

Titik $P$ terletak di dalam persegi panjang $ABCD$.

![Persegi panjang ABCD dengan A di kiri bawah, B di kanan bawah, C di kanan atas, dan D di kiri atas. Titik P di dalamnya, agak dekat ke sudut A, dihubungkan dengan ruas garis ke keempat titik sudut](persegi-panjang-titik-dalam.svg)

Diketahui $PA = 6$, $PB = 10$, dan $PC = 17$.

Tentukan panjang $PD$.

## Petunjuk

- Ukuran persegi panjangnya tidak diberikan, dan letak $P$ juga tidak. Kalau jawabannya tetap tunggal, pasti ada hubungan yang tidak bergantung pada keduanya.
- Tarik dari $P$ dua ruas yang tegak lurus sisi-sisi persegi panjang. Keempat jarak ke titik sudut jadi terpecah menjadi potongan mendatar dan tegak.
- Tuliskan keempat jaraknya lewat Pythagoras, lalu bandingkan $PA^2 + PC^2$ dengan $PB^2 + PD^2$.

## Pembahasan

**Pecah tiap jarak menjadi mendatar dan tegak.** Tarik lewat $P$ satu garis sejajar $AB$ dan
satu lagi sejajar $AD$. Sebut jarak $P$ ke sisi $AB$ dan $DC$ berturut-turut $y$ dan $y'$,
serta jarak ke sisi $AD$ dan $BC$ berturut-turut $x$ dan $x'$.

Keempat jarak ke titik sudut kini semuanya sisi miring segitiga siku-siku:

$$PA^2 = x^2 + y^2, \qquad PB^2 = x'^2 + y^2$$

$$PC^2 = x'^2 + y'^2, \qquad PD^2 = x^2 + y'^2$$

**Pasangkan yang berhadapan.** Jumlahkan yang sudutnya berseberangan:

$$PA^2 + PC^2 = x^2 + y^2 + x'^2 + y'^2$$

$$PB^2 + PD^2 = x'^2 + y^2 + x^2 + y'^2$$

Kedua ruas kanan memuat **keempat** suku yang sama persis. Maka

$$PA^2 + PC^2 = PB^2 + PD^2$$

**Masukkan angkanya.**

$$6^2 + 17^2 = 10^2 + PD^2$$

$$36 + 289 = 100 + PD^2 \quad \Longrightarrow \quad PD^2 = 225 \quad \Longrightarrow \quad PD = \boxed{15}$$

### Mengapa ukuran persegi panjangnya tidak pernah muncul

Panjang dan lebarnya memang tidak diperlukan: yang dipakai hanya bahwa $x + x'$ sama untuk
kedua sisi mendatar dan $y + y'$ sama untuk kedua sisi tegak — dan bahkan jumlah itu pun
tidak muncul di perhitungan akhir. Keempat suku sekadar berpindah tempat.

Karena itu soal ini punya jawaban tunggal meski gambarnya tidak tertentu. Kalau kamu merasa
kekurangan data, biasanya yang perlu dicari bukan data tambahan, melainkan besaran yang
**hilang saat dikurangkan**.

### Nama dan jangkauannya

Hubungan $PA^2 + PC^2 = PB^2 + PD^2$ dikenal sebagai teorema bendera Inggris, dan berlaku
untuk **setiap** titik $P$ — di dalam persegi panjang, di sisinya, bahkan di luarnya. Buktinya
tidak berubah sedikit pun, sebab yang dipakai cuma penguraian menjadi potongan mendatar dan
tegak.

Yang **tidak** berlaku: hubungan itu khusus persegi panjang. Pada jajaran genjang miring,
keempat suku tidak lagi berpasangan seperti itu.

### Periksa bahwa bangunnya memang ada

Angka $6$, $10$, $17$ tidak boleh dipilih sembarangan — harus ada persegi panjang yang benar
memuatnya. Dari perhitungan di atas, dengan memilih $y = 4$ diperoleh $x = \sqrt{20}$,
$x' = \sqrt{84}$, dan $y' = \sqrt{205}$, sehingga persegi panjangnya berukuran kira-kira
$13{,}6 \times 18{,}3$ dengan $P$ di dalamnya. Bangunnya ada, jadi soalnya sah.

Pemeriksaan semacam ini layak dibiasakan saat kamu **menyusun** soal sendiri: hubungan yang
benar tetap memberi jawaban meski bangunnya mustahil, dan angka mustahil tidak akan pernah
mengeluh.
