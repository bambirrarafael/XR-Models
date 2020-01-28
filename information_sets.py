import numpy as np
import matplotlib.pyplot as plt

#
# A. Information source Values
temp = np.linspace(0, 40)
F1 = []
F2 = []
F3 = []
p = []

def cold(x):
    # Inputs
    m = 0
    n = 12
    b = 20
    if m <= x <= n:
        return 1
    elif n <= x <= b:
        return (b - x) / (b - n)
    elif x > b:
        return 0

def warm(x):
    # Inputs
    a = 17
    m = 25
    b = 28
    if x <= a:
        return 0
    elif a <= x <= m:
        return (x - a) / (m - a)
    elif m <= x <= b:
        return (b - x) / (b - m)
    elif x >= b:
        return 0

def hot(x):
    # Inputs
    a = 25
    m = 30
    n = 40
    if x < a:
        return 0
    elif a <= x <= m:
        return (x - a) / (m - a)
    elif m <= x <= n:
        return 1

def probability(x):
    if 10 <= x < 15:
        return 0.2
    else:
        return 0


for i in range(len(temp)):
    F1.append(cold(temp[i]))
    F2.append(warm(temp[i]))
    F3.append(hot(temp[i]))
    p.append(probability(temp[i]))

plt.plot(F1)
plt.plot(F2)
plt.plot(F3)
plt.plot(p)
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
#
# B. Entropy function
#
# Shannon
Esh = 0
p = np.array(p) + 0.00000000000001
for i in range(len(p)):
    Esh += p[i]*np.log(p[i])
Esh = -Esh
#
# De Luca and Termini
'''Elt_cold = 0
Elt_warm = 0
Elt_hot = 0
F1 = np.array(F1) + 0.001
F2 = np.array(F2) + 0.001
F3 = np.array(F3) + 0.001
for i in range(len(temp)):
    Elt_cold += F1[i]*np.log(F1[i]) + (1 - F1[i])*np.log(1 - F1[i])
    Elt_warm += F2[i] * np.log(F2[i]) + (1 - F2[i]) * np.log(1 - F2[i])
    Elt_hot += F3[i] * np.log(F3[i]) + (1 - F3[i]) * np.log(1 - F3[i])
Elt_cold = -(1/len(temp))*Elt_cold
Elt_warm = -(1/len(temp))*Elt_warm
Elt_hot = -(1/len(temp))*Elt_hot'''
#
# Hanman-Anirban
Eha = 0
a = 0
b = 0
c = 1/0.3
d = 1
for i in range(len(temp)):
    Eha = p[i]*np.exp(-(a * (p[i])**3 + b * (p[i])**2 + c * (p[i]) + d))

