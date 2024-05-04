import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap

class EtkinlikYonetimSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Etkinlik Yonetim Sistemi")
        self.setGeometry(100, 100, 600, 400)

        self.background_label = QLabel(self)
        pixmap = QPixmap("C:\\Users\\mcana\\OneDrive\\Masaüstü\\85005498-86b8-4311-87f2-0d4d589fd28b.jpg")
        self.setStyleSheet(f"background-image: url({pixmap});")
        self.background_label.setPixmap(pixmap.scaled(self.size()))
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        self.etkinlik_adi_label = QLabel("Etkinlik Adı:")
        self.etkinlik_adi_input = QLineEdit()
        self.etkinlik_fiyati_label = QLabel("Etkinlik Fiyatı:")
        self.etkinlik_fiyati_input = QLineEdit()
        self.etkinlik_ekle_button = QPushButton("Etkinlik Kaydet!")
        self.etkinlik_ekle_button.clicked.connect(self.etkinlik_ekle_clicked)

        self.katilimci_adi_label = QLabel("Katılımcı Adı Ve Soyadı:")
        self.katilimci_adi_input = QLineEdit()
        self.katilimci_email_label = QLabel("Katılımcı Email Adresi:")
        self.katilimci_email_input = QLineEdit()
        self.katilimci_telefon_label = QLabel("Katılımcı Telefon Numarası:")
        self.katilimci_telefon_input = QLineEdit()
        self.katilimci_ekle_button = QPushButton("Katılımcı Ekle!")
        self.katilimci_ekle_button.clicked.connect(self.katilimci_ekle_clicked)

        self.katilimci_liste_button = QPushButton("Katılımcıları Görüntüle")
        self.katilimci_liste_button.clicked.connect(self.katilimci_listele_clicked)

        self.etkinlik_liste_button = QPushButton("Etkinlikleri Görüntüle")
        self.etkinlik_liste_button.clicked.connect(self.etkinlik_listele_clicked)

        self.katilimci_liste = QListWidget()
        self.etkinlik_liste = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.etkinlik_adi_label)
        layout.addWidget(self.etkinlik_adi_input)
        layout.addWidget(self.etkinlik_fiyati_label)
        layout.addWidget(self.etkinlik_fiyati_input)
        layout.addWidget(self.etkinlik_ekle_button)

        layout.addWidget(self.katilimci_adi_label)
        layout.addWidget(self.katilimci_adi_input)
        layout.addWidget(self.katilimci_email_label)
        layout.addWidget(self.katilimci_email_input)
        layout.addWidget(self.katilimci_telefon_label)
        layout.addWidget(self.katilimci_telefon_input)
        layout.addWidget(self.katilimci_ekle_button)

        layout.addWidget(self.katilimci_liste_button)
        layout.addWidget(self.katilimci_liste)

        layout.addWidget(self.etkinlik_liste_button)
        layout.addWidget(self.etkinlik_liste)

        self.setLayout(layout)

        self.katilimcilar = []
        self.etkinlikler = []

    def etkinlik_ekle_clicked(self):
        etkinlik_adi = self.etkinlik_adi_input.text()
        etkinlik_fiyati = self.etkinlik_fiyati_input.text()

        self.etkinlikler.append({"adi": etkinlik_adi, "fiyat": etkinlik_fiyati})

        QMessageBox.information(self, "Bilgi", "Etkinlik Başarıyla Kaydedildi!")

    def katilimci_ekle_clicked(self):
        katilimci_adi = self.katilimci_adi_input.text()
        katilimci_email = self.katilimci_email_input.text()
        katilimci_telefon = self.katilimci_telefon_input.text()

        self.katilimcilar.append((katilimci_adi, katilimci_email, katilimci_telefon))

        QMessageBox.information(self, "Bilgi", "Katılımcı Başarıyla Kaydedildi!")

    def katilimci_listele_clicked(self):
        self.katilimci_liste.clear()
        for katilimci in self.katilimcilar:
            item = QListWidgetItem(f"{katilimci[0]} - {katilimci[1]} - {katilimci[2]}")
            self.katilimci_liste.addItem(item)

    def etkinlik_listele_clicked(self):
        self.etkinlik_liste.clear()
        for etkinlik in self.etkinlikler:
            item = QListWidgetItem(f"{etkinlik['adi']} - {etkinlik['fiyat']}")
            self.etkinlik_liste.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EtkinlikYonetimSistemi()
    window.show()
    sys.exit(app.exec_())
