def maximum_product_of_two_numbers():
    input_list = list(map(int, input().split()))

    if len(input_list) == 3:
        print(input_list[0], input_list[1], input_list[2])
        return 1

    max_1 = -10 ** 8
    max_2 = -10 ** 8
    max_3 = -10 ** 8
    min_1 = 10 ** 8
    min_2 = 10 ** 8
    min_3 = 10 ** 8

    for elem in input_list:
        if elem <= min_1:
            min_3 = min_2
            min_2 = min_1
            min_1 = elem
        elif elem <= min_2:
            min_3 = min_2
            min_2 = elem
        elif elem <= min_3:
            min_3 = elem
        if elem >= max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = elem
        elif elem >= max_2:
            max_3 = max_2
            max_2 = elem
        elif elem >= max_3:
            max_3 = elem

    if max_1 < 0:
        print(max_1, max_2, max_3)
        return 1

    if min_1 * min_2 >= max_3 * max_2:
        print(min_1, min_2, max_1)
    else:
        print(max_3, max_2, max_1)

    return 1


maximum_product_of_two_numbers()