# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:37:27 2024

@author: Brenda
"""
import numpy as np
import matplotlib.pyplot as plt

u = np.array([[1],[0]])
A = np.array([[.8, .3], [.2, .7]])
x = u
k = np.array([0, 1, 2, 3, 4, 5, 6, 7])

while x.shape[1] <= 7:
    u = A@u
    x = np.concatenate((x, u), axis = 1)

plt.plot(k, x[0, :], label='x1')  # First row (x1 values)
plt.plot(k, x[1, :], label='x2')  # Second row (x2 values)
plt.grid()
plt.show()

