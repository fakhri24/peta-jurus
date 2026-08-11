---
id: persamaan-fungsional
nama: Persamaan Fungsional
pilar: aljabar
tahap: osn
prasyarat: [fungsi, induksi]
contoh: [pf-contoh-1]
latihan: [pf-01, pf-02, pf-03, pf-04, pf-05, pf-06]
---

## Kapan dipakai

Soal memberi hubungan yang berlaku **untuk semua** $x$ dan $y$, lalu meminta **seluruh**
fungsi yang memenuhinya. Dua kata itu yang menandainya: "untuk semua" berarti kamu boleh
memilih nilai apa pun, dan "seluruh" berarti menemukan satu jawaban belum menyelesaikan
soal.

Pemicu kedua: rumus $f$ **tidak pernah diberikan**. Kalau soal menyebut $f(x) = 2x+1$ lalu
menanyakan sesuatu, itu jurus Fungsi biasa; di sini $f$ justru yang dicari.

Pemicu ketiga: soal menyebut syarat tambahan seperti **monoton**, **kontinu**, atau
**$f: \mathbb{Z} \to \mathbb{Z}$**. Syarat itu bukan hiasan — ia yang menutup langkah
terakhir, dan soal yang sama tanpa syarat itu biasanya punya jawaban liar yang tak bisa
ditulis.

Pemicu keempat: hubungannya memuat **$f$ di dalam $f$** — $f(f(x)) = x$ atau
$f(x + f(y)) = \ldots$. Bentuk bersarang menuntut memeriksa apakah $f$ satu-satu atau pada
lebih dulu, dan itu biasanya langkah kedua setelah substitusi nilai khusus.

Yang wajib ada di jawaban dan paling sering hilang: **pemeriksaan balik**. Menemukan
kandidat belum membuktikan ia memenuhi, dan soal meminta seluruhnya.

## Intinya

Tidak ada rumus; yang ada urutan gerakan yang hampir selalu dicoba.

1. **Substitusi nilai khusus.** Coba $x = 0$, $y = 0$, $x = y$, $y = -x$, $y = 1$. Tiap
   substitusi memberi persamaan baru yang lebih sederhana.
2. **Cari $f(0)$ dan $f(1)$.** Keduanya biasanya terkunci sejak awal dan menjadi tumpuan
   langkah berikutnya.
3. **Periksa kesimetrian.** Tukar $x$ dan $y$; kalau ruas kiri simetris tetapi ruas kanan
   tidak, kamu mendapat persamaan tambahan secara gratis.
4. **Bangun bertahap.** Dari $f(1)$ ke $f(n)$ lewat induksi, lalu ke bilangan rasional.
5. **Tebak dan buktikan.** Setelah pola terlihat, tebak bentuk $f$, lalu **buktikan tidak
   ada yang lain**.

Langkah terakhir yang paling sering dilupakan. Menemukan satu fungsi yang memenuhi bukan
jawaban; soal menanyakan **semua** fungsi, jadi ketunggalannya harus ditegakkan.

Dan apa pun jawabannya, **periksa balik** — substitusikan fungsi yang kamu peroleh ke
persamaan aslinya. Langkah substitusi bisa memperluas himpunan solusi tanpa terasa.

## Jebakan umum

- **Lupa memeriksa balik.** Fungsi yang lahir dari rangkaian substitusi belum tentu
  memenuhi persamaan aslinya.
- **Mengira menemukan satu solusi sudah cukup.** Yang diminta seluruhnya.
- **Mengabaikan domain.** Sifat yang berlaku untuk bilangan rasional tidak otomatis
  berlaku untuk real tanpa syarat tambahan seperti kemonotonan atau kekontinuan.
