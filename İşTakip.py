import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QLineEdit, \
    QMessageBox
from PyQt5.QtGui import QPixmap


class ProjeArayüzü(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Proje Yönetim Arayüzü")

        self.calisanlar_label = QLabel("Çalışanlar")
        self.calisanlar_liste = QListWidget()
        self.gorevler_label = QLabel("Görevler")
        self.gorevler_liste = QListWidget()

        self.yeni_calisan_input = QLineEdit()
        self.yeni_calisan_button = QPushButton("Yeni Çalışan Ekle")
        self.yeni_gorev_input = QLineEdit()
        self.yeni_gorev_button = QPushButton("Yeni Görev Oluştur")
        self.gorev_ata_button = QPushButton("Görev Ata")

        self.arka_plan_label = QLabel()
        self.arka_plan_yukle()

        v_box = QVBoxLayout()
        v_box.addWidget(self.calisanlar_label)
        v_box.addWidget(self.calisanlar_liste)
        v_box.addWidget(self.gorevler_label)
        v_box.addWidget(self.gorevler_liste)
        v_box.addWidget(self.yeni_calisan_input)
        v_box.addWidget(self.yeni_calisan_button)
        v_box.addWidget(self.yeni_gorev_input)
        v_box.addWidget(self.yeni_gorev_button)
        v_box.addWidget(self.gorev_ata_button)
        v_box.addWidget(self.arka_plan_label)

        self.setLayout(v_box)

        self.yeni_calisan_button.clicked.connect(self.yeni_calisan_ekle)
        self.yeni_gorev_button.clicked.connect(self.yeni_gorev_olustur)
        self.gorev_ata_button.clicked.connect(self.gorev_ata)
        self.gorevler_liste.itemClicked.connect(self.gorevleri_goruntule)
        self.yeni_calisan_button.setStyleSheet("background-color: #8B4513; color: white")
        self.yeni_gorev_button.setStyleSheet("background-color: #8B4513; color: white")
        self.gorev_ata_button.setStyleSheet("background-color: #8B4513; color: white")
        self.yeni_calisan_button.setStyleSheet("font: bold 12px;")
        self.yeni_gorev_button.setStyleSheet("font: bold italic 14px;")
        self.gorev_ata_button.setStyleSheet("font: italic 10px;")

        self.calisanlar = []

    def arka_plan_yukle(self):
        pixmap = QPixmap("C:\\Users\\mcana\\Downloads\\Viral Pazarlama Nedir, Nasıl Yapılır_.jpg")
        self.arka_plan_label.setPixmap(pixmap)
        self.arka_plan_label.setScaledContents(True)

    def yeni_calisan_ekle(self):
        yeni_calisan_adi = self.yeni_calisan_input.text()
        if yeni_calisan_adi:
            self.calisanlar.append(Calisan(yeni_calisan_adi))
            self.calisanlar_liste.addItem(yeni_calisan_adi)
            self.yeni_calisan_input.clear()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir çalışan adı girin.")

    def yeni_gorev_olustur(self):
        yeni_gorev_adi = self.yeni_gorev_input.text()
        if yeni_gorev_adi:
            yeni_gorev = Gorev(yeni_gorev_adi, "")
            self.gorevler_liste.addItem(yeni_gorev_adi)
            self.yeni_gorev_input.clear()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir görev adı girin.")

    def gorev_ata(self):
        secili_calisan = self.calisanlar_liste.currentItem()
        secili_gorev = self.gorevler_liste.currentItem()
        if secili_calisan and secili_gorev:
            secili_gorev.setText(secili_gorev.text() + f" - Sorumlu: {secili_calisan.text()}")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir çalışan ve bir görev seçin.")

    def gorevleri_goruntule(self, item):
        pass


class Gorev:
    def __init__(self, ad, sorumlu_kişi):
        self.ad = ad
        self.sorumlu_kişi = sorumlu_kişi
        self.durum = "Devam Ediyor"


class Calisan:
    def __init__(self, ad):
        self.ad = ad



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    proje_arayuzu = ProjeArayüzü()
    proje_arayuzu.show()
    sys.exit(app.exec_())
