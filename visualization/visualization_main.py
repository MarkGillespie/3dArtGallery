import numpy as np
import polyscope as ps
from src.read_mesh import read_mesh
from src.read_skeleton import read_skeleton
from src.display_mesh import display_mesh
from src.skeleton_points_sampling import skeleton_points_fixed_length_sampling
from src.random_ray_vertices import rand_ray
from src.random_ray_vertices import rand_rays
from src.ray_triangle_intersection import ray_triangle_intersection

filename = input()
V, F = read_mesh(filename)
S_V, S_E = read_skeleton(filename)
S_P = skeleton_points_fixed_length_sampling(S_V, S_E, 5e-3)
vecs = rand_ray(S_V)
R_V, R_E = rand_rays(S_V, 3, 0.5)

C_V = []
intersected = np.array([0] * len(F))
for i, vec in enumerate(vecs):
    for j, f in enumerate(F):
        intersection_point = ray_triangle_intersection(V[f[0]], V[f[1]], V[f[2]], S_V[i], vec / np.linalg.norm(vec))
        if len(intersection_point) == 3:
            intersected[j] = 1
            C_V.append(intersection_point)
C_V = np.array(C_V)

display_mesh(V, F, C_V = C_V, intersected = intersected, R_V = R_V, R_E = R_E, S_V = S_V, S_E = S_E, S_P = S_P, vecs = vecs, ray_length = 1)