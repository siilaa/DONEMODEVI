import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap

class Hasta:
    def __init__(self, isim, tc):
        self.isim = isim
        self.tc = tc
        self.randevu_gecmisi = []

    def randevu_al(self, randevu):
        self.randevu_gecmisi.append(randevu)

    def __str__(self):
        return f"Hasta İsmi: {self.isim}, TC: {self.tc}"

class Doktor:
    def __init__(self, isim, uzmanlık_alanı):
        self.isim = isim
        self.uzmanlık_alanı = uzmanlık_alanı
        self.müsaitlik_durumu = True

    def __str__(self):
        return f"Doktor İsmi: {self.isim}, Uzmanlık Alanı: {self.uzmanlık_alanı}, Müsaitlik Durumu: {'Müsait' if self.müsaitlik_durumu else 'Müsait Değil'}"

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta

    def __str__(self):
        return f"Randevu Tarihi: {self.tarih}, Doktor: {self.doktor.isim}, Hasta: {self.hasta.isim}"

doktorlar = ["Dr. Sıla YETER", "Dr. Selcan ASLAN"]
tarihler = ["2024-05-13", "2024-05-14", "2024-05-15"]

class RandevuArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Randevu Sistemi")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        logo_label = QLabel(self)
        pixmap = QPixmap('C:\\Users\\silay\\Downloads\\Medical Concept with Hospital Stock Vector - Illustration of accident, concept_ 155129863.jpeg')  # Logo dosyanızın adını ve yolunu düzeltin
        logo_label.setPixmap(pixmap)
        logo_label.setScaledContents(True)
        logo_label.setStyleSheet("background-color: #f0f0f0;")

        layout.addWidget(logo_label)

        doktor_label = QLabel("Doktor Seçiniz:")
        doktor_label.setStyleSheet("background-color: #e6e6e6;")
        self.doktor_combo = QComboBox()
        self.doktor_combo.addItems(doktorlar)

        layout.addWidget(doktor_label)
        layout.addWidget(self.doktor_combo)

        tarih_label = QLabel("Randevu Tarihi Seçiniz:")
        tarih_label.setStyleSheet("background-color: #e6e6e6;")
        self.tarih_combo = QComboBox()
        self.tarih_combo.addItems(tarihler)

        layout.addWidget(tarih_label)
        layout.addWidget(self.tarih_combo)

        randevu_al_button = QPushButton("Randevu Al")
        randevu_al_button.setStyleSheet("background-color: #4CAF50; color: white;")
        randevu_al_button.clicked.connect(self.randevu_al)

        layout.addWidget(randevu_al_button)

        self.setLayout(layout)

    def randevu_al(self):

        doktor = self.doktor_combo.currentText()
        tarih = self.tarih_combo.currentText()

        QMessageBox.information(self, "Randevu Alındı", f"{doktor} için {tarih} tarihinde randevunuz alınmıştır.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    arayuz = RandevuArayuzu()
    arayuz.show()
    sys.exit(app.exec_())
