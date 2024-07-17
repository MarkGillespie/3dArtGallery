import polyscope as ps

def display_mesh(V, F, R_V = [], R_E = [], intersected = [], C_V = [], S_V = [], S_E = [], S_P = [], vecs = [], ray_length = 1):
    ps.init()
    ps.reset_camera_to_home_view()

    obj = ps.register_surface_mesh('Surface', V, F, edge_width=1)
    obj.set_transparency(0.6)

    if len(intersected) != 0:
        obj.add_scalar_quantity('Intersected', intersected, defined_on='faces', cmap='reds', enabled = True)

    if len(C_V) != 0:
        ps.register_point_cloud('Intersection', C_V, radius = 0.002, enabled = True)

    if len(R_V) != 0 and len(R_E) != 0:
        ps.register_curve_network('THE RAY', R_V, R_E, radius = 0.0005, enabled = True)

    if len(S_V) != 0 and len(S_E) != 0:
        skeleton = ps.register_curve_network('Skeleton', S_V, S_E, radius = 0.001, enabled = True)

        if len(S_P) != 0:
            ps.register_point_cloud('Skeleton Points Sampling', S_P, radius = 0.002, enabled = True)

        if len(vecs) != 0:
            skeleton.add_vector_quantity("Random ray vector", vecs, enabled = True, radius = 0.002, length = ray_length)

    ps.show()
