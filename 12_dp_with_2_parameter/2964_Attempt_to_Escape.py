def attempt_to_escape():
  N, M = map(int, input().split())
  A = []
  for i in range(N):
      list_str = list(map(int, input().split()))
      A.append(list_str)
  D = [[0] * M for _ in range(N)]
  if A[0][0] == 0:
    return 'Impossible'
  D[0][0] = 1
  for i in range(N):
    for j in range(M):
      if A[i][j] == 1:
        if i > 0:
          D[i][j] += D[i - 1][j]
        if j > 0:
          D[i][j] += D[i][j - 1]
  if D[N - 1][M - 1] == 0:
    return 'Impossible'
  else:
    return D[N - 1][M - 1]
print(attempt_to_escape())