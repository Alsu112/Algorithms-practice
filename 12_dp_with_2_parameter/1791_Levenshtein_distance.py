def edit_distance():
    def diff(a, b):
        if a == b:
            return 0
        else:
            return 1

    word1 = input()
    word2 = input()
    n = len(word1)
    m = len(word2)

    D = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
    D[0][0] = 0

    for i in range(1, n + 1):
        D[i][0] = i

    for j in range(1, m + 1):
        D[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = diff(word1[i - 1], word2[j - 1])
            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + c
            )

    print(D[n][m])

edit_distance()