---
id: sdl-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [sudut-lingkaran]
bentuk: uraian
kesulitan: 2
---

## Soal

Ruas $AB$ adalah diameter sebuah lingkaran berpusat $O$, dan $C$ sebarang titik pada keliling
lingkaran selain $A$ dan $B$.

Buktikan bahwa $\angle ACB = 90^\circ$.

## Petunjuk

- Gambarnya masih kurang satu ruas. Tambahkan ruas yang menghubungkan $C$ dengan titik yang paling banyak diketahui sifatnya.
- Tarik $OC$. Sekarang ada dua segitiga, dan keduanya punya sifat yang sama karena $OA$, $OB$, $OC$ semuanya jari-jari.
- Namai $\angle OAC = \alpha$ dan $\angle OBC = \beta$, lalu terapkan jumlah sudut pada $\triangle ABC$.

## Pembahasan

**Tarik garis bantu $OC$.** Tanpa ruas ini gambar hanya memuat satu segitiga dan tidak ada yang
bisa dipakai. Dengan ruas ini, $\triangle ABC$ terbelah menjadi $\triangle OAC$ dan
$\triangle OBC$ — dan keduanya sama kaki, sebab

$$OA = OB = OC$$

ketiganya jari-jari lingkaran yang sama.

**Namai kedua sudut alasnya.** Pada $\triangle OAC$ yang sama kaki dengan $OA = OC$:

$$\angle OCA = \angle OAC = \alpha$$

Pada $\triangle OBC$ yang sama kaki dengan $OB = OC$:

$$\angle OCB = \angle OBC = \beta$$

**Susun ketiga sudut $\triangle ABC$.** Karena $O$ terletak pada ruas $AB$, sinar $CA$ dan
$CB$ mengapit $CO$, sehingga

$$\angle ACB = \angle ACO + \angle OCB = \alpha + \beta$$

Sedangkan $\angle CAB = \alpha$ dan $\angle CBA = \beta$. Jumlah sudut $\triangle ABC$ memberi

$$\alpha + \beta + (\alpha + \beta) = 180^\circ$$

$$2(\alpha + \beta) = 180^\circ \quad \Longrightarrow \quad \alpha + \beta = 90^\circ$$

Karena $\angle ACB = \alpha + \beta$, maka

$$\angle ACB = 90^\circ \qquad \blacksquare$$

### Bentuk buktinya layak diperhatikan

Perhatikan bahwa $\alpha$ dan $\beta$ **tidak pernah dicari satu per satu** — dan memang tidak
bisa, sebab keduanya berubah-ubah seiring bergesernya $C$. Yang tidak berubah adalah
jumlahnya. Seluruh bukti bersandar pada kenyataan itu.

Pola "yang muncul cuma jumlahnya, jadi jangan mencari sukunya" ini akan terpakai berulang kali
di soal geometri yang jauh lebih panjang.

### Yang membuat buktinya berlaku untuk setiap letak $C$

Tidak ada satu langkah pun yang memakai letak $C$ secara khusus — tidak ada "andaikan $C$ di
atas $AB$", tidak ada pengukuran. Yang dipakai cuma bahwa $OC$ jari-jari. Karena itu
kesimpulannya berlaku untuk **setiap** titik pada keliling, di busur atas maupun busur bawah.

Satu-satunya yang perlu diperiksa adalah $C \ne A$ dan $C \ne B$: di kedua titik itu
$\triangle ABC$ tidak terbentuk sama sekali. Soal sudah menyebutnya, dan penyebutan semacam itu
bukan kelebihan kata — ia menutup satu-satunya kasus yang gagal.

### Kegunaannya dibalik

Yang baru saja dibuktikan sering dipakai dari arah sebaliknya: **kalau kamu melihat sudut
siku-siku, curigai ada lingkaran.** Titik siku-siku selalu terletak pada lingkaran yang
berdiameter sisi miringnya.

Kecurigaan itu yang membuka banyak soal olimpiade — terutama ketika ada **dua** sudut siku-siku
yang menghadap ruas yang sama, sebab keempat titiknya lalu terletak pada satu lingkaran.

## Rubrik

- Menarik $OC$ sebagai garis bantu
- Menyebut $OA = OB = OC$ dengan alasan ketiganya jari-jari
- Menyatakan $\triangle OAC$ dan $\triangle OBC$ sama kaki, lalu menamai kedua pasang sudut alasnya
- Menyatakan $\angle ACB = \alpha + \beta$ dengan alasan $O$ pada ruas $AB$
- Menerapkan jumlah sudut $\triangle ABC$ dan sampai pada $2(\alpha+\beta) = 180^\circ$
- Menyimpulkan $\angle ACB = 90^\circ$ tanpa mencari $\alpha$ dan $\beta$ satu per satu
