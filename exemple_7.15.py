'''
The  multicriteria  decision-making  problem  related  to  energy  planning  is considered in Beccali, Cellura, and
Ardente (1998).
It consists of the selection of the most appropriate technology in a renewable energy diffusion plan for Sardinia.
Here,  we  will consider the following six criteria:
1.  Targets of primary energy saving on a regional scale.
2.  Sustainability according to greenhouse pollutant emissions.
3.  Consistency of installation and maintenance requirements with local technical conditions.
4.  Continuity and predictability of performances.
5.  Market maturity.
6.  Compatibility with the political, legislative, and administrative situation.

The first two criteria are of a quantitative character.
The third, fourth, and sixth criteria are of  a  qualitative  character  and  can  be  evaluated  through  the  set  of
three  normalized  fuzzy values S(F)={small, middle, large}.
The fifth criterion is also of a qualitative character and can be evaluated through the set of five normalized fuzzy
values S (F)={very small, small, middle, large, very large}.

The following four options of energy sources are considered as alternatives:
1.  Solar (domestic solar water heaters).
2.  Wind (wind turbines of grid-connected type).
3.  Hydraulic (hydro plants in derivation schemes).
4.  Biomass (combined heat and power plants fed by agricultural wastes or energy crops).
'''

from xr_models import build_relation_matrix as brm
from xr_models import plot_membership_functions as plt
from xr_models import evaluate_on_xr_model as eval
import numpy as np

#
# Plot the membership functions
names_a = ['small', 'middle', 'large']
x_a = [[0, 0.3],
       [0.2, 0.5, 0.8],
       [0.7, 1]]
y_a = [[1, 0],
       [0, 1, 0],
       [0, 1]]
names_b = ['very small', 'small', 'middle', 'large', 'very large']
x_b = [[0, 0.15],
       [0.1, 0.25, 0.4],
       [0.35, 0.5, 0.65],
       [0.6, 0.75, 0.9],
       [0.85, 1]]
y_b = [[1, 0],
       [0, 1, 0],
       [0, 1, 0],
       [0, 1, 0],
       [0, 1]]
#plt(x_a, y_a, names_a)
#plt(x_b, y_b, names_b)
#
# Fuzzy non-strict preference relation matrix of 1° and 2° criteria
r_1 = np.array([[1, 0.106, 1, 0.297],
                [1, 1, 1, 1],
                [0.01, 0.001, 1, 0.003],
                [1, 0.357, 1, 1]])
r_2 = np.array([[1, 0.919, 0.919, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [0.396, 0.363, 0.363, 1]])
#
# Fuzzy non-strict preference relation matrix of 3°
x_3 = [[0.7, 1],
       [0, 0.3],
       [0.2, 0.5, 0.8],
       [0, 0.3]]
y_3 = [[0, 1],
       [1, 0],
       [0, 1, 0],
       [1, 0]]
r_3 = brm(x_3, y_3, 'max')
print('\n')
print('Fuzzy non-strict preference relation matrix of 3°')
print(r_3)
#
# Fuzzy non-strict preference relation matrix of 4°
x_4 = [[0, 0.3],
       [0, 0.3],
       [0.7, 1],
       [0.7, 1]]
y_4 = [[1, 0],
       [1, 0],
       [0, 1],
       [0, 1]]
r_4 = brm(x_4, y_4, 'max')
print('\n')
print('Fuzzy non-strict preference relation matrix of 4°')
print(r_4)
#
# Fuzzy non-strict preference relation matrix of 5°
x_5 = [[0.85, 1],
       [0.6, 0.75, 0.9],
       [0.85, 1],
       [0.6, 0.75, 0.9]]
y_5 = [[0, 1],
       [0, 1, 0],
       [0, 1],
       [0, 1, 0]]
r_5 = brm(x_5, y_5, 'max')
print('\n')
print('Fuzzy non-strict preference relation matrix of 5°')
print(r_5)
#
# Fuzzy non-strict preference relation matrix of 6°
x_6 = [[0, 0.3],
       [0, 0.3],
       [0.7, 1],
       [0.2, 0.5, 0.8]]
y_6 = [[1, 0],
       [1, 0],
       [0, 1],
       [0, 1, 0]]
r_6 = brm(x_6, y_6, 'max')
print('\n')
print('Fuzzy non-strict preference relation matrix of 6°')
print(r_6)
#
#
r = [r_1, r_2, r_3, r_4, r_5, r_6]
agreg_rel = np.mean(r, 0)
# pag 222 quantifier
# pag 242 result
