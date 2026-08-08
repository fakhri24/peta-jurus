/* Tangga petunjuk — mekanisme pedagogis inti situs ini, jadi ia hidup di satu
   tempat saja dan dipakai halaman jurus maupun halaman latihan.

   Pembahasan tidak pernah bisa dibuka sebelum semua petunjuk dilewati. Membaca
   pembahasan terlalu cepat terasa produktif tapi tidak menghasilkan apa-apa;
   jalan pintasnya dibuat sedikit lebih sulit dengan sengaja. */

var SoalUI = (function () {
  'use strict';

  function tanggaPetunjuk(soal, wadah, opsi) {
    opsi = opsi || {};
    var petunjuk = soal.petunjuk || [];
    var dibuka = 0;

    var daftar = document.createElement('div');
    var baris = document.createElement('div');
    baris.className = 'baris renggang';

    var tombolPetunjuk = document.createElement('button');
    var tombolBahas = document.createElement('button');
    tombolBahas.textContent = 'Lihat pembahasan';

    var kotakBahas = document.createElement('div');
    kotakBahas.className = 'pembahasan';
    kotakBahas.hidden = true;

    function segarkan() {
      if (dibuka < petunjuk.length) {
        tombolPetunjuk.textContent = 'Petunjuk ' + (dibuka + 1) +
          ' dari ' + petunjuk.length;
        tombolPetunjuk.hidden = false;
      } else {
        tombolPetunjuk.hidden = true;
      }
      tombolBahas.disabled = dibuka < petunjuk.length;
      tombolBahas.title = tombolBahas.disabled
        ? 'Buka semua petunjuknya dulu. Coba lagi sendiri sebentar.'
        : '';
    }

    tombolPetunjuk.addEventListener('click', function () {
      if (dibuka >= petunjuk.length) return;
      var p = document.createElement('div');
      p.className = 'petunjuk';
      p.innerHTML = '<b>PETUNJUK ' + (dibuka + 1) + '</b><br>' + petunjuk[dibuka];
      daftar.appendChild(p);
      Inti.renderRumus(p);
      dibuka += 1;
      segarkan();
      if (opsi.saatBuka) opsi.saatBuka(dibuka);
    });

    tombolBahas.addEventListener('click', function () {
      if (tombolBahas.disabled) return;
      kotakBahas.hidden = false;
      tombolBahas.hidden = true;
      if (opsi.saatBahas) opsi.saatBahas();
    });

    kotakBahas.innerHTML = '<h3>Pembahasan</h3>' + (soal.pembahasan || '<p>—</p>') +
      '<p class="sangat-samar">' + Inti.lolos(soal.sumber) + '</p>';

    baris.appendChild(tombolPetunjuk);
    baris.appendChild(tombolBahas);
    wadah.appendChild(daftar);
    wadah.appendChild(baris);
    wadah.appendChild(kotakBahas);

    segarkan();

    return {
      dibuka: function () { return dibuka; },
      bukaPembahasan: function () {
        dibuka = petunjuk.length;
        segarkan();
        kotakBahas.hidden = false;
        tombolBahas.hidden = true;
        tombolPetunjuk.hidden = true;
        Inti.renderRumus(kotakBahas);
      },
      renderRumus: function () { Inti.renderRumus(kotakBahas); }
    };
  }

  return { tanggaPetunjuk: tanggaPetunjuk };
})();
