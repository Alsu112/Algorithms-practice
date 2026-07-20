def func():
  n, k = map(int, input().split())
  k -= 1
  g = [[] for _ in range(n)]
  used = [-1] * n
  count = [-1] * n
  count_ = 0
  def dfs(used, g, v, count_):
    nonlocal count
    used[v] = 1
    count_ += 1
    count[v] = count_
    for to in g[v]:
      if used[to] != 1:
        dfs(used, g, to, count_)
  for i in range(n):
    list_str = list(map(int, input().split()))
    for j in range(n):
      if list_str[j] == 1:
        g[i].append(j)
        g[j].append(i)
  dfs(used, g, k, count_)
  ans = -1
  max_value = float('-inf')
  for i in range(n):
    if count[i] > max_value:
      max_value = count[i]
      ans = i
  if max_value == 0:
    print(k + 1)
  else:
    print(ans + 1)
func()