from xr_models import evaluate_on_xr_model as eval
from xr_models import plot_membership_functions as plt
from xr_models import build_relation_matrix as rel

altenative = ['1', '2', '3']
cost = [[20291, 22007, 22769, 27054],
        [21058, 21831, 22378, 25865],
        [21977, 22749, 23098, 24276]]
membership_value = [[0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0]]
plt(x=cost, y=membership_value, names=altenative)
eval(rel(cost, membership_value, 'min'))
