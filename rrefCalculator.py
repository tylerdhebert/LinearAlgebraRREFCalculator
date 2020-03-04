# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rref.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sympy import *
import winsound
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(378, 300))
        MainWindow.setMaximumSize(QtCore.QSize(378, 300))
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.oneOne = QtWidgets.QLineEdit(self.centralwidget)
        self.oneOne.setGeometry(QtCore.QRect(110, 100, 35, 20))
        self.oneOne.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.oneOne.setText("")
        self.oneOne.setPlaceholderText("")
        self.oneOne.setObjectName("oneOne")
        self.oneOne.hide()

        self.threeOne = QtWidgets.QLineEdit(self.centralwidget)
        self.threeOne.setGeometry(QtCore.QRect(110, 180, 35, 20))
        self.threeOne.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.threeOne.setText("")
        self.threeOne.setPlaceholderText("")
        self.threeOne.setObjectName("threeOne")
        self.threeOne.hide()

        self.threeTwo = QtWidgets.QLineEdit(self.centralwidget)
        self.threeTwo.setGeometry(QtCore.QRect(150, 180, 35, 20))
        self.threeTwo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.threeTwo.setText("")
        self.threeTwo.setPlaceholderText("")
        self.threeTwo.setObjectName("threeTwo")
        self.threeTwo.hide()

        self.threeThree = QtWidgets.QLineEdit(self.centralwidget)
        self.threeThree.setGeometry(QtCore.QRect(190, 180, 35, 20))
        self.threeThree.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.threeThree.setText("")
        self.threeThree.setPlaceholderText("")
        self.threeThree.setObjectName("threeThree")
        self.threeThree.hide()

        self.threeFour = QtWidgets.QLineEdit(self.centralwidget)
        self.threeFour.setGeometry(QtCore.QRect(230, 180, 35, 20))
        self.threeFour.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.threeFour.setText("")
        self.threeFour.setPlaceholderText("")
        self.threeFour.setObjectName("threeFour")
        self.threeFour.hide()

        self.fourOne = QtWidgets.QLineEdit(self.centralwidget)
        self.fourOne.setGeometry(QtCore.QRect(110, 220, 35, 20))
        self.fourOne.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.fourOne.setText("")
        self.fourOne.setPlaceholderText("")
        self.fourOne.setObjectName("fourOne")
        self.fourOne.hide()

        self.fourTwo = QtWidgets.QLineEdit(self.centralwidget)
        self.fourTwo.setGeometry(QtCore.QRect(150, 220, 35, 20))
        self.fourTwo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.fourTwo.setText("")
        self.fourTwo.setPlaceholderText("")
        self.fourTwo.setObjectName("fourTwo")
        self.fourTwo.hide()

        self.fourThree = QtWidgets.QLineEdit(self.centralwidget)
        self.fourThree.setGeometry(QtCore.QRect(190, 220, 35, 20))
        self.fourThree.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.fourThree.setText("")
        self.fourThree.setPlaceholderText("")
        self.fourThree.setObjectName("fourThree")
        self.fourThree.hide()

        self.fourFour = QtWidgets.QLineEdit(self.centralwidget)
        self.fourFour.setGeometry(QtCore.QRect(230, 220, 35, 20))
        self.fourFour.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.fourFour.setText("")
        self.fourFour.setPlaceholderText("")
        self.fourFour.setObjectName("fourFour")
        self.fourFour.hide()

        self.oneTwo = QtWidgets.QLineEdit(self.centralwidget)
        self.oneTwo.setGeometry(QtCore.QRect(150, 100, 35, 20))
        self.oneTwo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.oneTwo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.oneTwo.setText("")
        self.oneTwo.setPlaceholderText("")
        self.oneTwo.setObjectName("oneTwo")
        self.oneTwo.hide()

        self.oneThree = QtWidgets.QLineEdit(self.centralwidget)
        self.oneThree.setGeometry(QtCore.QRect(190, 100, 35, 20))
        self.oneThree.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.oneThree.setText("")
        self.oneThree.setPlaceholderText("")
        self.oneThree.setObjectName("oneThree")
        self.oneThree.hide()

        self.oneFour = QtWidgets.QLineEdit(self.centralwidget)
        self.oneFour.setGeometry(QtCore.QRect(230, 100, 35, 20))
        self.oneFour.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.oneFour.setText("")
        self.oneFour.setPlaceholderText("")
        self.oneFour.setObjectName("oneFour")
        self.oneFour.hide()

        self.twoOne = QtWidgets.QLineEdit(self.centralwidget)
        self.twoOne.setGeometry(QtCore.QRect(110, 140, 35, 20))
        self.twoOne.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.twoOne.setText("")
        self.twoOne.setPlaceholderText("")
        self.twoOne.setObjectName("twoOne")
        self.twoOne.hide()

        self.twoTwo = QtWidgets.QLineEdit(self.centralwidget)
        self.twoTwo.setGeometry(QtCore.QRect(150, 140, 35, 20))
        self.twoTwo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.twoTwo.setText("")
        self.twoTwo.setPlaceholderText("")
        self.twoTwo.setObjectName("twoTwo")
        self.twoTwo.hide()

        self.twoThree = QtWidgets.QLineEdit(self.centralwidget)
        self.twoThree.setGeometry(QtCore.QRect(190, 140, 35, 20))
        self.twoThree.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.twoThree.setText("")
        self.twoThree.setPlaceholderText("")
        self.twoThree.setObjectName("twoThree")
        self.twoThree.hide()

        self.twoFour = QtWidgets.QLineEdit(self.centralwidget)
        self.twoFour.setGeometry(QtCore.QRect(230, 140, 35, 20))
        self.twoFour.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.twoFour.setText("")
        self.twoFour.setPlaceholderText("")
        self.twoFour.setObjectName("twoFour")
        self.twoFour.hide()

        self.rowBox = QtWidgets.QComboBox(self.centralwidget)
        self.rowBox.setGeometry(QtCore.QRect(110, 50, 69, 22))
        self.rowBox.setObjectName("rowBox")
        self.rowBox.addItem("")
        self.rowBox.setItemText(0, "Rows")
        self.rowBox.addItem("")
        self.rowBox.addItem("")
        self.rowBox.addItem("")
        self.rowBox.addItem("")
        self.rowBox.currentTextChanged.connect(self.rowBoxChanged)

        self.colBox = QtWidgets.QComboBox(self.centralwidget)
        self.colBox.setGeometry(QtCore.QRect(190, 50, 69, 22))
        self.colBox.setObjectName("colBox")
        self.colBox.addItem("")
        self.colBox.setItemText(0, "Columns")
        self.colBox.addItem("")
        self.colBox.addItem("")
        self.colBox.addItem("")
        self.colBox.addItem("")
        self.colBox.currentTextChanged.connect(self.colBoxChanged)

        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(270, 100, 75, 23))
        self.calculateButton.setObjectName("calculateButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 50, 105, 200))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.oneOne.setTabOrder(self.oneOne, self.oneTwo)
        self.oneTwo.setTabOrder(self.oneTwo, self.oneThree)
        self.oneThree.setTabOrder(self.oneThree, self.oneFour)
        self.oneFour.setTabOrder(self.oneFour, self.twoOne)
        self.twoOne.setTabOrder(self.twoOne, self.twoTwo)
        self.twoTwo.setTabOrder(self.twoTwo, self.twoThree)
        self.twoThree.setTabOrder(self.twoThree, self.twoFour)
        self.twoFour.setTabOrder(self.twoFour, self.threeOne)

        arry = [self.oneOne, self.oneTwo, self.oneThree, self.oneFour], \
               [self.twoOne, self.twoTwo, self.twoThree, self.twoFour], \
               [self.threeOne, self.threeTwo, self.threeThree, self.threeFour], \
               [self.fourOne, self.fourTwo, self.fourThree, self.fourFour]

        self.calculateButton.clicked.connect(self.calculatePressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RREF Calculator"))
        self.rowBox.setItemText(1, _translate("MainWindow", "1"))
        self.rowBox.setItemText(2, _translate("MainWindow", "2"))
        self.rowBox.setItemText(3, _translate("MainWindow", "3"))
        self.rowBox.setItemText(4, _translate("MainWindow", "4"))
        self.colBox.setItemText(1, _translate("MainWindow", "1"))
        self.colBox.setItemText(2, _translate("MainWindow", "2"))
        self.colBox.setItemText(3, _translate("MainWindow", "3"))
        self.colBox.setItemText(4, _translate("MainWindow", "4"))
        self.calculateButton.setText(_translate("MainWindow", "Calculate!"))
        self.label.setText(_translate("MainWindow", "RREF Calculator"))
        self.label1.setText(_translate("MainWindow", "Tyler Hebert\nConnor Scoggins\nRoger Ramirez\n\nMATH 2318\n" \
                                       "Gauss-Jordan\nElimination"))

    def rowBoxChanged(self):
        if self.rowBox.currentText() == "1" and self.colBox.currentText() != "Columns":
            self.oneOne.show()
            if self.colBox.currentText() == "2":
                self.oneOne.show()
                self.oneTwo.show()
            if self.colBox.currentText() == "3":
                self.oneOne.show()
                self.oneTwo.show()
                self.oneThree.show()
            if self.colBox.currentText() == "4":
                self.oneOne.show()
                self.oneTwo.show()
                self.oneThree.show()
                self.oneFour.show()
            self.twoOne.hide()
            self.twoTwo.hide()
            self.threeOne.hide()
            self.fourOne.hide()
            self.threeTwo.hide()
            self.fourTwo.hide()
            self.twoThree.hide()
            self.threeThree.hide()
            self.fourThree.hide()
            self.twoFour.hide()
            self.threeFour.hide()
            self.fourFour.hide()
        if self.rowBox.currentText() == "2" and self.colBox.currentText() != "Columns":
            if self.colBox.currentText() == "1":
                self.oneOne.show()
                self.twoOne.show()
            if self.colBox.currentText() == "2":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
            if self.colBox.currentText() == "3":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
                self.oneThree.show()
                self.twoThree.show()
            if self.colBox.currentText() == "4":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
                self.oneThree.show()
                self.twoThree.show()
                self.oneFour.show()
                self.twoFour.show()
            self.threeOne.hide()
            self.fourOne.hide()
            self.threeTwo.hide()
            self.fourTwo.hide()
            self.threeThree.hide()
            self.fourThree.hide()
            self.threeFour.hide()
            self.fourFour.hide()
        if self.rowBox.currentText() == "3" and self.colBox.currentText() != "Columns":
            if self.colBox.currentText() == "1":
                self.oneOne.show()
                self.twoOne.show()
                self.threeOne.show()
            if self.colBox.currentText() == "2":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
                self.threeOne.show()
                self.threeTwo.show()
            if self.colBox.currentText() == "3":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
                self.oneThree.show()
                self.twoThree.show()
                self.threeOne.show()
                self.threeTwo.show()
                self.threeThree.show()
            if self.colBox.currentText() == "4":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
                self.oneThree.show()
                self.twoThree.show()
                self.oneFour.show()
                self.twoFour.show()
                self.threeOne.show()
                self.threeTwo.show()
                self.threeThree.show()
                self.threeFour.show()
            self.fourOne.hide()
            self.fourTwo.hide()
            self.fourThree.hide()
            self.fourFour.hide()
        if self.rowBox.currentText() == "4" and self.colBox.currentText() != "Columns":
            if self.colBox.currentText() == "1":
                self.oneOne.show()
                self.twoOne.show()
                self.threeOne.show()
                self.fourOne.show()
            if self.colBox.currentText() == "2":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
                self.threeOne.show()
                self.threeTwo.show()
                self.fourOne.show()
                self.fourTwo.show()
            if self.colBox.currentText() == "3":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
                self.oneThree.show()
                self.twoThree.show()
                self.threeOne.show()
                self.threeTwo.show()
                self.threeThree.show()
                self.fourOne.show()
                self.fourTwo.show()
                self.fourThree.show()
            if self.colBox.currentText() == "4":
                self.oneOne.show()
                self.twoOne.show()
                self.oneTwo.show()
                self.twoTwo.show()
                self.oneThree.show()
                self.twoThree.show()
                self.oneFour.show()
                self.twoFour.show()
                self.threeOne.show()
                self.threeTwo.show()
                self.threeThree.show()
                self.threeFour.show()
                self.fourOne.show()
                self.fourTwo.show()
                self.fourThree.show()
                self.fourFour.show()

    def colBoxChanged(self):
        if self.colBox.currentText() == "1" and self.rowBox.currentText() != "Rows":
            self.oneOne.show()
            self.oneTwo.hide()
            self.twoTwo.hide()
            self.threeTwo.hide()
            self.fourTwo.hide()
            self.oneThree.hide()
            self.twoThree.hide()
            self.threeThree.hide()
            self.fourThree.hide()
            self.oneFour.hide()
            self.twoFour.hide()
            self.threeFour.hide()
            self.fourFour.hide()
            if self.rowBox.currentText() == "2" or self.rowBox.currentText() == "3" or self.rowBox.currentText() == "4":
                self.twoOne.show()
            if self.rowBox.currentText() == "3" or self.rowBox.currentText() == "4":
                self.threeOne.show()
            if self.rowBox.currentText() == "4":
                self.fourOne.show()
        if self.colBox.currentText() == "2" and self.rowBox.currentText() != "Rows":
            self.oneOne.show()
            self.oneTwo.show()
            if self.rowBox.currentText() == "2" or self.rowBox.currentText() == "3" or self.rowBox.currentText() == "4":
                self.twoTwo.show()
                self.twoOne.show()
            if self.rowBox.currentText() == "3" or self.rowBox.currentText() == "4":
                self.threeOne.show()
                self.threeTwo.show()
            if self.rowBox.currentText() == "4":
                self.fourTwo.show()
                self.fourOne.show()
            self.oneThree.hide()
            self.twoThree.hide()
            self.threeThree.hide()
            self.fourThree.hide()
            self.oneFour.hide()
            self.twoFour.hide()
            self.threeFour.hide()
            self.fourFour.hide()
        if self.colBox.currentText() == "3" and self.rowBox.currentText() != "Rows":
            self.oneOne.show()
            self.oneTwo.show()
            self.oneThree.show()
            if self.rowBox.currentText() == "2" or self.rowBox.currentText() == "3" or self.rowBox.currentText() == "4":
                self.twoTwo.show()
                self.twoOne.show()
                self.twoThree.show()
            if self.rowBox.currentText() == "3" or self.rowBox.currentText() == "4":
                self.threeOne.show()
                self.threeTwo.show()
                self.threeThree.show()
            if self.rowBox.currentText() == "4":
                self.fourTwo.show()
                self.fourOne.show()
                self.fourThree.show()
            self.oneFour.hide()
            self.twoFour.hide()
            self.threeFour.hide()
            self.fourFour.hide()
        if self.colBox.currentText() == "4" and self.rowBox.currentText() != "Rows":
            self.oneOne.show()
            self.oneTwo.show()
            self.oneThree.show()
            self.oneFour.show()
            if self.rowBox.currentText() == "2" or self.rowBox.currentText() == "3" or self.rowBox.currentText() == "4":
                self.twoTwo.show()
                self.twoOne.show()
                self.twoThree.show()
                self.twoFour.show()
            if self.rowBox.currentText() == "3" or self.rowBox.currentText() == "4":
                self.threeOne.show()
                self.threeTwo.show()
                self.threeThree.show()
                self.threeFour.show()
            if self.rowBox.currentText() == "4":
                self.fourTwo.show()
                self.fourOne.show()
                self.fourThree.show()
                self.fourFour.show()
        print(self.oneOne.text())

    def calculatePressed(self):
        regexSpace = re.compile(r'\s+')
        regexCharacter = re.compile(r'[^\d\-.\/]')
        regexPeriod = re.compile(r'\.(?!\d)|(?<=\D)\.')
        regexFrac = re.compile(r'\/(?!\d)|(?<=\D)\/')
        if self.colBox.currentText() == "Columns" or self.rowBox.currentText() == "Rows":
            winsound.Beep(950, 325)
            return

        if self.colBox.currentText() == "1":
            cols = 0
        elif self.colBox.currentText() == "2":
            cols = 1
        elif self.colBox.currentText() == "3":
            cols = 2
        elif self.colBox.currentText() == "4":
            cols = 3

        if self.rowBox.currentText() == "1":
            rows = 0
        elif self.rowBox.currentText() == "2":
            rows = 1
        elif self.rowBox.currentText() == "3":
            rows = 2
        elif self.rowBox.currentText() == "4":
            rows = 3
        arr = [self.oneOne.text(), self.oneTwo.text(), self.oneThree.text(), self.oneFour.text()], \
              [self.twoOne.text(), self.twoTwo.text(), self.twoThree.text(), self.twoFour.text()], \
              [self.threeOne.text(), self.threeTwo.text(), self.threeThree.text(), self.threeFour.text()], \
              [self.fourOne.text(), self.fourTwo.text(), self.fourThree.text(), self.fourFour.text()]
        arrRef = [self.oneOne, self.oneTwo, self.oneThree, self.oneFour], \
                 [self.twoOne, self.twoTwo, self.twoThree, self.twoFour], \
                 [self.threeOne, self.threeTwo, self.threeThree, self.threeFour], \
                 [self.fourOne, self.fourTwo, self.fourThree, self.fourFour]
        for i in range(0, rows + 1):
            for j in range(0, cols + 1):
                arr[i][j] = re.sub(regexSpace, "", arr[i][j])
                arr[i][j] = re.sub(regexPeriod, "", arr[i][j])
                arr[i][j] = re.sub(regexFrac, "", arr[i][j])
                arr[i][j] = re.sub(regexCharacter, "", arr[i][j])
                if arr[i][j] == '':
                    winsound.Beep(950, 325)
                    return

        matrix = [[0 for i in range(cols + 1)] for j in range(rows + 1)]

        for row in range(0, rows + 1):
            for item in range(0, cols + 1):
                matrix[row][item] = arr[row][item]
        matrix_rref, trash = Matrix(matrix).rref(simplify=true)
        print(matrix)

        print(matrix_rref)
        # print(matrix_rref[5])

        self.oneOne.setText(str(matrix_rref[0]))
        if rows == 0 and cols == 1:
            self.oneTwo.setText(str(matrix_rref[1]))
        if rows == 0 and cols == 2:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.oneThree.setText(str(matrix_rref[2]))
        if rows == 0 and cols == 3:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.oneThree.setText(str(matrix_rref[2]))
            self.oneFour.setText(str(matrix_rref[3]))

        if rows == 1 and cols == 0:
            self.twoOne.setText(str(matrix_rref[1]))
        if rows == 1 and cols == 1:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.twoOne.setText(str(matrix_rref[2]))
            self.twoTwo.setText(str(matrix_rref[3]))
        if rows == 1 and cols == 2:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.oneThree.setText(str(matrix_rref[2]))
            self.twoOne.setText(str(matrix_rref[3]))
            self.twoTwo.setText(str(matrix_rref[4]))
            self.twoThree.setText(str(matrix_rref[5]))
        if rows == 1 and cols == 3:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.oneThree.setText(str(matrix_rref[2]))
            self.oneFour.setText(str(matrix_rref[3]))
            self.twoOne.setText(str(matrix_rref[4]))
            self.twoTwo.setText(str(matrix_rref[5]))
            self.twoThree.setText(str(matrix_rref[6]))
            self.twoFour.setText(str(matrix_rref[7]))

        if rows == 2 and cols == 0:
            self.twoOne.setText(str(matrix_rref[1]))
            self.threeOne.setText(str(matrix_rref[2]))
        if rows == 2 and cols == 1:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.twoOne.setText(str(matrix_rref[2]))
            self.twoTwo.setText(str(matrix_rref[3]))
            self.threeOne.setText(str(matrix_rref[4]))
            self.threeTwo.setText(str(matrix_rref[5]))
        if rows == 2 and cols == 2:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.oneThree.setText(str(matrix_rref[2]))
            self.twoOne.setText(str(matrix_rref[3]))
            self.twoTwo.setText(str(matrix_rref[4]))
            self.twoThree.setText(str(matrix_rref[5]))
            self.threeOne.setText(str(matrix_rref[6]))
            self.threeTwo.setText(str(matrix_rref[7]))
            self.threeThree.setText(str(matrix_rref[8]))
        if rows == 2 and cols == 3:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.oneThree.setText(str(matrix_rref[2]))
            self.oneFour.setText(str(matrix_rref[3]))
            self.twoOne.setText(str(matrix_rref[4]))
            self.twoTwo.setText(str(matrix_rref[5]))
            self.twoThree.setText(str(matrix_rref[6]))
            self.twoFour.setText(str(matrix_rref[7]))
            self.threeOne.setText(str(matrix_rref[8]))
            self.threeTwo.setText(str(matrix_rref[9]))
            self.threeThree.setText(str(matrix_rref[10]))
            self.threeFour.setText(str(matrix_rref[11]))

        if rows == 3 and cols == 0:
            self.twoOne.setText(str(matrix_rref[1]))
            self.threeOne.setText(str(matrix_rref[2]))
            self.fourOne.setText(str(matrix_rref[3]))
        if rows == 3 and cols == 1:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.twoOne.setText(str(matrix_rref[2]))
            self.twoTwo.setText(str(matrix_rref[3]))
            self.threeOne.setText(str(matrix_rref[4]))
            self.threeTwo.setText(str(matrix_rref[5]))
            self.fourOne.setText(str(matrix_rref[6]))
            self.fourTwo.setText(str(matrix_rref[7]))
        if rows == 3 and cols == 2:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.oneThree.setText(str(matrix_rref[2]))
            self.twoOne.setText(str(matrix_rref[3]))
            self.twoTwo.setText(str(matrix_rref[4]))
            self.twoThree.setText(str(matrix_rref[5]))
            self.threeOne.setText(str(matrix_rref[6]))
            self.threeTwo.setText(str(matrix_rref[7]))
            self.threeThree.setText(str(matrix_rref[8]))
            self.fourOne.setText(str(matrix_rref[9]))
            self.fourTwo.setText(str(matrix_rref[10]))
            self.fourThree.setText(str(matrix_rref[11]))
        if rows == 3 and cols == 3:
            self.oneTwo.setText(str(matrix_rref[1]))
            self.oneThree.setText(str(matrix_rref[2]))
            self.oneFour.setText(str(matrix_rref[3]))
            self.twoOne.setText(str(matrix_rref[4]))
            self.twoTwo.setText(str(matrix_rref[5]))
            self.twoThree.setText(str(matrix_rref[6]))
            self.twoFour.setText(str(matrix_rref[7]))
            self.threeOne.setText(str(matrix_rref[8]))
            self.threeTwo.setText(str(matrix_rref[9]))
            self.threeThree.setText(str(matrix_rref[10]))
            self.threeFour.setText(str(matrix_rref[11]))
            self.fourOne.setText(str(matrix_rref[12]))
            self.fourTwo.setText(str(matrix_rref[13]))
            self.fourThree.setText(str(matrix_rref[14]))
            self.fourFour.setText(str(matrix_rref[15]))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
