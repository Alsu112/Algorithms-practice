def count_diff_numbers():
    input_set = set(map(int, input().split()))
    return len(input_set)

print(count_diff_numbers())
# По памяти O(n)
# По времени O(n)