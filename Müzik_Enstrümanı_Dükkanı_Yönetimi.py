import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap

class DukkanYonetimi:
    def __init__(self):
        self.enstrumanlar = {}
        self.musteriler = {}
        self.siparis_kayitlari = {}

    def enstruman_ekle(self, ad, stok):
        if ad not in self.enstrumanlar:
            self.enstrumanlar[ad] = stok
            return True
        else:
            return False

    def musteri_ekle(self, ad, soyad, email):
        musteri_id = f"{ad}_{soyad}".lower().replace(" ", "_")
        self.musteriler[musteri_id] = {"ad": ad, "soyad": soyad, "email": email}

    def siparis_yap(self, musteri_id, urunler):
        if all(urun in self.enstrumanlar and self.enstrumanlar[urun] > 0 for urun in urunler):
            siparis_no = f"siparis_{len(self.siparis_kayitlari) + 1}"
            self.siparis_kayitlari[siparis_no] = {"musteri": musteri_id, "urunler": urunler}
            for urun in urunler:
                self.enstrumanlar[urun] -= 1
            return siparis_no
        else:
            return None

class DukkanArayuz(QWidget):
    def __init__(self, dukkan):
        super().__init__()
        self.dukkan = dukkan
        self.setWindowTitle("Müzik Enstrümanı Dükkanı")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        logo_label = QLabel(self)
        pixmap = QPixmap('C:\\Users\\silay\\OneDrive\\Masaüstü\\db2bfa0c-42dc-4d04-98c1-e1f481f5b9c5.jpg')
        logo_label.setPixmap(pixmap)
        logo_label.setScaledContents(True)

        layout.addWidget(logo_label)

        enstruman_ekle_label = QLabel("Enstrüman Ekle")
        self.enstruman_ad_input = QLineEdit()
        self.enstruman_ad_input.setPlaceholderText("Enstrüman Adı")
        self.miktar_input = QLineEdit()
        self.miktar_input.setPlaceholderText("Stok Miktarı")
        self.enstruman_ekle_button = QPushButton("Enstrüman Ekle")
        self.enstruman_ekle_button.clicked.connect(self.enstruman_ekle)

        layout.addWidget(enstruman_ekle_label)
        layout.addWidget(self.enstruman_ad_input)
        layout.addWidget(self.miktar_input)
        layout.addWidget(self.enstruman_ekle_button)

        self.setLayout(layout)

        enstruman_label = QLabel("Enstrüman Satın Al")
        self.enstruman_ad_input_satinal = QLineEdit()
        self.enstruman_ad_input_satinal.setPlaceholderText("Enstrüman Adı")
        self.miktar_input_satinal = QLineEdit()
        self.miktar_input_satinal.setPlaceholderText("Miktar")
        self.satin_al_button = QPushButton("Satın Al")
        self.satin_al_button.clicked.connect(self.satin_al)

        layout.addWidget(enstruman_label)
        layout.addWidget(self.enstruman_ad_input_satinal)
        layout.addWidget(self.miktar_input_satinal)
        layout.addWidget(self.satin_al_button)

        siparis_label = QLabel("Sipariş Geçmişi")
        self.siparis_gecmisi_text = QTextEdit()
        self.siparis_gecmisi_text.setReadOnly(True)

        layout.addWidget(siparis_label)
        layout.addWidget(self.siparis_gecmisi_text)

    def enstruman_ekle(self):
        enstruman_ad = self.enstruman_ad_input.text()
        miktar = self.miktar_input.text()
        if enstruman_ad and miktar:
            if self.dukkan.enstruman_ekle(enstruman_ad, int(miktar)):
                QMessageBox.information(self, "Başarılı", "Enstrüman başarıyla eklendi.")
            else:
                QMessageBox.warning(self, "Hata", "Bu isimde bir enstrüman zaten var.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen enstrüman adı ve stok miktarını girin.")

    def satin_al(self):
        enstruman_ad = self.enstruman_ad_input_satinal.text()
        miktar = self.miktar_input_satinal.text()
        if enstruman_ad and miktar:
            if enstruman_ad in self.dukkan.enstrumanlar and self.dukkan.enstrumanlar[enstruman_ad] >= int(miktar):
                siparis_no = self.dukkan.siparis_yap("musteri_id", [enstruman_ad])
                if siparis_no:
                    self.siparis_gecmisi_text.append(f"Sipariş Numarası: {siparis_no}, Satın Alınan Enstrüman: {enstruman_ad}, Miktar: {miktar}")
                    QMessageBox.information(self, "Başarılı", "Enstrüman başarıyla satın alındı.")
                else:
                    QMessageBox.warning(self, "Hata", "Sipariş verilemedi, stokta yeterli enstrüman yok.")
            else:
                QMessageBox.warning(self, "Hata", "Lütfen geçerli bir enstrüman adı ve miktar girin.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen enstrüman adı ve miktarı girin.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dukkan = DukkanYonetimi()
    arayuz = DukkanArayuz(dukkan)
    arayuz.show()
    sys.exit(app.exec_())
