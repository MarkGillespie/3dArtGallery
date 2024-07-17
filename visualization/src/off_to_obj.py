import os
import gpytoolbox as gpy
import numpy as np

def off_to_obj(filename):
    """
    Create .obj file from .off file

    Parameters
    ----------
    filename
        File's name in meshes folder
    """
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(THIS_DIR, "..", "..", "meshes")
    READ_PATH = DATA_DIR + "\\" + filename + '.off'
    WRITE_PATH = DATA_DIR + "\\" + filename + '.obj'

    f = open(READ_PATH, "r")
    
    # Discard the first line
    line = f.readline()

    # Second line is num_V, num_F, num_E
    line = f.readline()
    num_V, num_F, num_E = [int(x) for x in line.split(" ")]
    # print(num_V, num_F, num_E)

    # Next num_V lines are the coordinates
    V = []
    for _ in range(num_V):
        line = f.readline()
        V.append([float(x) for x in line.split(" ")])
        assert(len(V[len(V)-1]) == 3)

    # Next num_F lines are the number of vertices in the face and their indices (0 - indexed)
    F = []
    for _ in range(num_F):
        line = f.readline()
        data = [int(x) for x in line.split(" ")]
        assert(data[0] == 3)
        assert(len(data) == 4)
        F.append(data[1:])

    V = np.array(V)
    F = np.array(F)

    gpy.write_mesh(WRITE_PATH, V, F)