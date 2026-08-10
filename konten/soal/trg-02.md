---
id: trg-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [trigonometri-segitiga]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Pada segitiga $ABC$ diketahui $\angle B = 30^\circ$, $\angle C = 45^\circ$, dan
$AB = 6\sqrt{2}$.

Tentukan panjang $AC$.

## Petunjuk

- Yang diketahui dua sudut dan satu sisi. Aturan kosinus butuh dua sisi, jadi ia belum bisa dipakai.
- Aturan sinus memasangkan tiap sisi dengan sudut **di hadapannya**. Sudut mana yang berhadapan dengan $AC$, dan sudut mana dengan $AB$?
- $AC$ berhadapan dengan $\angle B$, dan $AB$ berhadapan dengan $\angle C$.

## Pembahasan

**Pasangkan sisi dengan sudut di hadapannya.** Ini seluruh isi soal ini:

- $AC$ berhadapan dengan $\angle B = 30^\circ$;
- $AB$ berhadapan dengan $\angle C = 45^\circ$.

**Pakai aturan sinus.**

$$\frac{AC}{\sin B} = \frac{AB}{\sin C}$$

$$AC = AB \cdot \frac{\sin B}{\sin C} = 6\sqrt2 \cdot \frac{\sin 30^\circ}{\sin 45^\circ}
= 6\sqrt2 \cdot \frac{1/2}{\sqrt2/2} = 6\sqrt2 \cdot \frac{1}{\sqrt2} = \boxed{6}$$

### Periksa lewat urutan panjangnya

Sudut ketiga adalah $\angle A = 180^\circ - 30^\circ - 45^\circ = 105^\circ$, jadi
segitiganya tumpul di $A$. Urutan sudutnya

$$\angle B\ (30^\circ) \ <\ \angle C\ (45^\circ)\ <\ \angle A\ (105^\circ)$$

harus diikuti urutan sisi di hadapannya:

$$AC\ (6) \ <\ AB\ (6\sqrt2 \approx 8{,}49)\ <\ BC$$

Cocok ✓. Sisi terpanjangnya $BC = 2R \sin 105^\circ \approx 11{,}59$, memang paling besar.

Pemeriksaan "sudut terbesar berhadapan dengan sisi terpanjang" murah sekali dan menangkap
hampir semua kesalahan pemasangan pada aturan sinus.

### Sekalian: jari-jari lingkaran luarnya

Bentuk lengkap aturan sinus memuat $2R$:

$$2R = \frac{AB}{\sin C} = \frac{6\sqrt2}{\sqrt2/2} = 12 \quad \Longrightarrow \quad R = 6$$

Jadi tiap sisi bisa dihitung sekaligus tanpa perbandingan bertingkat:

$$AC = 2R \sin B = 12 \cdot \tfrac12 = 6 \quad ✓$$

$$BC = 2R \sin A = 12 \sin 105^\circ \approx 11{,}59$$

Memakai $2R$ sebagai perantara sering lebih rapi daripada memasangkan dua sisi sekaligus,
terutama kalau yang diminta lebih dari satu sisi.

### Kenapa soal ini tidak punya kasus mendua

Aturan sinus bisa memberi dua segitiga kalau yang diketahui **dua sisi dan sudut yang tidak
diapitnya**. Di sini yang diketahui dua **sudut** dan satu sisi, jadi sudut ketiganya
tertentu, dan bentuk segitiganya tertentu sampai ukuran. Tidak ada cabang kedua yang perlu
diperiksa.

Bedakan baik-baik: yang menimbulkan kemenduaan bukan aturan sinusnya, melainkan susunan
keterangan yang diberikan soal.
