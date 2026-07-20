def complete_graph():
  n, m = map(int, input().split())
  g = [set() for _ in range(n)]
  for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a not in g[b] and a != b:
      g[b].add(a)
    if b not in g[a] and b != a:
      g[a].add(b)
  for i in range(n):
    if len(g[i]) != n - 1:
      return 'NO'
  return 'YES'
print(complete_graph())