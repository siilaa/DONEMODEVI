import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap

class Kitap:
    def __init__(self, ad, yazar, yayinevi):
        self.ad = ad
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.yorumlar = []

    def kitap_ekle(self):
        print(f"{self.ad} kitabı eklendi.")

    def kitap_oku(self):
        print(f"{self.ad} kitabı okunuyor...")

    def yorum_yap(self, yorum):
        self.yorumlar.append(yorum)
        print(f"Yorumunuz gönderildi: {yorum}")

class Kullanici:
    def __init__(self, ad, sifre):
        self.ad = ad
        self.sifre = sifre
        self.okuma_listesi = []

    def kitap_oku(self, kitap):
        self.okuma_listesi.append(kitap)
        print(f"{self.ad} kitabı okunuyor...")

    def yorum_yap(self, kitap, yorum):
        kitap.yorum_yap(yorum)

class KitapOkumaArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kitap Okuma Platformu")
        self.setGeometry(100, 100, 500, 400)

        self.kitaplar = [Kitap("Kitap 1", "Yazar 1", "Yayınevi 1"),
                         Kitap("Kitap 2", "Yazar 2", "Yayınevi 2"),
                         Kitap("Kitap 3", "Yazar 3", "Yayınevi 3")]

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.kitaplar_listesi = QLabel("Kitaplar:")
        layout.addWidget(self.kitaplar_listesi)

        self.kitaplar_combo = QLineEdit()
        self.kitaplar_combo.setPlaceholderText("Kitap seçin veya arama yapın")
        layout.addWidget(self.kitaplar_combo)


        self.image_label = QLabel(self)
        pixmap = QPixmap("C:\\Users\\90555\\Downloads\\Rectangle 84.png")
        self.image_label.setPixmap(pixmap)


        layout.addWidget(self.image_label)

        self.kitap_oku_button = QPushButton("Kitap Oku")
        self.kitap_oku_button.clicked.connect(self.kitap_oku)
        layout.addWidget(self.kitap_oku_button)

        self.yorum_yap_label = QLabel("Yorumunuz:")
        layout.addWidget(self.yorum_yap_label)

        self.yorum_yap_input = QTextEdit()
        layout.addWidget(self.yorum_yap_input)

        self.yorum_yap_button = QPushButton("Yorum Yap")
        self.yorum_yap_button.clicked.connect(self.yorum_yap)
        layout.addWidget(self.yorum_yap_button)

        self.setLayout(layout)

    def kitap_oku(self):
        secilen_kitap_adi = self.kitaplar_combo.text()
        secilen_kitap = next((kitap for kitap in self.kitaplar if kitap.ad == secilen_kitap_adi), None)
        if secilen_kitap:
            secilen_kitap.kitap_oku()
        else:
            QMessageBox.warning(self, "Uyarı", "Geçerli bir kitap seçiniz.")

    def yorum_yap(self):
        secilen_kitap_adi = self.kitaplar_combo.text()
        secilen_kitap = next((kitap for kitap in self.kitaplar if kitap.ad == secilen_kitap_adi), None)
        if secilen_kitap:
            yorum = self.yorum_yap_input.toPlainText()
            secilen_kitap.yorum_yap(yorum)
            self.yorum_yap_input.clear()
        else:
            QMessageBox.warning(self, "Uyarı", "Geçerli bir kitap seçiniz.")


def main():
    app = QApplication(sys.argv)
    arayuz = KitapOkumaArayuzu()
    arayuz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
