import numpy as np  
from src.point_visibility import point_visibility


  #check visibility for initial guards
def subtractive(P, V, F):
  sources= P.copy()
  intersected = np.zeros(len(F), dtype=int)
  visibility = []
  
  for p in P:
    _, p_intersected = point_visibility(p, V, F)
    visibility.append(p_intersected)
    intersected |= p_intersected
  
  if not intersected.all():
    return "missing full coverage"
    
  
  # iteratively remove guards with shared visibility
  i = 0
  while i < len(P):
  
    # checks what mesh coverage would look like without guard i
    temp_intersected = np.copy(intersected)
    temp_intersected &= ~visibility[i]
  
    # checks
    if temp_intersected.all():
      sources.pop(i)
      intersected = temp_intersected
      visibility.pop(i)
    else: 
      i += 1
 

  return np.array(sources)
