import cv2
import matplotlib.pyplot as plt

def baca(jalur_berkas):
    """Membaca citra menggunakan OpenCV."""
    return cv2.imread(jalur_berkas)

def tampil(img, judul=""):
    """Menampilkan citra menggunakan Matplotlib."""
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(judul)
    plt.axis('off')
    plt.show()
