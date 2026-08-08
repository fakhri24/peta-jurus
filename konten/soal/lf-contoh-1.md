---
id: lf-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [legendre-faktorial]
bentuk: isian
kesulitan: 2
jawaban: "24"
---

## Soal

Berapa banyak angka nol berurutan di ujung kanan $100!$?

## Petunjuk

- Nol di ujung lahir dari faktor $10$. Pecah $10$ atas prima, lalu tanyakan mana yang lebih langka.
- $10 = 2 \times 5$. Faktor $2$ jauh lebih berlimpah daripada $5$ di dalam faktorial, jadi banyaknya nol ditentukan oleh $5$.
- Pakai rumus Legendre: $v_5(100!) = \lfloor 100/5 \rfloor + \lfloor 100/25 \rfloor + \cdots$

## Pembahasan

Setiap nol di ujung kanan berasal dari satu faktor $10 = 2 \times 5$. Jadi banyaknya nol
sama dengan banyaknya pasangan $2$–$5$ yang bisa dibentuk, yaitu

$$\min\left(v_2(100!),\ v_5(100!)\right)$$

Kelipatan $2$ jauh lebih rapat daripada kelipatan $5$, sehingga $v_5$ selalu yang lebih
kecil. Cukup hitung pangkat $5$.

Rumus Legendre:

$$v_5(100!) = \left\lfloor \frac{100}{5} \right\rfloor + \left\lfloor \frac{100}{25} \right\rfloor
+ \left\lfloor \frac{100}{125} \right\rfloor + \cdots$$

$$= 20 + 4 + 0 = \boxed{24}$$

Cara membacanya: ada $20$ kelipatan $5$ di antara $1$ sampai $100$, masing-masing
menyumbang paling sedikit satu faktor $5$. Empat di antaranya — $25, 50, 75, 100$ —
menyumbang satu faktor lagi, dan itulah tambahan $4$ pada suku kedua. Tidak ada kelipatan
$125$, jadi jumlahnya berhenti.

Berhenti di $20$ adalah kesalahan yang paling sering terjadi. Suku kedua bukan koreksi
kecil yang boleh diabaikan.
