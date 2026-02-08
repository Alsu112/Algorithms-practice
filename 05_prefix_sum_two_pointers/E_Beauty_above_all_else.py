def beauty_above_all():
    N, K = map(int, input().split())
    trees_list = list(map(int, input().split()))
    k_dict = {}
    last = 0
    begin, end = 0, N
    for first in range(N):
        while last < N and len(k_dict) < K:
            if trees_list[last] not in k_dict:
                k_dict[trees_list[last]] = 1
            else:
                k_dict[trees_list[last]] += 1
            last += 1
        if len(k_dict) == K and end - begin > last - first:
            begin = first
            end = last
        if k_dict[trees_list[first]] == 1:
            del k_dict[trees_list[first]]
        else:
            k_dict[trees_list[first]] = k_dict[trees_list[first]] - 1
    print(begin + 1 , end)

beauty_above_all()