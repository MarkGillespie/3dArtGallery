import numpy as np

def ray_triangle_intersection(A, B, C, origin = np.array([0, 0, 0]), ray = np.array([1, 0, 0])):
    """
    Find the intersection between a ray and a triangle

    Parameters
    ----------
    A, B, C (Required)
        Coordinate of the triangle

    origin
        The coordinate of the start point of the ray

    ray
        The direction of the ray

    Returns
    -------
    P
        The intersection point (if exists), otherwise return [].
    """
    ## Ray
    e_ = ray/np.linalg.norm(ray)        # Unit vector (versor) of e => ê

    AB = B - A               # Oriented segment A to B
    AC = C - A               # Oriented segment A to C
    n = np.cross(AB, AC)     # Normal vector
    n_ = n/np.linalg.norm(n) # Normalized normal

    # Using the point A to find d
    d = - np.dot(n_, A)

    # Finding parameter t
    t = - (np.dot(n_, origin) + d)/np.dot(n_, e_)

    # Finding P
    P = origin + t*e_

    # Get the resulting vector for each vertex
    # following the construction order
    Pa = np.dot(np.cross(B - A, P - A), n_)
    Pb = np.dot(np.cross(C - B, P - B), n_)
    Pc = np.dot(np.cross(A - C, P - C), n_)

    if(t < 0):
        # Means that the triangle has the normal in the opposite direction (same
        # direction from the ray) or the triangle is behind the ray origin
        return []

    if (Pa >= 0 and Pb >= 0 and Pc >= 0):
        return P
    else:
        return []