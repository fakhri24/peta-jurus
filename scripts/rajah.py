#!/usr/bin/env python3
"""Pustaka rajah geometri: hitung dulu, gambar kemudian.

Rajah geometri dibaca dengan mata — siswa menyimpulkan dari apa yang dilihatnya.
Gambar yang lingkaran dalamnya tidak sungguh-sungguh menyinggung ketiga sisi
mengajarkan hal yang salah, dan kekeliruan macam itu lolos tanpa suara: tidak ada
galat, hanya rajah yang terlihat hampir benar.

Karena itu titik istimewa di sini **dihitung**, tidak ditaksir. Penulis rajah
menyebut A, B, C, lalu meminta `pusat_dalam(A, B, C)`; koordinatnya jatuh di mana
mestinya. Pola yang sama dengan `tata_letak()` di build.py — hitungannya di Python,
peramban tinggal menggambar.

Dipakai dari berkas di konten/rajah/, satu berkas satu rajah:

    from rajah import *

    A, B, C = titik(0, 0), titik(6, 0), titik(1.6, 4.2)
    I = pusat_dalam(A, B, C)

    RAJAH = (rajah("Segitiga ABC dengan lingkaran dalam berpusat I")
             .poligon(A, B, C)
             .lingkaran(I, jari_dalam(A, B, C), gaya="bantu")
             .titik(A, "A").titik(B, "B").titik(C, "C").titik(I, "I"))

Sumbu y di sini **matematis** — naik ke atas, seperti di buku. Pembalikannya ke
sistem koordinat SVG dikerjakan saat render, sekali, di `_layar()`. Tanpa itu tiap
penulis rajah harus membalik sendiri di kepalanya, dan cepat atau lambat ada yang
lupa.
"""

import math

# Satu satuan spec jadi berapa piksel. Segitiga beralas 6 keluar selebar ~200 px —
# muat di layar ponsel tanpa diperkecil peramban.
SKALA = 34

# Ruang di tepi viewBox. Label titik digambar di luar bangunnya, jadi kotak
# pembatas isi saja selalu kurang.
TEPI = 20

# Jari-jari busur penanda sudut, dalam piksel. Tetap, bukan ikut skala: penanda
# sudut adalah anotasi, besarnya tidak menyatakan apa-apa tentang bangunnya.
JARI_SUDUT = 20
SISI_SIKU = 11
PANJANG_TANDA = 7
JARAK_TANDA = 4

# Warna dicap ke dalam tiap berkas SVG, bukan diwarisi dari halaman. SVG yang
# dimuat lewat <img> adalah dokumen terpisah: ia tidak melihat CSS halaman sama
# sekali, jadi var(--tinta) dan currentColor mati di sana. Yang tetap berlaku
# adalah media query-nya sendiri — dan situs ini memang hanya mengikuti tema OS,
# tanpa tombol tema manual, jadi dua blok di bawah ini cukup.
#
# Nilainya sengaja disalin dari assets/styles.css. Kalau palet situs berubah,
# ubah di sini juga — tidak ada cara bagi SVG lepas untuk ikut sendiri.
GAYA = (
    "svg{--tinta:#16233b;--bantu:#8894a8;--tekan:#be3a2b;--isi:#16233b}"
    "@media(prefers-color-scheme:dark){"
    "svg{--tinta:#e9edf3;--bantu:#7f8da0;--tekan:#ee7466;--isi:#e9edf3}}"
    ".g{fill:none;stroke:var(--tinta);stroke-width:1.6;"
    "stroke-linecap:round;stroke-linejoin:round}"
    ".g.bantu{stroke:var(--bantu);stroke-width:1.2}"
    ".g.tekan{stroke:var(--tekan);stroke-width:2}"
    ".g.putus{stroke-dasharray:5 4}"
    ".n{fill:var(--tinta);stroke:none}"
    ".n.bantu{fill:var(--bantu)}"
    ".n.tekan{fill:var(--tekan)}"
    ".a{fill:var(--isi);opacity:.09;stroke:none}"
    ".a.tekan{fill:var(--tekan);opacity:.14}"
    # Label titik ditulis serif miring supaya terbaca senada dengan $A$ di prosa
    # sekitarnya. Font KaTeX tidak bisa dipakai: SVG lewat <img> tidak boleh
    # memuat berkas luar, jadi yang tersisa adalah serif yang ada di mana saja.
    ".t{font-family:Georgia,'Times New Roman',serif;font-style:italic;"
    "font-size:15px;fill:var(--tinta);stroke:none;"
    "text-anchor:middle;dominant-baseline:central}"
    ".t.bantu{fill:var(--bantu);font-size:13px}"
    ".t.tekan{fill:var(--tekan)}"
    # Keterangan panjang dan besar sudut bukan nama titik, jadi tegak, bukan miring.
    ".t.ukur{font-style:normal;font-size:13px}"
)


# ---------------------------------------------------------------- titik & garis

class Titik:
    """Titik pada bidang, sumbu y matematis (naik ke atas)."""

    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, lain):
        return Titik(self.x + lain.x, self.y + lain.y)

    def __sub__(self, lain):
        return Titik(self.x - lain.x, self.y - lain.y)

    def __mul__(self, k):
        return Titik(self.x * k, self.y * k)

    __rmul__ = __mul__

    def __truediv__(self, k):
        return Titik(self.x / k, self.y / k)

    def __repr__(self):
        return "titik(%.4g, %.4g)" % (self.x, self.y)

    def panjang(self):
        return math.hypot(self.x, self.y)

    def satuan(self):
        p = self.panjang()
        if p < 1e-12:
            raise GagalRajah("vektor nol tidak punya arah")
        return self / p

    def tegak(self):
        """Putar 90° berlawanan arah jarum jam."""
        return Titik(-self.y, self.x)


class Garis:
    """Garis tak berhingga lewat dua titik. Disimpan sebagai titik + arah."""

    __slots__ = ("p", "arah")

    def __init__(self, p, arah):
        self.p = p
        self.arah = arah.satuan()


class GagalRajah(Exception):
    """Bangun yang tidak mungkin — sudut nol, titik berimpit, garis sejajar.

    Dilempar, tidak dikumpulkan seperti galat build: rajah yang tidak bisa
    dihitung tidak punya keluaran sebagian yang masuk akal.
    """


def titik(x, y):
    return Titik(x, y)


def garis(p, q):
    return Garis(p, q - p)


def jarak(p, q):
    return (q - p).panjang()


def tengah(p, q):
    return (p + q) / 2


def bagi(p, q, t):
    """Titik pada PQ dengan PX : XQ = t : (1-t). t=0 di P, t=1 di Q."""
    return p + (q - p) * t


def putar(p, pusat, derajat):
    r = math.radians(derajat)
    v = p - pusat
    return pusat + Titik(
        v.x * math.cos(r) - v.y * math.sin(r),
        v.x * math.sin(r) + v.y * math.cos(r),
    )


def potong(g, h):
    """Titik potong dua garis. Sejajar berarti rajahnya salah, jadi dilempar."""
    d = g.arah.x * h.arah.y - g.arah.y * h.arah.x
    if abs(d) < 1e-12:
        raise GagalRajah("dua garis sejajar tidak berpotongan")
    w = h.p - g.p
    t = (w.x * h.arah.y - w.y * h.arah.x) / d
    return g.p + g.arah * t


def tegak_lurus(p, g):
    """Garis lewat P yang tegak lurus g."""
    return Garis(p, g.arah.tegak())


def sejajar(p, g):
    return Garis(p, g.arah)


def kaki(p, g):
    """Kaki garis tinggi dari P ke g."""
    return potong(g, tegak_lurus(p, g))


def sumbu(p, q):
    """Sumbu ruas PQ: tegak lurus di titik tengahnya."""
    return Garis(tengah(p, q), (q - p).tegak())


def sudut(a, b, c):
    """Besar sudut ABC dalam derajat, selalu antara 0 dan 180."""
    u, v = (a - b), (c - b)
    if u.panjang() < 1e-12 or v.panjang() < 1e-12:
        raise GagalRajah("sudut dengan titik berimpit tidak terdefinisi")
    kos = (u.x * v.x + u.y * v.y) / (u.panjang() * v.panjang())
    return math.degrees(math.acos(max(-1.0, min(1.0, kos))))


def garis_bagi(a, b, c):
    """Garis bagi sudut ABC, lewat B.

    Arahnya jumlah dua vektor satuan — cara itu benar untuk sudut berapa pun dan
    tidak perlu membedakan kasus seperti rumus setengah sudut.
    """
    return Garis(b, (a - b).satuan() + (c - b).satuan())


# ---------------------------------------------------------------- ruang

# Proyeksi miring (kabinet) untuk bangun ruang: sumbu y ruang — yang "masuk ke
# dalam" layar — digambar menyerong dan diperpendek separuh.
#
# Bukan perspektif, dan itu disengaja. Pada proyeksi ini rusuk yang sejajar tetap
# sejajar dan panjang di bidang xz tetap sejati, jadi siswa boleh membaca panjang
# di gambar untuk arah itu. Perspektif justru mengajarkan hal yang salah: ia
# memperkecil yang jauh, padahal jebakan baku soal ruang adalah mengukur di
# gambar. Penyusutan separuh pada arah y sudah cukup memberi kesan ruang tanpa
# menjanjikan apa pun tentang panjangnya.
#
# Serongnya 30°, bukan 45°. Pada 45° arah kedalaman menjadi (0,354; 0,354) —
# kemiringan yang sama persis dengan diagonal ruang kubus, sehingga diagonal AG
# tergambar melewati titik sudut F. Kebetulan proyeksi semacam itu tidak
# menggagalkan apa pun, ia hanya menyarankan kesegarisan yang tidak ada.
SERONG = 30
SUSUT = 0.5


def ruang(x, y, z):
    """Titik ruang (x, y, z) jadi titik gambar. Sumbu z naik, y masuk ke dalam."""
    r = math.radians(SERONG)
    return Titik(x + y * SUSUT * math.cos(r), z + y * SUSUT * math.sin(r))


# ---------------------------------------------------------------- titik istimewa

def titik_berat(a, b, c):
    return (a + b + c) / 3


def pusat_luar(a, b, c):
    """Perpotongan dua sumbu sisi."""
    return potong(sumbu(a, b), sumbu(b, c))


def jari_luar(a, b, c):
    return jarak(pusat_luar(a, b, c), a)


def pusat_dalam(a, b, c):
    """Rata-rata berbobot panjang sisi di hadapan tiap titik."""
    pa, pb, pc = jarak(b, c), jarak(a, c), jarak(a, b)
    jum = pa + pb + pc
    if jum < 1e-12:
        raise GagalRajah("segitiga dengan ketiga titik berimpit")
    return (a * pa + b * pb + c * pc) / jum


def jari_dalam(a, b, c):
    """Luas dibagi setengah keliling."""
    pa, pb, pc = jarak(b, c), jarak(a, c), jarak(a, b)
    s = (pa + pb + pc) / 2
    luas = abs((b - a).x * (c - a).y - (b - a).y * (c - a).x) / 2
    if s < 1e-12:
        raise GagalRajah("segitiga tanpa keliling")
    return luas / s


def titik_tinggi(a, b, c):
    """Perpotongan dua garis tinggi."""
    return potong(
        Garis(a, (c - b).tegak()),
        Garis(b, (c - a).tegak()),
    )


def singgung(p, pusat, jari):
    """Dua titik singgung dari P ke lingkaran. P harus di luar lingkaran."""
    d = jarak(p, pusat)
    if d < jari + 1e-9:
        raise GagalRajah(
            "titik singgung hanya ada dari titik di luar lingkaran "
            "(jarak %.4g, jari-jari %.4g)" % (d, jari)
        )
    # Titik singgung berjarak jari-jari dari pusat, dan sudutnya terhadap PO
    # memenuhi cos t = jari/d.
    t = math.degrees(math.acos(jari / d))
    arah = (p - pusat).satuan() * jari
    return pusat + _putar_vektor(arah, t), pusat + _putar_vektor(arah, -t)


def _putar_vektor(v, derajat):
    r = math.radians(derajat)
    return Titik(v.x * math.cos(r) - v.y * math.sin(r),
                 v.x * math.sin(r) + v.y * math.cos(r))


def potong_lingkaran(p1, r1, p2, r2):
    """Dua titik potong dua lingkaran, urut kiri-kanan terhadap garis pusatnya."""
    d = jarak(p1, p2)
    if d < 1e-12 or d > r1 + r2 - 1e-9 or d < abs(r1 - r2) + 1e-9:
        raise GagalRajah("dua lingkaran itu tidak berpotongan di dua titik")
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    tinggi = math.sqrt(max(0.0, r1 * r1 - a * a))
    tengah_tali = p1 + (p2 - p1).satuan() * a
    lebar = (p2 - p1).satuan().tegak() * tinggi
    return tengah_tali + lebar, tengah_tali - lebar


# ---------------------------------------------------------------- rajah

def _bil(v):
    """Angka sependek mungkin — SVG ini dikirim ke ponsel, bukan dibaca mesin."""
    s = "%.2f" % v
    s = s.rstrip("0").rstrip(".")
    return s if s not in ("", "-0") else "0"


def _kelas(dasar, gaya, putus=False):
    bagian = [dasar]
    if gaya:
        bagian.append(gaya)
    if putus:
        bagian.append("putus")
    return " ".join(bagian)


class Rajah:
    """Kumpulan bentuk plus alt-nya, dirender jadi satu berkas SVG."""

    def __init__(self, alt):
        if not alt or not alt.strip():
            raise GagalRajah(
                "rajah wajib punya alt — bagi siswa yang memakai pembaca layar, "
                "itu satu-satunya isi soalnya"
            )
        self.alt = alt.strip()
        self._bentuk = []       # (svg, ) potongan siap pakai
        self._batas = []        # titik yang ikut menentukan viewBox
        self._acuan = []        # titik bangun, untuk menaruh label otomatis

    # -- pencatat batas ------------------------------------------------

    def _catat(self, *titik_titik):
        self._batas.extend(titik_titik)

    def _catat_acuan(self, *titik_titik):
        self._acuan.extend(titik_titik)
        self._catat(*titik_titik)

    # -- bentuk --------------------------------------------------------

    def ruas(self, p, q, gaya=None, putus=False):
        self._catat_acuan(p, q)
        self._bentuk.append(
            '<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>'
            % ((_kelas("g", gaya, putus),) + self._xy(p) + self._xy(q))
        )
        return self

    def poligon(self, *titik_titik, gaya=None, putus=False):
        if len(titik_titik) < 3:
            raise GagalRajah("poligon butuh minimal tiga titik")
        self._catat_acuan(*titik_titik)
        self._bentuk.append(
            '<polygon class="%s" points="%s"/>'
            % (_kelas("g", gaya, putus), self._titik_titik(titik_titik))
        )
        return self

    def garis_patah(self, *titik_titik, gaya=None, putus=False):
        """Seperti poligon tapi tidak ditutup — untuk lintasan dan sudut terbuka."""
        if len(titik_titik) < 2:
            raise GagalRajah("garis patah butuh minimal dua titik")
        self._catat_acuan(*titik_titik)
        self._bentuk.append(
            '<polyline class="%s" points="%s"/>'
            % (_kelas("g", gaya, putus), self._titik_titik(titik_titik))
        )
        return self

    def lingkaran(self, pusat, jari, gaya=None, putus=False):
        if jari <= 0:
            raise GagalRajah("jari-jari lingkaran harus positif")
        self._catat(pusat + Titik(jari, jari), pusat - Titik(jari, jari))
        x, y = self._xy(pusat)
        self._bentuk.append(
            '<circle class="%s" cx="%s" cy="%s" r="%s"/>'
            % (_kelas("g", gaya, putus), x, y, _bil(jari * SKALA))
        )
        return self

    def busur(self, pusat, jari, dari, sampai, gaya=None, putus=False):
        """Busur dari sudut `dari` ke `sampai`, derajat, berlawanan jarum jam."""
        self._catat(pusat + Titik(jari, jari), pusat - Titik(jari, jari))
        self._bentuk.append(
            '<path class="%s" d="%s"/>'
            % (_kelas("g", gaya, putus),
               self._jalur_busur(pusat, jari * SKALA, dari, sampai))
        )
        return self

    def arsir(self, *titik_titik, gaya=None):
        """Daerah berbayang — untuk menunjuk luas yang sedang dibicarakan."""
        if len(titik_titik) < 3:
            raise GagalRajah("daerah arsiran butuh minimal tiga titik")
        self._catat(*titik_titik)
        # Disisipkan di depan supaya bayangannya tidak menutupi garis bangunnya.
        self._bentuk.insert(
            0,
            '<polygon class="%s" points="%s"/>'
            % (_kelas("a", gaya), self._titik_titik(titik_titik)),
        )
        return self

    # -- anotasi -------------------------------------------------------

    def titik(self, p, nama=None, arah=None, gaya=None):
        """Bulatan kecil, dan kalau diberi nama sekalian labelnya."""
        self._catat_acuan(p)
        x, y = self._xy(p)
        self._bentuk.append(
            '<circle class="%s" cx="%s" cy="%s" r="2.6"/>' % (_kelas("n", gaya), x, y)
        )
        if nama:
            self.label(p, nama, arah=arah, gaya=gaya)
        return self

    def label(self, p, teks, arah=None, jauh=15, gaya=None):
        """Tulisan di dekat P.

        Arah bawaan menjauhi pusat bangun — untuk titik sudut poligon itu hampir
        selalu benar, dan yang tidak bisa diperbaiki dengan `arah=(dx, dy)`.
        """
        self._catat(p)
        self._bentuk.append(
            _Label(p, teks, arah, jauh, _kelas("t", gaya))
        )
        return self

    def ukuran(self, p, q, teks, jauh=14, gaya=None):
        """Keterangan panjang di sisi ruas PQ, digeser tegak lurus dari ruasnya."""
        self._catat(p, q)
        arah = (q - p).satuan().tegak()
        # Selalu ke sisi yang menjauhi bangun, bukan selalu ke kiri ruas.
        self._bentuk.append(
            _Label(tengah(p, q), teks, (arah.x, arah.y), jauh,
                   _kelas("t", gaya) + " ukur", jauhi_pusat=True)
        )
        return self

    def tanda_sudut(self, a, b, c, rangkap=1, teks=None, gaya=None, jauh=None):
        """Busur kecil di titik sudut B, menandai sudut ABC.

        `jauh` menggeser keterangannya menjauhi titik sudut. Bawaannya pas untuk
        sudut yang lebar, tetapi pada sudut sempit busurnya berdesakan dengan kaki
        sudutnya sendiri dan tulisannya tertimpa garis — di situ jauh perlu
        dinaikkan tangan.
        """
        if sudut(a, b, c) > 179.5:
            raise GagalRajah("sudut ABC nyaris lurus, penandanya tidak terbaca")
        self._catat(b)
        d1 = math.degrees(math.atan2((a - b).y, (a - b).x))
        d2 = math.degrees(math.atan2((c - b).y, (c - b).x))
        # Ambil arah putar yang lewat dalam sudutnya, bukan yang memutari luar.
        if (d2 - d1) % 360 > 180:
            d1, d2 = d2, d1
        for i in range(rangkap):
            r = JARI_SUDUT + i * 4
            self._bentuk.append(
                '<path class="%s" d="%s"/>'
                % (_kelas("g", gaya), self._jalur_busur(b, r, d1, d2))
            )
        if teks:
            tengah_sudut = d1 + ((d2 - d1) % 360) / 2
            r = math.radians(tengah_sudut)
            self._bentuk.append(
                _Label(b, teks, (math.cos(r), math.sin(r)),
                       JARI_SUDUT + 6 + (rangkap - 1) * 4 if jauh is None else jauh,
                       _kelas("t", gaya) + " ukur")
            )
        return self

    def tanda_siku(self, a, b, c, gaya=None):
        """Persegi kecil di B — sudut siku-siku tidak ditandai busur."""
        self._catat(b)
        u = (a - b).satuan() * (SISI_SIKU / SKALA)
        v = (c - b).satuan() * (SISI_SIKU / SKALA)
        self._bentuk.append(
            '<polyline class="%s" points="%s"/>'
            % (_kelas("g", gaya), self._titik_titik([b + u, b + u + v, b + v]))
        )
        return self

    def tanda_sama(self, p, q, rangkap=1, gaya=None):
        """Garis-garis pendek di tengah ruas, menandai sisi yang sama panjang."""
        self._catat(p, q)
        arah = (q - p).satuan()
        tegak = arah.tegak() * (PANJANG_TANDA / SKALA)
        pusat = tengah(p, q)
        awal = -(rangkap - 1) / 2
        for i in range(rangkap):
            geser = arah * ((awal + i) * JARAK_TANDA / SKALA)
            a, b = pusat + geser + tegak, pusat + geser - tegak
            self._bentuk.append(
                '<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>'
                % ((_kelas("g", gaya),) + self._xy(a) + self._xy(b))
            )
        return self

    # -- render --------------------------------------------------------

    def _xy(self, p):
        """Ke koordinat layar. Sumbu y dibalik di sini, sekali, untuk semuanya."""
        return _bil(p.x * SKALA), _bil(-p.y * SKALA)

    def _titik_titik(self, deret):
        return " ".join("%s,%s" % self._xy(p) for p in deret)

    def _jalur_busur(self, pusat, jari, dari, sampai):
        """Jalur SVG untuk busur. `jari` selalu dalam piksel."""
        r = jari
        span = (sampai - dari) % 360
        awal = pusat + _putar_vektor(Titik(r / SKALA, 0), dari)
        akhir = pusat + _putar_vektor(Titik(r / SKALA, 0), sampai)
        x1, y1 = self._xy(awal)
        x2, y2 = self._xy(akhir)
        # Sumbu y dibalik, jadi arah sapuan ikut terbalik: berlawanan jarum jam
        # di koordinat matematis menjadi sweep-flag 0 di layar.
        besar = 1 if span > 180 else 0
        return "M%s %sA%s %s 0 %d 0 %s %s" % (x1, y1, _bil(r), _bil(r), besar, x2, y2)

    def _kotak(self):
        """viewBox dari kotak pembatas isi, ditambah ruang untuk label."""
        if not self._batas:
            raise GagalRajah("rajah kosong — tidak ada yang digambar")
        xs = [p.x * SKALA for p in self._batas]
        ys = [-p.y * SKALA for p in self._batas]
        return min(xs) - TEPI, min(ys) - TEPI, max(xs) + TEPI, max(ys) + TEPI

    def _pusat_acuan(self):
        if not self._acuan:
            return Titik(0, 0)
        jum = Titik(0, 0)
        for p in self._acuan:
            jum = jum + p
        return jum / len(self._acuan)

    def svg(self):
        pusat = self._pusat_acuan()
        potongan = []
        batas_label = []
        for b in self._bentuk:
            if isinstance(b, _Label):
                teks, kotak = b.render(self, pusat)
                potongan.append(teks)
                batas_label.append(kotak)
            else:
                potongan.append(b)

        x1, y1, x2, y2 = self._kotak()
        for kx1, ky1, kx2, ky2 in batas_label:
            x1, y1 = min(x1, kx1 - 4), min(y1, ky1 - 4)
            x2, y2 = max(x2, kx2 + 4), max(y2, ky2 + 4)

        lebar, tinggi = x2 - x1, y2 - y1
        return (
            '<svg xmlns="http://www.w3.org/2000/svg" '
            'viewBox="%s %s %s %s" width="%s" height="%s" '
            'role="img" aria-label="%s">'
            "<title>%s</title><style>%s</style>%s</svg>\n"
        ) % (
            _bil(x1), _bil(y1), _bil(lebar), _bil(tinggi),
            _bil(lebar), _bil(tinggi),
            _lolos_atribut(self.alt), _lolos_teks(self.alt), GAYA,
            "".join(potongan),
        )


class _Label:
    """Tulisan yang arahnya baru bisa ditentukan setelah semua titik terkumpul."""

    __slots__ = ("p", "teks", "arah", "jauh", "kelas", "jauhi_pusat")

    def __init__(self, p, teks, arah, jauh, kelas, jauhi_pusat=False):
        self.p = p
        self.teks = str(teks)
        self.arah = arah
        self.jauh = jauh
        self.kelas = kelas
        self.jauhi_pusat = jauhi_pusat

    def render(self, rajah_, pusat):
        if self.arah is not None:
            dx, dy = self.arah
            v = Titik(dx, dy)
            if self.jauhi_pusat and _searah(v, self.p - pusat) < 0:
                v = v * -1
        else:
            v = self.p - pusat
            if v.panjang() < 1e-9:
                v = Titik(0, -1)  # titik di pusat bangun: taruh labelnya di bawah
        v = v.satuan()

        x = self.p.x * SKALA + v.x * self.jauh
        y = -self.p.y * SKALA - v.y * self.jauh
        teks = '<text class="%s" x="%s" y="%s">%s</text>' % (
            self.kelas, _bil(x), _bil(y), _lolos_teks(self.teks)
        )
        # Perkiraan kasar lebar huruf, cukup untuk menjaga label tidak terpotong
        # tepi viewBox. Tidak perlu tepat — yang salah cuma sedikit ruang lebih.
        lebar = 8.5 * len(self.teks)
        return teks, (x - lebar / 2, y - 9, x + lebar / 2, y + 9)


def _searah(u, v):
    return u.x * v.x + u.y * v.y


def _lolos_teks(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _lolos_atribut(s):
    return _lolos_teks(s).replace('"', "&quot;")


def rajah(alt):
    return Rajah(alt)
