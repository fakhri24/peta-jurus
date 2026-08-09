---
id: eks-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [ekstremal]
bentuk: uraian
kesulitan: 4
---

## Soal

Beberapa titik ditempatkan pada bidang, tidak seluruhnya segaris. Melalui setiap dua titik
ditarik sebuah garis.

Buktikan bahwa **paling sedikit ada satu garis** yang melalui tepat dua di antara
titik-titik itu.

## Petunjuk

- Soal meminta membuktikan sesuatu ada, tanpa petunjuk di mana. Cari besaran yang bisa dipilih paling kecil.
- Tinjau seluruh pasangan (titik, garis) dengan titiknya **tidak** berada pada garis itu, lalu pilih pasangan yang **jaraknya terkecil**.
- Andaikan garis pada pasangan terpilih memuat tiga titik atau lebih, lalu bangun pasangan dengan jarak yang lebih kecil.

## Pembahasan

**Susun himpunan yang akan dipilih dari padanya.** Tinjau seluruh pasangan $(P, \ell)$ dengan
$P$ salah satu titik, $\ell$ garis yang melalui dua di antara titik-titik itu, dan
$P \notin \ell$.

**Himpunan itu tidak kosong.** Karena titiknya tidak seluruhnya segaris, ada garis $\ell$
lewat dua titik dan ada titik ketiga di luarnya.

**Himpunan itu berhingga,** sebab titiknya berhingga sehingga garisnya juga berhingga.

**Pilih yang paling.** Ambil pasangan $(P, \ell)$ dengan **jarak $P$ ke $\ell$ terkecil**.
Pilihan ini sah karena himpunannya berhingga dan tidak kosong.

**Klaim: $\ell$ melalui tepat dua titik.**

Andaikan tidak — yaitu $\ell$ memuat sedikitnya tiga titik, sebut $A$, $B$, $C$.

Jatuhkan kaki tegak lurus dari $P$ ke $\ell$, sebut $Q$. Titik $Q$ membagi $\ell$ menjadi dua
sisi. Karena ada tiga titik pada $\ell$, menurut prinsip sarang merpati **paling sedikit dua
di antaranya berada pada sisi yang sama** — termasuk kemungkinan salah satunya berimpit
dengan $Q$.

Sebut kedua titik itu $A$ dan $B$, dengan $A$ lebih dekat ke $Q$ daripada $B$.

Sekarang tinjau pasangan baru $(A, \ell')$ dengan $\ell'$ garis lewat $P$ dan $B$.

- $A$ tidak berada pada $\ell'$, sebab kalau ya maka $P$ berada pada garis $AB = \ell$,
  bertentangan dengan $P \notin \ell$.
- Jarak $A$ ke $\ell'$ **lebih kecil** daripada jarak $P$ ke $\ell$.

Alasan yang terakhir: tinjau segitiga $PQB$ yang siku-siku di $Q$. Titik $A$ berada pada ruas
$QB$, sehingga jarak dari $A$ ke garis $PB$ tidak melebihi jarak dari $Q$ ke garis $PB$, dan
jarak dari $Q$ ke $PB$ lebih kecil daripada $PQ$ — sebab pada segitiga siku-siku, tinggi ke
sisi miring selalu lebih pendek daripada kaki.

Jadi pasangan $(A, \ell')$ punya jarak yang lebih kecil daripada $(P, \ell)$, bertentangan
dengan pemilihan tadi.

**Maka $\ell$ melalui tepat dua titik.** $\blacksquare$

### Mengapa besaran yang dipilih adalah jarak

Besaran ekstrem harus dipilih sedemikian rupa sehingga sifat yang dilanggar dapat dipakai
untuk membangun sesuatu yang **lebih ekstrem**. Di sini, adanya titik ketiga pada garis
selalu memungkinkan menemukan pasangan yang lebih dekat — dan itu yang membuat jarak jadi
pilihan yang tepat.

Kalau yang dipilih misalnya "garis yang melalui titik terbanyak", tidak ada langkah lanjutan
yang jelas. Memilih besaran yang salah bukan kekeliruan hitung; ia hanya membuat buktinya
tidak berjalan, dan tandanya adalah sifat "paling" tidak pernah terpakai.

### Catatan tentang kehinggaan

Seluruh bukti bersandar pada adanya pasangan dengan jarak **terkecil**. Untuk himpunan titik
tak berhingga, jaminan itu hilang — dan pernyataannya memang tidak berlaku: seluruh titik
pada dua garis sejajar yang rapat memberi contoh yang tidak punya jarak terkecil.

Pernyataan ini dikenal sebagai teorema Sylvester–Gallai, dan bukti di atas adalah bukti
Kelly yang terkenal karena pendeknya.

## Rubrik

- Menyusun himpunan pasangan (titik, garis) dengan titik tidak pada garisnya
- Menyatakan himpunan itu tidak kosong dan berhingga, sebagai alasan adanya jarak terkecil
- Memilih pasangan dengan jarak terkecil
- Mengandaikan garisnya memuat tiga titik, lalu memakai sarang merpati pada kedua sisi kaki tegak lurus
- Membangun pasangan baru dan menunjukkan jaraknya lebih kecil
- Menyatakan pertentangannya dengan pemilihan jarak terkecil
