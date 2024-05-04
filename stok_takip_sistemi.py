import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from functools import partial

class Urun:
    def __init__(self, adi, stok_adedi):
        self.adi = adi
        self.stok_adedi = stok_adedi

    def urun_ekle(self, adet):
        self.stok_adedi += adet

    def siparis_olustur(self, adet):
        if adet <= self.stok_adedi:
            self.stok_adedi -= adet
            return True
        else:
            return False

    def stok_guncelle(self, adet):
        self.stok_adedi = adet


class Stok:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, urun):
        self.urunler[urun.adi] = urun

    def stok_guncelle(self, urun_adi, adet):
        if urun_adi in self.urunler:
            self.urunler[urun_adi].stok_guncelle(adet)

    def urunleri_listele(self):
        return self.urunler


class Siparis:
    def __init__(self, siparis_no, urun_adi, adet):
        self.siparis_no = siparis_no
        self.urun_adi = urun_adi
        self.adet = adet


class StokTakipArayuzu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stok Takip Sistemi")
        self.setGeometry(300, 400, 500, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.gorsel_label = QLabel()
        self.gorsel_label.setPixmap(QPixmap("C:\\Users\\pc\\Downloads\\6964210_stock-vector-ddelivery-equipment-warehouse.jpg"))  # Burada resmin dosya yolu verilmelidir.

        self.urun_adi_label = QLabel("Ürün Adı:")
        self.urun_adi_input = QLineEdit()

        self.stok_adedi_label = QLabel("Stok Adedi:")
        self.stok_adedi_input = QLineEdit()

        self.urun_ekle_button = QPushButton("Ürün Ekle")
        self.urun_ekle_button.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;")
        self.urun_ekle_button.clicked.connect(self.urun_ekle)

        self.stok_durumu_button = QPushButton("Stok Durumu")
        self.stok_durumu_button.setStyleSheet(
            "background-color: #f44336; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;")
        self.stok_durumu_button.clicked.connect(self.stok_durumu_goster)

        self.siparis_ver_button = QPushButton("Sipariş Ver")
        self.siparis_ver_button.setStyleSheet(
            "background-color: #008CBA; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;")
        self.siparis_ver_button.clicked.connect(self.siparis_ver)

        self.layout.addWidget(self.gorsel_label)
        self.layout.addWidget(self.urun_adi_label)
        self.layout.addWidget(self.urun_adi_input)
        self.layout.addWidget(self.stok_adedi_label)
        self.layout.addWidget(self.stok_adedi_input)
        self.layout.addWidget(self.urun_ekle_button)
        self.layout.addWidget(self.stok_durumu_button)
        self.layout.addWidget(self.siparis_ver_button)

        # Stok ve ürünlerin oluşturulması
        self.stok = Stok()
        self.stok.urun_ekle(Urun("Bilgisayar", 150))
        self.stok.urun_ekle(Urun("Telefon", 75))
        self.stok.urun_ekle(Urun("Klavye", 25))

    def urun_ekle(self):
        urun_adi = self.urun_adi_input.text()
        stok_adedi = int(self.stok_adedi_input.text())
        self.stok.urun_ekle(Urun(urun_adi, stok_adedi))
        QMessageBox.information(self, "Bilgi", f"{urun_adi} ürünü eklendi. Stok Adedi: {stok_adedi}")

    def stok_durumu_goster(self):
        stoklar = self.stok.urunleri_listele()
        stok_bilgisi = ""
        for urun_adi, urun in stoklar.items():
            stok_bilgisi += f"{urun.adi}: Stok Adedi - {urun.stok_adedi}\n"
        QMessageBox.information(self, "Stok Durumu", stok_bilgisi)

    def siparis_ver(self):
        urun_adi = self.urun_adi_input.text()
        adet = int(self.stok_adedi_input.text())
        if urun_adi in self.stok.urunleri_listele():
            if self.stok.urunleri_listele()[urun_adi].siparis_olustur(adet):
                QMessageBox.information(self, "Sipariş Ver",
                                        f"{adet} adet {urun_adi} ürünü için sipariş alındı.")
            else:
                QMessageBox.warning(self, "Hata", "Yeterli stok bulunmamaktadır.")
        else:
            QMessageBox.warning(self, "Hata", "Ürün bulunamadı.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StokTakipArayuzu()
    window.show()
    sys.exit(app.exec_())


