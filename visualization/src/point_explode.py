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

def fibonacci_point_explode(P, num_rays = 1000):
    """
    Given a point, try to draw a lot of rays shooting out of it.

    Parameters
    ----------
    P
        The point that we will explode from

    num_rays
        Self explained (Default to 1000)

    Returns
    -------
    R_V
        numpy array of rays' veritces' coordinates
    R_E
        numpy array of rays' edges' vertice list
    """
    
    R_V = [P]
    R_E = []

    phi = np.pi * (np.sqrt(5.) - 1.)  # golden angle in radians

    for i in range(num_rays):
        y = 1 - (i / float(num_rays - 1)) * 2  # y goes from 1 to -1
        radius = np.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = np.cos(theta) * radius
        z = np.sin(theta) * radius

        R_V.append([x, y, z])
        R_E.append([0, i + 1])
    
    return np.array(R_V), np.array(R_E)