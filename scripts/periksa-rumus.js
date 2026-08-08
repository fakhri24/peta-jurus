/* Periksa setiap rumus di data/*.json benar-benar bisa dirender KaTeX.

   Jalankan dari akar proyek, setelah scripts/build.py:

       node scripts/periksa-rumus.js

   Ini perkakas pengembangan, bukan dependensi situs. Ia memakai berkas KaTeX yang
   sudah ada di assets/katex/ — tidak ada package manager, tidak ada yang diunduh.
   Situsnya sendiri tetap tanpa dependensi selain KaTeX lokal itu.

   Gunanya: Markdown dan LaTeX memperebutkan _ * \\ &, dan tes Python di
   tests/test_build.py hanya menjaga keluaran markdown_ke_html. Yang tidak dijaganya
   adalah apakah rumus yang selamat itu memang sah menurut KaTeX. Rumus yang salah
   ketik lolos build tanpa keluhan dan baru terlihat sebagai kotak merah di layar
   siswa.

   Pemisahan rumusnya meniru auto-render: pindai kiri ke kanan, periksa '$$' lebih
   dulu baru '$' — persis urutan delimiters di Inti.renderRumus. Meniru urutan itu
   penting; memakai regex sendiri akan salah memasangkan dan memberi galat palsu.

   Mode strict-nya sengaja 'error', lebih ketat daripada situs, supaya karakter
   Unicode yang tak dikenal KaTeX ikut ketahuan di sini alih-alih diam-diam salah
   tampil di peramban. */
const fs = require('fs');
const path = require('path');
const AKAR = path.resolve(process.argv[2] || '.');

global.window = global;
/* compatMode diisi supaya KaTeX tidak mengeluh soal quirks mode di Node. */
global.document = { compatMode: 'CSS1Compat', createElement: () => ({ style: {} }) };
const katex = require(path.join(AKAR, 'assets/katex/katex.min.js'));

/* build.py sengaja meng-escape rumus, karena KaTeX di peramban membacanya lewat
   textContent yang sudah menerjemahkannya kembali. Di sini kita tirukan itu. */
const lolosBalik = (s) => s.replace(/&lt;/g, '<').replace(/&gt;/g, '>')
  .replace(/&quot;/g, '"').replace(/&#x27;/g, "'").replace(/&amp;/g, '&');

function pisah(teks) {
  const keluar = [];
  let i = 0;
  while (i < teks.length) {
    if (teks.startsWith('$$', i)) {
      const j = teks.indexOf('$$', i + 2);
      if (j < 0) { keluar.push(['GANTUNG', teks.slice(i, i + 40), true]); break; }
      keluar.push([teks.slice(i + 2, j), null, true]);
      i = j + 2;
    } else if (teks[i] === '$') {
      const j = teks.indexOf('$', i + 1);
      if (j < 0) { keluar.push(['GANTUNG', teks.slice(i, i + 40), false]); break; }
      keluar.push([teks.slice(i + 1, j), null, false]);
      i = j + 1;
    } else i++;
  }
  return keluar;
}

/* Soal dipecah per bidang; kumpulkan seluruhnya supaya tidak ada yang lolos periksa. */
const data = { soal: [] };
for (const f of fs.readdirSync(path.join(AKAR, 'data')).sort()) {
  if (!/^soal-.*\.json$/.test(f)) continue;
  data.soal.push(...JSON.parse(fs.readFileSync(path.join(AKAR, 'data', f), 'utf8')).soal);
}
const hanya = process.argv[3] ? new Set(process.argv[3].split(',')) : null;

let jumlah = 0; const gagal = [];
for (const s of data.soal) {
  if (hanya && !hanya.has(s.id)) continue;
  const teks = [s.soal, s.pembahasan, ...(s.petunjuk || []), ...(s.rubrik || [])].join('\n');
  for (const [isi, potongan, blok] of pisah(teks)) {
    if (isi === 'GANTUNG') { gagal.push(`${s.id}: delimiter tidak tertutup <<${potongan}>>`); continue; }
    jumlah++;
    try {
      katex.renderToString(lolosBalik(isi), { displayMode: blok, throwOnError: true, strict: 'error' });
    } catch (e) {
      gagal.push(`${s.id}: ${e.message.split('\n')[0]}  <<${isi.slice(0, 60)}>>`);
    }
  }
}
console.log(`soal diperiksa : ${hanya ? hanya.size : data.soal.length}`);
console.log(`rumus dirender : ${jumlah}`);
console.log(`gagal          : ${gagal.length}`);
gagal.slice(0, 25).forEach((g) => console.log('  ' + g));
process.exit(gagal.length ? 1 : 0);
