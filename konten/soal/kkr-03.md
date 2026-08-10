---
id: kkr-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kekongruenan, pythagoras]
bentuk: isian
kesulitan: 2
jawaban: "24"
---

## Soal

Pada segitiga $ABC$ berlaku $AB = AC = 25$ dan $BC = 14$. Garis bagi $\angle BAC$ memotong
$BC$ di titik $D$.

Tentukan panjang $AD$.

## Petunjuk

- Untuk memakai panjang $BC$, kamu perlu tahu di mana persisnya $D$ jatuh pada $BC$ — dan itu belum diberikan soal.
- Bandingkan $\triangle ABD$ dengan $\triangle ACD$: dua sisi dan sudut yang diapitnya sudah kamu miliki.
- Dari kekongruenannya, $D$ adalah titik tengah $BC$ **dan** $AD$ tegak lurus $BC$. Sesudah itu tinggal Pythagoras.

## Pembahasan

**Yang belum diketahui bukan panjangnya, melainkan letak $D$.** Soal memberi $BC = 14$, tetapi
tidak menyebut apakah $D$ jatuh di tengah. Menganggapnya di tengah tanpa alasan adalah lompatan
— dan alasan itu justru yang harus dicari lebih dulu.

**Buktikan letaknya lewat kekongruenan.** Bandingkan $\triangle ABD$ dan $\triangle ACD$:

1. $AB = AC = 25$ — diberikan;
2. $\angle BAD = \angle CAD$ — karena $AD$ garis bagi $\angle BAC$;
3. $AD = AD$ — sisi yang dipakai bersama.

Sudut yang diketahui terapit kedua sisi itu, jadi susunannya **S-Sd-S**:

$$\triangle ABD \cong \triangle ACD$$

**Panen dua akibatnya sekaligus.** Dari kekongruenan itu:

$$BD = CD \quad \Longrightarrow \quad BD = \tfrac{1}{2} \times 14 = 7$$

$$\angle ADB = \angle ADC$$

Karena kedua sudut itu berpelurus — $B$, $D$, $C$ segaris — masing-masing besarnya
$90^\circ$. Jadi $AD \perp BC$.

**Pythagoras pada $\triangle ABD$.** Sekarang segitiganya siku-siku di $D$ dengan sisi miring
$AB = 25$ dan salah satu sisi siku-siku $BD = 7$:

$$AD^2 = AB^2 - BD^2 = 25^2 - 7^2 = 625 - 49 = 576$$

$$AD = \sqrt{576} = \boxed{24}$$

**Periksa.** $(7, 24, 25)$ memang tripel Pythagoras: $49 + 576 = 625$. ✓

### Tiga peran $AD$ sekaligus

Pada segitiga **sama kaki**, garis bagi dari puncaknya sekaligus menjadi garis berat (membagi
alas sama panjang) dan garis tinggi (tegak lurus alas). Ketiganya berimpit, dan kekongruenan
di atas adalah buktinya.

Sifat ini tidak berlaku pada segitiga sembarang — di sana ketiga garis itu berbeda. Karena
itu langkah pertama tadi bukan formalitas: yang membuatnya sah adalah $AB = AC$, dan kalau
syarat itu hilang, $BD = 7$ ikut hilang bersamanya.

### Kalau soalnya diubah sedikit

Andaikan $AB = 25$ tetapi $AC = 20$. Garis bagi dari $A$ tidak lagi membagi $BC$ sama panjang;
yang berlaku adalah $\dfrac{BD}{DC} = \dfrac{AB}{AC} = \dfrac{5}{4}$, dan $AD$ tidak lagi
tegak lurus $BC$. Perbandingan itu dibahas di jurus kesebangunan — dan perbedaannya bermula
tepat di langkah kekongruenan yang gagal begitu $AB \ne AC$.
