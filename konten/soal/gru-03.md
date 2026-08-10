---
id: gru-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-ruang]
bentuk: isian
kesulitan: 2
jawaban: "2/3"
---

## Soal

Sebuah bola tepat muat di dalam sebuah tabung: bola itu menyinggung alas tabung, tutupnya, dan
seluruh selimutnya.

Tentukan perbandingan volume bola terhadap volume tabung. Tulis jawabanmu sebagai pecahan.

## Petunjuk

- Ukuran tabungnya tidak diberikan, dan memang tidak perlu — yang ditanyakan perbandingan. Namai jari-jari bolanya $r$ dan nyatakan ukuran tabungnya dalam $r$.
- Karena bola menyinggung selimut tabung, jari-jari tabung sama dengan $r$. Karena ia menyinggung alas dan tutup, tinggi tabung sama dengan $2r$.
- Bandingkan $\tfrac{4}{3}\pi r^3$ dengan $\pi r^2 \times 2r$.

## Pembahasan

**Nyatakan ukuran tabung dalam $r$.** Sebut jari-jari bola $r$.

- Bola menyinggung selimut tabung, jadi jari-jari tabung juga $r$.
- Bola menyinggung alas dan tutup, jadi tinggi tabung $2r$ — yaitu diameter bola.

**Hitung kedua volumenya.**

$$V_{\text{bola}} = \tfrac{4}{3}\pi r^3$$

$$V_{\text{tabung}} = \pi r^2 \times t = \pi r^2 \times 2r = 2\pi r^3$$

**Bandingkan.**

$$\frac{V_{\text{bola}}}{V_{\text{tabung}}} = \frac{\tfrac{4}{3}\pi r^3}{2\pi r^3}
= \frac{4}{3} \times \frac{1}{2} = \boxed{\frac{2}{3}}$$

### Perhatikan apa yang lenyap

Baik $\pi$ maupun $r^3$ hilang saat dibagi. Karena itu jawabannya **tidak bergantung pada
ukuran** — bola sebesar apa pun di dalam tabungnya yang pas mengisi tepat dua pertiganya.

Setiap kali soal menanyakan perbandingan dan tidak memberi ukuran, itu isyarat kuat bahwa
ukurannya memang akan lenyap. Menamai satu peubah lalu membiarkannya saling meniadakan adalah
langkah yang benar, bukan tanda kekurangan data.

### Penemuan yang diminta Archimedes untuk dipahat di nisannya

Perbandingan $2 : 3$ ini ditemukan Archimedes, dan menurut riwayat ia meminta gambar bola di
dalam tabung dipahat di makamnya. Ada satu lagi yang menyertainya, dan sama rapinya:

$$\frac{L_{\text{bola}}}{L_{\text{tabung, seluruhnya}}}
= \frac{4\pi r^2}{2\pi r^2 + 2\pi r \times 2r} = \frac{4\pi r^2}{6 \pi r^2} = \frac{2}{3}$$

Perbandingan **luas permukaannya juga $2 : 3$** — angka yang sama, meski yang satu berdimensi
tiga dan yang lain berdimensi dua. Itu kebetulan yang tidak berlaku umum, dan justru itu yang
membuatnya layak diingat.

### Sisa ruangnya

Ruang di dalam tabung yang tidak terisi bola adalah sepertiga volume tabung, yaitu

$$\tfrac{1}{3} \times 2\pi r^3 = \tfrac{2}{3}\pi r^3$$

yang kebetulan sama dengan volume **dua kerucut** berjari-jari $r$ dan bertinggi $r$. Kenyataan
itu bukan kebetulan — ia inti cara Archimedes menurunkan volume bola, jauh sebelum ada kalkulus.
