# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:34:31 2024

@author: Brenda
"""

import numpy as np
import matplotlib.pyplot as plt

u = np.array([[1],[0]])
v = np.array([[0],[1]])

A = np.array([[0.8, 0.3], [.2, .7]])

#define the arrays to save the results
x = u.copy()
y = v.copy()

for i in range(6):
    u = A@u
    v = A@v
    
    x = np.hstack((x, u))
    y = np.hstack((y, v))

print(x)
print(y)
plt.plot(range(x.shape[1]), x[0, :], label='Row 1 (First Variable x)')
plt.plot(range(x.shape[1]), x[1, :], label='Row 2 (Second Variable x)')
plt.plot(range(y.shape[1]), y[0, :], label='Row 1 (First Variable y)')
plt.plot(range(y.shape[1]), y[1, :], label= 'Row 2 (Second Variable y)')
plt.legend()
plt.grid()
plt.show()
