---
id: orde-elemen
nama: Orde Elemen
pilar: teori-bilangan
tahap: osn
prasyarat: [fungsi-euler]
contoh: []
latihan: []
---

## Kapan dipakai

Soal tentang **periode** — kapan $a^k$ berulang, atau mencari $n$ terkecil dengan
$a^n \equiv 1$. Juga saat kamu perlu membatasi prima yang mungkin membagi bentuk seperti
$2^n - 1$.

## Intinya

Orde $a$ modulo $n$, ditulis $\operatorname{ord}_n(a)$, adalah bilangan positif terkecil
$d$ dengan $a^d \equiv 1 \pmod n$ (ada asalkan $\gcd(a,n)=1$).

Sifat yang menjadi seluruh isi jurus ini:

$$a^k \equiv 1 \pmod n \quad\Longleftrightarrow\quad \operatorname{ord}_n(a) \mid k$$

Bukan "$k$ kelipatan sesuatu yang mirip" — tepat habis dibagi. Akibat langsungnya,
$\operatorname{ord}_n(a) \mid \varphi(n)$, dan untuk modulus prima
$\operatorname{ord}_p(a) \mid p - 1$.

Dari sini lahir jurus pembatas prima yang sangat berguna:

> Kalau $p \mid 2^n - 1$, maka $\operatorname{ord}_p(2) \mid n$. Digabung dengan
> $\operatorname{ord}_p(2) \mid p-1$, calon $p$ langsung tersaring jadi sedikit sekali.

## Jebakan umum

- **Mengira orde selalu $\varphi(n)$.** Itu hanya batas atas. Orde $2$ modulo $7$ adalah
  $3$, bukan $6$.
- **Menyimpulkan dari $a^k \equiv 1$ bahwa $k$ adalah ordenya.** $k$ hanya kelipatan orde.
- **Lupa syarat $\gcd(a,n) = 1$.** Tanpa itu $a^d \equiv 1$ tidak pernah tercapai.
