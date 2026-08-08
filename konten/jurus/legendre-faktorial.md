---
id: legendre-faktorial
nama: Pangkat Prima dalam Faktorial
pilar: teori-bilangan
tahap: osn-p
prasyarat: [bilangan-prima]
contoh: []
latihan: []
---

## Kapan dipakai

Soal menanyakan **berapa banyak nol di belakang** $n!$, atau pangkat tertinggi suatu prima
yang membagi faktorial atau koefisien binomial.

## Intinya

Rumus Legendre: pangkat prima $p$ dalam $n!$ adalah

$$v_p(n!) = \left\lfloor \frac{n}{p} \right\rfloor + \left\lfloor \frac{n}{p^2} \right\rfloor
+ \left\lfloor \frac{n}{p^3} \right\rfloor + \cdots$$

Jumlahnya berhenti sendiri begitu $p^k > n$.

Cara membacanya: suku pertama mencacah kelipatan $p$, suku kedua menambahkan satu lagi
untuk kelipatan $p^2$ (yang menyumbang dua faktor $p$), dan seterusnya. Tidak ada yang
terhitung dua kali — tiap bilangan disumbangkan sebanyak pangkat $p$ di dalamnya.

Untuk banyaknya nol di belakang $n!$, yang dicari adalah $v_5(n!)$ — bukan $v_2$. Nol
lahir dari pasangan $2 \times 5$, dan faktor $2$ selalu jauh lebih berlimpah, jadi $5$
yang menjadi penghambatnya.

## Jebakan umum

- **Berhenti di suku pertama.** $v_5(100!) = 20 + 4 = 24$, bukan $20$. Kelipatan $25$
  menyumbang dua kali.
- **Menghitung $v_2$ untuk soal nol di belakang.** Yang langka itu $5$.
- **Membulatkan, bukan membuang.** $\lfloor \cdot \rfloor$ selalu ke bawah.
