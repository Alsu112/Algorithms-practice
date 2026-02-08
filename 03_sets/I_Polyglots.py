def poliglots():
    N = int(input())
    languages = set()
    languages_all = set()

    for i in range(N):
        M = int(input())
        languages_curr = set()

        for j in range(M):
            language = input()
            languages_curr.add(language)
            if i == 0:
                languages.add(language)

        if i != 0:
            languages = languages.intersection(languages_curr)  # O(M)

        languages_all = languages_all.union(languages_curr)  # O(MN)

    print(len(languages))
    for item in languages:
        print(item)

    print(len(languages_all))
    for item in languages_all:
        print(item)


poliglots()
# O(MN**2) по времени
# O(MN) по памяти