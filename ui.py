import sys
from res import *


from PyQt6.QtCore import (QRect, QSize)
from PyQt6.QtWidgets import (QApplication, QLabel,
    QMainWindow, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)


class AppUI():
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Calculadora")
        MainWindow.setFixedSize(800,600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(84, 79, 99);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.centralwidget.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0.301136, y1:0.523, x2:1, y2:1, stop:0 rgba(110, 0, 150, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label.setGeometry(QRect(290, 100, 120, 24))
        self.label.setText("Digite a matriz")
        self.lineEdit = QLineEdit(self.centralwidget, editingFinished= self.UPDATE)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(u"font: 900 16pt \"Segoe UI Black\";\n"
    "border: none;")
        self.lineEdit.setGeometry(QRect(290, 125, 300, 24))
        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        self.label2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label2.setGeometry(QRect(150, 150, 200, 30))
        self.label2.setText("Digite a ordem da matriz: ")
        self.label3 = QLabel(self.centralwidget)
        self.label3.setObjectName(u"label")
        self.label3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label3.setGeometry(QRect(430, 220, 70, 30))
        self.label3.setText("Solução: ")
        self.solution = QLineEdit(self.centralwidget, editingFinished= self.solutionCatch)
        self.solution.setObjectName("solution")
        self.solution.setStyleSheet(u"font: 900 16pt \"Segoe UI Black\";\n"
    "border: none;")
        self.solution.setGeometry(QRect(500, 220, 70, 30))
        self.autovetor = QPushButton(self.centralwidget, clicked= self.autovetorShow)
        self.autovetor.setObjectName(u"autovetor")
        self.autovetor.setGeometry(QRect(300, 320, 60, 30))
        self.autovetor.setStyleSheet(u"background-color: rgb(164, 6, 255);\n"
"border-radius: 5px;")
        self.autovetor.setText("Autovetor")
        self.Autovalor = QPushButton(self.centralwidget, clicked= self.autovalorShow)
        self.Autovalor.setObjectName(u"Autovalor")
        self.Autovalor.setGeometry(QRect(300, 270, 60, 30))
        self.Autovalor.setStyleSheet(u"background-color: rgb(164, 6, 255);\n"
"border-radius: 5px;")
        self.Autovalor.setText("Autovalor")
        self.spinBox = QSpinBox(self.centralwidget, valueChanged=self.updtButtons)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setRange(2, 6)
        self.spinBox.setGeometry(QRect(400, 150, 30, 30))
        self.GaussJordan = QPushButton(self.centralwidget, clicked=self.gaussJordanShow)
        self.GaussJordan.setObjectName(u"GaussJordan")
        self.GaussJordan.setGeometry(QRect(300, 220, 100, 30))
        self.GaussJordan.setStyleSheet(u"background-color: rgb(164, 6, 255);\n"
"border-radius: 5px;")
        self.GaussJordan.setText("Gauss-Jordan")
        self.label5 = QLabel(self.centralwidget)
        self.label5.setObjectName(u"label")
        self.label5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label5.setGeometry(QRect(270, 380, 200, 200))

        
        
        


        MainWindow.setCentralWidget(self.centralwidget)


    def UPDATE(self):
        a = self.lineEdit.text().split(',')
        c = 0
        matriz = [[]]
        try:
            for i in range(self.spinBox.value() ** 2):
                matriz[c].append(int(a[i].replace(" ","")))
                if (i + 1) / self.spinBox.value() == 1 + c and i+1 !=self.spinBox.value() ** 2:
                    matriz.append([])
                    c += 1
        except:
            matriz = [[]]
        self.matriz = Matriz(matriz)

    def updtButtons(self):
        if self.spinBox.value() != 2:
            self.autovetor.setDisabled(True)
            self.Autovalor.setDisabled(True)
        else:
            self.autovetor.setEnabled(True)
            self.Autovalor.setEnabled(True)
    
    def solutionCatch(self):
        a = self.solution.text().split(',')
        result = []
        for i in range(len(a)):
            result.append(int(a[i].replace(" ","")))
        self.solve = result
    
    def autovalorShow(self):
        self.label5.setText(self.ToString(self.matriz.autoValor()))
        
    def autovetorShow(self):
        self.label5.setText(self.matriz.AutoVetor())
        

    
    def gaussJordanShow(self):
        try:
            self.matriz.solve = self.solve
        except:
            self.solve = []
        a = self.matriz.gaussJordan()
        if a == []:
            result = "Sistema sem solução real"
        else:
            result = self.ToString(a)
        self.label5.setText(result)
        self.UPDATE()

    def ToString(self, matriz: list):
        string = ''
        for i in range(len(matriz)):
            string += f"{str(matriz[i])}\n"
        return string