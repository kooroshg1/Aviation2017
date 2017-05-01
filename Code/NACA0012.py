import numpy as np
import matplotlib.pyplot as plt
import curvefit
import scipy.optimize as opt

def airfoil(x):
    y = 0.6 * (0.2969 * np.sqrt(x) - \
               0.1260 * x - \
               0.3516 * x**2 + \
               0.2843 * x**3 - \
               0.1015 * x**4)
    # x = np.concatenate([x, x])
    # y = np.concatenate([y, -y])
    return x, y

x = np.linspace(0, 1, 100)
x, y = airfoil(x)

P = np.array([[0, 0], [0.005, 0.08], [0.4, 0.08], [1, 0]])
Bx, By = curvefit.bezier(P, len(x))

plt.figure()
plt.plot(x, y, 'k',
         Bx, By,'r',
         P[:, 0], P[:, 1], 'ro')
plt.axis('equal')
plt.show()

