---
id: ind-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [induksi]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa $2^n > n$ untuk setiap bilangan asli $n$.

## Petunjuk

- Pernyataannya berlaku untuk setiap $n$, dan bentuk untuk $n+1$ bisa disusun dari bentuk untuk $n$ — meski yang dibandingkan pertidaksamaan, bukan kesamaan.
- Basis: periksa $n = 1$.
- Langkah induksi: dari $2^k > k$, kalikan dengan $2$ untuk memperoleh $2^{k+1} > 2k$. Lalu tinggal ditunjukkan $2k \ge k+1$.

## Pembahasan

### Basis

Untuk $n = 1$: $2^1 = 2 > 1$. Benar.

### Langkah induksi

Andaikan benar untuk $n = k$, yaitu

$$2^k > k$$

Akan ditunjukkan $2^{k+1} > k+1$.

**Kalikan hipotesis dengan $2$.** Karena $2 > 0$, arah pertidaksamaannya tidak berubah:

$$2^{k+1} = 2 \cdot 2^k > 2k$$

**Hubungkan $2k$ dengan $k+1$.** Untuk setiap bilangan asli $k \ge 1$,

$$2k - (k+1) = k - 1 \ \ge\ 0 \quad\Longrightarrow\quad 2k \ \ge\ k+1$$

**Rangkaikan keduanya.**

$$2^{k+1} > 2k \ \ge\ k+1$$

sehingga $2^{k+1} > k+1$.

### Kesimpulan

Basis benar dan langkah induksinya berlaku, jadi $2^n > n$ untuk setiap bilangan asli $n$.
$\blacksquare$

**Dua hal yang layak diperhatikan.**

Pertama, langkah induksi pada pertidaksamaan hampir selalu berbentuk rangkaian: dari
hipotesis diperoleh satu batas, lalu batas itu dibandingkan dengan yang diinginkan. Kedua
perbandingan disambung dengan tanda yang searah.

Kedua, perhatikan bahwa satu tanda tegas ($>$) dan satu tanda tidak tegas ($\ge$)
disambung menjadi tanda tegas. Itu sah: kalau $a > b$ dan $b \ge c$, maka $a > c$. Kalau
keduanya tidak tegas, kesimpulannya juga tidak tegas — dan pada soal yang menuntut
ketegasan, perbedaan itu menentukan.

Perhatikan pula bahwa $2k \ge k+1$ menjadi kesamaan tepat di $k=1$. Di situlah batas
argumennya paling ketat, dan itu sebabnya basisnya harus $n = 1$ dan bukan yang lain.

## Rubrik

- Memeriksa basis pada $n = 1$
- Menuliskan hipotesis induksi $2^k > k$ secara eksplisit
- Mengalikan hipotesis dengan $2$, dan menyebut bahwa arah tidak berubah karena pengalinya positif
- Membuktikan $2k \ge k+1$ untuk $k \ge 1$, bukan menyatakannya begitu saja
- Merangkaikan kedua pertidaksamaan menjadi $2^{k+1} > k+1$
