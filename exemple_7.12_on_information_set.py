from xr_models import evaluate_on_xr_model as xr
from xr_models import plot_membership_functions as plt
from xr_models import build_relation_matrix as brm
import membership_functions as mf
import numpy as np

altenative = ['1', '2', '3']
cost = [[20291, 22007, 22769, 27054],
        [21058, 21831, 22378, 25865],
        [21977, 22749, 23098, 24276]]
membership_value = [[0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0]]
plt(x=cost, y=membership_value, names=altenative)
#
# normalizing information set
IN = np.zeros(np.shape(cost))
for k in range(len(cost)):
    for i in range(len(cost[k])):
        IN[k][i] = (cost[k][i] - np.amin(cost[k]))/(np.amax(cost[k]) - np.amin(cost[k]))
#
# Uncertainty
E = []
EN = []
S = np.zeros(np.shape(IN))
H = np.zeros(len(IN))
for k in range(len(IN)):
    aux_ES = 0
    for i in range(len(IN[k])):
        S[k][i] = IN[k][i]*mf.trapezoidal_mf(a=IN[k][0], m=IN[k][1], n=IN[k][2], b=IN[k][3], x=IN[k][i])
        aux_ES += IN[k][i]*np.log(S[k][i]+0.001)
    E.append(np.sum(S[k]))
    EN.append(1/len(IN[k])*E[k])
    H[k] = -aux_ES
#
# Classic XR Model exemple 7.12
xr(brm(cost, membership_value, 'min'))



