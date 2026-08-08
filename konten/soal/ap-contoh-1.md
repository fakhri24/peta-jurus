---
id: ap-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [algoritma-pembagian]
bentuk: isian
kesulitan: 1
jawaban: "14"
---

## Soal

Ada berapa bilangan bulat $n$ dengan $1 \le n \le 100$ yang bersisa $3$ ketika dibagi $7$?

## Petunjuk

- Tulis bentuk umum bilangan yang bersisa 3 saat dibagi 7.
- $n = 7k + 3$. Sekarang cari $k$ mana saja yang membuat $n$ jatuh di rentang yang diminta.
- $1 \le 7k+3 \le 100$ memberi $0 \le k \le 13{,}857\ldots$, dan $k$ harus bulat.

## Pembahasan

Bilangan yang bersisa $3$ saat dibagi $7$ berbentuk $n = 7k + 3$ dengan $k$ bulat.

Syarat $1 \le n \le 100$ menjadi

$$1 \le 7k + 3 \le 100 \quad\Longrightarrow\quad -\tfrac{2}{7} \le k \le \tfrac{97}{7} = 13{,}857\ldots$$

Karena $k$ bulat, $k \in \{0, 1, \dots, 13\}$ — ada $\boxed{14}$ nilai.

Cek ujungnya: $k=0$ memberi $n = 3$, dan $k = 13$ memberi $n = 94$. Keduanya di dalam
rentang, sedangkan $k = 14$ memberi $101$ yang sudah lewat.
