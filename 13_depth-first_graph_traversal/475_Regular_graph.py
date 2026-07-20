def regular_graph():
  n, m = map(int, input().split())
  g = [set() for _ in range(n)]
  for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a not in g[b]:
      g[b].add(a)
    if b not in g[a]:
      g[a].add(b)
  for i in range(1, n):
    if len(g[i]) != len(g[i-1]):
      return 'NO'
  return 'YES'
print(regular_graph())