def connectivity_components():
  def dfs(used, g, v, count, ans_i ):
    used[v] = count
    ans_i.add(v + 1)
    for to in g[v]:
      if used[to] == 0:
        dfs(used , g, to, count, ans_i)
    return ans_i
  N = int(input())
  g = [[] for _ in range(N)]
  used = [0] * N
  ans = []
  for i in range(N):
    list_str = list(map(int, input().split()))
    for j in range(N):
      if list_str[j] == 1:
        g[i].append(j)
  count = 0
  for i in range(N):
    if used[i] == 0:
      count += 1
      ans_i = set()
      ans.append(dfs(used , g, i, count, ans_i))
  print(count)
  for i in range(count):
    print(len(ans[i]))
    print(*ans[i])
connectivity_components()