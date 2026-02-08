def count_diff_numbers():
    input_set_1 = set(map(int, input().split()))
    input_set_2 = set(map(int, input().split()))
    ans = set()
    for elem in input_set_1:
        if elem in input_set_2:
            ans.add(elem)
    print(*sorted(ans))

count_diff_numbers()
#O(nlogn) - временная сложность
#O(n) - пространственная сложность