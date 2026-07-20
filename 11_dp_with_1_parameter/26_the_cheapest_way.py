def func():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        list_input = list(map(int, input().split()))
        A.append(list_input)
    D = [[0] * M] * N
    D[0][0] = A[0][0]
    for i in range(N):
        for j in range(M):
            if i == 0 and j != 0:
                D[i][j] = D[i][j - 1] + A[i][j]
            elif j == 0 and i != 0:
                D[i][j] = D[i - 1][j] + A[i][j]
            elif j != 0 and i != 0:
                D[i][j] = min(D[i][j - 1], D[i - 1][j]) + A[i][j]
    path = []
    i = N - 1
    j = M - 1
    while not (i == 0 and j == 0):
        if i == 0:
            path.append([i, j - 1])
            j = j - 1
        elif j == 0:
            path.append([i - 1, j])
            i = i - 1
        elif D[i - 1][j] < D[i][j - 1]:
            path.append([i - 1, j])
            i = i - 1
        else:
            path.append([i, j - 1])
            j = j - 1

    print(D[N - 1][M - 1])
    # print(path)


func()