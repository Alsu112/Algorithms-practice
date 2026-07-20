def nvp2():
  N = int(input())
  A = list(map(int, input().split()))
  D = [0] * N
  for i in range(N):
    D[i] = 1
    for j in range(i):
      if A[i] > A[j]:
        D[i] = max(D[i], D[j] + 1)
  max_value = float('-inf')
  for i in range(N):
    if D[i] > max_value:
      max_value = D[i]
  ans = []
  curr = max_value
  for i in range(N- 1, - 1, -1):
    if D[i] == curr:
      ans.append(A[i])
      curr = curr - 1
  print(*ans[::-1])
nvp2()