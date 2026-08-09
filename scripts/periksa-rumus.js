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
const soal = [];
for (const f of fs.readdirSync(path.join(AKAR, 'data')).sort()) {
  if (!/^soal-.*\.json$/.test(f)) continue;
  soal.push(...JSON.parse(fs.readFileSync(path.join(AKAR, 'data', f), 'utf8')).soal);
}

/* Halaman jurus ikut diperiksa. 'Intinya' justru bagian yang paling padat rumus di
   seluruh situs — di situ identitasnya ditulis — dan halaman jurus dibuka jauh lebih
   sering daripada satu soal tertentu. Memeriksa soal saja meninggalkan kotak merah
   pada halaman yang paling banyak dibaca. */
const jurus = JSON.parse(
  fs.readFileSync(path.join(AKAR, 'data', 'jurus.json'), 'utf8')).simpul;

const hanya = process.argv[3] ? new Set(process.argv[3].split(',')) : null;
const gagal = [];
let jumlah = 0;

function periksa(id, potongan) {
  for (const [isi, cuplikan, blok] of pisah(potongan.filter(Boolean).join('\n'))) {
    if (isi === 'GANTUNG') {
      gagal.push(`${id}: delimiter tidak tertutup <<${cuplikan}>>`);
      continue;
    }
    jumlah++;
    try {
      katex.renderToString(lolosBalik(isi), { displayMode: blok, throwOnError: true, strict: 'error' });
    } catch (e) {
      gagal.push(`${id}: ${e.message.split('\n')[0]}  <<${isi.slice(0, 60)}>>`);
    }
  }
}

const soalDipakai = soal.filter((s) => !hanya || hanya.has(s.id));
const jurusDipakai = jurus.filter((j) => !hanya || hanya.has(j.id));

for (const s of soalDipakai) {
  periksa(s.id, [s.soal, s.pembahasan, ...(s.petunjuk || []), ...(s.rubrik || [])]);
}
for (const j of jurusDipakai) {
  periksa(j.id, [j.kapan_dipakai, j.inti, j.jebakan]);
}

console.log(`soal diperiksa : ${soalDipakai.length}`);
console.log(`jurus diperiksa: ${jurusDipakai.length}`);
console.log(`rumus dirender : ${jumlah}`);
console.log(`gagal          : ${gagal.length}`);
gagal.slice(0, 25).forEach((g) => console.log('  ' + g));
process.exit(gagal.length ? 1 : 0);
