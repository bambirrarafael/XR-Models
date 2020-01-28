def plot_membership_functions(x, y, names):
    '''
    Function that plots membership functions
    :param x: array of lists where each list is a point in the x axis
    :param y: array of lists where each list is a point in the y axis
    :param names: list with the names of the functions
    :return: image
    '''
    #
    # Imports
    import matplotlib.pyplot as plt
    #
    # Check x and y lists
    if len(x) != len(y):
        print('Error - Missing data for membership functions')
    for i in range(len(x)):
        if len(x[i]) != len((y[i])):
            print('Error - Wrong declaration of membership function ' + str(i + 1))
    #
    # Build plot
    for i in range(len(x)):
        plt.plot(x[i], y[i], label=names[i])
    plt.legend()
    plt.show()
