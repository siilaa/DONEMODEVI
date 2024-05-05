import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Sporcu:
    def __init__(self, ad, spor_dali):
        self.ad = ad
        self.spor_dali = spor_dali
        self.antrenmanlar = []

    def program_olustur(self, antrenman):
        self.antrenmanlar.append(antrenman)
        return f"{self.ad} için {antrenman.ad} antrenman programına eklendi."

    def ilerleme_kaydet(self, antrenman, ilerleme):
        antrenman.ilerleme_kaydet(ilerleme)
        return f"{self.ad}, {antrenman.ad} antrenmanı için ilerleme kaydetti."

    def rapor_al(self):
        rapor = f"{self.ad} için Spor Dalı: {self.spor_dali}\nAntrenmanlar:\n"
        for antrenman in self.antrenmanlar:
            rapor += f"- {antrenman.ad}: İlerleme: {antrenman.ilerleme}\n"
        return rapor


class Antrenman:
    def __init__(self, ad, detaylar):
        self.ad = ad
        self.detaylar = detaylar
        self.ilerleme = 0

    def ilerleme_kaydet(self, ilerleme):
        self.ilerleme = ilerleme


class TakipUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sporcu Antrenman Takip Uygulaması")
        self.setGeometry(100, 100, 400, 400)

        self.sporcu_label = QLabel("Sporcu Adı:")
        self.sporcu_input = QLineEdit()

        self.antrenman_label = QLabel("Antrenman Adı:")
        self.antrenman_input = QLineEdit()

        self.ilerleme_label = QLabel("İlerleme:")
        self.ilerleme_input = QLineEdit()

        self.program_olustur_button = QPushButton("Program Oluştur")
        self.program_olustur_button.clicked.connect(self.program_olustur)
        self.program_olustur_button.setStyleSheet("background-color: #4CAF50; color: white;")

        self.rapor_al_button = QPushButton("Rapor Al")
        self.rapor_al_button.clicked.connect(self.rapor_al)
        self.rapor_al_button.setStyleSheet("background-color: #008CBA; color: white;")

        self.rapor_text = QTextEdit()


        self.image_label = QLabel()
        pixmap = QPixmap("C:\\Users\\ahmet\\Downloads\\sporcu.jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        v_box = QVBoxLayout()
        v_box.addWidget(self.sporcu_label)
        v_box.addWidget(self.sporcu_input)
        v_box.addWidget(self.antrenman_label)
        v_box.addWidget(self.antrenman_input)
        v_box.addWidget(self.ilerleme_label)
        v_box.addWidget(self.ilerleme_input)
        v_box.addWidget(self.program_olustur_button)
        v_box.addWidget(self.rapor_al_button)
        v_box.addWidget(self.rapor_text)


        v_box.addWidget(self.image_label)

        self.setLayout(v_box)

        self.takip = {}

    def program_olustur(self):
        sporcu_ad = self.sporcu_input.text()
        antrenman_ad = self.antrenman_input.text()
        ilerleme = int(self.ilerleme_input.text())

        if sporcu_ad not in self.takip:
            self.takip[sporcu_ad] = Sporcu(sporcu_ad, "")

        sporcu = self.takip[sporcu_ad]
        antrenman = Antrenman(antrenman_ad, "")
        self.rapor_text.append(sporcu.program_olustur(antrenman))
        sporcu.ilerleme_kaydet(antrenman, ilerleme)

    def rapor_al(self):
        sporcu_ad = self.sporcu_input.text()

        if sporcu_ad in self.takip:
            self.rapor_text.append(self.takip[sporcu_ad].rapor_al())
        else:
            self.rapor_text.append(f"{sporcu_ad} adında bir sporcu bulunamadı.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TakipUygulamasi()
    window.show()
    sys.exit(app.exec_())
