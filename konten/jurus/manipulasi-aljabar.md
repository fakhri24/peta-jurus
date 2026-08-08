---
id: manipulasi-aljabar
nama: Manipulasi Bentuk Aljabar
pilar: aljabar
tahap: osn-k
prasyarat: []
contoh: [ma-contoh-1]
latihan: [ma-01, ma-02, ma-03, ma-04, ma-05, ma-06]
---

## Kapan dipakai

Hampir selalu, sebagai langkah pertama. Kamu melihat bentuk yang berantakan dan menduga
ada bentuk lain yang lebih jinak — jumlah kuadrat, hasil kali, atau pecahan yang bisa
disederhanakan.

## Intinya

Beberapa identitas yang harus dikenali seketika, bukan diturunkan ulang tiap kali:

$$(a \pm b)^2 = a^2 \pm 2ab + b^2, \qquad a^2 - b^2 = (a-b)(a+b)$$

$$a^3 \pm b^3 = (a \pm b)\left(a^2 \mp ab + b^2\right)$$

$$(a+b+c)^2 = a^2+b^2+c^2 + 2(ab+bc+ca)$$

Yang paling sering menolong di olimpiade adalah yang terakhir, dibalik: begitu kamu punya
$a+b+c$ dan $ab+bc+ca$, kamu punya $a^2+b^2+c^2$ tanpa tahu $a$, $b$, $c$ sama sekali.

Satu lagi yang sering menyelamatkan:

$$a^3+b^3+c^3-3abc = (a+b+c)\left(a^2+b^2+c^2-ab-bc-ca\right)$$

Akibatnya, kalau $a+b+c = 0$ maka $a^3+b^3+c^3 = 3abc$.

**Refleks yang dilatih di sini:** jangan menjabarkan kalau bisa memfaktorkan, dan jangan
mencari nilai tiap peubah kalau yang ditanya hanya bentuk simetrisnya.

## Jebakan umum

- **Menjabarkan lebih dulu.** Bentuk yang sudah terfaktor biasanya sudah berada di wujud
  paling berguna. Menjabarkannya membuang keterangan.
- **Mengira harus tahu tiap peubah.** Soal olimpiade sering hanya bisa dijawab lewat
  bentuk simetrisnya, dan memang tidak menuntut nilai satu-satu.
- **Salah tanda pada $a^3 - b^3$.** Faktor keduanya $a^2 + ab + b^2$ — tandanya berlawanan
  dengan faktor pertama.
