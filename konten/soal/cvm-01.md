---
id: cvm-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ceva-menelaus]
bentuk: isian
kesulitan: 3
jawaban: "9/2"
jawaban_alt: ["4,5", "4.5"]
---

## Soal

Sebuah garis lurus memotong sisi $AB$ segitiga $ABC$ di titik $F$, memotong sisi $AC$ di
titik $E$, lalu memotong perpanjangan sisi $BC$ di titik $D$.

![Segitiga ABC dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, dan puncak A di atas agak ke kiri. Sebuah garis lurus memotong sisi AB di titik F, memotong sisi AC di titik E, lalu diteruskan sampai memotong perpanjangan alas BC di titik D yang berada di luar segitiga, di sebelah kanan C. Bagian garis dari E sampai D dan bagian alas dari C sampai D digambar putus-putus karena keduanya di luar segitiga](segitiga-garis-menelaus.svg)

Diketahui $\dfrac{AF}{FB} = \dfrac{2}{3}$ dan $\dfrac{AE}{EC} = \dfrac{3}{1}$.

Tentukan nilai $\dfrac{BD}{DC}$.

## Petunjuk

- Ketiga titiknya terletak pada **satu garis lurus** yang melintasi segitiga. Teorema mana yang bicara tentang keadaan itu?
- Teorema Menelaus. Bentuk hasil kalinya sama persis dengan Ceva; yang berbeda adalah gambarnya.
- Susun berkeliling: $\dfrac{BD}{DC} \cdot \dfrac{CE}{EA} \cdot \dfrac{AF}{FB} = 1$. Perhatikan bahwa yang diketahui $\dfrac{AE}{EC}$, sedangkan yang dibutuhkan $\dfrac{CE}{EA}$.

## Pembahasan

**Kenali bentuknya.** Ketiga titik $D$, $E$, $F$ terletak pada satu garis lurus yang
melintasi segitiga. Itu Menelaus, bukan Ceva.

**Balik dulu perbandingan yang arahnya tidak sesuai.** Yang diketahui
$\dfrac{AE}{EC} = 3$, sedangkan rumusnya memakai

$$\frac{CE}{EA} = \frac{1}{3}$$

Langkah kecil ini yang paling sering terlewat, dan akibatnya jawabannya meleset dengan
faktor $9$.

**Terapkan Menelaus.**

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$

$$\frac{BD}{DC} \cdot \frac{1}{3} \cdot \frac{2}{3} = 1$$

$$\frac{BD}{DC} \cdot \frac{2}{9} = 1 \quad \Longrightarrow \quad \frac{BD}{DC} = \boxed{\frac92}$$

### Periksa bahwa $D$ memang di luar

Angka $\tfrac92$ sendiri tidak memberitahu letak $D$ — perbandingan tanpa tanda tidak
membedakan "di dalam" dari "di luar". Yang memberitahunya gambar, dan gambarnya menaruh $D$
di seberang $C$.

Dengan letak itu, $BD - DC = BC$. Dari $BD = 4{,}5\,DC$:

$$4{,}5\,DC - DC = BC \quad \Longrightarrow \quad DC = \tfrac{2}{7}BC, \qquad
BD = \tfrac{9}{7}BC$$

Perhatikan $BD = \tfrac97 BC > BC$ ✓ — memang lebih panjang daripada sisinya, persis seperti
yang harus terjadi kalau $D$ ada di luar. Kalau perhitunganmu memberi $BD < BC$, letak $D$
yang kamu pakai tidak cocok dengan gambarnya.

Kalau dihitung bertanda, hasil kali ketiganya $-1$, dan tanda negatif itulah yang mengumumkan
bahwa tepat satu di antara ketiga titik jatuh di perpanjangan.

### Kenapa tidak mungkin ketiganya di dalam

Menelaus tidak pernah bisa terjadi dengan ketiga titik di dalam sisi-sisinya. Alasannya bisa
dilihat tanpa rumus: sebuah garis lurus membagi bidang jadi dua sisi. Ketiga titik sudut
segitiga tersebar di kedua sisi itu — tidak mungkin ketiganya di satu sisi, sebab garisnya
memotong segitiga.

Jadi salah satu sisi memuat satu titik sudut, dan yang lain memuat dua. Sisi segitiga yang
kedua ujungnya berada di **bagian yang sama** tidak dipotong garisnya, jadi titik potongnya
jatuh di perpanjangan. Selalu ada tepat satu sisi seperti itu — atau tiga, kalau garisnya
lewat di luar segitiga sama sekali.

### Bandingkan dengan Ceva

Kedua teorema menuliskan hasil kali yang **sama persis**:

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB}$$

Kalau panjangnya tidak bertanda, keduanya bernilai $1$, dan yang membedakan tinggal
gambarnya: ruas dari titik sudut yang konkuren (Ceva), atau satu garis lurus yang melintas
(Menelaus).

Karena itu langkah pertama pada soal semacam ini bukan menulis rumus, melainkan **membaca
gambarnya** dan memutuskan yang mana. Rumus yang benar dengan gambar yang salah baca tetap
memberi jawaban yang salah.
