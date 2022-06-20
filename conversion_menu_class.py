# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:54:20 2022

@author: atknc
"""

import matplotlib.pyplot as plt
from skimage.color import rgb2hsv,rgb2gray


class Conversion_Menu:
    
    """In thiss class conversion operations were made. skimage library were used for image processing operations."""
    
    def rgb_to_gray(self):
        
        self.image = rgb2gray(self.img)
        plt.imsave('output.jpg', self.image, cmap = 'gray')
        self.show_output()
        
        
    def rgb_to_hsv(self):

        self.image = rgb2hsv(self.img)
        plt.imsave('output.jpg', self.image)
        self.show_output()