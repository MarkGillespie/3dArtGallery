import os
import gpytoolbox as gpy
import polyscope as ps

def read_mesh(filename):
    """
    Read mesh from file 

    Parameters
    ----------
    filename
        File's name in meshes folder

    Returns
    ----------
    V
        Mesh's vertices' coordinates

    F
        Mesh's faces' vertex list
    """
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(THIS_DIR, "..", "..", "meshes")
    READ_PATH = DATA_DIR + "\\" + filename + '.obj'

    V, F = gpy.read_mesh(READ_PATH)
    return V, F