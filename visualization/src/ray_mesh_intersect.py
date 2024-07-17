import numpy as np
import gpytoolbox as gpy

def ray_mesh_intersect(R_V, rays, V, F):
    ts, ids, _ = gpy.ray_mesh_intersect(R_V, rays, V, F)

    C_V = []
    intersected = np.array([0] * len(F))

    for i, (t, id) in enumerate(zip(ts, ids)):
        if id != -1:
            intersected[id] = 1
            C_V.append(R_V[i] + rays[i] * t)

    C_V = np.array(C_V)

    return C_V, intersected