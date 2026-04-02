def points_and_segments():
    n, m = map(int, input().split())
    events = []
    for i in range(n):
        a, b = map(int, input().split())
        events.append((min(a, b), -1))
        events.append((max(a, b), 1))
    list_points = list(map(int, input().split()))
    points_count = {}
    for point in list_points:
        events.append((point, 0))
        points_count[point] = 0
    events.sort()
    count = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            count += 1
        elif events[i][1] == 1:
            count -= 1
        else:
            points_count[events[i][0]] = count
    ans = []
    for point in list_points:
        ans.append(points_count[point])
    print(*ans)
points_and_segments()
