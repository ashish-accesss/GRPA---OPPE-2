'''For an introduction to plotting with Matplotlib, refer to this Google Colab notebook. You don't have to submit
any code in the portal for this problem. You can create a local copy of this file and start practicing these
problems.

Plot the following functions using Matplotlib, each on a separate graph.

f(x) = 3x - 4
f(x) = x^2 + 2x - 15
f(x)=5(x-1)(x-2)(x-3)
f(x) = e^x
f(x) = \log x
f(x) = \sin x'''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10,100)
y=3*x-4
plt.figure()
plt.plot(x,y)
plt.title("f(x=3x-4")
plt.grid()
plt.show()

x=np.linspace(-10,10,100)
y=x ** 2+2*x-15
plt.figure()
plt.plot(x,y)
plt.title("f(x=3x-4")
plt.grid()
plt.show()