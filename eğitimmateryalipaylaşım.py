import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QTextEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class DersMateryalArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ders Materyal Arayüzü")
        self.setGeometry(100, 100, 600, 400)

        self.dersler_label = QLabel("Dersler:")
        self.dersler_listesi = QListWidget()
        self.dersler_listesi.addItem("Matematik")
        self.dersler_listesi.addItem("Fizik")
        self.dersler_listesi.addItem("Kimya")
        self.dersler_listesi.addItem("Biyoloji")
        self.dersler_listesi.addItem("Tarih")
        self.dersler_listesi.addItem("Coğrafya")
        self.dersler_listesi.addItem("İngilizce")

        self.materyaller_label = QLabel("Materyaller:")
        self.materyaller_listesi = QListWidget()
        self.materyaller_listesi.addItem("Matematik - Ders Notları")
        self.materyaller_listesi.addItem("Fizik - Soru Bankası")
        self.materyaller_listesi.addItem("Kimya - Laboratuvar Deneyleri")
        self.materyaller_listesi.addItem("Biyoloji - Sunumlar")
        self.materyaller_listesi.addItem("Tarih - Belgeseller")
        self.materyaller_listesi.addItem("Coğrafya - Haritalar")
        self.materyaller_listesi.addItem("İngilizce - Konuşma Pratikleri")

        self.materyal_detay_label = QLabel("Materyal Detayları:")
        self.materyal_detay_text = QTextEdit()
        self.materyal_detay_text.setReadOnly(True)

        self.soru_sor_button = QPushButton("Soru Sor")
        self.soru_sor_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.soru_sor_button.clicked.connect(self.soru_sor)


        self.image_label = QLabel()
        pixmap = QPixmap("C:\\Users\\ahmet\\Downloads\\Öğretim-Materyalleri.jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        v_box = QVBoxLayout()
        v_box.addWidget(self.dersler_label)
        v_box.addWidget(self.dersler_listesi)
        v_box.addWidget(self.materyaller_label)
        v_box.addWidget(self.materyaller_listesi)
        v_box.addWidget(self.materyal_detay_label)
        v_box.addWidget(self.materyal_detay_text)
        v_box.addWidget(self.soru_sor_button)


        v_box.addWidget(self.image_label)

        self.setLayout(v_box)

    def soru_sor(self):
        selected_materyal = self.materyaller_listesi.currentItem().text()
        self.materyal_detay_text.append(f"Soru sormak için: {selected_materyal}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DersMateryalArayuzu()
    window.show()
    sys.exit(app.exec_())
