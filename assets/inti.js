/* Peta Jurus — bagian yang dipakai semua halaman.
   Memuat data, menyimpan kemajuan di perangkat, menjadwalkan pengulangan,
   dan merender rumus. Tidak ada server di mana pun: seluruh kemajuan siswa
   hanya ada di localStorage peramban ini. */

var Inti = (function () {
  'use strict';

  var KUNCI = 'peta-jurus/kemajuan/v1';

  /* Pilihan tampilan peta — bidang yang sedang dibuka dan batas tahap. Sengaja
     di kunci sendiri, terpisah dari kemajuan: ini preferensi perangkat, bukan
     hasil belajar, dan tidak boleh ikut terbawa saat kemajuan diekspor lalu
     dipindah ke perangkat lain. */
  var KUNCI_TAMPILAN = 'peta-jurus/tampilan/v1';

  /* Anak tangga pengulangan, dalam hari. Benar naik satu tangga, salah turun
     ke dasar. Sengaja tanpa faktor kemudahan — cukup, dan bisa dijelaskan ke
     siswa dalam satu kalimat. */
  var TANGGA = [1, 3, 7, 21, 60];

  /* Berapa kali benar berturut-turut sampai sebuah jurus dianggap dikuasai. */
  var AMBANG_KUASAI = 2;

  var SEBAB = {
    'salah-hitung': 'Salah hitung',
    'tidak-tahu-jurus': 'Tidak tahu jurusnya',
    'macet-di-tengah': 'Tahu jurusnya, macet di tengah',
    'salah-baca': 'Salah baca soal',
    'kehabisan-waktu': 'Kehabisan waktu'
  };

  var data = { jurus: {}, soal: {}, ukuran: {}, urutJurus: [], pilarSoal: {} };

  // ---------------------------------------------------------------- tanggal

  function hariIni() {
    var d = new Date();
    return [
      d.getFullYear(),
      String(d.getMonth() + 1).padStart(2, '0'),
      String(d.getDate()).padStart(2, '0')
    ].join('-');
  }

  function tambahHari(tanggal, n) {
    var b = tanggal.split('-').map(Number);
    var d = new Date(b[0], b[1] - 1, b[2] + n);
    return [
      d.getFullYear(),
      String(d.getMonth() + 1).padStart(2, '0'),
      String(d.getDate()).padStart(2, '0')
    ].join('-');
  }

  // ---------------------------------------------------------------- data

  /* Halaman menyatakan bidang apa yang soalnya dipakai:

         Inti.muatData({ soal: false })            jurus saja, tanpa soal
         Inti.muatData()                           semua bidang
         Inti.muatData({ soal: ['aljabar'] })      bidang tertentu
         Inti.muatData({ soal: function (d) {…} }) bidang ditentukan setelah jurus termuat

     Soal dipecah per bidang di data/soal-<pilar>.json. Peta tidak menyentuh
     data.soal sama sekali; halaman jurus hanya perlu satu bidang; latihan dan
     jurnal perlu bidang yang benar-benar dirujuk kemajuan siswa.

     Bawaannya memuat semuanya, jadi halaman yang lupa menyatakan kebutuhannya
     tetap bekerja — hanya tidak hemat.

     jurus.json selalu diambil lebih dulu dan sendirian: peta soal→bidang
     diturunkan darinya, dan bentuk fungsi di atas butuh data itu untuk memutuskan.
     Karena itu pemuatannya berurutan, bukan sejajar. */
  function muatData(perlu) {
    var spek = (perlu && 'soal' in perlu) ? perlu.soal : 'semua';

    return fetch('data/jurus.json').then(function (r) { return r.json(); })
      .then(function (hasil) {
        data.ukuran = hasil.ukuran || {};
        data.urutJurus = [];
        hasil.simpul.forEach(function (j) {
          data.jurus[j.id] = j;
          data.urutJurus.push(j.id);
          /* Tiap soal terdaftar di tepat satu jurus, jadi bidangnya bisa
             diturunkan di sini tanpa berkas tambahan. */
          j.contoh.concat(j.latihan).forEach(function (sid) {
            data.pilarSoal[sid] = j.pilar;
          });
        });

        var pilar = pilihPilar(spek);
        if (!pilar.length) return data;

        return Promise.all(pilar.map(function (p) {
          return fetch('data/soal-' + p + '.json').then(function (r) { return r.json(); });
        })).then(function (bagian) {
          bagian.forEach(function (b) {
            b.soal.forEach(function (s) { data.soal[s.id] = s; });
          });
          return data;
        });
      }).catch(function (e) {
        // fetch() memang gagal di file:// — ini penyebab tersering.
        throw new Error(
          'Data tidak bisa dimuat. Kalau kamu membuka berkas ini langsung lewat ' +
          'file://, jalankan "python3 -m http.server" dulu lalu buka localhost. (' + e.message + ')'
        );
      });
  }

  /* Bidang yang benar-benar punya berkas soal. Bidang tanpa soal tidak dibangun
     berkasnya, jadi memintanya akan 404 dan menggagalkan seluruh pemuatan. */
  function pilarBersoal() {
    var ada = {};
    data.urutJurus.forEach(function (jid) {
      var j = data.jurus[jid];
      if (j.contoh.length || j.latihan.length) ada[j.pilar] = true;
    });
    return Object.keys(ada);
  }

  function pilihPilar(spek) {
    if (spek === false) return [];
    if (typeof spek === 'function') spek = spek(data);
    if (spek === 'semua' || spek === true || spek == null) return pilarBersoal();

    var punya = pilarBersoal();
    return (Array.isArray(spek) ? spek : [spek]).filter(function (p, i, a) {
      return punya.indexOf(p) >= 0 && a.indexOf(p) === i;
    });
  }

  /* Bidang mana saja yang memuat daftar soal ini — dipakai halaman yang bertolak
     dari id soal (jurnal, latihan?soal=…) alih-alih dari jurus. */
  function pilarDariSoal(ids) {
    var ada = {};
    (ids || []).forEach(function (sid) {
      var p = data.pilarSoal[sid];
      if (p) ada[p] = true;
    });
    return Object.keys(ada);
  }

  // ---------------------------------------------------------------- kemajuan

  function kosong() {
    return { jurus: {}, riwayat: [], jurnal_salah: [] };
  }

  function kemajuan() {
    try {
      var mentah = localStorage.getItem(KUNCI);
      if (!mentah) return kosong();
      var k = JSON.parse(mentah);
      k.jurus = k.jurus || {};
      k.riwayat = k.riwayat || [];
      k.jurnal_salah = k.jurnal_salah || [];
      return k;
    } catch (e) {
      return kosong();
    }
  }

  function simpanKemajuan(k) {
    try {
      localStorage.setItem(KUNCI, JSON.stringify(k));
      return true;
    } catch (e) {
      alert('Kemajuan gagal disimpan. Penyimpanan peramban mungkin penuh atau ' +
            'sedang dalam mode penyamaran.');
      return false;
    }
  }

  // ---------------------------------------------------------------- tampilan peta

  function tampilan() {
    try {
      var t = JSON.parse(localStorage.getItem(KUNCI_TAMPILAN)) || {};
      return { pilar: t.pilar || '', tahap: t.tahap || 'osn' };
    } catch (e) {
      /* 'osn' adalah tahap terjauh, jadi bawaannya tidak menyembunyikan apa pun. */
      return { pilar: '', tahap: 'osn' };
    }
  }

  /* Gagal menyimpan pilihan tampilan tidak layak mengganggu siswa dengan alert —
     akibat terburuknya petanya kembali ke bidang pertama saat dimuat ulang. */
  function simpanTampilan(t) {
    try {
      localStorage.setItem(KUNCI_TAMPILAN, JSON.stringify(t));
    } catch (e) {}
  }

  // ---------------------------------------------------------------- status jurus

  function jatuhTempo(catatan) {
    return !!(catatan && catatan.ulang_pada && catatan.ulang_pada <= hariIni());
  }

  /* terkunci → terbuka → dipelajari → dikuasai, ditambah perlu-diulang saat
     tanggal ulangnya lewat. Status tidak disimpan mentah-mentah: ia dihitung
     ulang dari prasyarat + tanggal, supaya tidak pernah basi. */
  function statusJurus(jid, k) {
    k = k || kemajuan();
    var j = data.jurus[jid];
    if (!j) return 'terkunci';

    var terkunci = j.prasyarat.some(function (p) {
      var c = k.jurus[p];
      return !c || c.status !== 'dikuasai';
    });
    if (terkunci) return 'terkunci';

    var c = k.jurus[jid];
    if (!c) return 'terbuka';
    if (c.status === 'dikuasai' && jatuhTempo(c)) return 'perlu-diulang';
    return c.status;
  }

  function jurusPerluDiulang(k) {
    k = k || kemajuan();
    return data.urutJurus.filter(function (jid) {
      return statusJurus(jid, k) === 'perlu-diulang';
    });
  }

  function terbukaBelumDikuasai(k) {
    k = k || kemajuan();
    return data.urutJurus.filter(function (jid) {
      var s = statusJurus(jid, k);
      return s === 'terbuka' || s === 'dipelajari';
    });
  }

  // ---------------------------------------------------------------- penjadwalan

  /* Naikkan atau turunkan jadwal ulang sebuah jurus.

     Kenaikan tangga hanya terjadi kalau jurusnya memang sedang jatuh tempo.
     Tanpa syarat itu, siswa yang mengerjakan lima soal sekaligus dalam satu
     sore akan melompat dari tangga 1 ke tangga 60 hari — padahal ia belum
     membuktikan apa pun tentang ingatannya minggu depan. */
  function jadwalkan(jid, benar, k) {
    var simpanSendiri = !k;
    k = k || kemajuan();
    var c = k.jurus[jid] || { status: 'dipelajari', beruntun: 0, tangga: 0, ulang_pada: null };
    var tempo = jatuhTempo(c);

    if (benar) {
      c.beruntun += 1;
      if (c.status !== 'dikuasai' && c.beruntun >= AMBANG_KUASAI) {
        c.status = 'dikuasai';
        c.tangga = 0;
      } else if (c.status === 'dikuasai' && tempo) {
        c.tangga = Math.min(c.tangga + 1, TANGGA.length - 1);
      }
      if (c.status === 'dikuasai') {
        c.ulang_pada = tambahHari(hariIni(), TANGGA[c.tangga]);
      } else {
        c.status = 'dipelajari';
      }
    } else {
      c.beruntun = 0;
      c.status = 'dipelajari';
      c.tangga = 0;
      c.ulang_pada = null;
    }

    k.jurus[jid] = c;
    if (simpanSendiri) simpanKemajuan(k);
    return c;
  }

  // ---------------------------------------------------------------- mencatat

  function catatJawaban(soalId, benar, petunjukDipakai, detik) {
    var k = kemajuan();
    k.riwayat.push({
      soal: soalId,
      pada: hariIni(),
      benar: !!benar,
      petunjuk: petunjukDipakai || 0,
      detik: Math.round(detik || 0)
    });
    var s = data.soal[soalId];
    if (s) s.jurus.forEach(function (jid) { jadwalkan(jid, benar, k); });
    simpanKemajuan(k);
  }

  function catatSalah(soalId, sebab, catatan) {
    var k = kemajuan();
    k.jurnal_salah.push({
      soal: soalId,
      pada: hariIni(),
      sebab: sebab,
      catatan: catatan || ''
    });
    simpanKemajuan(k);
  }

  function riwayatSoal(soalId, k) {
    k = k || kemajuan();
    return k.riwayat.filter(function (r) { return r.soal === soalId; });
  }

  function sudahDikerjakan(soalId, k) {
    return riwayatSoal(soalId, k).length > 0;
  }

  // ---------------------------------------------------------------- memilih soal

  function soalJurus(jid) {
    var j = data.jurus[jid];
    if (!j) return [];
    return j.latihan.map(function (id) { return data.soal[id]; }).filter(Boolean);
  }

  /* Untuk sesi ulangan: ambil soal yang BELUM pernah dikerjakan untuk jurus ini.
     Mengulang jurus dengan soal yang sama hanya melatih ingatan jawabannya,
     bukan jurusnya. Kalau semua sudah habis, baru pakai yang paling lama tak
     disentuh. */
  function soalBerikutnya(jid, k) {
    k = k || kemajuan();
    var kandidat = soalJurus(jid);
    if (!kandidat.length) return null;

    var segar = kandidat.filter(function (s) { return !sudahDikerjakan(s.id, k); });
    if (segar.length) {
      return segar.sort(function (a, b) { return a.kesulitan - b.kesulitan; })[0];
    }

    var terakhir = {};
    k.riwayat.forEach(function (r, i) { terakhir[r.soal] = i; });
    return kandidat.sort(function (a, b) {
      return (terakhir[a.id] || 0) - (terakhir[b.id] || 0);
    })[0];
  }

  // ---------------------------------------------------------------- periksa jawaban

  function rapikan(s) {
    return String(s == null ? '' : s).trim().toLowerCase().replace(/\s+/g, '');
  }

  /* Sengaja lugu. Varian jawaban yang sah ditulis eksplisit di jawaban_alt
     pada berkas soalnya — bukan ditebak-tebak di sini. Satu-satunya kelonggaran
     adalah membandingkan sebagai angka, supaya "08" dan "8" dianggap sama. */
  function periksaJawaban(soal, isian) {
    var a = rapikan(isian);
    if (!a) return false;
    var kandidat = [soal.jawaban].concat(soal.jawaban_alt || []);
    return kandidat.some(function (kk) {
      var b = rapikan(kk);
      if (!b) return false;
      if (a === b) return true;
      var na = Number(a), nb = Number(b);
      return isFinite(na) && isFinite(nb) && na === nb;
    });
  }

  // ---------------------------------------------------------------- tampilan

  function renderRumus(el) {
    if (!window.renderMathInElement) return;
    window.renderMathInElement(el, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false }
      ],
      throwOnError: false,
      ignoredTags: ['script', 'noscript', 'style', 'textarea', 'option']
    });
  }

  var HALAMAN = [
    ['index.html', 'Peta'],
    ['latihan.html', 'Latihan'],
    ['jurnal.html', 'Jurnal'],
    ['simulasi.html', 'Simulasi']
  ];

  function pasangKepala(aktif) {
    var el = document.getElementById('kepala');
    if (!el) return;
    var nav = HALAMAN.map(function (h) {
      var kini = h[0] === aktif ? ' aria-current="page"' : '';
      return '<a href="' + h[0] + '"' + kini + '>' + h[1] + '</a>';
    }).join('');
    el.className = 'kepala';
    el.innerHTML =
      '<h1><a href="index.html">Peta Jurus</a></h1>' +
      '<nav class="nav">' + nav + '</nav>';
  }

  function lolos(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function bintangKesulitan(n) {
    return '●'.repeat(n) + '○'.repeat(Math.max(0, 5 - n));
  }

  function galat(pesan) {
    var el = document.getElementById('isi');
    if (el) el.innerHTML = '<div class="kartu"><p>' + lolos(pesan) + '</p></div>';
  }

  // ---------------------------------------------------------------- ekspor

  function ekspor() {
    var isi = JSON.stringify(kemajuan(), null, 1);
    var blob = new Blob([isi], { type: 'application/json' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'peta-jurus-' + hariIni() + '.json';
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  }

  function impor(teks) {
    var k = JSON.parse(teks);
    if (!k || typeof k !== 'object' || !k.jurus) {
      throw new Error('Berkas ini bukan cadangan Peta Jurus.');
    }
    k.riwayat = k.riwayat || [];
    k.jurnal_salah = k.jurnal_salah || [];
    simpanKemajuan(k);
    return k;
  }

  function hapusSemua() {
    localStorage.removeItem(KUNCI);
  }

  return {
    TANGGA: TANGGA,
    AMBANG_KUASAI: AMBANG_KUASAI,
    SEBAB: SEBAB,
    data: data,
    hariIni: hariIni,
    tambahHari: tambahHari,
    muatData: muatData,
    pilarDariSoal: pilarDariSoal,
    kemajuan: kemajuan,
    simpanKemajuan: simpanKemajuan,
    tampilan: tampilan,
    simpanTampilan: simpanTampilan,
    statusJurus: statusJurus,
    jatuhTempo: jatuhTempo,
    jurusPerluDiulang: jurusPerluDiulang,
    terbukaBelumDikuasai: terbukaBelumDikuasai,
    jadwalkan: jadwalkan,
    catatJawaban: catatJawaban,
    catatSalah: catatSalah,
    riwayatSoal: riwayatSoal,
    sudahDikerjakan: sudahDikerjakan,
    soalJurus: soalJurus,
    soalBerikutnya: soalBerikutnya,
    periksaJawaban: periksaJawaban,
    renderRumus: renderRumus,
    pasangKepala: pasangKepala,
    lolos: lolos,
    bintangKesulitan: bintangKesulitan,
    galat: galat,
    ekspor: ekspor,
    impor: impor,
    hapusSemua: hapusSemua
  };
})();
