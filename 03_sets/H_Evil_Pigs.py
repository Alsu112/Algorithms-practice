def angry_birds():
    N = int(input())
    set_x = set()
    ans = 0

    for i in range(N):
        x, y = map(int, input().split())
        if x not in set_x and x != 0:
            set_x.add(x)
        if x == 0:
            ans += 1

    return ans + len(set_x)


print(angry_birds())
# O(N)
# O(N)