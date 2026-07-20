def func():
    def relax(graph, dist, vertex, path):
        for i in range(len(graph[vertex])):
            next_vertex = graph[vertex][i][0]
            d = graph[vertex][i][1]
            if dist[vertex] + d < dist[next_vertex]:
                dist[next_vertex] = dist[vertex] + d
                path[next_vertex] = vertex

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
    path = [-2] * n
    used = [0] * n

    used[start] = 1
    dist[start] = 0
    path[start] = -1

    ans = []

    relax(g, dist, start, path)  # записываем расстояния от стартовой вершины в массив до всех ее соседей

    while True:
        min_dist = float('inf')
        new_vertex = -1

        for i in range(n):
            if used[i] == 0 and dist[i] < min_dist:  # находим ближайшую необработанную вершину
                min_dist = dist[i]
                new_vertex = i

        if new_vertex == -1:  # если больше нет достижимых вершин, выходим
            break

        relax(g, dist, new_vertex, path)  # обновляем расстояния до соседей
        used[new_vertex] = 1

    last_vertex = finish

    if dist[finish] == float('inf'):
        print(-1)
    else:
        while last_vertex != start:
            ans.append(last_vertex + 1)
            last_vertex = path[last_vertex]

        ans.append(start + 1)
        print(*ans[::-1])


func()