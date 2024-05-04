import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QPixmap, QColor


class HealthTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kişisel Sağlık Takip Uygulaması")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        background_color = QColor("#f0f0f0")
        block_color = QColor("#e0e0e0")
        text_color = QColor("#333333")

        self.setStyleSheet(f"background-color: {background_color.name()};")

        pixmap = QPixmap("C:\\Users\\silay\\Downloads\\Free Vector _ Illustration of healthy lifestyle.jpeg")
        self.image_label = QLabel()
        self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label)

        self.name_label = QLabel("Ad:")
        self.name_label.setStyleSheet(f"color: {text_color.name()};")
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet(f"background-color: {block_color.name()};")
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.age_label = QLabel("Yaş:")
        self.age_label.setStyleSheet(f"color: {text_color.name()};")
        self.age_input = QLineEdit()
        self.age_input.setStyleSheet(f"background-color: {block_color.name()};")
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)

        self.gender_label = QLabel("Cinsiyet:")
        self.gender_label.setStyleSheet(f"color: {text_color.name()};")
        self.gender_input = QLineEdit()
        self.gender_input.setStyleSheet(f"background-color: {block_color.name()};")
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)

        self.health_data_label = QLabel("Sağlık Verileri (örn. Kan Basıncı, Nabız, Kilo, Boy):")
        self.health_data_label.setStyleSheet(f"color: {text_color.name()};")
        self.health_data_input = QTextEdit()
        self.health_data_input.setStyleSheet(f"background-color: {block_color.name()};")
        layout.addWidget(self.health_data_label)
        layout.addWidget(self.health_data_input)

        self.exercise_label = QLabel("Egzersiz Planlama:")
        self.exercise_label.setStyleSheet(f"color: {text_color.name()};")
        self.exercise_input = QTextEdit()
        self.exercise_input.setStyleSheet(f"background-color: {block_color.name()};")
        layout.addWidget(self.exercise_label)
        layout.addWidget(self.exercise_input)

        self.save_data_btn = QPushButton("Verileri Kaydet")
        self.save_data_btn.setStyleSheet(f"background-color: {block_color.name()}; color: {text_color.name()};")
        self.save_exercise_btn = QPushButton("Egzersizi Kaydet")
        self.save_exercise_btn.setStyleSheet(f"background-color: {block_color.name()}; color: {text_color.name()};")
        self.show_report_btn = QPushButton("Raporu Görüntüle")
        self.show_report_btn.setStyleSheet(f"background-color: {block_color.name()}; color: {text_color.name()};")

        layout.addWidget(self.save_data_btn)
        layout.addWidget(self.save_exercise_btn)
        layout.addWidget(self.show_report_btn)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HealthTrackerApp()
    window.show()
    sys.exit(app.exec_())






