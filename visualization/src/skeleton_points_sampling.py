import numpy as np

def skeleton_points_uniform_sampling(V, E, points_per_edge = 9):
    """
    Skeleton Points Sampling by breaking an edge to many equal pieces

    Parameters
    ----------
    V
        Skeleton's vertices' coordinates

    E
        Skeleton's edges' vertex list

    points_per_edge
        The number of points per edge excluding the start and end points
        (Default to 9)

    Returns
    -------
    S_P
        The numpy array of points
    """
    P = []

    for edge in E:
        for i in range(1, points_per_edge + 1):
            P.append((V[edge[0]] * i + V[edge[1]] * (points_per_edge + 1 - i)) / (points_per_edge + 1))

    return np.concatenate((np.array(P), V), axis=0)

def skeleton_points_fixed_length_sampling(V, E, target_length = 1):
    """
    Skeleton Points Sampling by break an edge to be as close to the target_length as possible

    Parameters
    ----------
    V
        Skeleton's vertices' coordinates

    E
        Skeleton's edges' vertex list

    target_length
        Self explained (Default to 1)

    Returns
    -------
    S_P
        The numpy array of points
        If target_length is too big, return V
    """
    P = []

    for edge in E:
        u, v = V[edge[0]], V[edge[1]]
        edge_length = np.linalg.norm(u - v)
        points_per_edge = int(np.round(edge_length / target_length) - 1)

        for i in range(1, points_per_edge + 1):
            P.append((V[edge[0]] * i + V[edge[1]] * (points_per_edge + 1 - i)) / (points_per_edge + 1))

    if len(P) == 0:
        return V
    
    return np.concatenate((np.array(P), V), axis=0)