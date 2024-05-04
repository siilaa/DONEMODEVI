import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QListWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor

class Arac:
    def __init__(self, arac_id, model, kiralama_durumu=True):
        self.arac_id = arac_id
        self.model = model
        self.kiralama_durumu = kiralama_durumu

    def arac_durumu_guncelle(self, durum):
        self.kiralama_durumu = durum


class Musteri:
    def __init__(self, musteri_id, ad, soyad):
        self.musteri_id = musteri_id
        self.ad = ad
        self.soyad = soyad

    def __str__(self):
        return f"{self.ad} {self.soyad}"


class KiralamaSistemiArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Araç Kiralama Sistemi")
        self.setGeometry(100, 200, 500, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Arka plan rengini belirleme
        background_color = QColor("#f54fb5")  # Örnek bir arka plan rengi, lavanta rengi
        palette = self.palette()
        palette.setColor(QPalette.Background, background_color)
        self.setPalette(palette)

        # Üstteki görsel
        ust_gorsel_label = QLabel(self)
        ust_gorsel_pixmap = QPixmap("C:\\Users\\pc\\Downloads\\fb92a091a4b23215005c5fdef92a2fec.jpg")
        ust_gorsel_label.setPixmap(ust_gorsel_pixmap)
        layout.addWidget(ust_gorsel_label)

        # Arac ID ve musteri ID girişleri için yatay düzen
        input_layout = QHBoxLayout()

        self.arac_id_input = QLineEdit()
        self.arac_id_input.setPlaceholderText("Araç ID")
        input_layout.addWidget(self.arac_id_input)

        self.musteri_id_input = QLineEdit()
        self.musteri_id_input.setPlaceholderText("Müşteri ID")
        input_layout.addWidget(self.musteri_id_input)

        layout.addLayout(input_layout)

        # Butonlar için yatay düzen
        button_layout = QHBoxLayout()

        self.kiralama_button = QPushButton("Kiralama Yap")
        self.kiralama_button.clicked.connect(self.kiralama_yap)
        button_layout.addWidget(self.kiralama_button)

        self.iptal_button = QPushButton("Kiralama İptal Et")
        self.iptal_button.clicked.connect(self.kiralama_iptal_et)
        button_layout.addWidget(self.iptal_button)

        layout.addLayout(button_layout)

        # Altta bilgi alanı
        self.bilgi_label = QLabel()
        layout.addWidget(self.bilgi_label)

        # Ekstra bloklar
        ekstra_blok_layout = QHBoxLayout()

        # Örnek bir açıklama metni
        aciklama_label = QLabel("Bu uygulama araç kiralama işlemleri için kullanılır.")
        aciklama_label.setFont(QFont("Arial", 10))
        ekstra_blok_layout.addWidget(aciklama_label)

        # İletişim bilgileri
        iletişim_label = QLabel("İletişim: arackiralama@gmail.com - 535 885 55 85")
        iletişim_label.setFont(QFont("Arial", 10))
        ekstra_blok_layout.addWidget(iletişim_label)

        layout.addLayout(ekstra_blok_layout)

        self.setLayout(layout)

    def kiralama_yap(self):
        arac_id = self.arac_id_input.text()
        musteri_id = self.musteri_id_input.text()

        # Araç ID ve müşteri ID girilmiş mi kontrolü
        if not arac_id or not musteri_id:
            QMessageBox.warning(self, "Uyarı", "Lütfen Araç ID ve Müşteri ID giriniz.")
            return

        # Kiralama işlemi
        arac = Arac(arac_id, "Model Bilgisi")
        musteri = Musteri(musteri_id, "Nasıf", "Özgüç")  # Örnek müşteri bilgisi
        arac.arac_durumu_guncelle(False)  # Araç kiralama durumu güncelleme
        self.bilgi_label.setText(f"{musteri} adlı müşteri araç kiraladı.")

    def kiralama_iptal_et(self):
        arac_id = self.arac_id_input.text()

        # Araç ID girilmiş mi kontrolü
        if not arac_id:
            QMessageBox.warning(self, "Uyarı", "Lütfen Araç ID giriniz.")
            return

        # Kiralama iptali işlemi
        arac = Arac(arac_id, "Model Bilgisi")
        arac.arac_durumu_guncelle(True)  # Araç kiralama durumu güncelleme
        self.bilgi_label.setText(f"Araç kiralama iptal edildi.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KiralamaSistemiArayuzu()
    window.show()
    sys.exit(app.exec())