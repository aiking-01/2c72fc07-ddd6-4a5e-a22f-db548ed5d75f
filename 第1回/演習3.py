def distance(P,Q):
  p=P[0]+P[1]*1j
  q=Q[0]+Q[1]*1j
  ans=(p**2+q**2)**0.5
  return abs(ans)

# 点 (0, 0) と 点 (1, 1) の距離

print(distance([0,0],[1,1]))