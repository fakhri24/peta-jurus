/* Laporkan berkas data apa yang benar-benar diminta tiap halaman.

   Jalankan dari akar proyek:

       node scripts/periksa-muatan.js

   Perkakas pengembangan, bukan dependensi situs — tidak ada yang diunduh, dan
   berkas yang dijalankan adalah assets/*.js yang itu juga.

   Cara kerjanya: tiap skrip halaman dijalankan di Node dengan `fetch`, DOM, dan
   localStorage tiruan, lalu URL yang lewat `fetch` dicatat. Jadi yang diukur
   perilaku sungguhan, bukan tebakan dari membaca kode.

   Gunanya: halaman menyatakan kebutuhan datanya lewat `Inti.muatData({ soal: … })`,
   dan pernyataan itu mudah menjadi basi tanpa ada yang menandai. Peta misalnya tidak
   menyentuh data.soal sama sekali; kalau suatu saat ia diam-diam memuatnya lagi,
   angka di sini yang akan memberi tahu.

   Skrip ini juga alat ukur untuk 0.5 di PLAN.md — pemecahan soal.json per bidang.
   Sebelum dan sesudahnya, jalankan ini dan bandingkan angkanya.

   DOM tiruannya sengaja sangat dangkal: ia cukup untuk melewati pemasangan awal
   halaman, bukan untuk menguji tampilan. Kalau sebuah halaman gagal di sini karena
   ada API peramban yang belum ditiru, tambahkan tiruannya — jangan mengubah
   halamannya. */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const AKAR = path.resolve(process.argv[2] || '.');
/* Tiap halaman diukur beserta query yang khas dipakainya — tanpa itu, halaman
   yang bergantung pada ?id= atau ?jurus= akan terlihat lebih hemat daripada
   kenyataannya. */
const HALAMAN = process.argv[3]
  ? [[process.argv[3], process.argv[4] || '']]
  : [['peta.js', ''], ['jurus.js', '?id=vieta'], ['latihan.js', '?jurus=vieta'],
     ['latihan.js', ''], ['jurnal.js', ''], ['simulasi.js', '']];

function elemenPalsu() {
  return {
    innerHTML: '', textContent: '', value: '', checked: false,
    style: {}, classList: { add() {}, remove() {}, toggle() {}, contains: () => false },
    addEventListener() {}, removeEventListener() {}, appendChild() {}, removeChild() {},
    remove() {}, click() {}, focus() {}, scrollIntoView() {},
    querySelector: () => elemenPalsu(), querySelectorAll: () => [],
    getAttribute: () => '', setAttribute() {}, insertAdjacentHTML() {}
  };
}

function jalankan(halaman, query) {
  const diminta = [];
  const simpanan = {};

  const sandbox = {
    console: { log() {}, warn() {}, error() {} },
    fetch(url) {
      diminta.push(url);
      const berkas = path.join(AKAR, url);
      if (!fs.existsSync(berkas)) return Promise.reject(new Error('404 ' + url));
      return Promise.resolve({
        json: () => Promise.resolve(JSON.parse(fs.readFileSync(berkas, 'utf8')))
      });
    },
    localStorage: {
      getItem: (k) => (k in simpanan ? simpanan[k] : null),
      setItem: (k, v) => { simpanan[k] = String(v); },
      removeItem: (k) => { delete simpanan[k]; }
    },
    document: {
      getElementById: () => elemenPalsu(),
      querySelector: () => elemenPalsu(),
      querySelectorAll: () => [],
      createElement: () => elemenPalsu(),
      body: elemenPalsu()
    },
    location: { search: query || '', href: 'http://uji/' + (query || '') },
    setTimeout, clearTimeout, setInterval, clearInterval,
    Promise, URLSearchParams, Date, Math, JSON, Number, String, Array, Object, Error,
    isFinite, parseInt, parseFloat, encodeURIComponent, decodeURIComponent, RegExp,
    addEventListener() {}, removeEventListener() {},
    alert() {}, Blob: function () {},
    URL: { createObjectURL: () => '', revokeObjectURL() {} },
    navigator: {}
  };
  sandbox.window = sandbox;
  vm.createContext(sandbox);

  for (const berkas of ['assets/inti.js', 'assets/soal-ui.js', 'assets/' + halaman]) {
    const jalur = path.join(AKAR, berkas);
    if (!fs.existsSync(jalur)) continue;
    vm.runInContext(fs.readFileSync(jalur, 'utf8'), sandbox, { filename: berkas });
  }

  return diminta;
}

const baris = [];
let adaGagal = false;

for (const [halaman, query] of HALAMAN) {
  let diminta;
  try {
    diminta = jalankan(halaman, query);
  } catch (e) {
    baris.push([halaman + query, 'GAGAL: ' + e.message, '']);
    adaGagal = true;
    continue;
  }
  baris.push([halaman + query, diminta, null]);
}

/* fetch dipanggil di dalam Promise, jadi tunggu satu putaran sebelum melapor. */
setTimeout(() => {
  console.log('halaman                  berkas data yang diminta                        ukuran');
  console.log('------------------------ ---------------------------------------------- ------');
  for (const [halaman, diminta] of baris) {
    if (typeof diminta === 'string') {
      console.log(`${halaman.padEnd(24)} ${diminta}`);
      continue;
    }
    const daftar = diminta.length ? diminta.join(' + ') : '(tidak ada)';
    const kb = Math.round(
      diminta.reduce((n, u) => n + fs.statSync(path.join(AKAR, u)).size, 0) / 1024
    );
    console.log(`${halaman.padEnd(24)} ${daftar.padEnd(46)} ${String(kb).padStart(4)} KB`);
  }
  process.exit(adaGagal ? 1 : 0);
}, 300);
