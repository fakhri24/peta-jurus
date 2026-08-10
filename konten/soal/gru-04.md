---
id: gru-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-ruang]
bentuk: isian
kesulitan: 3
jawaban: "36"
---

## Soal

Kubus $ABCD.EFGH$ mempunyai rusuk $6$.

![Kubus ABCD titik EFGH dengan alas ABCD di bawah dan tutup EFGH di atas, E tepat di atas A. Rusuk yang tersembunyi di belakang digambar putus-putus. Segitiga BDE diarsir, membentuk bidang miring limas berpojok di A dengan ketiga rusuk AB, AD, dan AE saling tegak lurus](kubus-limas-sudut.svg)

Tentukan volume limas yang titik sudutnya $A$, $B$, $D$, dan $E$.

## Petunjuk

- Volume limas adalah sepertiga luas alas kali tinggi. Pilih alas dan tinggi yang membuat keduanya **tidak perlu dicari** — sudah tersedia sebagai rusuk kubus.
- Ketiga rusuk yang bertemu di $A$ — yaitu $AB$, $AD$, dan $AE$ — saling tegak lurus.
- Ambil $\triangle ABD$ sebagai alas; tingginya kemudian adalah $AE$ sendiri.

## Pembahasan

**Pilih alas yang menguntungkan.** Ambil $\triangle ABD$ sebagai alas. Ia terletak pada bidang
alas kubus, dan siku-siku di $A$ dengan kedua sisi siku-sikunya rusuk kubus:

$$[ABD] = \tfrac{1}{2} \times AB \times AD = \tfrac{1}{2} \times 6 \times 6 = 18$$

**Tingginya sudah tersedia.** Rusuk $AE$ tegak lurus bidang alas kubus, jadi ia tegak lurus
bidang $ABD$. Maka $AE$ **adalah** tinggi limas itu — tidak ada yang perlu dihitung:

$$t = AE = 6$$

**Hitung volumenya.**

$$V = \tfrac{1}{3} \times [ABD] \times AE = \tfrac{1}{3} \times 18 \times 6 = \boxed{36}$$

### Bentuk umumnya

Untuk limas yang ketiga rusuknya di satu pojok saling tegak lurus dengan panjang $p$, $q$, $r$:

$$V = \tfrac{1}{6}\,pqr$$

Di sini $\tfrac16 \times 6^3 = 36$ ✓. Bandingkan dengan volume kubusnya, $216$: limas pojok itu
tepat **seperenam** kubus.

### Memilih alas yang salah membuatnya jauh lebih sulit

Kalau $\triangle BDE$ dipilih sebagai alas, tingginya adalah jarak dari $A$ ke bidang $BDE$ —
besaran yang tidak tersedia dan harus dicari lebih dulu. Volumenya tetap $36$, tentu saja, dan
justru itu yang memberi jalan menghitung jaraknya:

$$BD = BE = DE = 6\sqrt2 \quad \Longrightarrow \quad
[BDE] = \frac{\sqrt3}{4}\left(6\sqrt2\right)^2 = 18\sqrt3$$

$$\text{jarak } A \text{ ke bidang } BDE = \frac{3V}{[BDE]}
= \frac{108}{18\sqrt3} = \frac{6}{\sqrt3} = 2\sqrt3$$

**Menghitung volume yang sama dengan dua alas berbeda** inilah cara baku mencari jarak titik ke
bidang — dan ia menghindari seluruh pekerjaan menggambar garis tegak lurus dalam ruang.

### Urutan yang benar

Perhatikan urutannya: **volume dulu lewat alas yang mudah, baru jarak lewat alas yang sulit.**
Mengerjakannya terbalik berarti mencari jarak titik ke bidang tanpa alat apa pun, dan itu jauh
lebih panjang.

Kebiasaan itu berlaku untuk limas mana pun, bukan hanya di kubus: kalau salah satu alasnya
membuat tinggi tersedia gratis, mulailah dari sana.
