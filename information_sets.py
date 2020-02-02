import numpy as np
import matplotlib.pyplot as plt
import membership_functions as mf
import xr_models as xr

#
# =================== Exemple 5.1 ==========================
information = [100, 200, 300, 400, 500]
membership_values = [0.333, 0.666, 1, 0.666, 0.333]
plt.plot(information, membership_values, label='Exemple 5.1')
plt.legend()
plt.show()
#
# normalized information
normalized_info = np.zeros(np.shape(information))
for i in range(len(information)):
    normalized_info[i] = (information[i] - np.amin(information))/(np.amax(information) - np.amin(information))
print('normalized information: ' + str(normalized_info))
#
# information set
info_set = np.zeros(np.shape(information))
for i in range(len(information)):
    info_set[i] = normalized_info[i]*membership_values[i]
print('information set: ' + str(info_set))
#
# normalized uncertainty information
entropy_norm = 1/len(info_set)*np.sum(info_set)
print('Entropy: ' + str(entropy_norm))
#
# =================== Exemple 5.2 ==========================
information = [[1000, 3000, 5000],
               [1000, 3000, 5000, 7000, 10000],
               [5000, 7000, 10000]]
membership_values = [[1, 0.5, 0],
                     [0, 0.5, 1, 0.5, 0],
                     [0, 0.5, 1]]
xr.plot_membership_functions(information, membership_values, names=['low', 'medium', 'high'])
#
# normalized information
normalized_info = np.array([[0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0]])
for i in range(len(information)):
    for j in range(len(information[i])):
        normalized_info[i][j] = (information[i][j] - np.amin(information[i]))/(np.amax(information[i]) -
                                                                               np.amin(information[i]))
print('normalized information: ' + '\n' + str(normalized_info))
#
# information set
info_set = np.array([[0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0]])
for i in range(len(information)):
    for j in range(len(information[i])):
        info_set[i][j] = normalized_info[i][j]*membership_values[i][j]
print('information set: ' + '\n' + str(info_set))
#
# normalized uncertainty information
entropy_norm = np.zeros(3)
for i in range(3):
    entropy_norm[i] = 1/len(info_set[i])*np.sum(info_set[i])
print('Entropy: ' + '\n' + str(entropy_norm))
#
# =================== Exemple 5.3 ==========================
information = [[2000, 3500, 5000, 6500],
               [3500, 5000, 6500, 8000, 9500]]
membership_values = [[1, 0.62, 0.4, 0.18],
                     [0.2, 0.4, 0.6, 0.8, 1]]
normalized_info = [[0, 0.33, 0.66, 1],
                   [0, 0.25, 0.5, 0.75, 1]]
# information set
info_set = np.array([[0, 0, 0, 0], [0, 0, 0, 0, 0]])
for i in range(len(information)):
    for j in range(len(information[i])):
        info_set[i][j] = normalized_info[i][j]*membership_values[i][j]
print('information set: ' + '\n' + str(info_set))
#
# normalized uncertainty information
entropy_norm = np.zeros(2)
for i in range(2):
    entropy_norm[i] = 1/len(info_set[i])*np.sum(info_set[i])
print('Entropy: ' + '\n' + str(entropy_norm))
#
# Uncertainty measure
uncertinty = np.zeros(2)
for i in range(len(normalized_info)):
    aux = 0
    for j in range(len(normalized_info[i])):
        aux += (normalized_info[i][j] + 0.001)*np.log(info_set[i][j]+0.001)
    uncertinty[i] = -aux
print('Uncertainty: ' + '\n' + str(uncertinty))
