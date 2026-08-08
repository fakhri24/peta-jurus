---
id: pk-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [persamaan-kuadrat]
bentuk: isian
kesulitan: 2
jawaban: "9"
---

## Soal

Tentukan nilai $m$ agar persamaan

$$x^2 - 6x + m = 0$$

mempunyai akar kembar.

## Petunjuk

- Kamu tidak perlu mencari akarnya. Ada satu besaran yang menentukan sifat akar tanpa menghitungnya.
- Diskriminan $D = b^2 - 4ac$ menjawab pertanyaan tentang jenis akar: dua akar berbeda, kembar, atau tidak real.
- Akar kembar terjadi tepat ketika $D = 0$.

## Pembahasan

Sifat akar persamaan kuadrat ditentukan oleh diskriminan

$$D = b^2 - 4ac$$

- $D > 0$: dua akar real berbeda
- $D = 0$: akar kembar
- $D < 0$: tidak ada akar real

Di sini $a = 1$, $b = -6$, $c = m$, jadi

$$D = (-6)^2 - 4(1)(m) = 36 - 4m$$

Akar kembar menuntut $D = 0$:

$$36 - 4m = 0 \quad\Longrightarrow\quad m = \boxed{9}$$

Periksa: dengan $m = 9$ persamaannya menjadi $x^2 - 6x + 9 = (x-3)^2 = 0$, yang memang
berakar kembar $x = 3$.

**Inilah pemakaian diskriminan yang paling sering muncul di olimpiade** — bukan untuk
menghitung akar, melainkan untuk menjawab pertanyaan **tentang** akar. Soal "tentukan
syarat agar punya dua akar berbeda" atau "agar tidak punya akar real" adalah soal tentang
$D$, dan akarnya tidak pernah perlu dicari.

Perhatikan syarat tersembunyi: rumus $D$ hanya berlaku kalau $a \ne 0$. Kalau koefisien
$x^2$ memuat parameter, kasus $a = 0$ harus diperiksa terpisah — di situ persamaannya
linear dan tidak punya akar kembar sama sekali.
