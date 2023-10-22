import numpy as np
import matplotlib.pyplot as plt

a = 3
print('a =', a, type(a))
b = 1/2
print('b =', b, type(b))

n = 3
x = 0.1
print('x =', x, type(x))

w = b**n * np.cos(a**n * np.pi * x)
print(w)

sw = 'b**n * np.cos(a**n * np.pi * x)'
print("sw = ", sw, type(sw))

w = sum(b**n * np.cos(a**n * np.pi * x) for n in range(0, 10))
print(w)
w = sum(eval(sw) for i in range(0, 50))
print(w)
w = sum(eval(sw) for i in range(0, 100))
print(w)

dx = 0.01
x = np.arange(-2, 2 + dx, dx)
print('x = ', x, type(x))
plt.plot(x, sum(eval(sw) for i in range(0, 100)))
plt.show()