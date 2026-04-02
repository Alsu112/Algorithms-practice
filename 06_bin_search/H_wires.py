def wires():
  N, K = map(int, input().split())
  length = []
  max_length = float('-inf')
  for i in range(N):
    length.append(int(input()))
    max_length = max(max_length, length[i])
  def check(x, params):
    N, K, length = params
    count = 0
    for i in range(N):
      count += length[i] //x
    return count >= K
  def rbinsearch(l, r, check, checkparams):
    while l < r:
      m = (l + r + 1) // 2
      if check(m, checkparams):
        l = m
      else:
        r = m - 1
    return l
  return rbinsearch(0, max_length, check, (N, K, length))
print(wires())