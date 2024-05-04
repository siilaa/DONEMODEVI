import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QColor

class Etkinlik:
    def __init__(self, ad, tarih, mekan):
        self.ad = ad
        self.tarih = tarih
        self.mekan = mekan
        self.biletler = []

    def etkinlik_ekle(self, bilet):
        self.biletler.append(bilet)
        print("Etkinlik oluşturuldu:", self.ad)

    def bilet_sat(self, bilet):
        self.biletler.append(bilet)
        print("Bilet satın alındı.")

    def bilet_al(self, bilet):
        self.biletler.remove(bilet)
        print("Bilet iade edildi.")

class Bilet:
    def __init__(self, bilet_no, etkinlik):
        self.bilet_no = bilet_no
        self.etkinlik = etkinlik

class Kullanici:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
        self.biletler = []

    def bilet_sat(self, bilet):
        self.biletler.append(bilet)
        print("Bilet satın alındı.")

    def bilet_iade(self, bilet):
        self.biletler.remove(bilet)
        print("Bilet iade edildi.")

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Bilet Satış Platformu")
        self.setGeometry(100, 100, 400, 300)

        self.etkinlik_ad_label = QLabel("Etkinlik Adı:")
        self.etkinlik_ad_input = QLineEdit()
        self.etkinlik_tarih_label = QLabel("Tarih:")
        self.etkinlik_tarih_input = QLineEdit()
        self.etkinlik_mekan_label = QLabel("Mekan:")
        self.etkinlik_mekan_input = QLineEdit()

        self.etkinlik_ekle_button = QPushButton("Etkinlik Ekle")
        self.etkinlik_ekle_button.setStyleSheet("background-color: lightpink")
        self.etkinlik_ekle_button.clicked.connect(self.etkinlik_ekle)

        self.gorsel_label = QLabel(self)
        pixmap = QPixmap("C:\\Users\\90555\\Downloads\\ticket.jpg")
        self.gorsel_label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(self.etkinlik_ad_label)
        layout.addWidget(self.etkinlik_ad_input)
        layout.addWidget(self.etkinlik_tarih_label)
        layout.addWidget(self.etkinlik_tarih_input)
        layout.addWidget(self.etkinlik_mekan_label)
        layout.addWidget(self.etkinlik_mekan_input)
        layout.addWidget(self.etkinlik_ekle_button)
        layout.addWidget(self.gorsel_label)

        self.setLayout(layout)

    def etkinlik_ekle(self):
        ad = self.etkinlik_ad_input.text()
        tarih = self.etkinlik_tarih_input.text()
        mekan = self.etkinlik_mekan_input.text()

        # Etkinlik ekleme işlemini gerçekleştir
        QMessageBox.information(self, "Bilgi", "Etkinlik başarıyla eklendi.")

def main():
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()