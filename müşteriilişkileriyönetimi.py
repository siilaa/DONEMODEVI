import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap


class CRMWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Müşteri İlişkileri Yönetimi")
        self.setGeometry(100, 100, 600, 400)


        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 50, 500, 200)


        pixmap = QPixmap("C:\\Users\\ahmet\\Downloads\\Great Learning launches SaaS-based digital campus solution.jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)


        self.customer_label = QLabel("Müşteri Adı:", self)
        self.customer_label.setGeometry(50, 270, 100, 30)

        self.customer_name_input = QLineEdit(self)
        self.customer_name_input.setGeometry(150, 270, 200, 30)

        self.customer_email_label = QLabel("E-posta:", self)
        self.customer_email_label.setGeometry(50, 310, 100, 30)

        self.customer_email_input = QLineEdit(self)
        self.customer_email_input.setGeometry(150, 310, 200, 30)

        self.customer_phone_label = QLabel("Telefon:", self)
        self.customer_phone_label.setGeometry(50, 350, 100, 30)

        self.customer_phone_input = QLineEdit(self)
        self.customer_phone_input.setGeometry(150, 350, 200, 30)

        self.add_customer_button = QPushButton("Müşteri Ekle", self)
        self.add_customer_button.setGeometry(200, 400, 150, 30)
        self.add_customer_button.clicked.connect(self.add_customer)

    def add_customer(self):
        name = self.customer_name_input.text()
        email = self.customer_email_input.text()
        phone = self.customer_phone_input.text()


        print("Müşteri Eklendi:", name, email, phone)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CRMWindow()
    window.show()
    sys.exit(app.exec_())

