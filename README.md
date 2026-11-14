# SIMUTEH - Sistem Pemrosesan Citra Daun Teh

Repositori ini berisi rangkaian eksperimen pengolahan citra untuk proyek SIMUTEH (Sistem Pemrosesan Citra Daun Teh) menggunakan dataset sintetis (`SEED = 1092`).

## Struktur Modul
- **B2_citra_warna.ipynb**: Analisis ruang warna RGB/HSV dan pemilihan kanal terbaik (Kanal Merah / R).
- **B3_histogram.ipynb**: Diagnosis mutu citra, peregangan kontras persentil, ekualisasi histogram, dan penerapan CLAHE.
- **B4_penapisan.ipynb**: Konvolusi spasial, pengujian penapis (rerata, Gaussian, median) terhadap derau, serta urutan redam-lalu-tajam.
- **B5_praproses.ipynb**: Integrasi rangkaian modul praproses akhir (`src/praproses.py`), evaluasi kuantitatif (Tabel 12), serta uji bercak palsu pada kelas sehat.
- **P5_tepi.ipynb**: Analisis gradien citra dan perbandingan operator deteksi tepi (Sobel, Prewitt, LoG, dan Canny) terhadap tepi acuan daun dan bercak.

## Parameter Final Praproses (`hasil/param_praproses.json`)
- **Lebar Target**: 640 piksel
- **Koreksi Gamma**: 1.0 (Dinonaktifkan)
- **CLAHE Kanal V**: `clipLimit = 2.0`, `tileGridSize = 8x8`
- **Redam Derau**: Penapis Gaussian (`kernel = 5`, `sigma = 1.0`)
- **Penajaman**: Unsharp Masking (`tajam_k = 0.5`)

## Ringkasan Hasil Pertemuan 5 (Deteksi Tepi)
- **Operator & Kanal Terbaik**: Canny (`30/90, sigma=2`) pada **Kanal R** menghasilkan skor F1 tertinggi dan paling konsisten di seluruh kondisi pencahayaan (`0.980` pada citra mentah dan `0.976` sesudah praproses).
- **Berkas Keluaran**: `hasil/p5_tabel_tepi.csv` dan `hasil/p5_f1_kondisi.png`.

## Cara Menjalankan
1. Hubungkan Google Colab ke Google Drive pada path `/content/drive/MyDrive/simuteh-2330511092/`.
2. Jalankan *notebook* secara berurutan mulai dari `B2` hingga `P5_tepi.ipynb`.
