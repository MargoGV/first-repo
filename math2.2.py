import numpy as np
import math
import matplotlib.pyplot as plt
x=np.arange(-10,10.01,0.01)
def f(x):
	z=math.log((x**2 + 1)*math.exp( - math.fabs(x)/10), 1+math.tan(1/(1+math.sin(x)**2)))
	return z
y = [f(_x) for _x in x]
plt.plot(x, y)
plt.show()
