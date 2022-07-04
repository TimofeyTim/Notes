from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QInputDialog, QLineEdit,QListWidget,QApplication,QTextEdit, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
import json
import os 
app = QApplication([])
win = QWidget()


if  os.path.exists('xzxz.json')==False and os.path.isfile('xzxz.json')==False:
    with open('xzxz.json', 'w') as file:
        json.dump({},file)

win.setWindowTitle('Умные заметки')
win.resize(600,400)
TEPEMOK = QTextEdit()#1 поле
TEPEMOK.setPlaceholderText('Введите здесь текст')
nadpisone = QLabel('Список заметок')
zametki = QListWidget()#2 поле
tututu = QLabel('Список тегов')
tegi = QListWidget()#3 поле
qlaneedit = QLineEdit()
qlaneedit.setPlaceholderText('Введите теги')
B1 = QPushButton('Создать заметку')
B2 = QPushButton('Удалите заметки')
B3 = QPushButton('Сохранить заметку')
B4 = QPushButton('Добавить к заметке')
B5 = QPushButton('Открепит от заметки')
B6 = QPushButton('Искать заметки по тегу')


mainline = QHBoxLayout()
l1 =  QVBoxLayout()
l1.addWidget(TEPEMOK)

l2 = QVBoxLayout()
l2.addWidget(nadpisone)
l2.addWidget(zametki)#Добавить все виджеты 
g1 = QHBoxLayout()
g1.addWidget(B1)
g1.addWidget(B2)
l2.addLayout(g1)
l2.addWidget(B3)
l2.addWidget(tututu)
l2.addWidget(tegi)
l2.addWidget(qlaneedit)


g2 = QHBoxLayout()
g2.addWidget(B4)
g2.addWidget(B5)
l2.addLayout(g2)
l2.addWidget(B6)
mainline.addLayout(l1)
mainline.addLayout(l2)
win.setLayout(mainline)


def obr():
    zametka = zametki.selectedItems()[0].text()
    print(zametka)
    TEPEMOK.setText(apu[zametka]['text'])  
    tegi.clear()
    tegi.addItems(apu[zametka]['tegs'])
zametki.itemClicked.connect(obr)
def create():
    name,state = QInputDialog.getText(win,'new zametka','Введите название')
    if state and name != '':
        apu[name] =  {'text':'','tegs':[]}
        tegi.clear()
        zametki.addItem(name)
def deleat():  
    if zametki.selectedItems():
        zametka = zametki.selectedItems()[0].text()
        del apu[zametka]
        TEPEMOK.clear()
        tegi.clear()
        zametki.clear()
        zametki.addItems(apu)
        with open('xzxz.json', 'w') as file:
            json.dump(apu,file)
    else:
        print('Выделите заметку для удаления ')
def save():
    if zametki.selectedItems():
        zametka = zametki.selectedItems()[0].text()
        apu[zametka]['text'] = TEPEMOK.toPlainText()
        with open('xzxz.json', 'w') as file:
            json.dump(apu,file)
    else:
        print('Выделите заметку для сохранения')
    





B1.clicked.connect(create)
B2.clicked.connect(deleat)
B3.clicked.connect(save)








with open('xzxz.json', 'r') as file:
    apu = json.load(file)
    zametki.addItems(apu)



























win.show()
app.exec()