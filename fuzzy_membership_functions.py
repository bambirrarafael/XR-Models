import numpy as np
import matplotlib.pyplot as plt

#
# Triangular membership function - Around 5
x = np.linspace(0, 10)
A = []
#
# Inputs
a = 3
m = 5
b = 7
#
# Logic
for i in range(len(x)):
    if x[i] <= a:
        A.append(0)
    elif a <= x[i] <= m:
        A.append((x[i] - a) / (m - a))
    elif m <= x[i] <= b:
        A.append((b - x[i]) / (b - m))
    elif x[i] >= b:
        A.append(0)
#
# Plot membership function
plt.plot(x, A)
plt.title('Triangular membership function - Around 5')
plt.show()
#
# ----------------------------------------------------------------------------------------------------------------------
#
# Trapezoidal membership function - Around 5
x = np.linspace(0, 10)
A = []
B = []
#
# Inputs
a = 3
m = 4
n = 6
b = 7
#
# Logic
for i in range(len(x)):
    if x[i] < a:
        A.append(0)
    elif a <= x[i] <= m:
        A.append((x[i] - a) / (m - a))
    elif m <= x[i] <= n:
        A.append(1)
    elif n <= x[i] <= b:
        A.append((b - x[i]) / (b - n))
    elif x[i] > b:
        A.append(0)
#
# Another logic that also works
for i in range(len(x)):
    B.append(np.max([np.min([(x[i] - a) / (m - a), 1, (b - x[i]) / (b - n)]), 0]))
#
# Plot membership function
plt.plot(x, A)
plt.plot(x, B, '.')
plt.title('Trapezoidal membership function - Around 5')
plt.show()
#
# ----------------------------------------------------------------------------------------------------------------------
#
# G membership function - Around 5
x = np.linspace(0, 10)
A = []
B = []
#
# Inputs
a = 5
k = 0.5
#
# Logic
for i in range(len(x)):
    if x[i] <= a:
        A.append(0)
    elif x[i] >= a:
        A.append(1 - np.exp(-k*(x[i] - a)**2))
#
# Another logic that also works
for i in range(len(x)):
    if x[i] <= a:
        B.append(0)
    elif x[i] >= a:
        B.append((k*(x[i] - a)**2)/(1 + k*(x[i] - a)**2))
#
# Plot membership function
plt.plot(x, A)
plt.plot(x, B, '.')
plt.title('G membership function - Around 5')
plt.show()
#
# ----------------------------------------------------------------------------------------------------------------------
#
# S membership function - Around 5
x = np.linspace(0, 10)
A = []
#
# Inputs
a = 3
b = 7
m = (a + b)/2
#
# Logic
for i in range(len(x)):
    if x[i] <= a:
        A.append(0)
    elif a <= x[i] <= m:
        A.append(2*((x[i] - a)/(b - a))**2)
    elif m <= x[i] <= b:
        A.append(1 - 2*((x[i] - b)/(b - a))**2)
    elif x[i] >= b:
        A.append(0)
#
# Plot membership function
plt.plot(x, A)
plt.title('S membership function - Around 5')
plt.show()
#
# ----------------------------------------------------------------------------------------------------------------------
#
# Gaussian membership function - Around 5
x = np.linspace(0, 10)
A = []
#
# Inputs
m = 5
s = 2
#
# Logic
for i in range(len(x)):
    A.append(np.exp(-(x[i] - m)**2 / (s)**2))
#
# Plot membership function
plt.plot(x, A)
plt.title('Gaussian membership function - Around 5')
plt.show()
#
# ----------------------------------------------------------------------------------------------------------------------
#
# Exponential like membership function - Around 5
x = np.linspace(0, 10)
A = []
#
# Inputs
m = 5
k = 0.5
#
# Logic
for i in range(len(x)):
    A.append(1/(1 + k*(x[i] - m)**2))
#
# Plot membership function
plt.plot(x, A)
plt.title('Exponential like membership function - Around 5')
plt.show()

