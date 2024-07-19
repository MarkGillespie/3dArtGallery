import numpy as np
from src.read_mesh import read_mesh
from src.read_skeleton import read_skeleton
from src.display_mesh import display_mesh
from src.greedy_approach import greedy
from src.random_points_in_mesh import random_points
import time

for filename in ['spot', 'homer', 'baby_doll', 'camel', 'donkey', 'kitten', 'man', 'running_pose', 'teapot']:
    V, F = read_mesh(filename)
    S_V, S_E = read_skeleton(filename)

    # Using Just Skeleton
    for i in range(5):
        start_time = time.time()
        sources, _ = greedy(S_V, V, F, accept_partial = True, verbose = False)
        print(f'Experiment #{i + 1} : {filename} using just skeletons uses {len(sources)} guards, and takes {time.time() - start_time} seconds to run.')

    # Adding Random Points in
    for i in range(5):
        start_time = time.time()
        P = random_points(V, F, 1000, verbose = False)
        sources, _ = greedy(np.concatenate((S_V, P)), V, F, accept_partial = True, verbose = False)
        print(f'Experiment #{i + 1} : {filename} using just skeletons uses {len(sources)} guards, and takes {time.time() - start_time} seconds to run.')
