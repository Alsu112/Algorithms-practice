def dict_synonyms():
    N = int(input())
    dict_syn = {}
    for i in range(N):
        word1, word2 = input().split()
        if word1 not in dict_syn and word2 not in dict_syn:
            dict_syn[word1] = word2
            dict_syn[word2] = word1
    word = input()
    return dict_syn[word]

print(dict_synonyms())
#O(N) - Временная сложность
#O(N) - Пространственная сложность