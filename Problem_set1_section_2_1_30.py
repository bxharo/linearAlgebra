# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:34:16 2024

@author: Brenda
"""

import numpy as np
import matplotlib.pyplot as plt

v = np.array([[0],[1]])
A = np.array([[.8, .3],[.2, .7]])
x = v
k = np.array([0, 1, 2, 3, 4, 5, 6, 7])


for j in np.arange(0,7):
    v = A@v
    x = np.concatenate((x, v), axis = 1)

plt.plot(k, x[0,:], label = 'x1')
plt.plot(k, x[1,:], label = 'x2')
plt.grid()
plt.show()
