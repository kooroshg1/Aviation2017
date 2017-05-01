import numpy as np
import matplotlib.pyplot as plt
import math

def nCk(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def bezier(P, n=20):
    t = np.linspace(0, 1, n)
    Bx = 0
    By = 0
    n = len(P) - 1
    for iP in range(0, len(P)):
        Bx = Bx + nCk(n, iP) * (1 - t)**(n - iP) * t**iP * P[iP, 0]
        By = By + nCk(n, iP) * (1 - t)**(n - iP) * t**iP * P[iP, 1]
    return Bx, By

