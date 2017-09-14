# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def solveX(x, dx, dt, a, numX):
    xnew = x

    for i in range(1, numX-1):
        xnew[i] = x[i] + (a * dt)/(dx ** 2) * (x[i+1] - 2 * x[i] + x[i-1])
    return xnew


# define parameters
c = 4181.   # Specific heat
U0_1 = 30
U0_2 = 50
U0_3 = 20
d = 1       # Density
A = 10   # Thermal Conductivity
U_env = 22

L = 1  # Length

numX = 15
dx = np.float64(L/(numX - 1))
dt = .05
numT = 2000

# a = A / (d * c)
a = 3.1934E-3  # Thermal Difusivity of Water at U = 40

T = np.zeros((numT, numX), np.float64)

for i in range(numT):
    T[0, :].fill(U0_3)
    T[0, 0] = U0_1
    T[0, numX-1] = U0_2


for t in range(numT-1):
    T[t+1] = solveX(T[t], dx, dt, a, numX)


x_axis = np.linspace(0, numX - 1, numX)

tests = [1500, 750, 375, 200, 100, 5]
labels = ["", "", "", "", "", "", ""]
labels[0] = "t = " + str(numT * dt) + "s"

for i in range(len(tests)):
    labels[i + 1] = "t = " + str(tests[i] * dt) + "s"


h1, = plt.plot(x_axis * dx, T[numT-1])
h2, = plt.plot(x_axis * dx, T[tests[0]-1])
h3, = plt.plot(x_axis * dx, T[tests[1]-1])
h4, = plt.plot(x_axis * dx, T[tests[2]-1])
h5, = plt.plot(x_axis * dx, T[tests[3]-1])
h6, = plt.plot(x_axis * dx, T[tests[4]-1])
h7, = plt.plot(x_axis * dx, T[tests[5]-1])

plt.title("Plots of Multiple T values")
plt.legend(handles=[h1, h2, h3, h4, h5, h6, h7],
           labels=labels)
plt.ylabel("Temp (C)")
plt.xlabel("Location on Pipe")
plt.show()
