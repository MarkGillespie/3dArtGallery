import os
import gpytoolbox as gpy
import numpy as np

def read_skeleton(filename):
    """
    Read skeleton from file 

    Parameters
    ----------
    filename
        File's name in meshes folder

    Returns
    ----------
    V
        Skeleton's vertices' coordinates

    E
        Skeleton's edges' vertex list
    """
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(THIS_DIR, "..", "..", "meshes")
    READ_PATH = DATA_DIR + "\\" + filename + '.cg'

    f = open(READ_PATH, "r")
    
    # Discard the first line
    line = f.readline()

    V = []
    E = []

    while True:
        line = f.readline()

        if not line:
            break

        # If the line starts with v, it is the vertex's coordinate
        if line[0] == 'v':
            words = line.split(" ")
            V.append([float(x) for x in words[1:]])
            assert(len(V[len(V)-1]) == 3)

        # If the line starts with e, it is their indices (1 - indexed) of vertice on the edge
        if line[0] == 'e':
            words = line.split(" ")
            data = [int(x) - 1 for x in words[1:]]
            assert(len(data) == 2)
            E.append(data)

    V = np.array(V)
    E = np.array(E)

    return V, E