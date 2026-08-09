---
id: eks-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [ekstremal]
bentuk: isian
kesulitan: 3
jawaban: "4"
---

## Soal

Sebuah graf memiliki $20$ titik, dan setiap titiknya berderajat paling sedikit $3$.

Berapa **paling sedikit** banyaknya titik yang dilalui lintasan terpanjang pada graf itu?

## Petunjuk

- Ambil lintasan terpanjang, lalu perhatikan tetangga-tetangga titik ujungnya.
- Kalau ada tetangga di luar lintasan, lintasan itu bisa diperpanjang — bertentangan dengan pemilihannya.
- Jadi seluruh tetangga titik ujung ada di dalam lintasan. Hitung berapa titik yang dituntutnya.

## Pembahasan

**Ambil lintasan terpanjang** $P: v_1 \to \cdots \to v_m$. Pilihan ini sah karena grafnya
berhingga dan lintasan pasti ada.

**Seluruh tetangga $v_1$ berada di dalam $P$.** Andaikan ada tetangga $u$ di luar; maka
$u \to v_1 \to \cdots \to v_m$ adalah lintasan yang lebih panjang, bertentangan dengan
pemilihan $P$.

**Hitung.** Titik $v_1$ punya paling sedikit $3$ tetangga, seluruhnya berada di dalam $P$
dan seluruhnya berbeda dari $v_1$. Maka

$$m \ \ge\ 3 + 1 = \boxed{4}$$

**Mengapa jawabannya tidak lebih besar.** Soal menanyakan angka **terkecil yang selalu
dijamin**, jadi harus ditunjukkan bahwa $4$ memang bisa terjadi — kalau tidak, jawabannya
mungkin lebih besar.

Ambil graf yang terdiri atas lima salinan $K_4$ yang terpisah satu sama lain. Seluruhnya
$5 \times 4 = 20$ titik, dan tiap titik berderajat tepat $3$. Lintasan terpanjang pada tiap
salinan memuat $4$ titik, dan tidak ada lintasan yang melompat antar-salinan karena keduanya
tidak terhubung.

Jadi ada graf yang memenuhi syarat soal dengan lintasan terpanjang tepat $4$ titik, sehingga
jawabannya tidak bisa dinaikkan.

**Perhatikan angka $20$ tidak berpengaruh pada jawabannya.** Yang menentukan hanyalah derajat
minimumnya. Graf dengan seribu titik yang tiap titiknya berderajat $3$ juga hanya dijamin
punya lintasan berisi $4$ titik — sebab ia bisa saja terpecah menjadi banyak salinan $K_4$.

Mengenali data mana yang tidak menentukan adalah bagian dari mengerjakan soal, dan di sini
kelebihan keterangan itu sengaja dipasang.

**Kalau grafnya dijamin terhubung,** kesimpulannya jauh lebih kuat — tetapi soal ini tidak
menjanjikannya, dan contoh lima salinan $K_4$ di atas menunjukkan mengapa hal itu
menentukan.
