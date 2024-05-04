import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QColor

class RestoranArayuz(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Restoran Sipariş ve Yönetim Sistemi')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.menu_label = QLabel('Menü')
        self.menu_list = QListWidget()
        self.menu_list.addItem('Makarna - 220')
        self.menu_list.addItem('Hamburger - 280')
        self.menu_list.addItem('Pizza - 340')
        self.layout.addWidget(self.menu_label)
        self.layout.addWidget(self.menu_list)

        self.menu_image = QLabel()
        pixmap = QPixmap("C:\\Users\\silay\\Downloads\\Free Vector _ Professional cooking set.jpeg")
        self.menu_image.setPixmap(pixmap)
        self.menu_image.setScaledContents(True)
        self.layout.addWidget(self.menu_image)

        self.set_background_color("C:\\Users\\silay\\Downloads\\Free Vector _ Professional cooking set.jpeg")

        self.order_label = QLabel('Sipariş Formu')
        self.product_label = QLabel('Ürün Adı:')
        self.product_input = QLineEdit()
        self.quantity_label = QLabel('Miktar:')
        self.quantity_input = QLineEdit()
        self.order_button = QPushButton('Sipariş Ver')
        self.layout.addWidget(self.order_label)
        self.layout.addWidget(self.product_label)
        self.layout.addWidget(self.product_input)
        self.layout.addWidget(self.quantity_label)
        self.layout.addWidget(self.quantity_input)
        self.layout.addWidget(self.order_button)

        self.cart_label = QLabel('Sepet')
        self.cart_list = QListWidget()
        self.layout.addWidget(self.cart_label)
        self.layout.addWidget(self.cart_list)

        self.confirm_button = QPushButton('Siparişi Onayla')
        self.layout.addWidget(self.confirm_button)

        self.setLayout(self.layout)

        self.order_button.clicked.connect(self.add_to_cart)
        self.confirm_button.clicked.connect(self.confirm_order)

    def set_background_color(self, image_path):
        image = QPixmap(image_path)
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), QColor(image.toImage().pixel(0, 0)))
        self.setPalette(palette)

    def add_to_cart(self):
        product = self.product_input.text()
        quantity = self.quantity_input.text()
        if product and quantity:
            order_text = f"{product} - {quantity}"
            self.cart_list.addItem(order_text)
            self.product_input.clear()
            self.quantity_input.clear()
        else:
            QMessageBox.warning(self, 'Uyarı', 'Ürün adı ve miktarı giriniz.')

    def confirm_order(self):
        selected_items = [item.text() for item in self.cart_list.selectedItems()]
        if selected_items:
            QMessageBox.information(self, 'Sipariş Onayı', 'Siparişiniz alındı.')
        else:
            QMessageBox.warning(self, 'Uyarı', 'Lütfen bir sipariş seçiniz.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    arayuz = RestoranArayuz()
    arayuz.show()
    sys.exit(app.exec_())



