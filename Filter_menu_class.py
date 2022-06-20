# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:56:20 2022

@author: atknc
"""


import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import filters


class Filter_Menu:
    
    """In thiss class filtering operations were made. skimage library were used for image processing operations."""
    
    def robert_filter(self):

        self.image = filters.roberts(rgb2gray(self.img))
        plt.imsave('output.jpg', self.image,cmap='gray')
        self.show_output()



    def sobel_filter(self):
        

        gray = rgb2gray(self.img)
        self.image = filters.sobel(gray)
        plt.imsave('output.jpg', self.image,cmap='gray')
        self.show_output()   

    
    def scharr_filter(self):
        

        gray = rgb2gray(self.img)
        self.image = filters.sobel(gray)
        plt.imsave('output.jpg',self.image,cmap='gray')
        self.show_output()  
        
    def prewitt_filter(self):
        

        gray = rgb2gray(self.img)
        self.image = filters.prewitt(gray)
        plt.imsave('output.jpg', self.image,cmap='gray')
        self.show_output()  