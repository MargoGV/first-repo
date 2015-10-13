import numpy as np
import matplotlib.pyplot as plt
import math
def f(x, t):
	y = eval(t)
	return y

t = input()
x=np.arange(-10,10.01,0.01)
y = [f(_x, t) for _x in x]
plt.xkcd()
plt.plot(x, y)
plt.show()
