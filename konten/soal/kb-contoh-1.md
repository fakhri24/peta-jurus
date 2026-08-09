---
id: kb-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [kombinasi]
bentuk: isian
kesulitan: 2
jawaban: "210"
---

## Soal

Dari $10$ orang akan dipilih $4$ orang untuk menjadi anggota sebuah tim. Keempat anggota
tim berkedudukan sama — tidak ada ketua, tidak ada jabatan apa pun.

Ada berapa tim yang mungkin terbentuk?

## Petunjuk

- Uji dulu apakah urutannya berarti: kalau dua anggota yang terpilih ditukar, apakah timnya menjadi tim yang lain?
- Hitung dulu seolah-olah urutannya berarti, lalu perbaiki kelebihannya.
- Tiap tim yang sama terhitung sebanyak cara mengurutkan keempat anggotanya.

## Pembahasan

**Uji urutannya lebih dulu.** Tim beranggotakan Ani, Budi, Cici, Dedi adalah tim yang
**sama** dengan tim beranggotakan Dedi, Cici, Budi, Ani. Menukar anggota tidak menghasilkan
tim baru, jadi urutannya tidak berarti — ini soal kombinasi.

**Hitung dulu seolah urutannya berarti.** Memilih $4$ orang berurutan dari $10$:

$$10 \times 9 \times 8 \times 7 = 5040$$

**Perbaiki kelebihannya.** Setiap tim terhitung berkali-kali di angka itu — tepat sebanyak
cara mengurutkan keempat anggotanya:

$$4! = 24$$

Jadi

$$\frac{5040}{24} = \boxed{210}$$

Dengan lambang kombinasi:

$$\binom{10}{4} = \frac{10!}{4!\,6!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$$

**Cara menghitung yang menghemat waktu.** Jangan menghitung $10!$ lalu membaginya. Tulis
saja $4$ faktor menurun di atas dan $4!$ di bawah, lalu coret sebelum mengalikan:

$$\frac{10 \times 9 \times \cancel{8} \times 7}{\cancel{4} \times \cancel{3} \times \cancel{2} \times 1}
\quad\longrightarrow\quad 10 \times 3 \times 7 = 210$$

**Pembagian oleh $k!$ itu inti seluruh jurus ini.** Polanya akan terpakai lagi berkali-kali:
hitung dulu dengan menganggap semuanya bisa dibedakan, lalu bagi dengan banyaknya cara
susunan yang sebenarnya dianggap sama.

**Bandingkan dengan soal saudaranya.** Kalau keempat orang itu diberi jabatan berbeda —
ketua, sekretaris, bendahara, humas — maka menukar dua orang menghasilkan susunan yang
lain, dan jawabannya kembali $5040$. Satu kalimat di soal memisahkan $210$ dari $5040$.
