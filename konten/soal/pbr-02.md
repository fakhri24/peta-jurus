---
id: pbr-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-berulang]
bentuk: isian
kesulitan: 2
jawaban: "75600"
---

## Soal

Ada berapa susunan huruf berbeda yang dapat dibentuk dari seluruh huruf pada kata

$$\textbf{STATISTIKA}$$

## Petunjuk

- Tuliskan hurufnya satu per satu dan hitung kemunculannya. Kata ini punya lebih dari satu huruf yang berulang.
- Periksa jumlah seluruh kemunculan itu sama dengan banyaknya huruf pada katanya.
- Tiap huruf yang berulang menyumbang satu faktor pembagi, dan faktor-faktor itu dikalikan.

## Pembahasan

**Daftar hurufnya dengan teliti.** Tulis satu per satu: S, T, A, T, I, S, T, I, K, A.

| Huruf | S | T | A | I | K |
|---|---|---|---|---|---|
| Banyaknya | $2$ | $3$ | $2$ | $2$ | $1$ |

Periksa jumlahnya: $2+3+2+2+1 = 10$. Cocok dengan panjang katanya.

Huruf T yang muncul **tiga** kali adalah bagian yang paling mudah terlewat — sekilas kata
ini terlihat seperti punya dua T saja.

**Hitung.**

$$\frac{10!}{2!\,3!\,2!\,2!} = \frac{3\,628\,800}{2 \times 6 \times 2 \times 2}
= \frac{3\,628\,800}{48} = \boxed{75600}$$

**Bandingkan dengan MATEMATIKA,** yang juga sepuluh huruf. Di sana pembaginya
$2!\,3!\,2! = 24$; di sini $48$ — dua kali lipat, karena ada satu huruf berulang lagi.
Akibatnya jawabannya tepat separuh: $151200$ berbanding $75600$.

Perbandingan itu memperlihatkan hal yang berguna: **yang menentukan jawaban bukan panjang
katanya, melainkan seberapa banyak huruf yang tidak bisa dibedakan.** Sepuluh huruf yang
seluruhnya berbeda memberi $3\,628\,800$; sepuluh huruf yang semuanya sama memberi $1$.

**Kebiasaan yang menyelamatkan.** Sebelum menghitung, tulis daftar kemunculannya dan
jumlahkan untuk memeriksa. Salah menghitung satu huruf saja mengubah jawaban dengan faktor
$2$ atau $3$, dan kekeliruan itu tidak akan terlihat lagi di langkah berikutnya.
