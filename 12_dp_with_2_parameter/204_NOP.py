def greatest_common():
  N = int(input())
  first_seq = list(map(int, input().split()))
  M = int(input())
  second_seq = list(map(int, input().split()))
  D = [[0] * (M) for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if first_seq[i] == second_seq[j]:
        if i != 0 and j != 0:
          D[i][j] = D[i - 1][j - 1] + 1
        else:
          D[i][j] = 1
      else:
        if j == 0 and i != 0:
          D[i][j] = D[i - 1][j]
        elif j != 0 and i == 0:
          D[i][j] = D[i][j - 1]
        else:
          D[i][j] = max(D[i][j - 1], D[i - 1][j])
  return D[N - 1][M - 1]
print(greatest_common())