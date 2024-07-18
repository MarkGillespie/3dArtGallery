import numpy as np
from src.point_visibility import point_visibility

def combine(intersected, visibility, num):

    for i in range(len(visibility)):
        if visibility[i]:
            intersected[i] = num

    return intersected

def greedy(P, V, F):
    """
    Greedy approach for placing guards.
    If multiple guards cover the same amount of triangles, randomly choose one (with the help of reservoir sampling)

    Parameters
    ----------
    P
        Numpy array of all possible locations for a guard

    V
        Mesh's vertices' coordinates

    F
        Mesh's faces' vertex list

    Returns
    -------
    sources
        Numpy array of guards' position

    colors
        Numpy array of values for coloring purpose (should be all nonzeros)
    """

    sources = []
    intersected = np.array([0] * len(F))
    colors = np.array([0] * len(F))
    used = np.array([0] * len(P))
    visibility = []

    for p in P:
        _, p_intersected = point_visibility(p, V, F)
        visibility.append(p_intersected)

    while not intersected.all():
        max_intersection = 0
        max_index = 0
        n = 2
        
        for i in range(len(P)):
            if used[i]:
                continue
            
            num_intersection = np.dot(1 - intersected, visibility[i])

            if num_intersection > max_intersection:
                max_intersection = num_intersection
                max_index = i
                n = 2
            elif num_intersection == max_intersection:
                if np.random.randint(n) == 0:
                    max_index = i
                n += 1

        if max_intersection == 0:
            break

        used[max_index] = 1
        sources.append(P[max_index])
        colors = combine(colors, visibility[max_index], len(sources))

        for i in range(len(F)):
            intersected[i] |= visibility[max_index][i]

    return np.array(sources), colors