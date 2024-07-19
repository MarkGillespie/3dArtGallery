import numpy as np
import polyscope as ps
import gpytoolbox as gpy
from src.read_mesh import read_mesh
from src.read_skeleton import read_skeleton
from src.display_mesh import display_mesh
from src.skeleton_points_sampling import skeleton_points_fixed_length_sampling
from src.random_ray_vertices import rand_ray
from src.random_ray_vertices import rand_rays
from src.ray_mesh_intersect import rays_mesh_intersect
from src.point_explode import fibonacci_point_explode
from src.point_visibility import point_visibility
from src.point_visibility import points_visibility
from src.greedy_approach import greedy
from src.subtractive_approach import subtractive
from src.greedy_approach import greedy_with_noise
from src.random_points_in_mesh import random_points
import time

filename = input()
start_time = time.time()
V, F = read_mesh(filename)
S_V, S_E = read_skeleton(filename)
S_P = skeleton_points_fixed_length_sampling(S_V, S_E, 5e-3)
# vecs = rand_ray(S_V)
# R_V, R_E = rand_rays(S_P, 3, 1)
# R_V = []
# R_E = []
# sources = np.array([S_V[np.random.randint(len(S_V))], S_V[np.random.randint(len(S_V))], S_V[np.random.randint(len(S_V))]])
# for source in sources:
#     r_v, r_e = fibonacci_point_explode(source, 10000)
#     R_V.append(r_v)
#     R_E.append(r_e)
# C_V, intersected = rays_mesh_intersect(R_V, R_E, V, F)
# C_V, intersected = points_visibility(sources, V, F)
P = []
P = random_points(V, F, 1000)
sources, intersected = greedy(np.concatenate((S_V, P)), V, F, accept_partial = True)
# sources, intersected = greedy(S_V, V, F, accept_partial = True)
# sources, intersected = greedy_with_noise(S_P, V, F, noise=1e-4, num_tries=100)
# sources, intersected = subtractive(S_V, V, F)

print(f'Time elapsed: {time.time() - start_time} seconds')
display_mesh(V, F, intersected = intersected, S_V = S_V, S_E = S_E, S_P = S_P, sources = sources, available_positions = P)
