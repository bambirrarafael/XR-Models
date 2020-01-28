def evaluate_on_xr_model(x):
    '''
    Function of evaluate non-strict preference relation matrix in <X, R> model
    :param x: ndarray square matrix of any size witch has the non-strict preference relation
    :return: non dominance score of alternatives
    '''
    #
    # Import
    import numpy as np
    #
    # Evaluate ir matrix is square
    n = np.shape(x)
    if n[0] != n[1]:
        print('Error - Matrix is not square!')
    #
    # Print relation matrix
    print('\n')
    print(' ---- Relation Matrix ---- ')
    print(x)
    #
    # Build preference matrix
    p = np.zeros(n)
    for i in range(n[0]):
        for j in range(n[1]):
            if i == j:
                p[i, j] = 0
            if x[i, j] - x[j, i] < 0:
                p[i, j] = 0
            else:
                p[i, j] = x[i, j] - x[j, i]
    #
    # Print preference matrix
    print('\n')
    print(' ---- Preference Matrix ---- ')
    print(p)
    #
    # Build alternative's non dominance matrix
    nd = 1 - np.amax(p, 0)
    #
    # Print non dominance matrix
    print('\n')
    print(' ---- Non Dominance Matrix ---- ')
    print(nd)
    return nd
