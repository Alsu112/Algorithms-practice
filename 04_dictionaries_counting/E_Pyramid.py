def pyramid():
    N = int(input())
    dict_pyramid = {}
    ans = 0
    for i in range(N):
        w, h = map(int, input().split())
        if w not in dict_pyramid:
            dict_pyramid[w] = h
        else:
            dict_pyramid[w] = max(dict_pyramid[w], h)  # Исправил dict на dict_pyramid
    for w in dict_pyramid:
        ans += dict_pyramid[w]
    return ans

print(pyramid())

#O(N) по времени
#O(N) по памяти