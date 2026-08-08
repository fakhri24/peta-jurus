/* Jurnal salah. Halaman yang paling jarang dibuka siswa dan paling banyak
   mengubah hasil belajarnya.

   Rekap sebab di atas bukan hiasan: kalau sebagian besar salahnya "salah hitung",
   menambah jurus baru tidak akan menolong apa pun. */

(function () {
  'use strict';

  function el(id) { return document.getElementById(id); }

  function ringkasan(k) {
    var total = k.riwayat.length;
    var benar = k.riwayat.filter(function (r) { return r.benar; }).length;
    var dikuasai = Object.keys(k.jurus).filter(function (jid) {
      var s = Inti.statusJurus(jid, k);
      return s === 'dikuasai' || s === 'perlu-diulang';
    }).length;
    var persen = total ? Math.round(benar / total * 100) : 0;

    return '<div class="petak renggang">' +
      '<div class="kartu"><div class="angka-besar">' + total + '</div>' +
        '<div class="samar">soal dikerjakan</div></div>' +
      '<div class="kartu"><div class="angka-besar">' + persen + '%</div>' +
        '<div class="samar">benar</div></div>' +
      '<div class="kartu"><div class="angka-besar">' + dikuasai + '</div>' +
        '<div class="samar">jurus dikuasai</div></div>' +
    '</div>';
  }

  function rekapSebab(k) {
    var hitung = {};
    Object.keys(Inti.SEBAB).forEach(function (kode) { hitung[kode] = 0; });
    k.jurnal_salah.forEach(function (j) {
      if (hitung[j.sebab] !== undefined) hitung[j.sebab] += 1;
    });

    var total = k.jurnal_salah.length;
    if (!total) {
      return '<section class="renggang"><h2>Rekap sebab</h2>' +
        '<p class="samar">Belum ada kesalahan yang tercatat. Rekapnya muncul setelah ' +
        'kamu menandai sebab pada soal yang salah.</p></section>';
    }

    var urut = Object.keys(hitung).sort(function (a, b) { return hitung[b] - hitung[a]; });
    var puncak = hitung[urut[0]];

    var baris = urut.map(function (kode) {
      var n = hitung[kode];
      var lebar = puncak ? Math.round(n / puncak * 100) : 0;
      return '<li>' +
        '<span class="nama-sebab">' + Inti.SEBAB[kode] + '</span>' +
        '<span class="batang"><span style="width:' + lebar + '%"></span></span>' +
        '<span class="angka">' + n + '</span>' +
      '</li>';
    }).join('');

    var teratas = urut[0];
    var bagian = Math.round(hitung[teratas] / total * 100);
    var nasihat = {
      'salah-hitung': 'Sebagian besar salahmu bukan soal materi. Perlambat hitungan, ' +
        'dan biasakan cek ulang satu langkah terakhir sebelum menulis jawaban. ' +
        'Menambah jurus baru tidak akan menolong.',
      'tidak-tahu-jurus': 'Ini memang soal materi. Baca ulang bagian "Kapan dipakai" ' +
        'pada jurus-jurus yang sudah terbuka — bagian itu yang melatih pengenalan pemicu.',
      'macet-di-tengah': 'Pengenalan jurusmu sudah jalan; yang kurang jam terbang ' +
        'mengeksekusi. Perbanyak soal pada jurus yang sama, jangan buru-buru pindah.',
      'salah-baca': 'Bukan kemampuan, tapi kebiasaan. Coba tulis ulang apa yang ' +
        'ditanyakan dengan kalimatmu sendiri sebelum mulai menghitung.',
      'kehabisan-waktu': 'Latih dengan timer. Buka halaman Simulasi, jangan latihan santai.'
    };

    return '<section class="renggang"><h2>Rekap sebab</h2>' +
      '<ul class="rekap">' + baris + '</ul>' +
      '<div class="ajakan renggang"><p>' + bagian + '% kesalahanmu bertanda ' +
        '<strong>' + Inti.SEBAB[teratas] + '</strong>. ' + nasihat[teratas] + '</p></div>' +
    '</section>';
  }

  function daftarSalah(k) {
    if (!k.jurnal_salah.length) return '';
    var butir = k.jurnal_salah.slice().reverse().slice(0, 40).map(function (j) {
      var s = Inti.data.soal[j.soal];
      return '<li>' +
        '<span class="sumber">' +
          (s
            ? '<a href="latihan.html?soal=' + encodeURIComponent(j.soal) + '">' +
              Inti.lolos(s.sumber) + '</a>'
            : Inti.lolos(j.soal)) +
          ' <span class="sangat-samar">' + Inti.SEBAB[j.sebab] + '</span>' +
        '</span>' +
        '<span class="jejak sangat-samar">' + j.pada + '</span>' +
      '</li>';
    }).join('');

    return '<section class="renggang"><h2>Kesalahan terakhir</h2>' +
      '<ul class="daftar-soal">' + butir + '</ul>' +
      (k.jurnal_salah.length > 40
        ? '<p class="sangat-samar">Menampilkan 40 terakhir dari ' + k.jurnal_salah.length + '.</p>'
        : '') +
    '</section>';
  }

  function jadwal(k) {
    var mendatang = Object.keys(k.jurus)
      .filter(function (jid) { return k.jurus[jid].ulang_pada && Inti.data.jurus[jid]; })
      .sort(function (a, b) {
        return k.jurus[a].ulang_pada < k.jurus[b].ulang_pada ? -1 : 1;
      });

    if (!mendatang.length) return '';

    var hari = Inti.hariIni();
    var butir = mendatang.map(function (jid) {
      var c = k.jurus[jid];
      var tempo = c.ulang_pada <= hari;
      return '<li>' +
        '<span class="sumber"><a href="jurus.html?id=' + encodeURIComponent(jid) + '">' +
          Inti.lolos(Inti.data.jurus[jid].nama) + '</a></span>' +
        '<span class="jejak' + (tempo ? ' salah' : ' sangat-samar') + '">' +
          (tempo ? 'jatuh tempo ' : '') + c.ulang_pada + '</span>' +
      '</li>';
    }).join('');

    return '<section class="renggang"><h2>Jadwal ulangan</h2>' +
      '<ul class="daftar-soal">' + butir + '</ul>' +
      '<p class="sangat-samar">Anak tangga: ' + Inti.TANGGA.join(' → ') + ' hari. ' +
      'Benar naik satu tangga, salah turun ke dasar.</p>' +
    '</section>';
  }

  var PINDAHAN =
    '<section class="renggang"><h2>Pindah perangkat</h2>' +
      '<p class="samar">Kemajuanmu hanya tersimpan di peramban ini — tidak ada server ' +
      'di mana pun. Untuk memindahkannya, ekspor di sini lalu impor di perangkat lain.</p>' +
      '<p class="baris">' +
        '<button id="ekspor">Ekspor cadangan</button>' +
        '<button id="impor">Impor cadangan</button>' +
        '<button class="bahaya" id="hapus">Hapus semua kemajuan</button>' +
      '</p>' +
      '<input type="file" id="berkas" accept="application/json,.json" hidden>' +
    '</section>';

  function pasangTombol() {
    el('ekspor').addEventListener('click', Inti.ekspor);
    el('impor').addEventListener('click', function () { el('berkas').click(); });

    el('berkas').addEventListener('change', function (e) {
      var f = e.target.files[0];
      if (!f) return;
      var pembaca = new FileReader();
      pembaca.onload = function () {
        try {
          Inti.impor(pembaca.result);
          location.reload();
        } catch (err) {
          alert('Gagal mengimpor: ' + err.message);
        }
      };
      pembaca.readAsText(f);
    });

    el('hapus').addEventListener('click', function () {
      if (!confirm('Hapus seluruh kemajuan di peramban ini? Tidak bisa dibatalkan. ' +
                   'Ekspor dulu kalau belum.')) return;
      Inti.hapusSemua();
      location.reload();
    });
  }

  function gambar() {
    var k = Inti.kemajuan();
    el('isi').innerHTML =
      '<h1>Jurnal salah</h1>' +
      ringkasan(k) +
      rekapSebab(k) +
      daftarSalah(k) +
      jadwal(k) +
      PINDAHAN;
    Inti.renderRumus(el('isi'));
    pasangTombol();
  }

  Inti.pasangKepala('jurnal.html');
  /* Jurnal hanya menampilkan soal yang pernah dikerjakan siswa, jadi bidangnya
     diturunkan dari riwayat dan jurnal salahnya sendiri. */
  Inti.muatData({
    soal: function () {
      var k = Inti.kemajuan();
      return Inti.pilarDariSoal(
        k.riwayat.map(function (r) { return r.soal; })
          .concat(k.jurnal_salah.map(function (r) { return r.soal; }))
      );
    }
  }).then(gambar).catch(function (e) { Inti.galat(e.message); });
})();
