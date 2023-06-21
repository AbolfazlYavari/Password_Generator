# Importing required libraries
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMenuBar, QStatusBar, QWidget, QFrame, \
    QCheckBox, QSlider, QTextEdit, QMessageBox
from PyQt5.QtGui import QClipboard
from PyQt5 import uic
from PyQt5 import QtCore
import sys
from random import randint


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # Load the UI file
        uic.loadUi("password-generator.ui", self)

        # Find UI elements
        self.textedit = self.findChild(QTextEdit, "textEdit_2")
        self.generatepass = self.findChild(QPushButton, "pushButton")
        self.clipboard = self.findChild(QPushButton, "pushButton_3")
        self.label = self.findChild(QLabel, "label")
        self.label1 = self.findChild(QLabel, "label_2")
        self.label2 = self.findChild(QLabel, "label_3")
        self.label3 = self.findChild(QLabel, "label_4")
        self.frame = self.findChild(QFrame, "frame")
        self.Uppercase = self.findChild(QCheckBox, "checkBox")
        self.Lowercase = self.findChild(QCheckBox, "checkBox_2")
        self.Numbers = self.findChild(QCheckBox, "checkBox_3")
        self.Symbols = self.findChild(QCheckBox, "checkBox_4")
        self.slider = self.findChild(QSlider, "horizontalSlider")

        # Set default checkbox values
        self.Uppercase.setChecked(True)
        self.Lowercase.setChecked(True)
        self.Numbers.setChecked(True)
        self.Symbols.setChecked(True)

        # Connect button clicks to functions
        self.generatepass.clicked.connect(self.passgenerate)
        self.clipboard.clicked.connect(self.copy)
        self.slider.valueChanged.connect(self.slide_it)
        self.slider.setMinimum(1)

        # Show the UI
        self.show()

    def slide_it(self, value):
         """
        Updates the label text when the slider value changes.

        Args:
            value (int): The new value of the slider.
        """

        global plength
        plength = value
        self.label2.setText(str(value))

    def passgenerate(self):
        """
        Generates a password based on the selected checkboxes and displays it in the textedit.

        Raises:
            QMessageBox.warning: If no checkbox is selected.
        """
        global plength
        

        symbols = "!@#$%^&*()_+-=[]{}|\\;:'\"<>,./?~`"
        number_s = "0123456789"
        number_splussymbols = "0123456789!@#$%^&*()_+-=[]{}|\\;:'\"<>,./?~`"

        if self.Uppercase.isChecked() == False and self.Lowercase.isChecked() == False and self.Symbols.isChecked() == False and self.Numbers.isChecked() == False:
            QMessageBox.warning(self, "Invalid Selection", "Please select at least one option")
            return

        if self.Uppercase.isChecked() and self.Lowercase.isChecked() and self.Numbers.isChecked() and self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                my_password += chr(randint(33, 126))

            self.textedit.setText(my_password)

        if self.Uppercase.isChecked() and not self.Lowercase.isChecked() and self.Numbers.isChecked() and not self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while char in symbols:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password.upper())

        if self.Uppercase.isChecked() and not self.Lowercase.isChecked() and not self.Numbers.isChecked() and self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while char in number_s:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password.upper())
        if self.Uppercase.isChecked() and not self.Lowercase.isChecked() and not self.Numbers.isChecked() and not self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                my_password += chr(randint(65, 90))

            self.textedit.setText(my_password)

        if self.Uppercase.isChecked() and not self.Lowercase.isChecked() and self.Numbers.isChecked() and self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                my_password += chr(randint(33, 126))

            self.textedit.setText(my_password.upper())

        if self.Uppercase.isChecked() and self.Lowercase.isChecked() and not self.Numbers.isChecked() and self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while char in number_s:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password)
        
        if self.Uppercase.isChecked() and self.Lowercase.isChecked() and not self.Numbers.isChecked() and not self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while char in number_splussymbols:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password)

        if self.Uppercase.isChecked() and self.Lowercase.isChecked() and self.Numbers.isChecked() and not self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while char in symbols:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password.upper())

        if not self.Uppercase.isChecked() and self.Lowercase.isChecked() and self.Numbers.isChecked() and self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                my_password += chr(randint(33, 126))

            self.textedit.setText(my_password.lower())

        if not self.Uppercase.isChecked() and self.Lowercase.isChecked() and not self.Numbers.isChecked() and self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while char in number_s:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password.lower())
        

        if not self.Uppercase.isChecked() and self.Lowercase.isChecked() and self.Numbers.isChecked() and not self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while char in symbols:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password.lower())

        if not self.Uppercase.isChecked() and self.Lowercase.isChecked() and not self.Numbers.isChecked() and not self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while char in number_splussymbols:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password.lower())

        if not self.Uppercase.isChecked() and not self.Lowercase.isChecked() and self.Numbers.isChecked() and not self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                my_password += chr(randint(48, 57))

            self.textedit.setText(my_password)

        
        if not self.Uppercase.isChecked() and not self.Lowercase.isChecked() and not self.Numbers.isChecked() and self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while not char in symbols:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password)
        if not self.Uppercase.isChecked() and not self.Lowercase.isChecked() and self.Numbers.isChecked() and self.Symbols.isChecked():
            pw_length = int(plength)
            my_password = ""
            for x in range(pw_length):
                char = chr(randint(33, 126))
                while not char in number_splussymbols:
                    char = chr(randint(33, 126))
                my_password += char

            self.textedit.setText(my_password)

    def copy(self):
        """
        Copies the password from the textedit to the clipboard.
        """
        text = self.textedit.toPlainText()
        if text:
            app = QApplication.instance()
            clipboard = app.clipboard()
            clipboard.setText(text, mode=QClipboard.Clipboard)
            self.textedit.clear()


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
