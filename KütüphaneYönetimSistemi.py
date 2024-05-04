import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtGui import QPixmap

class KütüphaneArayüzü(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Kütüphane Yönetim Sistemi")
        self.setGeometry(100, 100, 400, 300)


        self.kitap_id_label = QLabel("Kitap ID:")
        self.kitap_id_input = QLineEdit()
        self.ad_label = QLabel("Kitap Adı:")
        self.ad_input = QLineEdit()
        self.yazar_label = QLabel("Yazar:")
        self.yazar_input = QLineEdit()
        self.kitap_ekle_button = QPushButton("Kitap Ekle")
        self.kitap_ekle_button.clicked.connect(self.kitap_ekle)
        self.kitap_ekle_button.setStyleSheet("background-color: #8C4B26 ;")


        self.uye_id_label = QLabel("Üye ID:")
        self.uye_id_input = QLineEdit()
        self.ad_soyad_label = QLabel("Ad Soyad:")
        self.ad_soyad_input = QLineEdit()
        self.uye_ekle_button = QPushButton("Üye Ekle")
        self.uye_ekle_button.clicked.connect(self.uye_ekle)
        self.uye_ekle_button.setStyleSheet("background-color: #8C4B26;")


        self.odunc_al_button = QPushButton("Ödünç Al")
        self.odunc_al_button.clicked.connect(self.odunc_al)
        self.odunc_al_button.setStyleSheet("background-color: #8C4B26;")

        self.iade_et_button = QPushButton("İade Et")
        self.iade_et_button.clicked.connect(self.iade_et)
        self.iade_et_button.setStyleSheet("background-color: #8C4B26;")


        self.gorsel_label = QLabel(self)
        pixmap = QPixmap("C:/Users/90555/Downloads/aaa.webp")
        self.gorsel_label.setPixmap(pixmap)


        layout = QVBoxLayout()

        kitap_layout = QVBoxLayout()
        kitap_layout.addWidget(self.kitap_id_label)
        kitap_layout.addWidget(self.kitap_id_input)
        kitap_layout.addWidget(self.ad_label)
        kitap_layout.addWidget(self.ad_input)
        kitap_layout.addWidget(self.yazar_label)
        kitap_layout.addWidget(self.yazar_input)
        kitap_layout.addWidget(self.kitap_ekle_button)

        uye_layout = QVBoxLayout()
        uye_layout.addWidget(self.uye_id_label)
        uye_layout.addWidget(self.uye_id_input)
        uye_layout.addWidget(self.ad_soyad_label)
        uye_layout.addWidget(self.ad_soyad_input)
        uye_layout.addWidget(self.uye_ekle_button)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.odunc_al_button)
        button_layout.addWidget(self.iade_et_button)

        layout.addWidget(self.gorsel_label)
        layout.addLayout(kitap_layout)
        layout.addLayout(uye_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def kitap_ekle(self):
        kitap_id = self.kitap_id_input.text()
        ad = self.ad_input.text()
        yazar = self.yazar_input.text()



        QMessageBox.information(self, "Bilgi", "Kitap başarıyla eklendi.")

    def uye_ekle(self):
        uye_id = self.uye_id_input.text()
        ad_soyad = self.ad_soyad_input.text()



        QMessageBox.information(self, "Bilgi", "Üye başarıyla eklendi.")

    def odunc_al(self):
        kitap_id, ok = QInputDialog.getText(self, 'Ödünç Al', 'Ödünç almak istediğiniz kitabın ID\'sini giriniz:')
        if ok:

            pass
        else:
            QMessageBox.warning(self, "Uyarı", "Kitap ID'si girilmedi.")

    def iade_et(self):
        kitap_id, ok = QInputDialog.getText(self, 'İade Et', 'İade etmek istediğiniz kitabın ID\'sini giriniz:')
        if ok:

            pass
        else:
            QMessageBox.warning(self, "Uyarı", "Kitap ID'si girilmedi.")

def main():
    app = QApplication(sys.argv)
    arayüz = KütüphaneArayüzü()
    arayüz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
