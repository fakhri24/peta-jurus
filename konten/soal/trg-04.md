---
id: trg-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [trigonometri-segitiga, luas-bidang]
bentuk: isian
kesulitan: 3
jawaban: "41"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 5$, $AC = 8$, dan luasnya $16$. Diketahui pula bahwa
$\angle BAC$ lancip.

Tentukan nilai $BC^2$.

## Petunjuk

- Luas segitiga bisa ditulis memakai dua sisi beserta sudut yang diapitnya. Sisi mana yang mengapit sudut $A$?
- Dari $L = \tfrac12 \cdot AB \cdot AC \sin A$ kamu memperoleh $\sin A$; dari situ carilah $\cos A$.
- Keterangan "lancip" dipakai tepat pada langkah mencari $\cos A$ dari $\sin A$ — ia memilih salah satu dari dua tanda.

## Pembahasan

**Ambil $\sin A$ dari luasnya.** Sisi $AB$ dan $AC$ mengapit sudut $A$, jadi

$$L = \tfrac12 \cdot AB \cdot AC \cdot \sin A = \tfrac12 \cdot 5 \cdot 8 \cdot \sin A = 20 \sin A$$

$$20 \sin A = 16 \quad \Longrightarrow \quad \sin A = \frac{4}{5}$$

**Ambil $\cos A$ dari identitas dasar.**

$$\cos^2 A = 1 - \sin^2 A = 1 - \frac{16}{25} = \frac{9}{25} \quad \Longrightarrow \quad
\cos A = \pm \frac35$$

Di sinilah keterangan "lancip" dipakai: untuk sudut lancip $\cos A > 0$, jadi
$\cos A = \tfrac35$.

**Pakai aturan kosinus.**

$$BC^2 = AB^2 + AC^2 - 2 \cdot AB \cdot AC \cos A = 25 + 64 - 2 \cdot 5 \cdot 8 \cdot \tfrac35$$

$$= 89 - 48 = \boxed{41}$$

### Kalau sudutnya tumpul

Tanpa keterangan lancip, cabang kedua sama sahnya: $\cos A = -\tfrac35$ memberi

$$BC^2 = 89 + 48 = 137$$

Dua segitiga berbeda, sisi $5$ dan $8$ yang sama, luas $16$ yang sama — hanya sudut apitnya
berpelurus. Perhatikan bahwa keduanya benar-benar segitiga: $\sqrt{41} \approx 6{,}40$ dan
$\sqrt{137} \approx 11{,}70$, keduanya memenuhi ketaksamaan segitiga terhadap $5$ dan $8$.

Jadi keterangan "lancip" di soal bukan hiasan. Menghapusnya membuat soalnya punya dua
jawaban, dan itu memang bentuk yang sering muncul di olimpiade: satu kata yang kalau
terlewat mengubah jumlah jawabannya.

### Periksa lewat Heron

Dengan $BC = \sqrt{41}$, keliling setengahnya $s = \dfrac{5 + 8 + \sqrt{41}}{2}$. Perhitungan
Heron langsung berantakan, jadi pakai bentuk yang setara dan lebih ramah — **rumus Heron
dalam bentuk kuadrat**:

$$16 L^2 = 2a^2b^2 + 2b^2c^2 + 2c^2a^2 - a^4 - b^4 - c^4$$

Dengan $a = BC$, $a^2 = 41$, $b = 8$, $c = 5$:

$$2(41)(64) + 2(64)(25) + 2(25)(41) - 41^2 - 8^4 - 5^4$$

$$= 5248 + 3200 + 2050 - 1681 - 4096 - 625 = 4096$$

$$L^2 = \frac{4096}{16} = 256 \quad \Longrightarrow \quad L = 16 \quad ✓$$

Bentuk kuadrat ini berguna justru saat salah satu sisinya berbentuk akar: seluruh
perhitungannya cuma menyentuh $a^2$, tidak pernah $a$.

### Yang membuat soal ini bukan soal aturan kosinus biasa

Aturan kosinus di langkah terakhir cuma penutup. Yang dilatih soal ini adalah **rantai
luas → $\sin$ → $\cos$**, dan satu-satunya tempat yang bisa salah adalah pemilihan tanda di
tengah rantai itu.

Pola yang sama muncul tiap kali soal memberi luas dan menanyakan panjang, atau sebaliknya.
Kalau soal tidak menyebut lancip atau tumpul, jawablah **kedua** kemungkinannya — itu bukan
kehati-hatian berlebihan, melainkan bagian dari jawaban.
