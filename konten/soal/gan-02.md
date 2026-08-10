---
id: gan-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-analitik]
bentuk: isian
kesulitan: 2
jawaban: "14/5"
jawaban_alt: ["2,8", "2.8"]
---

## Soal

Tentukan jarak dari titik $(7, 3)$ ke garis $3x - 4y + 5 = 0$.

Tulis jawabanmu sebagai pecahan atau desimal.

## Petunjuk

- Jarak dari titik ke garis selalu diukur tegak lurus, bukan sembarang arah.
- Ada rumus langsung untuk itu, dan ia memerlukan persamaan garisnya dalam bentuk $ax + by + c = 0$ — bentuk yang sudah diberikan soal.
- Perhatikan nilai mutlaknya di pembilang, dan $\sqrt{a^2+b^2}$ di penyebut.

## Pembahasan

**Kenali $a$, $b$, $c$.** Dari $3x - 4y + 5 = 0$:

$$a = 3, \qquad b = -4, \qquad c = 5$$

**Masukkan ke rumus jarak.**

$$d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2+b^2}}
= \frac{|3(7) + (-4)(3) + 5|}{\sqrt{3^2 + (-4)^2}}$$

$$= \frac{|21 - 12 + 5|}{\sqrt{25}} = \frac{14}{5} = \boxed{\frac{14}{5}} = 2{,}8$$

### Mengapa nilai mutlaknya wajib

Tanpa nilai mutlak, hasilnya bisa negatif — dan jarak negatif tidak ada artinya. Tandanya
sebenarnya membawa keterangan: ia memberitahu **di sisi mana** titik itu berada terhadap
garisnya. Titik di sisi berlawanan memberi tanda yang berlawanan.

Keterangan itu berguna di soal lain (misalnya memeriksa dua titik berada di sisi yang sama),
tetapi untuk jarak, nilai mutlaknya wajib.

### Periksa tanpa rumus

Garis $3x - 4y + 5 = 0$ punya gradien $\tfrac{3}{4}$, sehingga garis tegak lurusnya bergradien
$-\tfrac{4}{3}$. Lewat $(7,3)$:

$$y - 3 = -\tfrac{4}{3}(x - 7) \quad \Longrightarrow \quad 4x + 3y = 37$$

Selesaikan bersama $3x - 4y = -5$: dari kedua persamaan didapat kaki tegak lurusnya

$$\left(\frac{133}{25}, \frac{131}{25}\right)$$

Jaraknya

$$\sqrt{\left(7 - \tfrac{133}{25}\right)^2 + \left(3 - \tfrac{131}{25}\right)^2}
= \sqrt{\left(\tfrac{42}{25}\right)^2 + \left(-\tfrac{56}{25}\right)^2}
= \frac{\sqrt{1764 + 3136}}{25} = \frac{\sqrt{4900}}{25} = \frac{70}{25} = \frac{14}{5} \quad ✓$$

Perhatikan berapa panjang jalan kedua ini dibanding rumusnya. Itulah gunanya rumus jarak ke
garis: ia memampatkan seluruh pekerjaan mencari kaki tegak lurus menjadi satu baris.

### Bentuk garisnya harus benar dulu

Rumus ini menuntut ruas kanan **nol**. Untuk garis yang diberikan sebagai $y = 2x + 7$, ubah
dulu menjadi $2x - y + 7 = 0$ sebelum memakai rumusnya. Memasukkan koefisien dari bentuk
$y = mx + c$ apa adanya adalah kekeliruan yang paling sering di jurus ini.

Satu kegunaan penting: **jarak dari pusat lingkaran ke sebuah garis** menentukan garis itu
memotong ($d < r$), menyinggung ($d = r$), atau tidak menyentuh lingkaran ($d > r$) — tanpa
menyelesaikan persamaan kuadrat apa pun.
