# SIMUTEH - Sistem Pemrosesan Citra Daun Teh

Repositori ini berisi rangkaian eksperimen dan modul praproses pengolahan citra untuk proyek SIMUTEH (Sistem Pemrosesan Citra Daun Teh).

## Struktur Modul
- **B2_citra_warna.ipynb**: Analisis ruang warna RGB/HSV dan pemilihan kanal terbaik (Kanal Merah).
- **B3_histogram.ipynb**: Diagnosis mutu citra, peregangan kontras, ekualisasi histogram, dan penerapan CLAHE.
- **B4_penapisan.ipynb**: Konvolusi spasial, pengujian berbagai penapis (rerata, Gaussian, median) terhadap derau, serta pengujian urutan redam-lalu-tajam.
- **B5_praproses.ipynb**: Integrasi rangkaian modul praproses akhir (`src/praproses.py`), evaluasi kuantitatif (Tabel 12), serta uji bercak palsu pada kelas sehat.

## Parameter Final Praproses
Disimpan dalam format JSON pada `hasil/param_praproses.json`:
- **Lebar Target**: 640 piksel
- **Koreksi Gamma**: 1.0 (Dinonaktifkan)
- **CLAHE Kanal V**: `clipLimit = 2.0`, `tileGridSize = 8x8`
- **Redam Derau**: Penapis Gaussian (`kernel = 5`, `sigma = 1.0`)
- **Penajaman**: Unsharp Masking (`tajam_k = 0.5`)

## Cara Menjalankan
1. Pastikan lingkungan Google Colab terhubung ke Google Drive di path `/content/drive/MyDrive/simuteh-2330511092/`.
2. Jalankan *notebook* secara berurutan mulai dari Bagian 2 hingga Bagian 5.
