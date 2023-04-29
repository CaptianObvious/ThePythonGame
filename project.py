#Импорт
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

#Сделать окно
app = QApplication([])
window = QWidget()


window.setWindowTitle('Игра')
#question = QLabel('')
version = QLabel('Version: Beta-Test')

#расположение виджетов по лэйаутам
layout_main = QVBoxLayout()
layout1 = QHBoxLayout()

layout_main.addWidget(version)
window.setLayout(layout_main)


window.show()
app.exec()