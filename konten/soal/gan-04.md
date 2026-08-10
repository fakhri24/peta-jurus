---
id: gan-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-analitik, persamaan-kuadrat]
bentuk: isian
kesulitan: 3
jawaban: "10"
---

## Soal

Garis $y = 2x + c$ menyinggung lingkaran $x^2 + y^2 = 20$.

Tentukan nilai $c$ yang positif.

## Petunjuk

- "Menyinggung" berarti garis dan lingkaran bertemu di tepat **satu** titik. Bagaimana keadaan itu terbaca dari persamaannya?
- Substitusikan $y = 2x + c$ ke persamaan lingkaran. Hasilnya persamaan kuadrat dalam $x$, dan banyaknya titik potong sama dengan banyaknya akarnya.
- Satu akar kembar berarti diskriminannya nol.

## Pembahasan

**Substitusikan garis ke lingkaran.**

$$x^2 + (2x + c)^2 = 20$$

$$x^2 + 4x^2 + 4cx + c^2 = 20$$

$$5x^2 + 4cx + \left(c^2 - 20\right) = 0$$

**Terjemahkan "menyinggung".** Tiap akar persamaan itu adalah satu titik potong. Menyinggung
berarti tepat satu titik, yakni akar kembar, yakni

$$D = 0$$

**Hitung diskriminannya.**

$$D = (4c)^2 - 4 \times 5 \times \left(c^2 - 20\right) = 16c^2 - 20c^2 + 400 = 400 - 4c^2$$

$$400 - 4c^2 = 0 \quad \Longrightarrow \quad c^2 = 100 \quad \Longrightarrow \quad c = \pm 10$$

Yang positif adalah $c = \boxed{10}$.

### Periksa lewat jarak pusat ke garis

Lingkaran $x^2 + y^2 = 20$ berpusat $(0,0)$ dengan $r = \sqrt{20} = 2\sqrt5$. Garisnya, dalam
bentuk baku, $2x - y + c = 0$. Menyinggung berarti jarak pusat ke garis sama dengan jari-jari:

$$\frac{|2(0) - 0 + c|}{\sqrt{2^2 + (-1)^2}} = \frac{|c|}{\sqrt5} = 2\sqrt5
\quad \Longrightarrow \quad |c| = 10 \quad ✓$$

Cara kedua ini lebih pendek dan tidak memerlukan diskriminan sama sekali. Layak dijadikan
langkah pertama tiap kali soal menyangkut garis dan lingkaran.

### Baca ketiga kemungkinannya dari satu besaran

| Diskriminan | Jarak pusat ke garis | Keadaan |
|---|---|---|
| $D > 0$ | $d < r$ | memotong di dua titik |
| $D = 0$ | $d = r$ | menyinggung |
| $D < 0$ | $d > r$ | tidak menyentuh |

Kedua kolom pertama selalu sejalan; keduanya cara berbeda membaca kenyataan yang sama.

### Mengapa ada dua nilai $c$

Kedua nilai $c = 10$ dan $c = -10$ memberi dua garis sejajar yang menyinggung lingkaran di dua
sisi berlawanan — di $(-4, 2)$ dan di $(4, -2)$. Keduanya jawaban yang sah bagi pertanyaan
"garis mana yang menyinggung", dan soal meminta yang positif justru untuk membuat jawabannya
tunggal.

Kalau perhitunganmu hanya menghasilkan satu nilai, kemungkinan besar ada akar yang hilang saat
menarik akar kuadrat.
