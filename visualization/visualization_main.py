import numpy as np
import polyscope as ps
from src.read_mesh import read_mesh
from src.read_skeleton import read_skeleton
from src.display_mesh import display_mesh
from src.skeleton_points_sampling import skeleton_points_fixed_length_sampling
from src.random_ray_vertices import rand_ray
from src.random_ray_vertices import rand_rays

filename = input()
V, F = read_mesh(filename)
S_V, S_E = read_skeleton(filename)
S_P = skeleton_points_fixed_length_sampling(S_V, S_E, 5e-3)
vecs = rand_ray(S_V)
R_V, R_E = rand_rays(S_V, 3, 0.5)

display_mesh(V, F, R_V = R_V, R_E = R_E, S_V = S_V, S_E = S_E, S_P = S_P, vecs = vecs, ray_length = 1)