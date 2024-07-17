import os
import numpy as np
import polyscope as ps
from src.read_skeleton import read_skeleton

def rand_ray(S_V, ray_length = 1):
  """
  Get one random ray per vertex

  Parameters
  ----------
  S_V
      Skeleton's vertices. |S_V| * 3 numpy array of vertices coordinates.

  ray_length
      Self explained. Default to 1.

  Returns
  -------
  vecs
      numpy array of rays
  """
  num_vert = len(S_V)
  vecs = []
  
  for _ in range(num_vert):
    v = np.random.rand(3) - 0.5
    vecs.append(v / np.linalg.norm(v))
  
  return np.array(vecs)

def rand_rays(S_V, num_rays = 1, ray_length = 1):
  """
  Get multiple random rays per vertex

  Parameters
  ----------
  S_V
      |S_V| * 3 numpy array of vertices coordinates.

  num_rays
      Self explained. Default to 1.

  ray_length
      Self explained. Default to 1.

  Returns
  -------
  R_V
      numpy array of rays' veritces' coordinates
  R_E
      numpy array of rays' edges' vertice list
  """
  num_vert = len(S_V)

  R_V = list(S_V)
  R_E = []

  for j in range(1, num_rays + 1):
    vecs = np.random.rand(num_vert, 3) - 0.5
    for i, vec in enumerate(vecs):
      R_V.append(R_V[i] + vec / np.linalg.norm(vec) * ray_length)
      R_E.append([i, i + j * num_vert])

  return np.array(R_V), np.array(R_E)