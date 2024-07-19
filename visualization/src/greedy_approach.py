import numpy as np
from src.point_visibility import point_visibility

def combine(intersected, visibility, num):
    for i in range(len(visibility)):
        if visibility[i]:
            intersected[i] = num

    return intersected

def remove_unnecessary(sources, colors, contains_zero):
    ret_sources = []
    now, next = 1, 1
    temp = sorted(list(set(colors)))
    color_map = {i: j + 1 - contains_zero for i, j in zip(temp, list(range(len(temp))))}

    for i in range(len(colors)):
        colors[i] = color_map[colors[i]]

    for t in temp:
        if t >= 1:
            ret_sources.append(sources[t-1])

    return np.array(ret_sources), colors

def greedy(P, V, F, accept_partial = True):
    """
    Greedy approach for placing guards.
    If multiple guards cover the same amount of triangles, randomly choose one (with the help of reservoir sampling)

    Parameters
    ----------
    P
        Numpy array of all possible locations for a guard

    V
        Mesh's vertices' coordinates

    F
        Mesh's faces' vertex list

    accept_partial
        Still return values even if not all faces can be covered

    Returns
    -------
    sources
        Numpy array of guards' position

    colors
        Numpy array of values for coloring purpose (should be all nonzeros)
    """

    sources = []
    intersected = np.array([0] * len(F))
    colors = np.array([0] * len(F))
    used = np.array([0] * len(P))
    visibility = []

    print('Calculating Visibility...')

    for p in P:
        _, p_intersected = point_visibility(p, V, F)
        visibility.append(p_intersected)

    print('Applying Greedy Algorithm...')

    iter = 1

    while not intersected.all():
        max_intersection = 0
        max_index = 0
        n = 2

        print(f'Iteration # {iter}')
        iter += 1
        
        for i in range(len(P)):
            if used[i]:
                continue
            
            num_intersection = np.dot(1 - intersected, visibility[i])

            if num_intersection > max_intersection:
                max_intersection = num_intersection
                max_index = i
                n = 2
            elif num_intersection == max_intersection:
                if np.random.randint(n) == 0:
                    max_index = i
                n += 1

        if max_intersection == 0:
            num_tries -= 1
            if num_tries == 0:
                break

        used[max_index] = 1
        sources.append(P[max_index])
        colors = combine(colors, visibility[max_index], len(sources))

        for i in range(len(F)):
            intersected[i] |= visibility[max_index][i]

    if not accept_partial and not intersected.all():
        print('UNSOLVABLE')
        assert(False)

    print('Removing Unnecessary Guards...')

    return remove_unnecessary(np.array(sources), colors, intersected.all())

def greedy_with_noise(P, V, F, noise = 1e-6, num_tries = 5):
    """
    Greedy approach for placing guards.
    A noise is added to every position for each iteration of the algorithm
    If multiple guards cover the same amount of triangles, randomly choose one (with the help of reservoir sampling)
    
    IMPORTANT: THIS MAY TAKE VERY LONG TIME
    
    Parameters
    ----------
    P
        Numpy array of all possible locations for a guard

    V
        Mesh's vertices' coordinates

    F
        Mesh's faces' vertex list

    noise
        Randomly add noise to the array P in [-noise, noise] range
        Default to 1e-6

    num_tries
        Amount of tries before giving up (only applicable when noise is nonzero)
        Default to 5

    Returns
    -------
    sources
        Numpy array of guards' position

    colors
        Numpy array of values for coloring purpose (should be all nonzeros)
    """

    old_P = np.copy(P)
    sources = []
    intersected = np.array([0] * len(F))
    colors = np.array([0] * len(F))
    used = np.array([0] * len(P))
    visibility = []

    print('Applying Greedy Algorithm...')

    iter = 1

    while not intersected.all():
        max_intersection = 0
        max_index = 0
        n = 2

        print(f'Iteration # {iter}')
        iter += 1

        print('Calculating Visibility...')

        for i in range(len(P)):
            P[i] += (np.random.rand(3) - 0.5) * 2 * noise

        for p in P:
            _, p_intersected = point_visibility(p, V, F)
            visibility.append(p_intersected)
        
        for i in range(len(P)):
            if used[i]:
                continue
            
            num_intersection = np.dot(1 - intersected, visibility[i])

            if num_intersection > max_intersection:
                max_intersection = num_intersection
                max_index = i
                n = 2
            elif num_intersection == max_intersection:
                if np.random.randint(n) == 0:
                    max_index = i
                n += 1

        if max_intersection == 0:
            num_tries -= 1
            print(f'FAIL ({num_tries} tries left)')
            if num_tries == 0:
                break
        else:
            print('SUCCESS')

        # used[max_index] = 1
        sources.append(P[max_index])
        colors = combine(colors, visibility[max_index], len(sources))

        for i in range(len(F)):
            intersected[i] |= visibility[max_index][i]

        P = np.copy(old_P)

    if not intersected.all():
        print('UNSOLVABLE')
        assert(False)

    print('Removing Unnecessary Guards...')

    return remove_unnecessary(np.array(sources), colors)