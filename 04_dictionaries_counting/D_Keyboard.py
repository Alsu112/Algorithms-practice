def keyboard():
    n = int(input())
    max_number_of_clicks = list(map(int, input().split()))
    k = int(input())
    sequence_of_clicks = list(map(int, input().split()))

    for i in range(k):
        max_number_of_clicks[sequence_of_clicks[i] - 1] -= 1

    for i in range(n):
        if max_number_of_clicks[i] < 0:
            print('YES')
        else:
            print('NO')


keyboard()
# O(k+n)  - по времени
# O(n + k) - по памяти