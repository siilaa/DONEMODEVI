import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QListWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QFont

class TarihciArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarihçi - Tarihi Olaylar")
        self.setGeometry(200, 200, 600, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

       
        ust_gorsel_label = QLabel(self)
        ust_gorsel_pixmap = QPixmap("C:\\Users\\pc\\Downloads\\FC2ULeOXoAASlDM.jpeg")
        ust_gorsel_label.setPixmap(ust_gorsel_pixmap.scaledToWidth(600))  
        layout.addWidget(ust_gorsel_label)

      
        self.olay_listesi = QListWidget()
        self.olay_listesi.setFont(QFont("Arial", 12))
        layout.addWidget(self.olay_listesi)

        arama_label = QLabel("Olayları arayın...", self)
        arama_label.setFont(QFont("Arial", 14))
        layout.addWidget(arama_label)

        self.arama_input = QLineEdit()
        layout.addWidget(self.arama_input)

        self.olay_detaylari = QTextEdit()
        self.olay_detaylari.setFont(QFont("Arial", 12))
        layout.addWidget(self.olay_detaylari)

     
        self.sorgula_button = QPushButton("Sorgula")
        self.sorgula_button.clicked.connect(self.sorgula)
        layout.addWidget(self.sorgula_button)

   
        self.olaylari_listele()

        self.setStyleSheet("background-color: #ff2e1a;")

        self.setLayout(layout)

    def olaylari_listele(self):
     
        self.olaylar = {
            "İstanbul'un Fethi": "6 Nisan 1453 - 29 Mayıs 1453 tarihleri arasında- İstanbul'un fethedildiği gün.",
            "TBMM Açılışı": "23 Nisan 1920 - Türkiye Büyük Millet Meclisi açıldı..",
            "Çanakkale Zaferi": "18 Mart 1915 - Çanakkale Zaferi'nin kazanıldığı gün."
        }

        for olay_adi, aciklama in self.olaylar.items():
            self.olay_listesi.addItem(olay_adi)

    def sorgula(self):
       
        aranan_metin = self.arama_input.text()

       
        bulunan_olaylar = []
        for olay_adi, aciklama in self.olaylar.items():
            if aranan_metin.lower() in olay_adi.lower():
                bulunan_olaylar.append((olay_adi, aciklama))

       
        self.olay_detaylari.clear()
        if bulunan_olaylar:
            self.olay_detaylari.append("Bulunan Olaylar:")
            for olay_adi, aciklama in bulunan_olaylar:
                self.olay_detaylari.append(f"Olay: {olay_adi}\nBilgi: {aciklama}")
        else:
            QMessageBox.information(self, "Bilgi", "Aranan metinle eşleşen bir olay bulunamadı.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TarihciArayuzu()
    window.show()
    sys.exit(app.exec_())
