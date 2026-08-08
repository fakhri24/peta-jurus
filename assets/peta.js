/* Halaman peta. Koordinat simpul sudah dihitung scripts/build.py, jadi di sini
   tinggal menggambar SVG — tanpa pustaka graf apa pun. */

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

    var label = status === 'terkunci' ? 'terkunci — ' : '';

    return '<a href="jurus.html?id=' + encodeURIComponent(j.id) + '" ' +
             'class="simpul ' + status + '" ' +
             'aria-label="' + Inti.lolos(label + j.nama) + '">' +
             cincin +
             '<rect class="kotak" x="' + j.x + '" y="' + j.y + '" width="' + LEBAR +
               '" height="' + TINGGI + '"></rect>' +
             '<text class="judul" text-anchor="middle">' + teks + '</text>' +
             '<text class="tanda" x="' + (j.x + 10) + '" y="' + (j.y + TINGGI - 10) + '">' +
               (NAMA_TAHAP[j.tahap] || j.tahap) + '</text>' +
             '<text class="tanda" x="' + (j.x + LEBAR - 10) + '" y="' + (j.y + TINGGI - 10) +
               '" text-anchor="end">' + GLIF[status] + '</text>' +
           '</a>';
  }

  function gambarPilar(pilar, simpul, ukuran, k) {
    var status = {};
    simpul.forEach(function (j) { status[j.id] = Inti.statusJurus(j.id, k); });

    var tepi = simpul.map(function (j) {
      return j.prasyarat.map(function (p) {
        var dari = Inti.data.jurus[p];
        if (!dari || dari.pilar !== pilar) return '';
        return gambarTepi(dari, j, status[p] === 'dikuasai' || status[p] === 'perlu-diulang');
      }).join('');
    }).join('');

    var kotak = simpul.map(function (j) { return gambarSimpul(j, status[j.id]); }).join('');

    var dikuasai = simpul.filter(function (j) {
      return status[j.id] === 'dikuasai' || status[j.id] === 'perlu-diulang';
    }).length;

    return '<section class="renggang">' +
      '<h2>' + Inti.lolos(NAMA_PILAR[pilar] || pilar) + ' ' +
        '<span class="sangat-samar">' + dikuasai + ' dari ' + simpul.length + ' dikuasai</span></h2>' +
      '<div class="peta-bungkus">' +
        '<svg class="peta" width="' + ukuran.lebar + '" height="' + ukuran.tinggi +
          '" viewBox="0 0 ' + ukuran.lebar + ' ' + ukuran.tinggi + '" role="img" ' +
          'aria-label="Peta prasyarat ' + Inti.lolos(NAMA_PILAR[pilar] || pilar) + '">' +
          tepi + kotak +
        '</svg>' +
      '</div>' +
    '</section>';
  }

  function gambarAjakan(k) {
    var ulang = Inti.jurusPerluDiulang(k);
    if (ulang.length) {
      return '<div class="ajakan">' +
        '<p><strong>' + ulang.length + ' jurus</strong> perlu diulang hari ini.</p>' +
        '<a class="tombol" href="latihan.html">Mulai sesi hari ini</a>' +
      '</div>';
    }
    var terbuka = Inti.terbukaBelumDikuasai(k);
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

  var KUNCI_PETA =
    '<div class="kunci-peta">' +
      '<span><i class="k-terkunci"></i> terkunci</span>' +
      '<span><i></i> terbuka</span>' +
      '<span><i class="k-dipelajari"></i> sedang dipelajari</span>' +
      '<span><i class="k-dikuasai"></i> dikuasai</span>' +
      '<span><i class="k-ulang"></i> perlu diulang</span>' +
    '</div>';

  function gambar() {
    var k = Inti.kemajuan();
    var perPilar = {};
    Inti.data.urutJurus.forEach(function (jid) {
      var j = Inti.data.jurus[jid];
      (perPilar[j.pilar] = perPilar[j.pilar] || []).push(j);
    });

    var bagian = Object.keys(perPilar).map(function (pilar) {
      return gambarPilar(pilar, perPilar[pilar], Inti.data.ukuran[pilar], k);
    }).join('');

    document.getElementById('isi').innerHTML =
      gambarAjakan(k) + bagian + KUNCI_PETA;
  }

  Inti.pasangKepala('index.html');
  Inti.muatData().then(gambar).catch(function (e) { Inti.galat(e.message); });
})();
