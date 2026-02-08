def cubes():
  N, M = map(int, input().split())
  set_Anya = set()
  set_Borya = set()
  for i in range(N):
    set_Anya.add(int(input()))
  for i in range(M):
    set_Borya.add(int(input()))
  set_intersection = sorted(set_Anya & set_Borya) #O(min(N, M)log min(N, M))
  set_Anya = sorted(set_Anya.difference(set_intersection)) #O(max(N, M)log max(N, M) )
  set_Borya = sorted(set_Borya.difference(set_intersection)) #O(max(N, M)log max(N, M))
  print(len(set_intersection))
  print(*set_intersection)
  print(len(set_Anya))
  print(*set_Anya)
  print(len(set_Borya))
  print(*set_Borya)

cubes()
# O(max(N, M)log max(N, M)) - временная сложность
# O(N + M)