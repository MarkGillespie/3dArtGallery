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
    target_intersect= 0 
    num_inter= []
    new_index= 0 
    next_index = 0
    
    for i in range(len(P)):
      if temp_guard[i]:
        continue
      num_inter = np.dot(1 - intersected, visibility[i])
      
      if num_inter > target_intersect:
        target_intersect= num_inter
        new_index= i
        next_index= i+1
        num_inter = np.dot(1 - intersected, visibility[next_index])
        
        if num_inter > target_intersect:
          target_intersect= num_inter
          sources.pop(i)
          new_index= next_index
        
    if target_intersect == 0:
      sources.pop(i)
      
    # checks what mesh coverage would look like without guard i
    #temp_intersected = np.copy(intersected)
    #temp_intersected &= ~visibility[i]

 

  return np.array(sources), intersected
