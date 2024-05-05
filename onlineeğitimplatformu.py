import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Kurs:
    def __init__(self, kurs_adi, egitmen, icerik):
        self.kurs_adi = kurs_adi
        self.egitmen = egitmen
        self.icerik = icerik
        self.ogrenciler = []

    def kurs_olustur(self):
        print(f"{self.kurs_adi} adlı kurs oluşturuldu.")

    def kaydol(self, ogrenci):
        self.ogrenciler.append(ogrenci)
        print(f"{ogrenci.isim} adlı öğrenci kursa kaydoldu.")

    def icerik_yukle(self):
        print(f"{self.kurs_adi} kursunun içeriği yüklendi.")

class Egitmen:
    def __init__(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani

    def bilgi_goster(self):
        print(f"Eğitmen: {self.isim}, Uzmanlık Alanı: {self.uzmanlik_alani}")

class Ogrenci:
    def __init__(self, isim, email):
        self.isim = isim
        self.email = email

    def bilgi_goster(self):
        print(f"Öğrenci: {self.isim}, E-posta: {self.email}")

class AnaArayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Online Eğitim Platformu")
        self.setGeometry(100, 100, 800, 600)

        self.kurs_adi_label = QLabel("Kurs Adı:")
        self.kurs_adi_input = QLineEdit()
        self.kayit_button = QPushButton("Kursa Kaydol")
        self.kayit_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")
        self.kayit_button.clicked.connect(self.kursa_kaydol)

        self.icerik_text = QTextEdit()
        self.icerik_text.setReadOnly(True)

        self.image_label = QLabel()
        pixmap = QPixmap("C:\\Users\\ahmet\\Downloads\\kurs.jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        v_box = QVBoxLayout()
        v_box.addWidget(self.kurs_adi_label)
        v_box.addWidget(self.kurs_adi_input)
        v_box.addWidget(self.kayit_button)
        v_box.addWidget(self.icerik_text)
        v_box.addWidget(self.image_label)

        self.setLayout(v_box)

    def kursa_kaydol(self):
        kurs_adi = self.kurs_adi_input.text()

        self.icerik_text.clear()
        self.icerik_text.append(f"{kurs_adi} kursuna başarıyla kaydoldunuz!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_arayuz = AnaArayuz()
    ana_arayuz.show()
    sys.exit(app.exec_())
