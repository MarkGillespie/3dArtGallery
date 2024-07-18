import numpy as np
import gpytoolbox as gpy

def ray_mesh_intersect(R_V, rays, V, F):
    """
    Find intersection points and intersected faces
    Work best with rand_ray

    Parameters
    ----------
    R_V
        Numpy array of vertices coordinates.

    rays
        Numpy array of the direction of rays shooting out of each vertex in R_V

    V
        Mesh's vertices' coordinates

    F
        Mesh's faces' vertices list

    Returns
    -------
    C_V
        numpy array of intersection points' coordinates
        
    intersected
        |F| array of 0 or 1 where 1 means this face is intersected with some rays.
    """
    ts, ids, _ = gpy.ray_mesh_intersect(R_V, rays, V, F)

    C_V = []
    intersected = np.array([0] * len(F))

    for i, (t, id) in enumerate(zip(ts, ids)):
        if id != -1:
            intersected[id] = 1
            C_V.append(R_V[i] + rays[i] * t)

    C_V = np.array(C_V)

    return C_V, intersected

def ray_mesh_intersect_2(R_V, R_E, V, F):
    """
    Find intersection points and intersected faces
    Work best with rand_rays

    Parameters
    ----------
    R_V
        Numpy array of vertices coordinates.

    R_E
        numpy array of rays' edges' vertice list

    V
        Mesh's vertices' coordinates

    F
        Mesh's faces' vertices list

    Returns
    -------
    C_V
        numpy array of intersection points' coordinates
        
    intersected
        |F| array of 0 or 1 where 1 means this face is intersected with some rays.
    """
    new_R_V = []
    rays = []
    for e in R_E:
        v = R_V[e[1]] - R_V[e[0]]
        rays.append(v / np.linalg.norm(v))
        new_R_V.append(R_V[e[0]])

    ts, ids, _ = gpy.ray_mesh_intersect(np.array(new_R_V), np.array(rays), V, F)

    C_V = []
    intersected = np.array([0] * len(F))

    for i, (t, id) in enumerate(zip(ts, ids)):
        if id != -1:
            intersected[id] = 1
            C_V.append(new_R_V[i] + rays[i] * t)

    C_V = np.array(C_V)

    return C_V, intersected

def rays_mesh_intersect(R_V, R_E, V, F):
    """
    Find intersection points and intersected faces
    Support multi-colored output
    Work best with rand_rays

    Parameters
    ----------
    R_V
        Numpy array of Numpy array of vertices coordinates.

    R_E
        Numpy array of numpy array of rays' edges' vertice list

    V
        Mesh's vertices' coordinates

    F
        Mesh's faces' vertices list

    Returns
    -------
    C_V
        numpy array of intersection points' coordinates
        
    intersected
        |F| array of values each value corresponding to a color.
    """

    C_V = []
    intersected = np.array([0] * len(F))

    for k, (r_v, r_e) in enumerate(zip(R_V, R_E)):
        new_R_V = []
        rays = []
        for e in r_e:
            v = r_v[e[1]] - r_v[e[0]]
            rays.append(v / np.linalg.norm(v))
            new_R_V.append(r_v[e[0]])

        ts, ids, _ = gpy.ray_mesh_intersect(np.array(new_R_V), np.array(rays), V, F)

        for i, (t, id) in enumerate(zip(ts, ids)):
            if id != -1:
                intersected[id] = k
                C_V.append(new_R_V[i] + rays[i] * t)

    C_V = np.array(C_V)

    return C_V, intersected