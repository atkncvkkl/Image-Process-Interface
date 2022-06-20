# -*- coding: utf-8 -*-
"""
Created on Sun May 22 21:49:31 2022

@author: atknc
"""


from PyQt5.QtWidgets import QMenu,QGroupBox, QPushButton , QMainWindow, QLabel,QAction
from PyQt5 import uic
from file_menu_class2 import File_Menu
from conversion_menu_class import Conversion_Menu
from segmentation_menu_class import Segmentation_Menu
from Filter_menu_class import Filter_Menu


        

class UI(QMainWindow,File_Menu,Conversion_Menu,Segmentation_Menu,Filter_Menu):
    
    def __init__(self):
        super(UI, self).__init__()
            
        
        uic.loadUi("lab_final_son.ui",self)
        
        self.label = self.findChild(QLabel, "label_I")
        self.label_2 = self.findChild(QLabel, "label_O")
        
        self.open_push = self.findChild(QPushButton,"B_Open")
        self.close_push = self.findChild(QPushButton, "B_Close")
        self.close_push_2 = self.findChild(QPushButton, "B_Close_I")
        self.save_as_push = self.findChild(QPushButton, "B_save_as_output")
        self.export_as_source_push = self.findChild(QPushButton, "B_Export_input")
        self.export_as_output_push = self.findChild(QPushButton, "B_export_output")
        self.undo_push = self.findChild(QPushButton, "B_undo_output")
        self.redo_push = self.findChild(QPushButton, "B_redo_output")
        self.rgb_to_gray_push = self.findChild(QPushButton, "B_RGB_to_Grayscale")
        self.rgb_to_hsv_push = self.findChild(QPushButton, "B_RGB_to_HSV")
        self.prewitt_push = self.findChild(QPushButton, "B_Prewitt")
        self.roberts_push = self.findChild(QPushButton, "B_Roberts")
        self.scharr_push = self.findChild(QPushButton, "B_Scharr")
        self.sobel_push = self.findChild(QPushButton, "B_Sobel")
        self.multi_otsu_push = self.findChild(QPushButton, "B_Multi_Otsu_Thresholding")
        self.chan_vese_push = self.findChild(QPushButton, "B_Chan_Vese_Segmentation")
        self.morphological_snakes_push = self.findChild(QPushButton, "B_Morphological_Snakes")
        
        self.A_actionSave_As_Output = self.findChild(QAction, "actionSave_As_Output")
        self.A_actionSave_Output = self.findChild(QAction, "actionSave_Output")
        self.A_actionExportSource = self.findChild(QAction, "actionExportSource")
        self.A_actionExportOutput = self.findChild(QAction, "actionExportOutput")
        
        
        self.G_segmentation = self.findChild(QGroupBox, "G_Segmentation")
        self.G_edgeDetection = self.findChild(QGroupBox, "G_Edge_Detection")
        self.G_conversion = self.findChild(QGroupBox, "G_Conversion")
        self.G_output = self.findChild(QGroupBox, "G_Output")
        
        self.M_edit = self.findChild(QMenu, "menuEdit")
        self.M_conversion = self.findChild(QMenu, "menuConversion")
        self.M_segmentation = self.findChild(QMenu, "menuSegmentation")
        self.M_edgeDetection = self.findChild(QMenu, "menuEdge_Detection")
        
        
        #File Menu

        self.open_push.clicked.connect(self.clicker)
        self.save_as_push.clicked.connect(self.filesave)
        self.export_as_source_push.clicked.connect(self.export_as_source)
        self.export_as_output_push.clicked.connect(self.export_as_output)
        self.undo_push.clicked.connect(self.undoFile)
        self.redo_push.clicked.connect(self.redoFile)

        #Conversion Operations
        self.rgb_to_gray_push.clicked.connect(self.rgb_to_gray)
        self.rgb_to_hsv_push.clicked.connect(self.rgb_to_hsv)
        #Segmentation Operations
        self.multi_otsu_push.clicked.connect(self.multi_otsu)
        self.chan_vese_push.clicked.connect(self.chan_vese_seg)
        self.morphological_snakes_push.clicked.connect(self.morphological_snakes)
        #Edge Detection Operations
        self.roberts_push.clicked.connect(self.robert_filter)
        self.sobel_push.clicked.connect(self.sobel_filter)
        self.scharr_push.clicked.connect(self.scharr_filter)
        self.prewitt_push.clicked.connect(self.prewitt_filter)

        
        self.show()


        
        
