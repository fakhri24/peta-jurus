/* Simulasi ujian. Semua soal tampil sekaligus seperti naskah asli, timer jalan,
   dan petunjuk dimatikan — tidak ada tangga petunjuk di halaman ini sama sekali.

   Jumlah soal dan lama waktunya diatur sendiri, bukan ditetapkan di kode.
   Format resmi OSN berubah dari tahun ke tahun; menanamkan satu angka di sini
   hanya akan jadi klaim yang cepat basi. */

(function () {
  'use strict';

  var TAHAP = { 'osn-k': 'OSN-K', 'osn-p': 'OSN-P', 'osn': 'OSN' };

  var antrean = [];
  var mulai = 0;
  var batasDetik = 0;
  var jamId = null;
  var selesai = false;

  function el(id) { return document.getElementById(id); }

  function acak(daftar) {
    var a = daftar.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* Naskah dibagi rata antar bidang, bukan diacak dari satu kolam.

     Mengacak satu kolam terdengar adil, tapi hasilnya ditentukan oleh bidang mana
     yang kebetulan punya soal paling banyak: naskah 10 soal bisa keluar 8 teori
     bilangan dan 2 aljabar, dan siswa yang mengerjakannya tidak sedang berlatih
     ujian campuran. Begitu bidangnya jadi empat, keadaannya makin timpang.

     Caranya sengaja bergiliran satu-satu, bukan menghitung kuota per bidang:
     bidang yang kehabisan soal berhenti ikut dan jatahnya jatuh ke bidang lain,
     jadi naskahnya tetap penuh meski satu bidang masih tipis — yang pasti terjadi
     setiap kali bidang baru dibuka. Tidak ada kuota yang perlu dijaga tetap
     berjumlah 100%. */
  function susunNaskah(kolam, jumlah) {
    var perPilar = {};
    kolam.forEach(function (s) {
      (perPilar[s.pilar] = perPilar[s.pilar] || []).push(s);
    });

    /* Urutan bidang ikut diacak. Tanpa itu sisa pembagian selalu jatuh ke bidang
       yang sama — 8 soal untuk 3 bidang berarti satu bidang selalu dapat lebih. */
    var antre = acak(Object.keys(perPilar)).map(function (p) { return acak(perPilar[p]); });

    var terpilih = [];
    while (terpilih.length < jumlah) {
      var adaYangKeluar = false;
      for (var i = 0; i < antre.length && terpilih.length < jumlah; i++) {
        if (antre[i].length) {
          terpilih.push(antre[i].pop());
          adaYangKeluar = true;
        }
      }
      if (!adaYangKeluar) break;  // seluruh kolam habis sebelum jumlahnya terpenuhi
    }

    return terpilih.sort(function (a, b) { return a.kesulitan - b.kesulitan; });
  }

  function jamTeks(sisa) {
    var m = Math.floor(Math.abs(sisa) / 60);
    var d = Math.abs(sisa) % 60;
    return (sisa < 0 ? '-' : '') + m + ':' + String(d).padStart(2, '0');
  }

  // ---------------------------------------------------------------- persiapan

  function tampilkanPersiapan() {
    var tersedia = {};
    var bidang = {};
    Object.keys(Inti.data.soal).forEach(function (sid) {
      var s = Inti.data.soal[sid];
      tersedia[s.tahap] = (tersedia[s.tahap] || 0) + 1;
      bidang[s.pilar] = true;
    });
    var jumlahBidang = Object.keys(bidang).length;

    var pilihanTahap = ['semua'].concat(Object.keys(TAHAP)).map(function (t) {
      var n = t === 'semua' ? Object.keys(Inti.data.soal).length : (tersedia[t] || 0);
      if (!n) return '';
      return '<option value="' + t + '">' + (t === 'semua' ? 'Semua tahap' : TAHAP[t]) +
             ' (' + n + ' soal)</option>';
    }).join('');

    el('isi').innerHTML =
      '<h1>Simulasi ujian</h1>' +
      '<p>Semua soal tampil sekaligus, timer berjalan, dan petunjuk dimatikan. ' +
      'Kerjakan seperti ujian sungguhan — di kertas, tanpa membuka jurus.</p>' +

      '<div class="kartu">' +
        '<p class="baris"><label for="tahap">Tahap</label> ' +
          '<select id="tahap">' + pilihanTahap + '</select></p>' +
        '<p class="baris"><label for="jumlah">Jumlah soal</label> ' +
          '<select id="jumlah"><option>5</option><option selected>8</option>' +
          '<option>10</option><option>15</option></select></p>' +
        '<p class="baris"><label for="menit">Waktu (menit)</label> ' +
          '<select id="menit"><option>30</option><option selected>90</option>' +
          '<option>120</option><option>150</option><option>210</option></select></p>' +
        '<p class="renggang"><button class="utama" id="mulai">Mulai simulasi</button></p>' +
      '</div>' +

      '<p class="sangat-samar">Jumlah soal dan lama waktunya kamu atur sendiri. ' +
      'Samakan dengan naskah tahun yang sedang kamu latih.' +
      (jumlahBidang > 1
        ? ' Naskahnya dibagi rata antar ' + jumlahBidang + ' bidang yang sudah terisi, ' +
          'bukan diacak dari satu tumpukan — jadi kamu tidak akan dapat naskah yang ' +
          'isinya nyaris satu bidang saja.'
        : '') +
      '</p>';

    el('mulai').addEventListener('click', mulaiSimulasi);
  }

  // ---------------------------------------------------------------- jalannya ujian

  function mulaiSimulasi() {
    var tahap = el('tahap').value;
    var jumlah = Number(el('jumlah').value);
    batasDetik = Number(el('menit').value) * 60;

    var kolam = Object.keys(Inti.data.soal)
      .map(function (sid) { return Inti.data.soal[sid]; })
      .filter(function (s) { return tahap === 'semua' || s.tahap === tahap; });

    if (!kolam.length) {
      alert('Belum ada soal untuk tahap itu.');
      return;
    }

    antrean = susunNaskah(kolam, jumlah);

    mulai = Date.now();
    selesai = false;
    gambarLembar();
    jamId = setInterval(perbaruiJam, 1000);
    perbaruiJam();
  }

  function gambarLembar() {
    var butir = antrean.map(function (s, i) {
      return '<div class="kartu">' +
        '<span class="label-pilar">Soal ' + (i + 1) + ' · ' +
          (TAHAP[s.tahap] || s.tahap) + ' · ' +
          '<span class="kesulitan">' + Inti.bintangKesulitan(s.kesulitan) + '</span></span>' +
        '<div class="soal-teks">' + s.soal + '</div>' +
        (s.bentuk === 'isian'
          ? '<p class="baris"><input type="text" data-soal="' + s.id + '" ' +
            'placeholder="jawaban" autocomplete="off" spellcheck="false"></p>'
          : '<p class="samar">Uraian — tulis pembuktiannya di kertas. Dinilai sendiri ' +
            'dengan rubrik setelah waktu habis.</p>') +
      '</div>';
    }).join('');

    el('isi').innerHTML =
      '<div class="ajakan"><p><strong>Simulasi berjalan.</strong> ' +
        'Jangan buka halaman jurus.</p>' +
        '<span class="jam" id="jam">—</span>' +
        '<button class="utama" id="kumpulkan">Kumpulkan</button>' +
      '</div>' + butir +
      '<p class="renggang"><button class="utama" id="kumpulkan-bawah">Kumpulkan</button></p>';

    Inti.renderRumus(el('isi'));
    el('kumpulkan').addEventListener('click', konfirmasiKumpul);
    el('kumpulkan-bawah').addEventListener('click', konfirmasiKumpul);
  }

  function perbaruiJam() {
    var sisa = batasDetik - Math.floor((Date.now() - mulai) / 1000);
    var jam = el('jam');
    if (!jam) return;
    jam.textContent = jamTeks(sisa);
    jam.classList.toggle('mepet', sisa <= 300);
    if (sisa <= 0 && !selesai) kumpulkan(true);
  }

  function konfirmasiKumpul() {
    if (confirm('Kumpulkan sekarang? Jawaban tidak bisa diubah lagi.')) kumpulkan(false);
  }

  // ---------------------------------------------------------------- penilaian

  function kumpulkan(habisWaktu) {
    if (selesai) return;
    selesai = true;
    clearInterval(jamId);

    var jawaban = {};
    document.querySelectorAll('input[data-soal]').forEach(function (i) {
      jawaban[i.dataset.soal] = i.value;
    });

    var terpakai = Math.min((Date.now() - mulai) / 1000, batasDetik);
    var perSoal = terpakai / antrean.length;

    var benarOtomatis = 0;
    var jumlahIsian = 0;

    var butir = antrean.map(function (s, i) {
      if (s.bentuk === 'isian') {
        jumlahIsian += 1;
        var benar = Inti.periksaJawaban(s, jawaban[s.id] || '');
        if (benar) benarOtomatis += 1;
        Inti.catatJawaban(s.id, benar, 0, perSoal);
        return '<div class="kartu">' +
          '<span class="label-pilar">Soal ' + (i + 1) + '</span>' +
          '<div class="hasil ' + (benar ? 'benar' : 'salah') + '">' +
            (benar ? '✓ Benar' : '✗ Salah — jawabmu "' +
              Inti.lolos(jawaban[s.id] || '(kosong)') + '", seharusnya "' +
              Inti.lolos(s.jawaban) + '"') +
          '</div>' +
          '<p class="baris"><a class="tombol" href="latihan.html?soal=' +
            encodeURIComponent(s.id) + '">Buka pembahasan</a>' +
            (benar ? '' : '<a class="tombol" href="jurnal.html">Catat sebabnya</a>') +
          '</p>' +
        '</div>';
      }
      return '<div class="kartu">' +
        '<span class="label-pilar">Soal ' + (i + 1) + ' · uraian</span>' +
        '<p class="samar">Nilai sendiri dengan rubriknya.</p>' +
        '<p class="baris"><a class="tombol" href="latihan.html?soal=' +
          encodeURIComponent(s.id) + '">Buka rubrik &amp; pembahasan</a></p>' +
      '</div>';
    }).join('');

    var jumlahUraian = antrean.length - jumlahIsian;

    el('isi').innerHTML =
      '<h1>' + (habisWaktu ? 'Waktu habis' : 'Simulasi selesai') + '</h1>' +
      '<div class="petak renggang">' +
        '<div class="kartu"><div class="angka-besar">' + benarOtomatis + '/' + jumlahIsian +
          '</div><div class="samar">isian singkat</div></div>' +
        '<div class="kartu"><div class="angka-besar">' + jamTeks(Math.floor(terpakai)) +
          '</div><div class="samar">waktu terpakai</div></div>' +
      '</div>' +
      (jumlahUraian
        ? '<p class="samar">' + jumlahUraian + ' soal uraian belum dinilai. Buka rubriknya ' +
          'satu per satu di bawah — nilai uraian tidak bisa diotomatiskan, dan itu ' +
          'memang bagian dari latihannya.</p>'
        : '') +
      butir +
      '<p class="renggang"><a class="tombol" href="simulasi.html">Simulasi lagi</a> ' +
        '<a class="tombol" href="jurnal.html">Buka jurnal</a></p>';

    Inti.renderRumus(el('isi'));
    window.scrollTo(0, 0);
  }

  window.addEventListener('beforeunload', function (e) {
    if (jamId && !selesai) { e.preventDefault(); e.returnValue = ''; }
  });

  Inti.pasangKepala('simulasi.html');
  /* Simulasi menyusun naskah dari seluruh kolam soal, jadi semua bidang dimuat. */
  Inti.muatData().then(tampilkanPersiapan).catch(function (e) { Inti.galat(e.message); });
})();
