/* Halaman peta. Koordinat simpul sudah dihitung scripts/build.py, jadi di sini
   tinggal menggambar SVG — tanpa pustaka graf apa pun.

   Petanya digambar satu bidang pada satu waktu, dengan batas tahap yang bisa
   dipasang siswa. Menyaring tahap hanya menyembunyikan simpul; tidak ada
   koordinat yang dihitung ulang di peramban. Tinggi SVG untuk tiap batas pun
   sudah ikut dibangun (`ukuran.tinggi_sampai`). */

(function () {
  'use strict';

  var LEBAR = 168;
  var TINGGI = 60;
  var MAKS_BARIS = 2;
  var MAKS_HURUF = 21;

  var GLIF = {
    'terkunci': '',
    'terbuka': '',
    'dipelajari': '·',
    'dikuasai': '✓',
    'perlu-diulang': '↺'
  };

  var NAMA_PILAR = {
    'teori-bilangan': 'Teori Bilangan',
    'aljabar': 'Aljabar',
    'geometri': 'Geometri',
    'kombinatorika': 'Kombinatorika'
  };

  var NAMA_TAHAP = { 'osn-k': 'OSN-K', 'osn-p': 'OSN-P', 'osn': 'OSN' };

  /* Dari yang paling awal ke paling akhir — salinan TAHAP_SAH di build.py. */
  var URUT_TAHAP = ['osn-k', 'osn-p', 'osn'];

  var TANDA_LUAR = '↗';

  var perPilar = {};
  var urutPilar = [];

  function urutTahap(tahap) {
    var i = URUT_TAHAP.indexOf(tahap);
    return i < 0 ? 0 : i;
  }

  function dalamBatas(j, batas) {
    return urutTahap(j.tahap) <= urutTahap(batas);
  }

  function namaPilar(pilar) {
    return NAMA_PILAR[pilar] || pilar;
  }

  /* Prasyarat yang pangkalnya di bidang lain. Garisnya tidak bisa digambar —
     tiap pilar punya SVG sendiri — jadi simpulnya diberi penanda dan daftar
     namanya, supaya gembok tidak pernah muncul tanpa sebab yang bisa dibaca. */
  function prasyaratLuar(j) {
    return j.prasyarat.filter(function (p) {
      var dari = Inti.data.jurus[p];
      return dari && dari.pilar !== j.pilar;
    });
  }

  /* SVG tidak bisa membungkus teks sendiri, jadi dipatah manual per kata. */
  function patahBaris(teks) {
    var kata = teks.split(' ');
    var baris = [];
    var kini = '';
    for (var i = 0; i < kata.length; i++) {
      var coba = kini ? kini + ' ' + kata[i] : kata[i];
      if (coba.length > MAKS_HURUF && kini) {
        baris.push(kini);
        kini = kata[i];
      } else {
        kini = coba;
      }
    }
    if (kini) baris.push(kini);
    if (baris.length > MAKS_BARIS) {
      baris = baris.slice(0, MAKS_BARIS);
      baris[MAKS_BARIS - 1] = baris[MAKS_BARIS - 1].slice(0, MAKS_HURUF - 1) + '…';
    }
    return baris;
  }

  function gambarTepi(dari, ke, aktif) {
    var x1 = dari.x + LEBAR / 2, y1 = dari.y + TINGGI;
    var x2 = ke.x + LEBAR / 2, y2 = ke.y;
    var d = 'M ' + x1 + ' ' + y1 +
            ' C ' + x1 + ' ' + (y1 + 26) + ', ' + x2 + ' ' + (y2 - 26) + ', ' + x2 + ' ' + y2;
    return '<path class="tepi' + (aktif ? ' aktif' : '') + '" d="' + d + '"></path>';
  }

  function gambarSimpul(j, status) {
    var baris = patahBaris(j.nama);
    var mulai = baris.length === 1 ? j.y + 30 : j.y + 23;
    var teks = baris.map(function (b, i) {
      return '<tspan x="' + (j.x + LEBAR / 2) + '" y="' + (mulai + i * 15) + '">' +
             Inti.lolos(b) + '</tspan>';
    }).join('');

    var cincin = status === 'perlu-diulang'
      ? '<rect class="cincin" x="' + (j.x - 4) + '" y="' + (j.y - 4) + '" width="' +
        (LEBAR + 8) + '" height="' + (TINGGI + 8) + '"></rect>'
      : '';

    var luar = prasyaratLuar(j).map(function (p) {
      var dari = Inti.data.jurus[p];
      return dari.nama + ' (' + namaPilar(dari.pilar) + ')';
    });

    var tandaLuar = luar.length
      ? '<text class="tanda luar" x="' + (j.x + LEBAR - 10) + '" y="' + (j.y + 17) +
          '" text-anchor="end">' + TANDA_LUAR + '</text>'
      : '';

    /* Satu kalimat yang dipakai dua kali: tooltip peramban lewat <title>, dan
       pembaca layar lewat aria-label. */
    var keterangan = (status === 'terkunci' ? 'terkunci — ' : '') + j.nama +
      (luar.length ? '. Prasyarat dari bidang lain: ' + luar.join(', ') : '');

    return '<a href="jurus.html?id=' + encodeURIComponent(j.id) + '" ' +
             'class="simpul ' + status + '" ' +
             'aria-label="' + Inti.lolos(keterangan) + '">' +
             '<title>' + Inti.lolos(keterangan) + '</title>' +
             cincin +
             '<rect class="kotak" x="' + j.x + '" y="' + j.y + '" width="' + LEBAR +
               '" height="' + TINGGI + '"></rect>' +
             '<text class="judul" text-anchor="middle">' + teks + '</text>' +
             '<text class="tanda" x="' + (j.x + 10) + '" y="' + (j.y + TINGGI - 10) + '">' +
               (NAMA_TAHAP[j.tahap] || j.tahap) + '</text>' +
             '<text class="tanda" x="' + (j.x + LEBAR - 10) + '" y="' + (j.y + TINGGI - 10) +
               '" text-anchor="end">' + GLIF[status] + '</text>' +
             tandaLuar +
           '</a>';
  }

  function gambarPilar(pilar, k, batas) {
    var simpul = perPilar[pilar] || [];
    var ukuran = Inti.data.ukuran[pilar] || {};

    var tampak = simpul.filter(function (j) { return dalamBatas(j, batas); });
    if (!tampak.length) {
      return '<p class="kosong">Belum ada jurus ' + Inti.lolos(namaPilar(pilar)) +
             ' sampai tahap ' + (NAMA_TAHAP[batas] || batas) + '.</p>';
    }

    var status = {};
    var terlihat = {};
    tampak.forEach(function (j) {
      status[j.id] = Inti.statusJurus(j.id, k);
      terlihat[j.id] = true;
    });

    var tepi = tampak.map(function (j) {
      return j.prasyarat.map(function (p) {
        var dari = Inti.data.jurus[p];
        /* Tepi dilewati kalau pangkalnya di bidang lain — simpulnya sudah diberi
           penanda ↗ — atau kalau pangkalnya disembunyikan saringan tahap. */
        if (!dari || dari.pilar !== pilar || !terlihat[p]) return '';
        return gambarTepi(dari, j, status[p] === 'dikuasai' || status[p] === 'perlu-diulang');
      }).join('');
    }).join('');

    var kotak = tampak.map(function (j) { return gambarSimpul(j, status[j.id]); }).join('');

    var dikuasai = tampak.filter(function (j) {
      return status[j.id] === 'dikuasai' || status[j.id] === 'perlu-diulang';
    }).length;

    var tinggi = (ukuran.tinggi_sampai && ukuran.tinggi_sampai[batas]) || ukuran.tinggi;
    var adaLuar = tampak.some(function (j) { return prasyaratLuar(j).length > 0; });

    return '<section class="renggang">' +
      '<h2>' + Inti.lolos(namaPilar(pilar)) + ' ' +
        '<span class="sangat-samar">' + dikuasai + ' dari ' + tampak.length +
        ' dikuasai</span></h2>' +
      '<div class="peta-bungkus">' +
        '<svg class="peta" width="' + ukuran.lebar + '" height="' + tinggi +
          '" viewBox="0 0 ' + ukuran.lebar + ' ' + tinggi + '" role="img" ' +
          'aria-label="Peta jurus ' + Inti.lolos(namaPilar(pilar)) + '">' +
          tepi + kotak +
        '</svg>' +
      '</div>' +
      kunciPeta(adaLuar) +
    '</section>';
  }

  function kunciPeta(adaLuar) {
    return '<div class="kunci-peta">' +
      '<span><i class="k-terkunci"></i> terkunci</span>' +
      '<span><i></i> terbuka</span>' +
      '<span><i class="k-dipelajari"></i> sedang dipelajari</span>' +
      '<span><i class="k-dikuasai"></i> dikuasai</span>' +
      '<span><i class="k-ulang"></i> perlu diulang</span>' +
      (adaLuar
        ? '<span><b class="k-luar">' + TANDA_LUAR + '</b> prasyaratnya di bidang lain</span>'
        : '') +
    '</div>';
  }

  function gambarAjakan(k, batas) {
    /* Jurus yang jatuh tempo tidak disaring batas tahap. Ulangan itu soal apa
       yang sudah dipelajari, bukan soal apa yang sedang disasar — menyembunyikan
       ulangan OSN-P dari siswa yang menyetel OSN-K justru membuat ia melupakan
       jurus yang sudah susah payah dikuasainya. */
    var ulang = Inti.jurusPerluDiulang(k);
    if (ulang.length) {
      return '<div class="ajakan">' +
        '<p><strong>' + ulang.length + ' jurus</strong> perlu diulang hari ini.</p>' +
        '<a class="tombol" href="latihan.html">Mulai sesi hari ini</a>' +
      '</div>';
    }

    /* Saran jurus berikutnya sebaliknya memang ikut batas tahap: tidak ada
       gunanya mendorong siswa OSN-K membuka jurus tingkat OSN. */
    var terbuka = Inti.terbukaBelumDikuasai(k).filter(function (jid) {
      return dalamBatas(Inti.data.jurus[jid], batas);
    });
    if (terbuka.length) {
      var j = Inti.data.jurus[terbuka[0]];
      return '<div class="ajakan tenang">' +
        '<p>Tidak ada yang jatuh tempo. Lanjutkan ke <strong>' +
          Inti.lolos(j.nama) + '</strong>.</p>' +
        '<a class="tombol" href="jurus.html?id=' + encodeURIComponent(j.id) + '">Buka jurus</a>' +
      '</div>';
    }
    return '<div class="ajakan tenang"><p>Semua jurus yang terbuka sudah dikuasai, ' +
           'dan belum ada yang jatuh tempo. Istirahat dulu.</p></div>';
  }

  function gambarKendali(pilarAktif, batas) {
    /* Satu bidang tidak perlu tab — barisnya cuma jadi hiasan yang tak bisa
       ditekan. Ia muncul sendiri begitu bidang kedua masuk. */
    var tab = urutPilar.length < 2 ? '' :
      '<div class="tab-pilar" role="tablist" aria-label="Bidang">' +
        urutPilar.map(function (p) {
          var aktif = p === pilarAktif;
          return '<button type="button" role="tab" data-pilar="' + Inti.lolos(p) + '" ' +
                 'class="tab' + (aktif ? ' aktif' : '') + '" ' +
                 'aria-selected="' + aktif + '">' + Inti.lolos(namaPilar(p)) + '</button>';
        }).join('') +
      '</div>';

    var pilihan = URUT_TAHAP.map(function (t) {
      return '<option value="' + t + '"' + (t === batas ? ' selected' : '') + '>' +
             NAMA_TAHAP[t] + '</option>';
    }).join('');

    return '<div class="kendali-peta">' + tab +
      '<p class="saring"><label for="saring-tahap">Tampilkan sampai tahap</label> ' +
        '<select id="saring-tahap">' + pilihan + '</select></p>' +
    '</div>';
  }

  function gambar() {
    var t = Inti.tampilan();
    var batas = URUT_TAHAP.indexOf(t.tahap) < 0 ? 'osn' : t.tahap;
    /* Pilihan yang tersimpan bisa menunjuk bidang yang sudah tidak ada lagi. */
    var pilarAktif = perPilar[t.pilar] ? t.pilar : urutPilar[0];

    var k = Inti.kemajuan();
    document.getElementById('isi').innerHTML =
      gambarAjakan(k, batas) +
      gambarKendali(pilarAktif, batas) +
      gambarPilar(pilarAktif, k, batas);

    var tabs = document.querySelectorAll('.tab-pilar .tab');
    Array.prototype.forEach.call(tabs, function (b) {
      b.addEventListener('click', function () {
        Inti.simpanTampilan({ pilar: b.getAttribute('data-pilar'), tahap: batas });
        gambar();
      });
    });

    document.getElementById('saring-tahap').addEventListener('change', function (e) {
      Inti.simpanTampilan({ pilar: pilarAktif, tahap: e.target.value });
      gambar();
    });
  }

  function jalan() {
    Inti.data.urutJurus.forEach(function (jid) {
      var j = Inti.data.jurus[jid];
      if (!perPilar[j.pilar]) {
        perPilar[j.pilar] = [];
        urutPilar.push(j.pilar);
      }
      perPilar[j.pilar].push(j);
    });
    gambar();
  }

  Inti.pasangKepala('index.html');
  /* Halaman ini tidak menyentuh data.soal sama sekali — status, gembok, dan ajakan
     semuanya dihitung dari jurus dan kemajuan. */
  Inti.muatData({ soal: false }).then(jalan).catch(function (e) { Inti.galat(e.message); });
})();
