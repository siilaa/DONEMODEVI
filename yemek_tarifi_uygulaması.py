import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QListWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap, QColor

class YemekTarifiUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.tarifler = {
            "Pilav": {
                "Malzemeler": "2 su bardağı pirinç, \nYarım su bardağı arpa şehriye, \n3 su bardağı su, \n2 yemek kaşığı tereyağı, \n1–2 damla limon suyu, \nTuz",
                "İçerik": "Pirinci yıkayın, dinlenmeye bırakın,tencerede arpa şehriye ve yağı kavurun , kavrulan şehriyelere pirinci ekleyin su tuz ve 2 damla limon suyu ekleyip kısık ateşte pişmeye bırakın.\nAFİYET OLSUN."

            },
            "Kek": {
                "Malzemeler": "1,5 sb. Şeker, \n3 Adet Yumurta, \n1 sb. Süt, \n1 sb. Yağ, \n1 paket Kakao , \n2,5 sb. Un , \n1 paket Vanilya, \n1 paket Kabartma Tozu ",
                "İçerik": "Öncelikli olarak şeker ve yumurta çırpılır. Daha sonra karışıma sıvı malzemeler eklenir. En son kuru malzemeler ile birlikte aldığı kadar un eklenip yağlanmış kek kalıbında 180 derecelik fırında yaklaşık 30-35 dakika pişiriyoruz. \nAFİYET OLSUN."
            },
            "Mercimek Çorbası": {
                "Malzemeler": "2 sb. Kırmızı mercimek, 1 yemek kaşığı salça , su, 1 adet soğan, 1 adet  havuç, tuz,",
                "İçerik": "Soğanı doğrayın, salça ile kavurun  kavrulduktan sonra küp küp doğranmış havuç ve iyice yıkanıp suyu süzülen mercimekler ilave edilir. Üzerine su eklenerek karıştırılır ve tencerenin kapağı kapatılır. Çorbamız kaynayana kadar orta ateşte, kaynadıktan sonra mercimekler ve havuçlar yumuşayana kadar ara ara karıştırılarak kısık ateşte pişirilir. Üzerine su eklenerek karıştırılır ve tencerenin kapağı kapatılır. Çorbamız kaynayana kadar orta ateşte, kaynadıktan sonra mercimekler ve havuçlar yumuşayana kadar ara ara karıştırılarak kısık ateşte pişirilir. \nAFİYET OLSUN."
            }
        }
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Yemek Tarifi Uygulaması')
        self.setGeometry(200, 200, 500, 500)

        layout = QVBoxLayout()
        layout.setSpacing(10)

        # Görseli ekle
        self.label_resim = QLabel()
        pixmap = QPixmap('C:\\Users\\pc\\Downloads\\preview-xl.jpg')  # Resmin dosya yolunu verin
        self.label_resim.setPixmap(pixmap)
        layout.addWidget(self.label_resim)

        # Tarif seçimi için yatay düzen
        tarif_layout = QHBoxLayout()
        self.label_tarif = QLabel('Tarif Seçin:')
        self.label_tarif.setStyleSheet("color: #e76900")  # Yazı rengi turuncu
        tarif_layout.addWidget(self.label_tarif)

        self.list_tarif = QListWidget()
        self.list_tarif.addItems(self.tarifler.keys())
        self.list_tarif.clicked.connect(self.tarif_secildi)
        tarif_layout.addWidget(self.list_tarif)
        layout.addLayout(tarif_layout)

        self.label_malzemeler = QLabel('Malzemeler:')
        self.label_malzemeler.setStyleSheet("color: #fb0308")  # Yazı rengi açık yeşil
        layout.addWidget(self.label_malzemeler)

        self.input_malzemeler = QTextEdit()
        layout.addWidget(self.input_malzemeler)

        self.label_icerik = QLabel('Tarif İçeriği:')
        self.label_icerik.setStyleSheet("color: #fe0601")  # Yazı rengi mavi
        layout.addWidget(self.label_icerik)

        self.input_icerik = QTextEdit()
        layout.addWidget(self.input_icerik)

        self.setStyleSheet("background-color: #fed59e;")

        self.setLayout(layout)

    def tarif_secildi(self):
        selected_tarif = self.list_tarif.currentItem().text()
        tarif = self.tarifler[selected_tarif]
        self.input_malzemeler.setText(tarif["Malzemeler"])
        self.input_icerik.setText(tarif["İçerik"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YemekTarifiUygulamasi()
    ex.show()
    sys.exit(app.exec_())
