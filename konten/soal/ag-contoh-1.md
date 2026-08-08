---
id: ag-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [am-gm]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Untuk $x > 0$, tentukan nilai terkecil dari

$$x + \frac{9}{x}$$

## Petunjuk

- Kedua sukunya positif, dan hasil kalinya ternyata tetap. Periksa berapa nilai $x \cdot \frac9x$.
- Kalau hasil kali dua bilangan positif tetap, jumlahnya paling kecil ketika keduanya sama.
- Ketaksamaan yang menyatakan itu: $a + b \ge 2\sqrt{ab}$ untuk $a, b > 0$.

## Pembahasan

Perhatikan hasil kali kedua sukunya:

$$x \cdot \frac{9}{x} = 9$$

**Tetap** — tidak bergantung pada $x$ sama sekali. Itulah keadaan yang dijawab AM-GM.

Untuk dua bilangan positif $a$ dan $b$:

$$\frac{a+b}{2} \ \ge\ \sqrt{ab} \quad\Longleftrightarrow\quad a + b \ \ge\ 2\sqrt{ab}$$

dengan kesamaan **tepat ketika $a = b$**.

Terapkan dengan $a = x$ dan $b = \frac9x$, keduanya positif karena $x > 0$:

$$x + \frac{9}{x} \ \ge\ 2\sqrt{x \cdot \frac9x} = 2\sqrt{9} = 6$$

**Periksa kesamaannya tercapai.** Dibutuhkan

$$x = \frac{9}{x} \quad\Longrightarrow\quad x^2 = 9 \quad\Longrightarrow\quad x = 3$$

(akar negatifnya dibuang karena $x > 0$). Substitusikan: $3 + \frac93 = 6$. Tercapai.

Nilai terkecilnya adalah $\boxed{6}$.

**Langkah terakhir itu bagian dari jawaban.** AM-GM hanya memberi batas bawah; ia menjadi
nilai minimum setelah ditunjukkan ada $x$ sah yang mencapainya. Kalau kendala soal
melarang nilai itu — misalnya kalau soal menuntut $x \ge 5$ — batasnya tidak tercapai dan
minimumnya lebih besar.

**Syarat $x > 0$ juga tidak bisa dibuang.** Untuk $x < 0$ bentuk ini justru bernilai
paling besar $-6$; contohnya $x = -3$ memberi $-6$, dan $x = -1$ memberi $-10$. AM-GM
memang hanya berlaku untuk bilangan positif.
