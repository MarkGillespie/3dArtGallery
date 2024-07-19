import os
import numpy as np
from src.read_mesh import read_mesh
from src.read_skeleton import read_skeleton
from src.display_mesh import display_mesh
from src.greedy_approach import greedy
from src.random_points_in_mesh import random_points
import time

for filename in ['torus', 'spot', 'homer', 'baby_doll', 'camel', 'donkey', 'kitten', 'man', 'running_pose', 'teapot']:
    V, F = read_mesh(filename)
    S_V, S_E = read_skeleton(filename)

    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(THIS_DIR, "..", "result")

    sk_time = []
    sk_guards = []

    # Using Just Skeleton
    for i in range(5):
        SOURCE_PATH = DATA_DIR  + "\\sk-" + filename + '-' + str(i + 1) + '.source'
        COLORS_PATH = DATA_DIR + "\\sk-" + filename + '-' + str(i + 1) + '.colors'
        start_time = time.time()
        sources, intersected = greedy(S_V, V, F, accept_partial = True, verbose = False)
        t = time.time() - start_time
        print(f'Experiment #{i + 1} : {filename} using just skeletons uses {len(sources)} guards, and takes {t} seconds to run.')
        sk_time.append(t)
        sk_guards.append(len(sources))

        np.savetxt(SOURCE_PATH, sources)
        np.savetxt(COLORS_PATH, intersected)

    rd_time = []
    rd_guards = []

    # Adding Random Points in
    for i in range(5):
        SOURCE_PATH = DATA_DIR + "\\rd-" + filename + '-' + str(i + 1) + '.source'
        COLORS_PATH = DATA_DIR + "\\rd-" + filename + '-' + str(i + 1) + '.colors'
        start_time = time.time()
        P = random_points(V, F, 1000, verbose = False)
        sources, intersected = greedy(np.concatenate((S_V, P)), V, F, accept_partial = True, verbose = False)
        t = time.time() - start_time
        print(f'Experiment #{i + 1} : {filename} using skeletons + 1000 random points uses {len(sources)} guards, and takes {t} seconds to run.')
        rd_time.append(t)
        rd_guards.append(len(sources))

        np.savetxt(SOURCE_PATH, sources)
        np.savetxt(COLORS_PATH, intersected)

    sk_time = sorted(sk_time)
    sk_guards = sorted(sk_guards)
    rd_time = sorted(rd_time)
    rd_guards = sorted(rd_guards)

    print('Just Skeleton')
    print(f'Time => Min: {sk_time[0]},  Max: {sk_time[4]}, Avg: {sum(sk_time) / 5}')
    print(f'Guards => Min: {sk_guards[0]},  Max: {sk_guards[4]}, Avg: {sum(sk_guards) / 5}')
    print('Skeleton + 1K')
    print(f'Time => Min: {rd_time[0]},  Max: {rd_time[4]}, Avg: {sum(rd_time) / 5}')
    print(f'Guards => Min: {rd_guards[0]},  Max: {rd_guards[4]}, Avg: {sum(rd_guards) / 5}')