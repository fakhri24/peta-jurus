/* Periksa bahwa soal yang dipecah build.py benar-benar tersusun kembali di klien.

   Jalankan dari akar proyek:

       node scripts/periksa-gabung.js

   Perkakas pengembangan, bukan dependensi situs. Jalankan setelah build.py,
   karena yang diperiksa hasilnya.

   Kenapa perlu perkakas sendiri. `tests/test_build.py` menjaga separuh Python-nya:
   berkas ringan tidak membawa MEDAN_BAHAS, dan tiap soal punya pasangan di
   bahas-<pilar>.json. Yang tidak bisa dijaganya separuh JavaScript-nya — apakah
   `muatData()` benar-benar menempelkan keduanya kembali menjadi satu objek.

   Kegagalan di situ **tidak terlihat**. Halaman tetap termuat, soalnya tetap
   tampil, tombol tetap ada; yang hilang cuma petunjuk dan pembahasan, yaitu isi
   yang justru paling dicari siswa. Persis itu yang sempat terlihat saat 6.1
   dikerjakan — dan penyebabnya ternyata service worker lama, bukan kodenya. Tanpa
   pemeriksaan ini tidak ada cara cepat membedakan keduanya.

   Caranya sama dengan periksa-muatan.js: inti.js yang itu juga dijalankan di Node
   dengan fetch tiruan, jadi tidak ada service worker yang bisa menyesatkan. */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const AKAR = path.resolve(process.argv[2] || '.');
const MEDAN_BAHAS = ['petunjuk', 'pembahasan', 'rubrik'];

function muat(spek) {
  const diminta = [];
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
    localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
    document: {
      getElementById: () => null, querySelector: () => null,
      querySelectorAll: () => [], createElement: () => ({ style: {} })
    },
    location: { search: '', href: 'http://uji/' },
    setTimeout, clearTimeout, setInterval, clearInterval,
    Promise, URLSearchParams, Date, Math, JSON, Number, String, Array, Object, Error,
    isFinite, parseInt, parseFloat, encodeURIComponent, decodeURIComponent, RegExp,
    addEventListener() {}, removeEventListener() {}, navigator: {}
  };
  sandbox.window = sandbox;
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync(path.join(AKAR, 'assets/inti.js'), 'utf8'), sandbox);
  return sandbox.Inti.muatData(spek).then((data) => ({ data, diminta }));
}

let gagal = 0;

function lapor(nama, benar, keterangan) {
  console.log('%s %s%s', benar ? ' ok ' : 'GAGAL', nama,
              keterangan ? '  — ' + keterangan : '');
  if (!benar) gagal++;
}

(async () => {
  const jurus = JSON.parse(
    fs.readFileSync(path.join(AKAR, 'data/jurus.json'), 'utf8'));
  const pilar = [...new Set(jurus.simpul
    .filter((j) => j.contoh.length || j.latihan.length)
    .map((j) => j.pilar))];

  for (const p of pilar) {
    const { data } = await muat({ soal: [p] });
    const punya = Object.values(data.soal);
    const kurang = punya.filter(
      (s) => MEDAN_BAHAS.some((m) => !(m in s)));
    lapor(p.padEnd(16), kurang.length === 0,
          kurang.length
            ? `${kurang.length} soal kehilangan medan bahas, mis. ${kurang[0].id}`
            : `${punya.length} soal utuh`);
  }

  /* Sisi sebaliknya: yang menyatakan bahas:false harus benar-benar hemat, bukan
     sekadar tidak memakainya. Kalau berkas beratnya tetap diminta, seluruh guna
     pemecahan di 6.1 hilang tanpa ada yang menandai. */
  const { data, diminta } = await muat({ soal: pilar, bahas: false });
  lapor('bahas:false hemat'.padEnd(16),
        !diminta.some((u) => u.includes('/bahas-')),
        diminta.length + ' berkas: ' + diminta.join(' + '));
  lapor('bahas:false bersih'.padEnd(16),
        Object.values(data.soal).every((s) => s.pembahasan === undefined),
        'tidak ada pembahasan yang ikut terbawa');

  process.exit(gagal ? 1 : 0);
})();
