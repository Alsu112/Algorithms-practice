def func():
    def relax(graph, dist, vertex):
        for i in range(len(graph[vertex])):
            next_vertex = graph[vertex][i][0]
            d = graph[vertex][i][1]
            if dist[vertex] + d < dist[next_vertex]:
                dist[next_vertex] = dist[vertex] + d

    n, s, f = map(int, input().split())
    g = [[] for _ in range(n)]

    for i in range(n):
        list_str = list(map(int, input().split()))
        for j in range(n):
            if list_str[j] >= 0:
                g[i].append((j, list_str[j]))
                # g[j].append((i, list_str[j]))

    start = s - 1
    finish = f - 1

    dist = [float('inf')] * n
    used = [0] * n
    used[start] = 1
    dist[start] = 0

    relax(g, dist, start)

    while True:
        min_dist = float('inf')
        new_vertex = -1

        for i in range(n):
            if used[i] == 0 and dist[i] < min_dist:
                min_dist = dist[i]
                new_vertex = i

        if new_vertex == -1:
            break

        relax(g, dist, new_vertex)
        used[new_vertex] = 1

    if dist[finish] == float('inf'):
        return -1
    else:
        return dist[finish]


print(func())