# SIMUTEH - Sistem Pemrosesan Citra Daun Teh

Repositori ini berisi rangkaian eksperimen pengolahan citra untuk proyek SIMUTEH (Sistem Pemrosesan Citra Daun Teh) menggunakan dataset sintetis (SEED = 1092).

## Struktur Modul
- `B2_citra_warna.ipynb`: Analisis ruang warna RGB/HSV dan pemilihan kanal terbaik (Kanal Merah / R).
- `B3_histogram.ipynb`: Diagnosis mutu citra, peregangan kontras persentil, ekualisasi histogram, dan penerapan CLAHE.
- `B4_penapisan.ipynb`: Konvolusi spasial, pengujian penapis (rerata, Gaussian, median) terhadap derau, serta urutan redam-lalu-tajam.
- `B5_praproses.ipynb`: Integrasi rangkaian modul praproses akhir (`src/praproses.py`), evaluasi kuantitatif (Tabel 12), serta uji bercak palsu pada kelas sehat.
- `P5_tepi.ipynb`: Analisis gradien citra dan perbandingan operator deteksi tepi (Sobel, Prewitt, LoG, dan Canny) terhadap tepi acuan daun dan bercak.
- `P6_morfologi.ipynb`: Pembersihan morfologi (*opening* & *closing*), penyaringan komponen bercak, serta integrasi modul analisis bercak (`src/bercak.py`) dan evaluasi pada seluruh dataset.

## Parameter Final Praproses (`hasil/param_praproses.json`)
- Lebar Target: 640 piksel
- Koreksi Gamma: 1.0 (Dinonaktifkan)
- CLAHE Kanal V: `clipLimit = 2.0`, `tileGridSize = 8x8`
- Redam Derau: Penapis Gaussian (`kernel = 5`, `sigma = 1.0`)
- Penajaman: Unsharp Masking (`tajam_k = 0.5`)

## Parameter Final Bercak (`hasil/param_bercak.json`)
- Segmentasi Awal: Kanal Merah (`kanal = 2`), ambang `median + 4.0 * MAD` (`k = 4.0`)
- Morfologi: SE `elips`, `se_open = 5`, `se_close = 5`
- Penyaringan Komponen (Konektivitas 8): `luas_min = 20` piksel, `bulat_min = 0.5`, `rasio_maks = 1.8`
- Klasifikasi & Skala: `batas_ringan = 0.1%`, `batas_berat = 2.0%`, `mm_per_px = 0.4375`

## Ringkasan Hasil Pertemuan 5 (Deteksi Tepi)
- Operator & Kanal Terbaik: Canny (30/90, sigma=2) pada Kanal R menghasilkan skor F1 tertinggi dan paling konsisten di seluruh kondisi pencahayaan (0.980 pada citra mentah dan 0.976 sesudah praproses).
- Berkas Keluaran: `hasil/p5_tabel_tepi.csv` dan `hasil/p5_f1_kondisi.png`.

## Ringkasan Hasil Pertemuan 6 (Morfologi & Analisis Bercak)
- Pembersihan & Penyaringan: Kombinasi *opening* dan *closing* elips `5x5` disertai filter `luas + kebulatan + rasio` menekan galat jumlah komponen ke titik terendah (`1.00` berat, `1.30` ringan, `0.70` sehat) dan memangkas daun sehat dengan bercak palsu menjadi 6 citra.
- Evaluasi Modul `src/bercak.py` (60 Citra): Galat absolut rerata persen bercak `0.47`, korelasi persen prediksi vs acuan `0.966`, dan akurasi kelas mutu `0.867` (52 dari 60 citra tepat: 19 Bercak Berat, 14 Bercak Ringan, 19 Sehat).
- Berkas Keluaran: `hasil/param_bercak.json` dan `hasil/p6_evaluasi_bercak.csv`.

## Cara Menjalankan
1. Hubungkan Google Colab ke Google Drive pada path `/content/drive/MyDrive/simuteh-2330511092/`.
2. Jalankan notebook secara berurutan mulai dari `B2` hingga `P6_morfologi.ipynb`.

## Cara Menggunakan `analisis_daun` (`src/bercak.py`)
Fungsi `analisis_daun(img_praproses, p=None)` menerima citra BGR hasil praproses dan mengembalikan kamus berisi hasil segmentasi serta klasifikasi mutu daun:

```python
import json
import cv2
from src.praproses import praproses
from src.bercak import analisis_daun

# 1. Muat parameter tersimpan
with open("hasil/param_praproses.json") as f:
    param_pra = json.load(f)
with open("hasil/param_bercak.json") as f:
    param_bercak = json.load(f)

# 2. Praproses citra daun dan jalankan analisis bercak
img = cv2.imread("data/citra/teh_041.png")
img_pra = praproses(img, param_pra)
hasil = analisis_daun(img_pra, p=param_bercak)

print("Kelas Mutu    :", hasil["kelas"])          # "Sehat", "Bercak Ringan", atau "Bercak Berat"
print("Jumlah Bercak :", hasil["jumlah_bercak"])  # int
print("Persen Bercak :", hasil["persen_bercak"])  # float (%)
print("Daftar Bercak :", hasil["bercak"])         # detail luas_px, luas_mm2, kebulatan, rasio_aspek
```
