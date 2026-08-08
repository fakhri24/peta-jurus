/* Halaman latihan. Tiga cara masuk:

     latihan.html                sesi hari ini — jurus yang jatuh tempo dulu
     latihan.html?jurus=ID       kerjakan satu jurus berurutan
     latihan.html?soal=ID        satu soal saja

   Pembahasan dikunci sampai semua petunjuk dibuka — tapi begitu siswa menekan
   "Jawab", kuncinya lepas. Gerbangnya ada untuk mencegah mengintip sebelum
   mencoba, bukan untuk menahan penjelasan dari orang yang sudah mencoba. */

(function () {
  'use strict';

  var MAKS_SESI = 6;

  var antrean = [];
  var indeks = 0;
  var judulSesi = '';

  var soalKini = null;
  var tangga = null;
  var mulai = 0;
  var dijawab = false;

  // ---------------------------------------------------------------- antrean

  function dariJurus(jid, k) {
    var j = Inti.data.jurus[jid];
    if (!j) return [];
    return j.latihan
      .map(function (id) { return Inti.data.soal[id]; })
      .filter(Boolean)
      .sort(function (a, b) { return a.kesulitan - b.kesulitan; });
  }

  function belumDikerjakan(daftar, k) {
    return daftar.filter(function (s) { return !Inti.sudahDikerjakan(s.id, k); });
  }

  function bangunAntrean() {
    var p = new URLSearchParams(location.search);
    var k = Inti.kemajuan();

    var sid = p.get('soal');
    if (sid) {
      var s = Inti.data.soal[sid];
      judulSesi = 'Satu soal';
      return s ? [s] : [];
    }

    var jid = p.get('jurus');
    if (jid) {
      var j = Inti.data.jurus[jid];
      judulSesi = j ? j.nama : jid;
      return dariJurus(jid, k);
    }

    /* Sesi hari ini. Yang jatuh tempo lebih dulu, satu soal per jurus —
       menumpuk lima soal dari satu jurus yang sama tidak menguji ingatan,
       hanya menguji stamina. */
    var ulang = Inti.jurusPerluDiulang(k);
    if (ulang.length) {
      judulSesi = 'Ulangan hari ini';
      return ulang.map(function (id) { return Inti.soalBerikutnya(id, k); })
                  .filter(Boolean)
                  .slice(0, MAKS_SESI);
    }

    var terbuka = Inti.terbukaBelumDikuasai(k);
    for (var i = 0; i < terbuka.length; i++) {
      var segar = belumDikerjakan(dariJurus(terbuka[i], k), k);
      if (segar.length) {
        judulSesi = Inti.data.jurus[terbuka[i]].nama;
        return segar.slice(0, MAKS_SESI);
      }
    }
    judulSesi = '';
    return [];
  }

  // ---------------------------------------------------------------- tampilan

  function el(id) { return document.getElementById(id); }

  function tampilkanSelesai() {
    var kembali = new URLSearchParams(location.search).get('jurus');
    el('isi').innerHTML =
      '<h1>Sesi selesai</h1>' +
      '<p>' + antrean.length + ' soal dikerjakan. Jadwal ulangnya sudah diperbarui.</p>' +
      '<p class="baris renggang">' +
        '<a class="tombol" href="index.html">Lihat peta</a>' +
        '<a class="tombol" href="jurnal.html">Buka jurnal salah</a>' +
        (kembali
          ? '<a class="tombol" href="jurus.html?id=' + encodeURIComponent(kembali) + '">Kembali ke jurus</a>'
          : '') +
      '</p>';
  }

  function tampilkanKosong() {
    el('isi').innerHTML =
      '<h1>Belum ada yang perlu dikerjakan</h1>' +
      '<p>Tidak ada jurus yang jatuh tempo, dan latihan di jurus yang terbuka ' +
      'sudah habis kamu kerjakan.</p>' +
      '<p class="samar">Buka jurus berikutnya dari peta, atau tunggu jadwal ulangan ' +
      'berikutnya jatuh tempo.</p>' +
      '<p class="renggang"><a class="tombol" href="index.html">Lihat peta</a></p>';
  }

  function namaJurusSoal(s) {
    return s.jurus.map(function (jid) {
      var j = Inti.data.jurus[jid];
      return j
        ? '<a href="jurus.html?id=' + encodeURIComponent(jid) + '">' + Inti.lolos(j.nama) + '</a>'
        : Inti.lolos(jid);
    }).join(', ');
  }

  function tampilkanSoal() {
    soalKini = antrean[indeks];
    dijawab = false;
    mulai = Date.now();

    var isian = soalKini.bentuk === 'isian';

    el('isi').innerHTML =
      '<p class="label-pilar">' + Inti.lolos(judulSesi) +
        ' · soal ' + (indeks + 1) + ' dari ' + antrean.length + '</p>' +
      '<h1>' + Inti.lolos(soalKini.sumber) + '</h1>' +
      '<p class="samar">Jurus: ' + namaJurusSoal(soalKini) +
        ' · tingkat kesulitan <span class="kesulitan">' +
        Inti.bintangKesulitan(soalKini.kesulitan) + '</span></p>' +

      '<div class="kartu">' +
        '<div class="soal-teks" id="teks-soal">' + soalKini.soal + '</div>' +
      '</div>' +

      (isian
        ? '<div class="baris" id="kotak-jawab">' +
            '<input type="text" id="jawaban" placeholder="jawaban" ' +
              'autocomplete="off" autocapitalize="off" spellcheck="false">' +
            '<button class="utama" id="kirim">Jawab</button>' +
          '</div>'
        : '<div class="kartu"><p class="samar">Soal uraian. Kerjakan dulu di kertas — ' +
          'tulis pembuktiannya utuh. Kalau sudah, buka rubriknya dan nilai sendiri ' +
          'dengan jujur.</p>' +
          '<button class="utama" id="nilai-sendiri">Saya sudah mengerjakan</button></div>') +

      '<div id="hasil"></div>' +
      '<div id="petunjuk-wadah"></div>';

    tangga = SoalUI.tanggaPetunjuk(soalKini, el('petunjuk-wadah'), {});
    Inti.renderRumus(el('isi'));

    if (isian) {
      el('kirim').addEventListener('click', jawabIsian);
      el('jawaban').addEventListener('keydown', function (e) {
        if (e.key === 'Enter') jawabIsian();
      });
      el('jawaban').focus();
    } else {
      el('nilai-sendiri').addEventListener('click', bukaRubrik);
    }
  }

  // ---------------------------------------------------------------- menjawab

  function detik() { return (Date.now() - mulai) / 1000; }

  function selesaikan(benar, tambahan) {
    dijawab = true;
    // Hitung petunjuk direkam SEBELUM pembahasan dibuka, kalau tidak jumlahnya
    // ikut melonjak ke jumlah petunjuk penuh.
    Inti.catatJawaban(soalKini.id, benar, tangga.dibuka(), detik());
    tangga.bukaPembahasan();

    var kotak = el('hasil');
    kotak.innerHTML = '<div class="hasil ' + (benar ? 'benar' : 'salah') + '">' +
      (benar ? '✓ Benar.' : '✗ Belum benar.') + (tambahan || '') + '</div>';

    if (benar) lanjutkan(kotak);
    else tanyaSebab(kotak);
  }

  function jawabIsian() {
    if (dijawab) return;
    var isi = el('jawaban').value;
    if (!isi.trim()) return;
    el('jawaban').disabled = true;
    el('kirim').disabled = true;
    var benar = Inti.periksaJawaban(soalKini, isi);
    selesaikan(benar, benar ? '' :
      ' Jawaban yang benar: <span class="mono">' + Inti.lolos(soalKini.jawaban) + '</span>');
  }

  function bukaRubrik() {
    if (dijawab) return;
    el('nilai-sendiri').disabled = true;
    // Direkam sekarang: sebentar lagi pembahasannya dibuka, dan itu memaksa
    // penghitung petunjuk ke angka penuh.
    var petunjukDipakai = tangga.dibuka();

    var butir = soalKini.rubrik.map(function (r, i) {
      return '<li><input type="checkbox" id="r' + i + '"><label for="r' + i + '">' +
             r + '</label></li>';
    }).join('');

    el('hasil').innerHTML =
      '<div class="kartu">' +
        '<h3>Rubrik — centang langkah yang benar-benar ada di lembar jawabmu</h3>' +
        '<ul class="rubrik">' + butir + '</ul>' +
        '<p class="baris renggang">' +
          '<button class="utama" id="simpan-nilai">Simpan penilaian</button>' +
          '<span class="samar" id="hitung-centang"></span>' +
        '</p>' +
      '</div>';
    Inti.renderRumus(el('hasil'));
    tangga.bukaPembahasan();

    var kotak = el('hitung-centang');
    function hitung() {
      var n = el('hasil').querySelectorAll('input:checked').length;
      kotak.textContent = n + ' dari ' + soalKini.rubrik.length + ' langkah';
      return n;
    }
    hitung();
    el('hasil').addEventListener('change', hitung);

    el('simpan-nilai').addEventListener('click', function () {
      var benar = hitung() === soalKini.rubrik.length;
      dijawab = true;
      Inti.catatJawaban(soalKini.id, benar, petunjukDipakai, detik());
      var pesan = document.createElement('div');
      pesan.className = 'hasil ' + (benar ? 'benar' : 'salah');
      pesan.textContent = benar
        ? '✓ Lengkap. Tersimpan.'
        : '✗ Ada langkah yang terlewat. Tersimpan sebagai belum benar.';
      el('hasil').appendChild(pesan);
      el('simpan-nilai').disabled = true;
      if (benar) lanjutkan(el('hasil'));
      else tanyaSebab(el('hasil'));
    });
  }

  // ---------------------------------------------------------------- jurnal salah

  function tanyaSebab(kotak) {
    var tombol = Object.keys(Inti.SEBAB).map(function (kode) {
      return '<button data-sebab="' + kode + '">' + Inti.SEBAB[kode] + '</button>';
    }).join('');

    var blok = document.createElement('div');
    blok.className = 'kartu renggang';
    blok.innerHTML =
      '<h3>Kenapa salah?</h3>' +
      '<p class="samar">Satu ketukan. Rekapnya nanti yang memberi tahu kamu harus ' +
      'memperbaiki apa — bukan soal berikutnya.</p>' +
      '<div class="sebab">' + tombol + '</div>';
    kotak.appendChild(blok);

    blok.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-sebab]');
      if (!b) return;
      Inti.catatSalah(soalKini.id, b.dataset.sebab, '');
      blok.innerHTML = '<p class="samar">Tercatat sebagai <strong>' +
        Inti.SEBAB[b.dataset.sebab] + '</strong> di jurnal salah.</p>';
      lanjutkan(kotak);
    });
  }

  // ---------------------------------------------------------------- lanjut

  function lanjutkan(kotak) {
    var baris = document.createElement('p');
    baris.className = 'baris renggang';
    var t = document.createElement('button');
    t.className = 'utama';
    t.textContent = indeks + 1 < antrean.length ? 'Soal berikutnya' : 'Selesaikan sesi';
    t.addEventListener('click', function () {
      indeks += 1;
      if (indeks < antrean.length) {
        tampilkanSoal();
        window.scrollTo(0, 0);
      } else {
        tampilkanSelesai();
      }
    });
    baris.appendChild(t);
    kotak.appendChild(baris);
    t.focus();
  }

  // ---------------------------------------------------------------- mulai

  function jalan() {
    antrean = bangunAntrean();
    if (!antrean.length) { tampilkanKosong(); return; }
    tampilkanSoal();
  }

  Inti.pasangKepala('latihan.html');
  Inti.muatData().then(jalan).catch(function (e) { Inti.galat(e.message); });
})();
