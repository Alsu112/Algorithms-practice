def Merry_Mullein():
    N = int(input())
    input_list = list(map(int, input().split()))
    max_1 = -1
    for elem in input_list:
        if elem > max_1:
            max_1 = elem
    ans = -1
    place_number = 0
    max_was_before = False
    for i in range(1, len(input_list) - 1):
        if input_list[i - 1] == max_1 or input_list[0] == max_1:
            max_was_before = True
        if input_list[i] % 10 == 5 and max_was_before == True and input_list[i] > input_list[i + 1] and ans < \
                input_list[i]:
            ans = input_list[i]
    if ans == -1:
        return 0
    for elem in input_list:
        if elem > ans:
            place_number += 1
    return place_number + 1


print(Merry_Mullein())
