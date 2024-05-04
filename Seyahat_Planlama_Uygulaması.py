import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QInputDialog, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap, QColor, QImage

class SeyahatPlanlayici(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Seyahat Planlayıcı')
        self.setGeometry(200, 200, 400, 300)

        self.rota_listesi = QListWidget()
        self.konaklama_listesi = QListWidget()
        self.plan_listesi = QListWidget()

        self.rota_ekle_buton = QPushButton('Rota Ekle')
        self.konaklama_goster_buton = QPushButton('Konaklama Seçeneklerini Göster')
        self.plan_duzenle_buton = QPushButton('Seyahat Planını Düzenle')

        self.rota_listesi.setStyleSheet("background-color: #8B4513; color: white;")
        self.konaklama_listesi.setStyleSheet("background-color: #8B4513; color: white;")
        self.plan_listesi.setStyleSheet("background-color: #8B4513; color: white;")

        self.rota_ekle_buton.setStyleSheet("background-color: #8B4513; color: white;")
        self.konaklama_goster_buton.setStyleSheet("background-color: #8B4513; color: white;")
        self.plan_duzenle_buton.setStyleSheet("background-color: #8B4513; color: white;")

        pixmap = QPixmap('C:\\Users\\silay\\OneDrive\\Resimler\\NYC SKYLINE.jpg')

        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)

        image = QImage('C:\\Users\\silay\\OneDrive\\Resimler\\NYC SKYLINE.jpg')
        dominant_color = QColor(image.pixel(0, 0))

        background_color = dominant_color.name()
        self.setStyleSheet(f"background-color: {background_color};")

        v_box = QVBoxLayout()
        v_box.addWidget(self.rota_listesi)
        v_box.addWidget(self.rota_ekle_buton)
        v_box.addWidget(self.konaklama_listesi)
        v_box.addWidget(self.konaklama_goster_buton)
        v_box.addWidget(self.plan_listesi)
        v_box.addWidget(self.plan_duzenle_buton)
        v_box.addWidget(self.image_label)

        self.setLayout(v_box)

        self.rota_ekle_buton.clicked.connect(self.rota_ekle)
        self.konaklama_goster_buton.clicked.connect(self.konaklama_goster)
        self.plan_duzenle_buton.clicked.connect(self.plan_duzenle)

    def rota_ekle(self):
        rota_adi, ok_pressed = QInputDialog.getText(self, "Rota Ekle", "Rota Adı:")
        if ok_pressed:
            if rota_adi.strip():
                self.rota_listesi.addItem(rota_adi)
            else:
                QMessageBox.warning(self, "Uyarı", "Lütfen bir rota adı girin.")

    def konaklama_goster(self):
        konaklama_secenekleri = ["Warwick Otel", "33 Seaport Otel", "Pod 39 Otel"]
        self.konaklama_listesi.clear()
        self.konaklama_listesi.addItems(konaklama_secenekleri)

    def plan_duzenle(self):
        selected_item = self.rota_listesi.currentItem()
        if selected_item:
            gun_adi, ok_pressed = QInputDialog.getText(self, "Seyahat Planı Düzenle", "Gün Adı:")
            if ok_pressed:
                if gun_adi.strip():
                    aktivite, ok_pressed = QInputDialog.getText(self, "Seyahat Planı Düzenle", "Aktivite:")
                    if ok_pressed:
                        if aktivite.strip():
                            self.plan_listesi.addItem(f"{gun_adi}: {aktivite}")
                        else:
                            QMessageBox.warning(self, "Uyarı", "Lütfen bir aktivite adı girin.")
                else:
                    QMessageBox.warning(self, "Uyarı", "Lütfen bir gün adı girin.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir rota seçin.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SeyahatPlanlayici()
    window.show()
    sys.exit(app.exec_())
