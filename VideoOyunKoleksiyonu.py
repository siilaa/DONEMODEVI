import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QPixmap, QFont

class Oyun:
    def __init__(self, adi):
        self.adi = adi

class Koleksiyon:
    def __init__(self):
        self.oyunlar = []

    def oyun_ekle(self, oyun):
        self.oyunlar.append(oyun)

class Oyuncu:
    def __init__(self, adi):
        self.adi = adi
        self.koleksiyon = Koleksiyon()

class OyunArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Oyun Koleksiyon Yöneticisi")
        self.setGeometry(100, 100, 600, 400)

        self.bg_label = QLabel(self)
        self.bg_pixmap = QPixmap("C:\\Users\\mcana\\Downloads\\DOTA 2.jpg")
        self.bg_label.setPixmap(self.bg_pixmap)
        self.bg_label.setGeometry(0, 0, self.bg_pixmap.width(), self.bg_pixmap.height())

        self.label_adi = QLabel("OYUNCU ADI:", self)
        self.label_adi.setStyleSheet("color: white; font-size: 20px;")
        self.edit_adi = QLineEdit(self)

        self.label_oyun_adi = QLabel("OYUN ADI:", self)
        self.label_oyun_adi.setStyleSheet("color: white; font-size: 20px;")
        self.edit_oyun_adi = QLineEdit(self)

        self.button_oyun_ekle = QPushButton("OYUN EKLE", self)
        self.button_oyun_ekle.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px;")
        self.button_oyun_ekle.clicked.connect(self.oyun_ekle)

        self.button_koleksiyonu_goruntule = QPushButton("KOLEKSİYONU GÖRÜNTÜLÜ!", self)
        self.button_koleksiyonu_goruntule.setStyleSheet("background-color: #008CBA; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px;")
        self.button_koleksiyonu_goruntule.clicked.connect(self.koleksiyonu_goruntule)

        self.text_edit = QTextEdit(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_adi)
        vbox.addWidget(self.edit_adi)
        vbox.addWidget(self.label_oyun_adi)
        vbox.addWidget(self.edit_oyun_adi)
        vbox.addWidget(self.button_oyun_ekle)
        vbox.addWidget(self.button_koleksiyonu_goruntule)
        vbox.addWidget(self.text_edit)

        self.setLayout(vbox)

    def oyun_ekle(self):
        oyuncu_adi = self.edit_adi.text()
        oyun_adi = self.edit_oyun_adi.text()
        if oyuncu_adi and oyun_adi:
            oyun = Oyun(oyun_adi)
            oyuncu = self.get_oyuncu(oyuncu_adi)
            oyuncu.koleksiyon.oyun_ekle(oyun)
            self.text_edit.append(f"{oyun_adi} oyunu, {oyuncu_adi} koleksiyonuna eklendi.")

    def koleksiyonu_goruntule(self):
        oyuncu_adi = self.edit_adi.text()
        if oyuncu_adi:
            oyuncu = self.get_oyuncu(oyuncu_adi)
            self.text_edit.append(f"{oyuncu_adi} koleksiyonu:")
            for oyun in oyuncu.koleksiyon.oyunlar:
                self.text_edit.append(f"- {oyun.adi}")

    def get_oyuncu(self, adi):
        if adi not in oyuncular:
            oyuncular[adi] = Oyuncu(adi)
        return oyuncular[adi]

oyuncular = {}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OyunArayuzu()
    window.show()
    sys.exit(app.exec_())
