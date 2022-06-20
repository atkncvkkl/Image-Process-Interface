# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:28:22 2022

@author: atknc
"""

from PyQt5.QtWidgets import QApplication
import sys
from lab_final_son import UI

"""To run the application"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()

