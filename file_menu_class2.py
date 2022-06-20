# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:52:24 2022

@author: atknc
"""


from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton , QMainWindow, QLabel, QMenuBar,QMessageBox
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt





undo_stack=[]#undo stack
redo_stack=[]#redo stack used circular stack

class File_Menu:
    
    
    """In this class all the file operations were made. Open, save, export... This class also include setEnabled functions to activate
    buttons when file is opened."""
    
    def clicker(self):
        
        fname = QFileDialog.getOpenFileName(self,"Open File", "c:\Desktop" , "Images (*.jpg , *.png)")
        self.img = plt.imread(fname[0])
        self.pixmap = QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)
        
        
            
        self.M_edit.setEnabled(True)
        self.M_conversion.setEnabled(True)
        self.M_segmentation.setEnabled(True)
        self.M_edgeDetection.setEnabled(True)
        self.G_segmentation.setEnabled(True)
        self.G_edgeDetection.setEnabled(True)
        self.G_conversion.setEnabled(True)
        self.G_output.setEnabled(True)
        self.export_as_source_push.setEnabled(True)
        self.close_push_2.setEnabled(True)
        self.A_actionSave_As_Output.setEnabled(True)
        self.A_actionSave_Output.setEnabled(True)
        self.A_actionExportSource.setEnabled(True)
        self.A_actionExportOutput.setEnabled(True)
        
        
    def filesave(self):
        
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image","H:\Image","Images (*.jpg)")
        plt.imsave(fileName+'.jpg', self.image, cmap='gray')
        
        
    def export_as_source(self):

        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image","H:\Image","PDF (*.pdf)")
        plt.imshow(self.img)
        plt.savefig(fileName+'.pdf')

        
    def export_as_output(self):
        
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image","H:\Image","PDF (*.pdf)")
        plt.imshow(self.image, cmap = 'gray')
        plt.savefig(fileName+'.pdf')
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def undoFile(self):
        redo_stack.append(undo_stack.pop())
        pixmap_done=undo_stack[-1]
        self.label_2.setPixmap(pixmap_done)
    def redoFile(self):
        pixmap_done=redo_stack[-1]
        self.label_2.setPixmap(pixmap_done)
        redo_stack.pop()
        
    def show_output(self):
        
        pixmap2 = QPixmap('output.jpg')
        self.label_2.setPixmap(pixmap2)  
        undo_stack.append(pixmap2)