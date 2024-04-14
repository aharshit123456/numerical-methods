import numpy as np
import matplotlib.pyplot as plt

a = 1
U = 0
m = 511000
hbc = 197
k = 2*m/hbc**2

E = 13
dE = 0.001
psi = 0
psidot = 1
psiddot = -k*psi*E

x = 0
dx = 0.001

psip = []
xp = []
psifinal = 1

while np.abs(psifinal)>0.01:
    psi = 0
    psidot = 1
    psip = []
    xp = []
    x = 0

    while x < a:
        psiddot = -k*psi*(E-U)
        psidot = psidot + psiddot*dx
        psi = psi + psidot*dx
        x = x + dx
        psip = psip + [psi]
        xp = xp + [x]
    psifinal = psi
    E = E + dE


print("E = ", E,"eV")
plt.plot(xp, psip)
plt.xlabel("x")
plt.ylabel("psi")
plt.grid()
plt.show()