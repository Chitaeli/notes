#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QListWidget, QInputDialog)

#показ заметки
def show_note():
    key = werh_widg.selectedItems()[0].text()
    dlinni_widg.setText(notes[key]['текст'])
    niz_widg.clear()
    niz_widg.addItems(notes[key]['теги'])
#создание заметок
def add_note():
    notes_name, ok = QInputDialog.getText(
        window, 'Добавить заметку', 'Название заметки:' )
    if ok:
        notes[notes_name] = {
            'текст': '',
            'теги': []
        }
    werh_widg.clear()
    werh_widg.addItems(notes)
    with open('notes_data.json','w',encoding='utf-8') as file:
        json.dump(notes,file, sort_keys=True, ensure_ascii=False)

#удаление заметки
def del_note():
    if werh_widg.selectedItems():
        key = werh_widg.selectedItems()[0].text()
        del notes[key]
        werh_widg.clear()
        werh_widg.addItems(notes)
        dlinni_widg.clear()
        niz_widg.clear()
        with open('notes_data.json','w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

#сохранение заметки
def self_note():
    if werh_widg.selectedItems():
        key = werh_widg.selectedItems()[0].text()
        notes[key]['текст'] = dlinni_widg.toPlainText()
        with open('notes_data.json','w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

#функция добавления тега
def add_tag():
    if werh_widg.selectedItems():
        key = werh_widg.selectedItems()[0].text()
        tag = poisk.text()
        if tag != '' and not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            niz_widg.addItem(tag)
            poisk.clear()
            with open('notes_data.json','w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)

#удаление тега
def del_tag():
        if niz_widg.selectedItems():
            key = werh_widg.selectedItems()[0].text()
            tag = niz_widg.selectedItems()[0].text()
            notes[key]['теги'].remove(tag)
            niz_widg.clear()
            niz_widg.addItems(notes[key]['теги'])
            with open('notes_data.json','w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)

#поиск по заметке
def search_tag():
    tag = poisk.text()
    if tag != '' and rbtn_6.text() == 'Искать заметки по тегу':
        notes_filtered = dict()
        for key in notes:
            if tag in notes[key]['теги']:
                notes_filtered[key] = notes[key]
        rbtn_6.setText('Сбросить поиск')
        werh_widg.clear()
        niz_widg.clear()
        dlinni_widg.clear()
        werh_widg.addItems(notes_filtered)
    else:
        werh_widg.clear()
        werh_widg.addItems(notes)
        poisk.clear()
        rbtn_6.setText('Искать заметки по тегу')


#создание окна
app = QApplication([])
window = QWidget()
window.resize(900,600)
window.setWindowTitle('Умные заметки')

#создание кнопок
rbtn_1 = QPushButton('Создать заметку')
rbtn_2 = QPushButton('Удалить заметку')
rbtn_3 = QPushButton('Сохранить заметку')
rbtn_4 = QPushButton('Добавить к заметке')
rbtn_5 = QPushButton('Открепить от заметки')
rbtn_6 = QPushButton('Искать заметки по тегу')

#создание надписей
spisok_z = QLabel('Список заметок')
spisok_t = QLabel('Список тегов')

#создание окон
dlinni_widg = QTextEdit()
werh_widg = QListWidget()
niz_widg = QListWidget()

#поиск одной строкой
poisk = QLineEdit()
poisk.setPlaceholderText('Введите тег')

#создание линии главного окна
h_line = QHBoxLayout() #глав
h_line1 = QHBoxLayout() # второстепенные
h_line2 = QHBoxLayout()
v_line3 = QVBoxLayout()
v_line4 = QVBoxLayout()

#прикрепеление линий 
v_line3.addWidget(dlinni_widg)
v_line4.addWidget(spisok_z)
v_line4.addWidget(werh_widg)
h_line1.addWidget(rbtn_1)
h_line1.addWidget(rbtn_2)
v_line4.addLayout(h_line1)
v_line4.addWidget(rbtn_3)
v_line4.addWidget(spisok_t)
v_line4.addWidget(niz_widg)
v_line4.addWidget(poisk)
h_line2.addWidget(rbtn_4)
h_line2.addWidget(rbtn_5)
v_line4.addLayout(h_line2)
v_line4.addWidget(rbtn_6)
h_line.addLayout(v_line3)
h_line.addLayout(v_line4)

#json
with open('notes_data.json','r') as file:
    notes = json.load(file)

werh_widg.addItems(notes)
werh_widg.itemClicked.connect(show_note)
rbtn_1.clicked.connect(add_note)
rbtn_2.clicked.connect(del_note)
rbtn_3.clicked.connect(self_note)
rbtn_4.clicked.connect(add_tag)
rbtn_5.clicked.connect(del_tag)
rbtn_6.clicked.connect(search_tag)
#запуск кода
window.setLayout(h_line)
window.show()
app.exec_()
