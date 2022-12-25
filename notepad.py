from PyQt6.QtWidgets import QApplication, QWidget, QMenuBar, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QComboBox, QLineEdit, QSpinBox, QFontDialog, QTextEdit, QMessageBox, QInputDialog, QColorDialog
from PyQt6.QtGui import QIcon, QFont, QAction
from PyQt6.QtCore import QSize

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 700, 400)
        self.setWindowTitle("Блокнот")

        menu = QMenuBar()

        file_menu = menu.addMenu("Файл")

        file_save = QAction("Сохранить", self)
        file_save.triggered.connect(self.save_file_func)

        file_open = QAction("Открыть", self)
        file_open.triggered.connect(self.open_file_func)

        file_exit = QAction("Выйти", self)
        file_exit.triggered.connect(self.close)

        file_menu.addAction(file_save)
        file_menu.addAction(file_open)
        file_menu.addAction(file_exit)


        edit_menu = menu.addMenu("Изменить")

        edit_font = QAction("Шрифт", self)
        edit_font.triggered.connect(self.change_font)

        edit_color = QAction("Цвет", self)
        edit_color.triggered.connect(self.change_color)

        edit_find = QAction("Найти", self)
        edit_find.triggered.connect(self.find_something)

        edit_menu.addAction(edit_font)
        edit_menu.addAction(edit_color)
        edit_menu.addAction(edit_find)


        spravka_menu = menu.addMenu("Справка")

        open_spravka = QAction("Инструкция", self)
        open_spravka.triggered.connect(self.spravka_func)

        spravka_menu.addAction(open_spravka)

        vbox = QVBoxLayout()

        self.text = QTextEdit()
        self.text.setStyleSheet("font:16px")
        self.text.setText("")

        vbox.addWidget(menu)
        vbox.addWidget(self.text)

        self.setLayout(vbox)

    def save_file_func(self):
        try:
            savename, savestatus = QInputDialog.getText(self, "Ввод:", "Задайте название файла:")
            with open("{}.txt".format(savename), "w", encoding='UTF-8') as f:
                f.write(self.text.toPlainText())
        except:
            print("Произошла ошибка!")

        """with open("Безымянный.txt", "w", encoding='UTF-8') as f:
            f.write(self.text.toPlainText())"""

    def open_file_func(self):
        try:
            file_name, status = QInputDialog.getText(self, "Ввод:", "Введите название файла:")

            with open("{}.txt".format(file_name), "r", encoding='UTF-8') as r:

                retext = r.read()

                self.text.setText("")
                self.text.setText(retext)

        except:
            self.text.setText("Что-то пошло не так.")



    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text.setFont(font)

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            txt = self.text.toPlainText()
            self.text.setTextColor(color)
            self.text.setText(txt)

    def find_something(self):
        pass


    def spravka_func(self):
        QMessageBox.information(self, "Внимание!!!!!!!!!!", "Спасибо за внимание🥶🥶🥶🥶")









app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())