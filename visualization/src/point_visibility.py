import numpy as np
from src.ray_mesh_intersect import ray_mesh_intersect_2
from src.ray_mesh_intersect import rays_mesh_intersect

def point_visibility(P, V, F):
    """
    Given a point, which triangle faces can it see.
    Use the centroid of triangle to determine the result.

    Parameters
    ----------
    P
        The point where the guard is

    V (Required)
        Mesh's vertices' coordinates

    F (Required)
        Mesh's faces' vertex list

    Returns
    -------
    C_V
        numpy array of intersection points' coordinates
        
    intersected
        |F| array of 0 or 1 where 1 means this face is intersected with some rays.
    """
    
    R_V = [P]
    R_E = []

    for i, f in enumerate(F):
        R_V.append((V[f[0]] + V[f[1]] + V[f[2]]) / 3)
        R_E.append([0, i + 1])
    
    return ray_mesh_intersect_2(R_V, R_E, V, F)

def points_visibility(P, V, F):
    """
    Given multiple points, which triangle faces can at least one of them see.
    Use the centroid of triangle to determine the result.

    Parameters
    ----------
    P
        Numpy array of points where the guards are

    V (Required)
        Mesh's vertices' coordinates

    F (Required)
        Mesh's faces' vertex list

    Returns
    -------
    C_V
        numpy array of intersection points' coordinates
        
    intersected
        |F| array of 0 or 1 where 1 means this face is intersected with some rays.
    """
    
    R_V = []
    R_E = []

    r_v = []
    r_e = []

    for i, f in enumerate(F):
        r_v.append((V[f[0]] + V[f[1]] + V[f[2]]) / 3)
        r_e.append([len(F), i])

    for p in P:
        R_V.append(r_v + [p])
        R_E.append(r_e)
    
    return rays_mesh_intersect(np.array(R_V), np.array(R_E), V, F)