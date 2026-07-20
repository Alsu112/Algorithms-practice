def traversing_a_table():
  N, M = map(int, input().split())
  i,j = 0, 0
  D = [[0] * M] * (N)
  for i in range(N):
    for j in range(M):
      if i == 0 or j == 0:
        D[i][j] = 1
      else:
        D[i][j] = D[i-1][j] + D[i][j - 1]
  return D[N-1][M-1]
print(traversing_a_table())