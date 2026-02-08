def open_calculator():
    xyz = set(map(int, input().split()))
    number = int(input())
    digits_set = set()

    if number == 0:
        digits_set.add(0)
    else:
        temp = number
        while temp:
            digit = temp % 10
            digits_set.add(digit)
            temp = temp // 10

    missing_digits = digits_set.difference(xyz)
    print(len(missing_digits))


open_calculator()
# O(d) - где d - кол-во цифр в числе. Временная сложность
# O(1) - множество максимум длины 10