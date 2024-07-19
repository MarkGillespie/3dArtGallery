import numpy as np
import polyscope as ps

def display_mesh(V, F, R_V = [], R_E = [], sources = [], intersected = [], C_V = [], S_V = [], S_E = [], S_P = [], vecs = [], ray_length = 1):
    """
    Display the mesh

    Parameters
    ----------
    V (Required)
        Mesh's vertices' coordinates

    F (Required)
        Mesh's faces' vertex list

    R_V
        Rays' vertices' coordiantes

    R_E
        Rays' edges' vertex list

    intersected
        |F| array of 0 or 1 where 1 means this face is intersected with some rays.

    C_V
        Intersection points' coordiantes

    S_V
        Skeleton's vertices' coordinates

    S_E
        Skeleton's edges' vertex list

    S_P
        Skeleton point sampling's vertices' coordinates

    vecs
        Numpy array of random rays shooting out of each point of the skeleton's vertices

    ray_length
        length of vecs (default to 1)
    """
    ps.init()
    ps.set_background_color([0., 0., 0.])
    ps.reset_camera_to_home_view()

    obj = ps.register_surface_mesh('Surface', V, F, edge_width=1)
    obj.set_transparency(0.6)

    if len(sources) != 0:
        guards = ps.register_point_cloud('Guards', sources, radius = 0.02, enabled = True)
        index = np.array(range(1, len(sources) + 1))
        guards.add_scalar_quantity('Index', index, cmap='rainbow', vminmax = (0, len(sources)), enabled = True)

    if len(intersected) != 0:
        obj.add_scalar_quantity('Intersected', intersected, defined_on='faces', cmap='rainbow', vminmax = (0, len(sources)), enabled = True)

    if len(C_V) != 0:
        ps.register_point_cloud('Intersection', C_V, radius = 0.002, enabled = True)

    if len(R_V) != 0 and len(R_E) != 0:
        for i in range(len(R_V)):
            ps.register_curve_network('RAY ' + str(i + 1), R_V[i], R_E[i], radius = 0.0005, enabled = False)

    if len(S_V) != 0 and len(S_E) != 0:
        skeleton = ps.register_curve_network('Skeleton', S_V, S_E, radius = 0.001, enabled = True)

        if len(S_P) != 0:
            ps.register_point_cloud('Skeleton Points Sampling', S_P, radius = 0.002, enabled = False)

        if len(vecs) != 0:
            skeleton.add_vector_quantity("Random ray vector", vecs, enabled = False, radius = 0.002, length = ray_length)

    ps.show()
