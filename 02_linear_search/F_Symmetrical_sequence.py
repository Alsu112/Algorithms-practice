def symmetric_sequence():
    def is_palindrom(suffix):
        for i in range(len(suffix) // 2):
            if suffix[i] != suffix[len(suffix) - 1 - i]:
                return False
        return True

    N = int(input())
    list_input = list(map(int, input().split()))
    index = N - 1
    ans = N - 1

    for i in range(N):
        if is_palindrom(list_input[index:N]):
            ans = index
        index = index - 1

    print(ans)
    print(*list_input[:ans][::-1])


symmetric_sequence()