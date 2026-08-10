---
id: trg-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [trigonometri-segitiga]
bentuk: isian
kesulitan: 4
jawaban: "16/65"
jawaban_alt: ["0,246153846", "0.246153846"]
---

## Soal

Pada segitiga $ABC$ diketahui $\sin A = \dfrac{3}{5}$ dan $\cos B = \dfrac{5}{13}$.

Tentukan nilai $\cos C$.

## Petunjuk

- Ketiga sudut segitiga tidak bebas: jumlahnya tetap. Nyatakan $C$ dengan $A$ dan $B$.
- Dari $A + B + C = 180^\circ$ diperoleh $C = 180^\circ - (A+B)$, sehingga $\cos C = -\cos(A+B)$.
- Nilai $\sin A = \tfrac35$ dipenuhi oleh sudut lancip **dan** sudut tumpul. Periksa kedua kemungkinannya, dan buang yang membuat jumlah ketiga sudutnya melampaui $180^\circ$.

## Pembahasan

**Pakai hubungan yang berlaku pada setiap segitiga.** Karena $A + B + C = 180^\circ$:

$$\cos C = \cos\left(180^\circ - (A+B)\right) = -\cos(A+B)$$

$$= -\left(\cos A \cos B - \sin A \sin B\right) = \sin A \sin B - \cos A \cos B$$

**Lengkapi nilai yang belum ada.** Dari $\cos B = \tfrac{5}{13}$ dan $B$ sudut segitiga
(jadi $0 < B < 180^\circ$, sehingga $\sin B > 0$):

$$\sin B = \sqrt{1 - \tfrac{25}{169}} = \sqrt{\tfrac{144}{169}} = \frac{12}{13}$$

Untuk $\cos A$ tandanya belum tentu:

$$\cos A = \pm\sqrt{1 - \tfrac{9}{25}} = \pm\frac45$$

**Buang cabang yang tidak mungkin.** Ini inti soalnya.

Karena $\cos B = \tfrac{5}{13} > 0$, sudut $B$ lancip, dan $B \approx 67{,}38^\circ$.

- Kalau $A$ tumpul, maka $\cos A = -\tfrac45$ dan $A \approx 143{,}13^\circ$. Jumlahnya
  $A + B \approx 210{,}5^\circ > 180^\circ$ — **mustahil**, karena tidak menyisakan ruang
  bagi $C$.
- Jadi $A$ lancip dan $\cos A = \tfrac45$, dengan $A \approx 36{,}87^\circ$.

**Hitung.**

$$\cos C = \frac{3}{5}\cdot\frac{12}{13} - \frac{4}{5}\cdot\frac{5}{13}
= \frac{36}{65} - \frac{20}{65} = \boxed{\frac{16}{65}}$$

### Periksa

Dengan $A \approx 36{,}87^\circ$ dan $B \approx 67{,}38^\circ$:

$$C \approx 180^\circ - 36{,}87^\circ - 67{,}38^\circ = 75{,}75^\circ$$

$$\cos 75{,}75^\circ \approx 0{,}2462, \qquad \frac{16}{65} \approx 0{,}2462 \quad ✓$$

Nilainya positif, jadi $C$ lancip — ketiga sudutnya lancip, dan itu konsisten dengan
$A + B < 180^\circ$ yang tadi dipakai.

### Cara membuang cabang tanpa kalkulator

Menyebut $143^\circ$ butuh nilai hampiran, dan di lembar jawaban itu kurang rapi. Ada
alasan yang murni:

Andaikan $A$ tumpul, jadi $\cos A = -\tfrac45$. Hitung $\sin(A+B)$:

$$\sin(A+B) = \sin A\cos B + \cos A \sin B
= \frac{3}{5}\cdot\frac{5}{13} - \frac{4}{5}\cdot\frac{12}{13}
= \frac{15}{65} - \frac{48}{65} = -\frac{33}{65}$$

Hasilnya **negatif**. Padahal $A + B = 180^\circ - C$ dengan $0^\circ < C < 180^\circ$,
sehingga $0^\circ < A+B < 180^\circ$ — dan sinus pada selang itu selalu positif. Cabang $A$
tumpul karena itu gugur, tanpa satu pun bilangan berkoma.

### Kenapa hanya $\sin A$ yang bermasalah

Perhatikan bentuk keterangannya. Yang diberikan untuk $B$ adalah **kosinus**, dan pada
selang $0^\circ$ sampai $180^\circ$ kosinus bernilai berbeda-beda untuk tiap sudut: satu
nilai kosinus menentukan satu sudut, tanpa cabang.

Sinus tidak begitu: $\sin\theta = \sin(180^\circ - \theta)$, jadi satu nilai sinus selalu
menunjuk dua sudut yang mungkin. Itu sebabnya aturan sinus melahirkan kasus mendua
sementara aturan kosinus tidak pernah.

Aturan praktisnya: **keterangan berupa sinus selalu bercabang dua, keterangan berupa
kosinus tidak pernah.** Kalau soal memberi sinus, cabangnya wajib diperiksa — kadang
keduanya sah, dan jawabannya jadi dua.
