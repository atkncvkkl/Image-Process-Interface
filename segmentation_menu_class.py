# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:55:15 2022

@author: atknc
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_multiotsu
from skimage.segmentation import chan_vese,morphological_chan_vese,checkerboard_level_set


class Segmentation_Menu:
    
    """In thiss class segmentations operations were made. skimage library were used for image processing operations. numpy library also
    used to make operations on image."""
    
    def multi_otsu(self):
    

        gray = rgb2gray(self.img)
        thresholds = threshold_multiotsu(gray)
        self.image = np.digitize(gray, bins=thresholds)
        plt.imsave('output.jpg', self.image)
        self.show_output() 
        
    def chan_vese_seg(self):
    

        gray = rgb2gray(self.img)
        
        self.cv = chan_vese(gray, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
                       max_num_iter=50, dt=0.5, init_level_set="checkerboard",
                       extended_output=False)
    
        plt.imsave('output.jpg', self.cv,cmap='gray')
        self.show_output()

    def morphological_snakes(self):
    
        init_ls = checkerboard_level_set(rgb2gray(self.img).shape, 6)
        ls = morphological_chan_vese(rgb2gray(self.img), num_iter=35, init_level_set=init_ls,
                                     smoothing=3)
        
        self.image = ls
        
        plt.imsave('output.jpg', self.image)
        self.show_output()