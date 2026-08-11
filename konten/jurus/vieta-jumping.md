---
id: vieta-jumping
nama: Vieta Jumping
pilar: teori-bilangan
tahap: osn
prasyarat: [turun-tak-hingga]
contoh: [vj-contoh-1]
latihan: [vj-01, vj-02, vj-03, vj-04, vj-05, vj-06]
---

## Kapan dipakai

Soal memuat persamaan Diophantine **simetris kuadratik** dalam dua peubah bulat positif $(a, b)$, dengan bentuk khas pecahan $\frac{a^2 + b^2}{ab + k} = k$ bernilai bulat. Ini pola paling ikonik di olimpiade (termasuk IMO 1988 No 6).

Pemicu kedua: soal meminta membuktikan bahwa nilai rasional pecahan kuadrat simetris $\frac{A(a,b)}{B(a,b)}$ yang bernilai bulat **harus berupa kuadrat sempurna**.

Pemicu ketiga: konstruksi barisan solusi tak hingga melalui hubungan rekurensi Vieta. Jika $(a, b)$ solusi dengan $a \ge b$, kita membuat akar baru $a' = \frac{b^2 - k}{a} < a$ yang menghasilkan solusi minimal hingga menabrak kontradiksi batas.

Pemicu keempat: teknik pembalikan (jumping up/down) untuk membuktikan tidak adanya pasangan solusi bulat positif di luar keluarga solusi sepele $(k, 0)$ atau $(k, k)$.

## Intinya

Perlakukan persamaannya sebagai **kuadrat dalam satu variabel**, dengan variabel lain
dianggap tetap. Kalau $(a, b)$ solusi, maka $a$ adalah akar dari suatu persamaan kuadrat —
dan akar keduanya, sebut $a'$, memberi solusi baru $(a', b)$.

Rumus Vieta memberi kedua akar tanpa perlu menghitung apa pun:

$$a + a' = (\text{koefisien}), \qquad a \cdot a' = (\text{konstanta})$$

Yang pertama menjamin $a'$ **bulat**; yang kedua sering menjamin $a'$ **positif**. Jadi
lompatan itu menghasilkan solusi bulat positif yang lebih kecil — dan kamu kembali ke
turun tak hingga.

Kerangka pembuktiannya hampir selalu sama:

1. Ambil solusi dengan $a + b$ terkecil, misalkan $a \ge b$.
2. Lompat: ganti $a$ dengan akar Vieta yang lain, $a'$.
3. Tunjukkan $(a', b)$ juga solusi, bulat, tak negatif, dan lebih kecil.
4. Kontradiksi dengan keminimalan — kecuali di kasus dasar, yang justru memberi jawabannya.

## Jebakan umum

- **Lupa membuktikan $a'$ bulat.** Itu datang dari $a + a' = $ bilangan bulat, bukan dari
  rumus akar kuadrat.
- **Lupa membuktikan $a' \ge 0$.** Tanpa itu penurunannya tidak sah, karena bisa lolos ke
  bilangan negatif.
- **Melewatkan kasus dasar.** Justru di situ jawabannya berada — nilai yang dicari muncul
  ketika penurunan berhenti.
- **Memakainya pada persamaan tak simetris.** Kesimetrian yang membuat pertukaran peran
  $a$ dan $b$ sah.
