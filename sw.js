/* Service worker Peta Jurus.

   Perbedaan sengaja dari info-kurikulum: di sana data/*.json diambil dari
   jaringan lebih dulu karena Google Sheet sering berubah. Di sini kebalikannya
   — cache dulu, perbarui diam-diam di latar — karena isinya jarang berubah dan
   latihan saat offline justru intinya. */

var CACHE = 'peta-jurus-v13';

/* Wajib ada. Kalau salah satu gagal, install ikut gagal — lebih baik ketahuan
   daripada situsnya setengah jalan saat offline. */
var KERANGKA = [
  './',
  'index.html',
  'jurus.html',
  'latihan.html',
  'jurnal.html',
  'simulasi.html',
  'manifest.webmanifest',
  'assets/styles.css',
  'assets/inti.js',
  'assets/peta.js',
  'assets/jurus.js',
  'assets/latihan.js',
  'assets/jurnal.js',
  'assets/simulasi.js',
  'assets/icons/icon.svg',
  'assets/katex/katex.min.css',
  'assets/katex/katex.min.js',
  'assets/katex/auto-render.min.js',
  'data/jurus.json'
];

/* Soal per bidang dan rajah geometri. Sengaja **tidak** di KERANGKA: menunggunya
   membuat install memanjang oleh ratusan KB yang belum tentu dipakai siswa hari
   itu — dan dengan empat bidang, angkanya berlipat. Sebagai gantinya keduanya
   diambil di latar setelah install selesai, jadi latihan offline tetap utuh tanpa
   menahan pemasangan.

   Daftarnya diturunkan dari jurus.json, bukan ditulis tangan, supaya bidang baru
   dan rajah baru tidak pernah terlupa. Untuk rajah itu bukan kemewahan: soal
   geometri tanpa bangunnya bukan soal yang lebih sulit, melainkan soal yang tidak
   bisa dikerjakan sama sekali. */
function berkasLatar(c) {
  return c.match('data/jurus.json')
    .then(function (r) { return r ? r.json() : null; })
    .then(function (d) {
      if (!d) return [];
      var ada = {};
      d.simpul.forEach(function (j) {
        if (j.contoh.length || j.latihan.length) ada[j.pilar] = true;
      });
      var daftar = Object.keys(ada).map(function (p) {
        return 'data/soal-' + p + '.json';
      });
      /* Dibaca dengan penjaga: jurus.json dari cache versi lama belum punya
         kunci ini. */
      return daftar.concat((d.rajah || []).map(function (n) {
        return 'assets/rajah/' + n;
      }));
    });
}

/* Font KaTeX. Boleh gagal satu-dua tanpa menggagalkan install — yang jarang
   dipakai (Fraktur, Script) tidak layak menjatuhkan seluruh pemasangan. */
var FONT = [
  'assets/katex/fonts/KaTeX_AMS-Regular.woff2',
  'assets/katex/fonts/KaTeX_Caligraphic-Bold.woff2',
  'assets/katex/fonts/KaTeX_Caligraphic-Regular.woff2',
  'assets/katex/fonts/KaTeX_Fraktur-Bold.woff2',
  'assets/katex/fonts/KaTeX_Fraktur-Regular.woff2',
  'assets/katex/fonts/KaTeX_Main-Bold.woff2',
  'assets/katex/fonts/KaTeX_Main-BoldItalic.woff2',
  'assets/katex/fonts/KaTeX_Main-Italic.woff2',
  'assets/katex/fonts/KaTeX_Main-Regular.woff2',
  'assets/katex/fonts/KaTeX_Math-BoldItalic.woff2',
  'assets/katex/fonts/KaTeX_Math-Italic.woff2',
  'assets/katex/fonts/KaTeX_SansSerif-Bold.woff2',
  'assets/katex/fonts/KaTeX_SansSerif-Italic.woff2',
  'assets/katex/fonts/KaTeX_SansSerif-Regular.woff2',
  'assets/katex/fonts/KaTeX_Script-Regular.woff2',
  'assets/katex/fonts/KaTeX_Size1-Regular.woff2',
  'assets/katex/fonts/KaTeX_Size2-Regular.woff2',
  'assets/katex/fonts/KaTeX_Size3-Regular.woff2',
  'assets/katex/fonts/KaTeX_Size4-Regular.woff2',
  'assets/katex/fonts/KaTeX_Typewriter-Regular.woff2'
];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE)
      .then(function (c) {
        return c.addAll(KERANGKA).then(function () {
          /* Font boleh gagal satu-dua tanpa menggagalkan install, dan soal serta
             rajah diambil di latar — keduanya tidak ditunggu. */
          Promise.all(FONT.map(function (u) { return c.add(u).catch(function () {}); }))
            .then(function () { return berkasLatar(c); })
            .then(function (daftar) {
              return Promise.all(daftar.map(function (u) {
                return c.add(u).catch(function () {});
              }));
            });
        });
      })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys()
      .then(function (nama) {
        return Promise.all(nama.map(function (n) {
          return n === CACHE ? null : caches.delete(n);
        }));
      })
      .then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  var permintaan = e.request;
  if (permintaan.method !== 'GET') return;

  var url = new URL(permintaan.url);
  if (url.origin !== self.location.origin) return;

  /* Kunci cache selalu dibuang query-nya.

     Situs ini memakai query di mana-mana: jurus.html?id=…, latihan.html?soal=…,
     latihan.html?jurus=…. Padahal kerangka HTML-nya sama persis — yang
     membedakan hanya location.search yang dibaca skrip di sisi klien. Tanpa
     pembuangan ini, caches.match tidak pernah cocok saat offline dan seluruh
     navigasi jatuh ke index.html. */
  var kunci = url.origin + url.pathname;

  /* Cache dulu, lalu perbarui diam-diam untuk kunjungan berikutnya. */
  e.respondWith(
    caches.match(kunci).then(function (tersimpan) {
      var dariJaringan = fetch(permintaan).then(function (jawaban) {
        if (jawaban && jawaban.ok) {
          var salinan = jawaban.clone();
          caches.open(CACHE).then(function (c) { c.put(kunci, salinan); });
        }
        return jawaban;
      }).catch(function () {
        return tersimpan || caches.match('index.html');
      });
      return tersimpan || dariJaringan;
    })
  );
});
