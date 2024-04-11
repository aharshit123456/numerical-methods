import numpy as np
import matplotlib.pyplot as plt


def centraldiff(f,a,h=0.01):
    return (f(a+h)-f(a-h))/(2*h)

def forwarddiff(f,a,h=0.01):
    return (f(a+h)-f(a))/(h)

def backwarddiff(f,a,h=0.01):
    return (f(a)-f(a-h))/(h)


x = np.linspace(0,5*np.pi, 100)
fdydx = forwarddiff(np.sin, x)
bdydx = backwarddiff(np.sin, x)
cdydx = centraldiff(np.sin, x)

dYdx = np.cos(x)

plt.figure(figsize=(12,5))
plt.plot(x,cdydx, 'r.',label="Central Difference")
plt.plot(x,fdydx, 'y',label="Forward Difference")
plt.plot(x,bdydx, 'g',label="Backward Difference")

#plt.plot(x, dYdx, 'b', label="True Value")
plt.title('Derivative')
plt.legend(loc='best')
plt.show()