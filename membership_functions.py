def triangular_mf(a, m, b, x):
    """
    Triangular membership function
    :param a: Beginning of the triangle
    :param m: top of the triangle
    :param b: end of the triangle
    :param x: current value that is going to be evaluated
    :return: membership value of the function
    """
    # Logic
    if x <= a:
        return 0.0
    elif a <= x <= m:
        return (x - a) / (m - a)
    elif m <= x <= b:
        return (b - x) / (b - m)
    elif x >= b:
        return 0.0


def trapezoidal_mf(a, m, n, b, x):
    """
    trapezoidal membership function
    :param a: beginning of the trapezoid
    :param m: left side of the trapezoid's top
    :param n: right side of the trapezoid's top
    :param b: end of trapezoid
    :param x: current value that is evaluated
    :return: membership value
    """
    if x < a:
        return 0.0
    elif a <= x <= m:
        return (x - a) / (m - a)
    elif m <= x <= n:
        return 1.0
    elif n <= x <= b:
        return (b - x) / (b - n)
    elif x > b:
        return 0.0
    # import numpy as np
    # return np.max([np.min([(x - a) / (m - a), 1, (b - x) / (b - n)]), 0])


def information_gain(a, b, c, d, x, alpha):
    import numpy as np
    return np.exp(-(a*x**3 + b*x**2 + c*x + d)**alpha)
