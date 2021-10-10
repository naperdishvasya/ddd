from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, Qlabel
QMessegeBox, QRadioButton
app = QApplication([])
main_win = QtWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win = resize(400, 200)
question = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
layout_main = QVBoxLayout()
layoutH1 = QVBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()

layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment= Qt.AlignCenter)
layout2.addWidget(btn_answer2, alignment= Qt.AlignCenter)
layout3.addWidget(btn_answer3, alignment= Qt.AlignCenter)
layout3.addWidget(btn_answer4, alignment= Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Верно! \nВы выиграли гироскрутер')
    victory_win.exec_()
def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Нет, в 2015 году! \nВы выиграли фирменный плакат')
    victory_win.exec_()
btn_answer3.clicked.connect(show_win)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)
main_win.show()
app.exec_()