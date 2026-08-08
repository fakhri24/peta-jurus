---
id: fkt-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [faktorisasi]
bentuk: isian
kesulitan: 2
jawaban: "4"
---

## Soal

Ada berapa akar real dari persamaan

$$x^4 - 5x^2 + 4 = 0\ ?$$

## Petunjuk

- Derajatnya empat, tetapi yang muncul hanya pangkat genap. Itu tanda ada bentuk kuadrat yang tersembunyi.
- Perlakukan $x^2$ sebagai satu kesatuan: bentuknya menjadi $u^2 - 5u + 4$ dengan $u = x^2$.
- Setelah $u$ ditemukan, jangan lupa mengembalikannya menjadi $x$ — tiap $u$ positif memberi dua nilai $x$.

## Pembahasan

Hanya pangkat genap yang muncul, jadi substitusikan $u = x^2$:

$$u^2 - 5u + 4 = 0$$

Faktorkan — dua bilangan berjumlah $-5$ dan berhasil kali $4$ adalah $-1$ dan $-4$:

$$(u-1)(u-4) = 0 \quad\Longrightarrow\quad u = 1 \text{ atau } u = 4$$

**Kembalikan substitusinya.**

$$x^2 = 1 \ \Longrightarrow\ x = \pm 1, \qquad x^2 = 4 \ \Longrightarrow\ x = \pm 2$$

Keempatnya real dan berbeda, jadi ada $\boxed{4}$ akar real.

Langkah terakhir itu yang paling sering terlewat. Menemukan $u = 1$ dan $u = 4$ belum
menjawab apa pun — yang ditanya $x$, dan tiap $u$ positif menyumbang **dua** nilai $x$.

Perhatikan pula bahwa $u$ harus tak negatif, karena $u = x^2$. Kalau salah satu akar
kuadratnya bernilai negatif, ia tidak menyumbang akar real sama sekali. Pada
$x^4 + 3x^2 - 4 = 0$ misalnya, $u = 1$ dan $u = -4$; hanya yang pertama terpakai, sehingga
akar realnya cuma dua.

Bentuk yang hanya memuat pangkat genap disebut **bikuadrat**, dan substitusi $u = x^2$
selalu bekerja padanya.
