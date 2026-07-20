def func():
  def dfs(used, g, v):
    used[v] = 1
    for to in g[v]:
      if used[to] != 1:
        dfs(used , g, to)
  N, S = map(int, input().split())
  g = [[] for _ in range(N)]
  used = [0] * N
  for i in range(N):
    list_str = list(map(int, input().split()))
    for j in range(N):
      if list_str[j] == 1:
        g[i].append(j)
        g[j].append(i)
  count = 0
  dfs(used, g, S - 1)
  for i in range(N):
    if used[i] == 1:
      count += 1
  return count
print(func())