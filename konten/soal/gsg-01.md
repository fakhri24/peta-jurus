---
id: gsg-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [garis-singgung]
bentuk: isian
kesulitan: 1
jawaban: "15"
---

## Soal

Dari titik $P$ di luar lingkaran berpusat $O$ dan berjari-jari $8$, ditarik sebuah garis
singgung yang menyentuh lingkaran di titik $T$. Diketahui $OP = 17$.

Tentukan panjang $PT$.

## Petunjuk

- Gambarnya belum memuat segitiga apa pun. Ruas mana yang perlu ditarik supaya muncul satu, dan mengapa ruas itu?
- Tarik jari-jari $OT$. Jari-jari tegak lurus garis singgung di titik singgungnya.
- Segitiga $OTP$ siku-siku di $T$ dengan sisi miring $OP$.

## Pembahasan

**Tarik jari-jari ke titik singgungnya.** Ini gerakan pertama jurus ini, dan yang paling sering
dilupakan. Jari-jari $OT$ tegak lurus garis singgung di $T$, sehingga

$$\angle OTP = 90^\circ$$

**Kenali sisi miringnya.** Pada $\triangle OTP$ yang siku-siku di $T$, sisi miringnya adalah
$OP$ — sisi di hadapan sudut siku-siku — bukan $PT$.

$$OP^2 = OT^2 + PT^2$$

$$17^2 = 8^2 + PT^2$$

$$PT^2 = 289 - 64 = 225 \quad \Longrightarrow \quad PT = \boxed{15}$$

**Periksa.** $(8, 15, 17)$ adalah tripel Pythagoras ✓.

### Kekeliruan yang paling sering di soal semacam ini

Menjumlahkan alih-alih mengurangkan: $\sqrt{17^2 + 8^2} = \sqrt{353}$. Yang menentukan bukan
angka mana yang lebih besar, melainkan **sisi mana yang berhadapan dengan sudut siku-siku**.

Pemeriksaan kewajaran satu detik: $PT$ adalah salah satu sisi siku-siku, jadi ia harus **lebih
pendek** daripada $OP = 17$. Jawaban $\sqrt{353} \approx 18{,}8$ gagal di situ sebelum
diperiksa lebih jauh.

### Panjang singgung itu punya nama

Besaran $PT^2 = OP^2 - r^2$ disebut **kuasa titik** $P$ terhadap lingkaran, dan ia muncul lagi
pada jurus tingkat berikutnya dalam bentuk

$$PT^2 = PA \cdot PB$$

untuk garis lewat $P$ yang memotong lingkaran di $A$ dan $B$.

Yang layak dicatat sekarang: nilainya **positif** tepat ketika $P$ di luar lingkaran, nol
ketika $P$ pada lingkaran, dan negatif ketika di dalam — dan dalam kasus terakhir tidak ada
garis singgung dari $P$ sama sekali, yang cocok dengan akar bilangan negatif yang muncul.

### Titik singgung yang kedua

Dari $P$ sebenarnya ada **dua** garis singgung, menyentuh lingkaran di dua titik berbeda.
Keduanya sama panjang — dua-duanya $15$ — dan alasannya perhitungan yang persis sama, sebab
yang dipakai cuma $OP$ dan $r$.
