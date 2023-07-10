from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QComboBox , QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys
import os
import requests
import time




class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

		# Load the ui file
        uic.loadUi("gui_layout.ui", self)
        self.logic = 0
# 		# Define Our Widgets 
        self.url = self.findChild(QLineEdit, 'url')
        self.start_number = self.findChild(QLineEdit, 'start_number')
        self.output_folder = self.findChild(QLineEdit, 'output_folder')
        self.browse_button = self.findChild(QPushButton, 'browse_button')
        self.start_button = self.findChild(QPushButton, 'start_button')
        self.stop_button = self.findChild(QPushButton, 'stop_button')
        
        self.browse_button.clicked.connect(self.browse_folder)
        self.start_button.clicked.connect(self.start_)
        
        #if stop button is clicked stop the loop of start function using threading
        
        self.stop_button.clicked.connect(self.stop_)
        

		# Show The App
        # self.show()       

    def browse_folder(self):
        self.output_folder.setText(QFileDialog.getExistingDirectory(self, "Select Directory"))

    #use pyqtSlot decorator to make the function a slot and connect it to the signal
    # start has while loop 

    @pyqtSlot()
    def start_(self):
        self.logic = 1
        while self.logic == 1:
            url = self.url.text()
            start_number = int(self.start_number.text())
            output_folder = self.output_folder.text()
            print(url)
            print(start_number)
            print(output_folder)
            start_number = start_number + 1
            self.start_number.setText(str(start_number))
            time.sleep(1)
            # print(url)
            # print(start_number)
            # print(output_folder)
            # print("start")

    @pyqtSlot()
    def stop_(self):
        self.logic = 0
        print("stop")


    


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
# # Initialize The App
# app = QApplication(sys.argv)
# UIWindow = UI()
# app.exec_()
