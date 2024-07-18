import numpy as np

def point_explode(P, horizontal = 10, vertical = 10):
    """
    Given a point, try to draw a lot of rays shooting out of it.

    Parameters
    ----------
    P
        The point that we will explode from

    horizontal
        Amount of ray horizontally

    vertical
        Amount of rays vertically
        Must be at least 2

    Returns
    -------
    R_V
        numpy array of rays' veritces' coordinates
    R_E
        numpy array of rays' edges' vertice list
    """
    
    R_V = [P]
    R_E = []

    for i in range(horizontal):
        alpha = 2 * i * np.pi / horizontal
        for j in range(vertical):
            theta = j * np.pi / (vertical - 1)
            Q = [np.sin(alpha) * np.cos(theta), np.cos(alpha), np.sin(alpha) * np.sin(theta)]
            R_V.append(P + Q)
            R_E.append([0, i * horizontal + j + 1])
    
    return np.array(R_V), np.array(R_E)