def nvp():
  N = int(input())
  A = list(map(int, input().split()))
  D = [0] * N
  for i in range(N):
    D[i] = 1
    for j in range(i):
      if A[i] > A[j]:
        D[i] = max(D[i], D[j] + 1)
  return max(D)
print(nvp())