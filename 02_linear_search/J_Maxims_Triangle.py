def triangle_Maxim():
    N = int(input())
    left = 30
    right = 4000
    first_number = float(input())

    for i in range(N - 1):
        line = input().split()
        second_number = float(line[0])
        mark = line[1]
        center = (first_number + second_number) * 0.5

        if mark == 'closer':
            if second_number > first_number:
                left = max(left, center)
            else:
                right = min(right, center)
        else:  # mark == 'further'
            if second_number > first_number:
                right = min(right, center)
            else:
                left = max(left, center)

        first_number = second_number

    print(float(left), float(right))


triangle_Maxim()