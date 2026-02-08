def space_genom():
    genom_1 = input()  # N
    genom_2 = input()  # M
    set_2 = set()
    ans = 0

    for i in range(len(genom_2) - 1):
        set_2.add(genom_2[i:i + 2])

    for i in range(len(genom_1) - 1):
        if genom_1[i:i + 2] in set_2:
            ans += 1

    return ans


# O( N + M)
# O( N + M )
print(space_genom())