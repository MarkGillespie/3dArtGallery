import os
import numpy as np
import polyscope as ps
from src.read_skeleton import read_skeleton

def rand_ray(S_V):
  num_vert = len(S_V)
  vecs = np.random.rand(num_vert, 3) - 0.5
  
  return vecs

def rand_rays(S_V, num_rays = 1, ray_length = 1):
  num_vert = len(S_V)

  R_V = list(S_V)
  R_E = []

  for j in range(1, num_rays + 1):
    vecs = np.random.rand(num_vert, 3) - 0.5
    for i, vec in enumerate(vecs):
      R_V.append(R_V[i] + vec / np.linalg.norm(vec) * ray_length)
      R_E.append([i, i + j * num_vert])

  return np.array(R_V), np.array(R_E)