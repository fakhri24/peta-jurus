/* Halaman satu jurus. Susunannya selalu lima bagian yang sama, tidak pernah
   berubah urutannya — supaya siswa hafal di mana mencari apa. */

(function () {
  'use strict';

  var NAMA_TAHAP = { 'osn-k': 'OSN-K', 'osn-p': 'OSN-P', 'osn': 'OSN' };
  var NAMA_PILAR = {
    'teori-bilangan': 'Teori Bilangan',
    'aljabar': 'Aljabar',
    'geometri': 'Geometri',
    'kombinatorika': 'Kombinatorika'
  };
  var NAMA_STATUS = {
    'terkunci': 'terkunci',
    'terbuka': 'belum disentuh',
    'dipelajari': 'sedang dipelajari',
    'dikuasai': 'dikuasai',
    'perlu-diulang': 'perlu diulang'
  };

  function tautanJurus(jid) {
    var j = Inti.data.jurus[jid];
    if (!j) return Inti.lolos(jid);
    return '<a href="jurus.html?id=' + encodeURIComponent(jid) + '">' +
           Inti.lolos(j.nama) + '</a>';
  }

  function gembok(j, k) {
    var kurang = j.prasyarat.filter(function (p) {
      var c = k.jurus[p];
      return !c || c.status !== 'dikuasai';
    });
    if (!kurang.length) return '';
    return '<div class="gembok">' +
      '<p><strong>Jurus ini masih terkunci.</strong> Prasyaratnya belum dikuasai: ' +
      kurang.map(tautanJurus).join(', ') + '.</p>' +
      '<p class="samar">Kamu tetap boleh membacanya. Tapi urutannya ada alasannya — ' +
      'tanpa prasyarat itu, latihannya kemungkinan besar terasa buntu.</p>' +
    '</div>';
  }

  function ringkasJejak(soalId, k) {
    var r = Inti.riwayatSoal(soalId, k);
    if (!r.length) return '<span class="jejak sangat-samar">belum</span>';
    var terakhir = r[r.length - 1];
    var kelas = terakhir.benar ? 'benar' : 'salah';
    var tanda = terakhir.benar ? '✓' : '✗';
    return '<span class="jejak ' + kelas + '">' + tanda +
           (r.length > 1 ? ' ×' + r.length : '') + '</span>';
  }

  function daftarLatihan(j, k) {
    if (!j.latihan.length) {
      return '<p class="samar">Latihan untuk jurus ini belum ditulis.</p>';
    }
    var butir = j.latihan.map(function (sid) {
      var s = Inti.data.soal[sid];
      if (!s) return '';
      return '<li>' +
        '<span class="kesulitan">' + Inti.bintangKesulitan(s.kesulitan) + '</span>' +
        '<span class="sumber"><a href="latihan.html?soal=' + encodeURIComponent(sid) + '">' +
          Inti.lolos(s.sumber) + '</a>' +
          (s.bentuk === 'uraian' ? ' <span class="sangat-samar">uraian</span>' : '') +
        '</span>' +
        ringkasJejak(sid, k) +
      '</li>';
    }).join('');
    return '<ul class="daftar-soal">' + butir + '</ul>';
  }

  function pasangContoh(j) {
    var wadah = document.getElementById('contoh');
    if (!wadah) return;
    if (!j.contoh.length) {
      wadah.innerHTML = '<p class="samar">Contoh terpandu untuk jurus ini belum ditulis.</p>';
      return;
    }
    j.contoh.forEach(function (sid, i) {
      var s = Inti.data.soal[sid];
      if (!s) return;
      var kartu = document.createElement('div');
      kartu.className = 'kartu';
      kartu.innerHTML =
        '<span class="label-pilar">Contoh ' + (i + 1) + '</span>' +
        '<div class="soal-teks">' + s.soal + '</div>';
      wadah.appendChild(kartu);
      SoalUI.tanggaPetunjuk(s, kartu, {});
      Inti.renderRumus(kartu);
    });
  }

  function gambar() {
    var id = new URLSearchParams(location.search).get('id');
    var j = Inti.data.jurus[id];
    if (!j) {
      Inti.galat('Jurus "' + (id || '') + '" tidak ada. Kembali ke peta.');
      return;
    }

    document.title = j.nama + ' — Peta Jurus';
    var k = Inti.kemajuan();
    var status = Inti.statusJurus(id, k);
    var c = k.jurus[id];

    var jadwal = '';
    if (c && c.ulang_pada) {
      jadwal = status === 'perlu-diulang'
        ? ' · <span style="color:var(--merah)">jatuh tempo ' + c.ulang_pada + '</span>'
        : ' · ulang ' + c.ulang_pada;
    }

    document.getElementById('isi').innerHTML =
      '<p class="label-pilar">' + Inti.lolos(NAMA_PILAR[j.pilar] || j.pilar) +
        ' · ' + (NAMA_TAHAP[j.tahap] || j.tahap) + '</p>' +
      '<h1>' + Inti.lolos(j.nama) + '</h1>' +
      '<p class="samar">Status: ' + NAMA_STATUS[status] + jadwal +
        (j.prasyarat.length
          ? ' · prasyarat: ' + j.prasyarat.map(tautanJurus).join(', ')
          : ' · tanpa prasyarat') +
      '</p>' +

      gembok(j, k) +

      '<div class="pemicu">' +
        '<span class="label-pilar">Kapan dipakai</span>' + j.kapan_dipakai +
      '</div>' +

      '<section><h2>Intinya</h2>' + j.inti + '</section>' +

      '<section class="renggang"><h2>Contoh terpandu</h2>' +
        '<div id="contoh"></div>' +
      '</section>' +

      '<section class="renggang"><h2>Latihan berjenjang</h2>' +
        daftarLatihan(j, k) +
        (j.latihan.length
          ? '<p class="renggang"><a class="tombol" href="latihan.html?jurus=' +
            encodeURIComponent(id) + '">Kerjakan berurutan</a></p>'
          : '') +
      '</section>' +

      (j.jebakan
        ? '<section class="renggang"><h2>Jebakan umum</h2>' + j.jebakan + '</section>'
        : '') +

      '<p class="renggang"><a href="index.html">← Kembali ke peta</a></p>';

    pasangContoh(j);
    Inti.renderRumus(document.getElementById('isi'));
  }

  Inti.pasangKepala('');
  /* Halaman ini hanya menampilkan satu jurus, jadi cukup soal bidangnya sendiri. */
  Inti.muatData({
    soal: function (d) {
      var j = d.jurus[new URLSearchParams(location.search).get('id')];
      return j ? [j.pilar] : [];
    }
  }).then(gambar).catch(function (e) { Inti.galat(e.message); });
})();
