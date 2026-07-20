def func():
  N, M = map(int, input().split())
  A = [[0] * (M + 4) for _ in range(N + 4)]
  A[2][2] = 1
  for i in range(N + 4):
    for j in range(M + 4):
      if i < 2 or j < 2 or i > N + 1 or j > M + 1:
        A[i][j] = -1
  for i in range(2, N + 2):
    for j in range(2, M + 2):
      if A[i-2][j - 1] > 0 or A[i-1][j - 2] > 0:
        A[i][j] = max(A[i-2][j - 1], 0) + max(0, A[i-1][j - 2])
  print(A[N+1][M+1])
func()    