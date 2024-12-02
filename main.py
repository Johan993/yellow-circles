import sys
import random

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import uic


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 430, 121, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Желтые кружочки"))
        self.pushButton.setText(_translate("Form", "Нажми на меня"))


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.do_paint = False
        self.ui.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(int(random.uniform(0, 255)), int(random.uniform(0, 255)),
                               int(random.uniform(0, 255))))
            r = random.randint(1, self.height() // 2)
            x, y = random.randint(r, self.width() - r), random.randint(r, self.height() - r)
            qp.drawEllipse(QPoint(x, y), r, r)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
