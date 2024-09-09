import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from calculatorDesing import Ui_MainWindow

"""

        self.MainWindow = MainWindow
"""
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.operation = ""
        self.Themes("blue")
        
        self.buttonSystem()
    def buttonSystem(self):
        self.ui.pushButton_0.clicked.connect(lambda: self.Clicked("0"))
        self.ui.pushButton_1.clicked.connect(lambda: self.Clicked("1"))
        self.ui.pushButton_2.clicked.connect(lambda: self.Clicked("2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.Clicked("3"))
        self.ui.pushButton_4.clicked.connect(lambda: self.Clicked("4"))
        self.ui.pushButton_5.clicked.connect(lambda: self.Clicked("5"))
        self.ui.pushButton_6.clicked.connect(lambda: self.Clicked("6"))
        self.ui.pushButton_7.clicked.connect(lambda: self.Clicked("7"))
        self.ui.pushButton_8.clicked.connect(lambda: self.Clicked("8"))
        self.ui.pushButton_9.clicked.connect(lambda: self.Clicked("9"))
        self.ui.pushButton_Plus.clicked.connect(lambda: self.Clicked("+"))
        self.ui.pushButton_Minus.clicked.connect(lambda: self.Clicked("-"))
        self.ui.pushButton_Multiply.clicked.connect(lambda: self.Clicked("x"))
        self.ui.pushButton_Divided.clicked.connect(lambda: self.Clicked("÷"))
        self.ui.pushButton_Equal.clicked.connect(lambda: self.Clicked("="))
        self.ui.pushButton_Clear.clicked.connect(lambda: self.Clicked("Clear"))
        self.ui.pushButton_Delete.clicked.connect(lambda: self.Clicked("Delete"))
        self.ui.actionBlue.triggered.connect(lambda: self.Themes("blue"))
        self.ui.actionOrange.triggered.connect(lambda: self.Themes("orange"))
    
    def Clicked(self, name:str):
        #sender = self.sender()
        
        if name == "0":
            if self.ui.lineEdit.text() == "HATA": self.ui.lineEdit.setText("0")
            elif not self.ui.lineEdit.text() == "0": self.ui.lineEdit.setText(self.ui.lineEdit.text() + "0")
                
        elif name == "1" or name == "2" or name == "3" or name == "4" or name == "5" or name == "6" or name == "7" or name == "8" or name == "9":
            if self.ui.lineEdit.text() == "0" or self.ui.lineEdit.text() == "HATA": self.ui.lineEdit.setText("")
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + name)
        
        elif name == "+" or name == "-" or name == "x" or name == "÷":
            if not self.ui.lineEdit.text() == "HATA":
                if self.operation == "":
                    self.operation = name
                    self.ui.lineEdit.setText(self.ui.lineEdit.text() + name)
                elif not self.ui.lineEdit.text()[-1].isnumeric():
                    self.ui.lineEdit.setText(self.ui.lineEdit.text()[:-1] + name)                
                    self.operation = name
                else :
                    result = self.calculate()
                    self.operation = name
                    if result == "HATA":self.ui.lineEdit.setText(str(result))
                    else:self.ui.lineEdit.setText(str(result)+name)
            else :self.ui.lineEdit.setText("0" + name)
        elif name == "=":
            if not self.ui.lineEdit.text() == "HATA":
                if self.ui.lineEdit.text()[-1].isnumeric() and not self.operation == "":
                    result = self.calculate()
                    self.ui.lineEdit.setText(str(result))
                    self.operation = ""
                elif self.ui.lineEdit.text()[-1].isnumeric():self.ui.lineEdit.setText(self.ui.lineEdit.text())
                else : self.ui.lineEdit.setText(self.ui.lineEdit.text()[:-1])
                self.operation = ""
            else :self.ui.lineEdit.setText("0")
        
        elif name == "Delete":
            if self.ui.lineEdit.text() == "HATA":self.ui.lineEdit.setText("0")
                
            if not self.ui.lineEdit.text()[-1].isnumeric():
                self.operation = ""
            
            self.ui.lineEdit.setText(self.ui.lineEdit.text()[:-1])
            if len(self.ui.lineEdit.text()) == 0: 
                self.ui.lineEdit.setText("0")
        
        elif name == "Clear":
            self.operation = ""            
            self.ui.lineEdit.setText("0")
        
        if len(self.ui.lineEdit.text()) > 10: self.ui.lineEdit.setFont(QFont("arial",20,QFont.Bold))
        else: self.ui.lineEdit.setFont(QFont("arial",25,QFont.Bold))
            
    def calculate(self):
        calculation = self.ui.lineEdit.text().split(self.operation)
        if self.operation == "+": result = eval(calculation[0] + "+" + calculation[1])
        elif self.operation == "-": result = eval(calculation[0] + "-" + calculation[1])
        elif self.operation == "x": result = eval(calculation[0] + "*" + calculation[1])
        elif self.operation == "÷":
            try:
                result = eval(calculation[0] + "/" + calculation[1])
                result = round(result,13)
                if float(result).is_integer():
                    result = int(result)
            except ZeroDivisionError:
                result = "HATA"
        return str(result)
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.ui.pushButton_Equal.click()
        elif e.key() == Qt.Key_Z:
            self.ui.pushButton_Divided.click()
        elif e.key() == Qt.Key_X:
            self.ui.pushButton_Multiply.click()
            
    def Themes(self, color):
        blue ="""
        QPushButton{
	background-color: rgb(255, 255, 255);
	border: none;
	border-radius: 10px;
	color: #3daeda;
}
QPushButton:hover {
	background: #1341a6;
	color: #81d0e6;
}
QPushButton:pressed {
	background-color: #0c2673;
}
QPushButton#pushButton_Delete{
	background-color:#1341a6;
	color: #3daeda;
}
QPushButton#pushButton_Delete:hover {
	background-color: #3daeda;
	color: white;
}
QPushButton#pushButton_Delete:pressed {
	background: white;
	color: #3daeda;
}
QLineEdit{
	padding: 1px 18px 1px 3px;
	border: 0;
	border-radius: 10px;
    background: #3daeda;
	color:white;
}
QLineEdit:hover{
	background-color: white;
	color: #3daeda;
}

QMenuBar {
    background-color: #3daeda;
    color: white;
}
QMenuBar::item {
    background-color: #3daeda;
    color: white;
	border-top: 2px solid #3daeda;
	border-bottom: 2px solid #3daeda;
	border-left: 5px solid #3daeda;
	border-right: 1px solid white;
	padding-right:5px;
}
QMenuBar::item::selected {
	border-color:white;
	border-right-color: #3daeda;
	background-color:white;
	color: #3daeda;
}
QMenu {
    background-color:rgb(255, 255, 255);
	color: #3daeda;        
}
QMenu::item::selected {
	background: #3daeda;
    color: white;
}
        """
        orange ="""
        QPushButton{
	background-color: rgb(255, 255, 255);
	border: none;
	border-radius: 10px;
	color: #eb8817;
}
QPushButton:hover {
	background: #38ad6b;
	color: #81d0e6;
}
QPushButton:pressed {
	background-color: #0c2673;
}
QPushButton#pushButton_Delete{
	background-color:#38ad6b;
	color: #81d0e6;
}
QPushButton#pushButton_Delete:hover {
	background-color: #eb8817;
	color: white;
}
QPushButton#pushButton_Delete:pressed {
	background: white;
	color: #eb8817;
}
QLineEdit{
	padding: 1px 18px 1px 3px;
	border: 0;
	border-radius: 10px;
    background: #eb8817;
	color:white;
}
QLineEdit:hover{
	background-color: white;
	color: #eb8817;
}

QMenuBar {
    background-color: #eb8817;
    color: white;
}
QMenuBar::item {
    background-color: #eb8817;
    color: white;
	border-top: 2px solid #eb8817;
	border-bottom: 2px solid #eb8817;
	border-left: 5px solid #eb8817;
	border-right: 1px solid white;
	padding-right:5px;
}
QMenuBar::item::selected {
	border-color:white;
	border-right-color: #eb8817;
	background-color:white;
	color: #eb8817;
}
QMenu {
    background-color:rgb(255, 255, 255);
	color: #eb8817;        
}
QMenu::item::selected {
	background: #eb8817;
    color: white;
}
        """
        if color == "blue":
            self.ui.MainWindow.setWindowOpacity(0.95)
            self.ui.MainWindow.setStyleSheet(blue)
            self.ui.actionBlue.setChecked(True)
            self.ui.actionOrange.setChecked(False)
        elif color == "orange":
            self.ui.MainWindow.setStyleSheet(orange)
            self.ui.actionBlue.setChecked(False)
            self.ui.actionOrange.setChecked(True)

app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())