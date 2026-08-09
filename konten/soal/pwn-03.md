---
id: pwn-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [pewarnaan]
bentuk: uraian
kesulitan: 4
---

## Soal

Dari papan catur $8 \times 8$ dibuang dua petak di sudut yang **berdekatan** — misalnya
$(1,1)$ dan $(1,8)$, keduanya pada baris teratas. Tersisa $62$ petak.

Tunjukkan bahwa sisa papan itu **dapat** ditutup seluruhnya oleh $31$ domino $1 \times 2$,
dan jelaskan mengapa pewarnaan papan catur tidak dapat dipakai untuk menjawab soal ini.

## Petunjuk

- Hitung dulu warna kedua petak yang dibuang. Apakah keduanya sewarna?
- Kalau hitungan warnanya cocok, pewarnaan tidak menutup apa pun — dan soal jenis ini hanya bisa dijawab dengan memberikan penutupannya.
- Untuk menyusun penutupannya, perhatikan baris teratas terpisah dari enam baris di bawahnya.

## Pembahasan

### Mengapa pewarnaan tidak menjawab soal ini

Warnai menurut paritas $i+j$. Petak $(1,1)$ punya $i+j = 2$ dan petak $(1,8)$ punya
$i+j = 9$ — berbeda paritas, sehingga **berlainan warna**.

Setelah keduanya dibuang, sisa papan punya

$$32 - 1 = 31 \text{ petak hitam}, \qquad 32 - 1 = 31 \text{ petak putih}$$

Penutupan dengan $31$ domino menuntut tepat $31$ petak tiap warna. Persediaannya cocok
persis, sehingga **pewarnaan tidak menutup kemungkinan apa pun.**

Itu bukan berarti penutupannya ada. Hitungan warna yang cocok hanya berarti tidak ada
halangan dari arah itu; halangan lain bisa saja tetap ada. Karena itu satu-satunya cara
menjawab adalah **memberikan penutupannya**.

### Penutupannya

Bagi papannya menjadi dua bagian.

**Baris teratas.** Kedua ujungnya sudah dibuang, sehingga tersisa petak $(1,2)$ sampai
$(1,7)$ — yaitu $6$ petak berjajar. Tutup dengan $3$ domino mendatar:

$$(1,2){-}(1,3), \qquad (1,4){-}(1,5), \qquad (1,6){-}(1,7)$$

**Tujuh baris sisanya.** Baris $2$ sampai $8$ membentuk papan $7 \times 8$ yang utuh. Tutup
tiap baris dengan $4$ domino mendatar, sebab tiap baris berisi $8$ petak:

$$7 \times 4 = 28 \text{ domino}$$

**Jumlahkan.**

$$3 + 28 = 31 \text{ domino}$$

Seluruh $62$ petak tertutup, tidak ada yang bertumpuk, dan tidak ada yang melewati tepi
papan. $\blacksquare$

### Pelajaran yang dibawa soal ini

Bandingkan dengan soal sudut berlawanan:

| Yang dibuang | Warna | Selisih | Kesimpulan |
|---|---|---|---|
| Dua sudut berlawanan | sewarna | $2$ | mustahil — dibuktikan pewarnaan |
| Dua sudut berdekatan | berlainan | $0$ | bisa — dibuktikan konstruksi |

Kedua soal terlihat hampir sama dan hanya berbeda petak mana yang dibuang, tetapi menuntut
**jenis jawaban yang berbeda sama sekali**. Yang pertama dijawab dengan alasan; yang kedua
hanya bisa dijawab dengan contoh.

Kekeliruan yang paling sering pada soal ubin adalah menyimpulkan "bisa" karena hitungan
warnanya cocok. Invarian — dan pewarnaan adalah invarian yang dipilih sengaja — hanya pernah
membuktikan **tidak mungkin**.

### Catatan lanjutan

Untuk papan $8\times8$, kenyataannya lebih kuat daripada yang dibuktikan di sini:
**setiap** pembuangan satu petak hitam dan satu petak putih menyisakan papan yang selalu
bisa ditutup, di mana pun kedua petak itu berada. Membuktikannya menuntut gagasan lain —
bukan pewarnaan, melainkan konstruksi lintasan tertutup yang melewati seluruh papan.

## Rubrik

- Menentukan warna kedua petak yang dibuang lewat paritas $i+j$, dan menyimpulkan keduanya berlainan warna
- Menghitung sisa $31$ petak tiap warna dan menyatakan pewarnaan tidak menutup kemungkinan
- Menyatakan dengan jelas bahwa hitungan warna yang cocok tidak membuktikan penutupannya ada
- Memberikan penutupan yang lengkap dan dapat diperiksa
- Menghitung banyaknya domino pada tiap bagian dan memastikan totalnya $31$
- Menyimpulkan perbedaan jenis jawaban antara soal ini dan soal sudut berlawanan
