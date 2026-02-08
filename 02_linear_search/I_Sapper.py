def saper():
    N, M, K = map(int, input().split())
    matrix = [['0' for _ in range(M)] for _ in range(N)]

    for i in range(K):
        n, m = map(int, input().split())
        matrix[n - 1][m - 1] = '*'

    for i in range(N):
        for j in range(M):
            if matrix[i][j] != '*':
                sum = 0
                for ii in range(max(0, i - 1), min(N, i + 2)):
                    for jj in range(max(0, j - 1), min(M, j + 2)):
                        if matrix[ii][jj] == '*':
                            sum += 1
                matrix[i][j] = str(sum)

    for i in range(N):
        print(*matrix[i])


saper()
