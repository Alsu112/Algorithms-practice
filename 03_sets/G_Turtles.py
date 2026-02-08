def turtle():
    N = int(input())
    set_N = set()

    for i in range(N):
        n_before, n_after = map(int, input().split())
        if n_before + n_after + 1 == N and n_before >= 0 and n_after >= 0:
            set_N.add(n_before + 1)

    return len(set_N)


print(turtle())

# O(N)
# O(N)