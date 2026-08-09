---
id: permutasi
nama: Permutasi
pilar: kombinatorika
tahap: osn-k
prasyarat: [aturan-pencacahan]
contoh: [pm-contoh-1]
latihan: [pm-01, pm-02, pm-03, pm-04, pm-05, pm-06]
---

## Kapan dipakai

Objeknya **berbeda semua**, **urutan penting**, dan kamu menyusun sebagian atau seluruhnya
berjajar. Uji cepatnya: kalau menukar dua objek terpilih menghasilkan susunan yang dihitung
**berbeda**, ini permutasi.

Kata yang biasa muncul: disusun, dijajar, diurutkan, juara 1–2–3, sandi yang urutannya
berarti.

## Intinya

Menyusun $k$ objek dari $n$ objek berbeda:

$$P(n,k) = n(n-1)(n-2)\cdots(n-k+1) = \frac{n!}{(n-k)!}$$

Menyusun seluruhnya, $k = n$, memberi $n!$.

Rumus itu tidak perlu dihafal terpisah — ia hanya aturan kali dengan pilihan yang menyusut:
tempat pertama punya $n$ calon, tempat kedua $n-1$ karena satu sudah terpakai, dan
seterusnya sampai $k$ tempat terisi.

Dua nilai yang harus otomatis: $0! = 1$ dan $P(n,0) = 1$. Keduanya masuk akal karena ada
tepat satu cara memilih tidak satu pun.

**Susunan dengan pembatasan** dikerjakan dengan mendahulukan yang paling terkekang. Kalau
dua objek harus berdampingan, ikat keduanya jadi satu blok lalu kalikan dengan susunan di
dalam blok itu.

## Jebakan umum

- **Memakai permutasi padahal urutannya tidak berarti.** Kalau yang diminta "pilih 3 orang
  jadi anggota tim", menukar dua nama tidak menghasilkan tim baru.
- **Mengira $0! = 0$.** Nilainya $1$, dan itu bukan kesepakatan kosong — dengan itu rumusnya
  tetap benar di ujung.
- **Menghitung objek yang identik sebagai berbeda.** Dua huruf A pada satu kata tidak bisa
  dibedakan, jadi $n!$ akan kelebihan.
