import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QListWidget, QMessageBox
from PyQt5.QtGui import QPixmap


class Film:
    def __init__(self, ad, yonetmen, tur):
        self.ad = ad
        self.yonetmen = yonetmen
        self.tur = tur

    def icerik_izle(self):
        print(f"{self.ad} filmi izleniyor...")


class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.izleme_gecmisi = []

    def izleme_gecmisine_ekle(self, film):
        self.izleme_gecmisi.append(film)
        print(f"{self.kullanici_adi} kullanıcısının izleme geçmişine {film.ad} filmi eklendi.")


class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Film ve Dizi İzleme Platformu")
        self.setGeometry(100, 100, 600, 400)

        self.kullanici_adi_label = QLabel("Kullanıcı Adı:")
        self.kullanici_adi_input = QLineEdit()
        self.sifre_label = QLabel("Şifre:")
        self.sifre_input = QLineEdit()
        self.sifre_input.setEchoMode(QLineEdit.Password)

        self.giris_button = QPushButton("Giriş Yap")
        self.giris_button.clicked.connect(self.giris_yap)
        self.giris_button.setStyleSheet("background-color: #FFDEA8;")

        self.izleme_gecmisi_label = QLabel("İzleme Geçmişi:")
        self.izleme_gecmisi_liste = QListWidget()

        self.izle_button = QPushButton("İzle")
        self.izle_button.clicked.connect(self.icerik_izle)
        self.izle_button.setStyleSheet("background-color: #FFDEA8;")

        self.yenile_button = QPushButton("İzleme Geçmişini Temizle")
        self.yenile_button.clicked.connect(self.yenile_liste)
        self.yenile_button.setStyleSheet("background-color: #FFDEA8;")

        self.gorsel_label = QLabel()
        pixmap = QPixmap("C:\\Users\\90555\\Downloads\\Rectangle 83.png")
        self.gorsel_label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(self.kullanici_adi_label)
        layout.addWidget(self.kullanici_adi_input)
        layout.addWidget(self.sifre_label)
        layout.addWidget(self.sifre_input)
        layout.addWidget(self.giris_button)
        layout.addWidget(self.gorsel_label)
        layout.addWidget(self.izleme_gecmisi_label)
        layout.addWidget(self.izleme_gecmisi_liste)
        layout.addWidget(self.izle_button)
        layout.addWidget(self.yenile_button)

        self.setLayout(layout)

    def giris_yap(self):
        kullanici_adi = self.kullanici_adi_input.text()
        sifre = self.sifre_input.text()

        self.izleme_gecmisi_liste.addItem("Interstellar")
        self.izleme_gecmisi_liste.addItem("Leon")

    def icerik_izle(self):
        secilen_icerik = self.izleme_gecmisi_liste.currentItem().text()
        QMessageBox.information(self, "Bilgi", f"{secilen_icerik} filmi izleniyor...")

    def yenile_liste(self):
        self.izleme_gecmisi_liste.clear()


def main():
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()