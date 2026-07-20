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
                D[i][j] = max(D[i][j - 1], D[i - 1][j]) + A[i][j]
    i = N - 1
    j = M - 1
    print(D[N - 1][M - 1])


func()