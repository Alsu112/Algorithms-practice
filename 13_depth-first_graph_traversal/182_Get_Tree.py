def func():
    ans = set()
    def dfs(used, g,  v):
        nonlocal ans
        used[v] = 1
        for to in g[v]:
            if used[to] == 0:
              ans.add((v + 1, to + 1))
              dfs(used, g, to)


    N, M = map(int, input().split())

    g = [[] for _ in range(N)]
    used = [0] * N
    p = [-1] * N

    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    dfs(used, g, 0)
    for pair in ans:
      print(*pair)
func()