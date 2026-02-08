def word_occurrence_number():
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()
    dict_words = {}
    ans = []
    for word in words:
        if word not in dict_words:
            dict_words[word] = 1
            ans.append(0)
        else:
            ans.append(dict_words[word])
            dict_words[word] += 1
    print(*ans)

word_occurrence_number()
#O(N) - Временная сложность
#O(N) - Пространственная сложность