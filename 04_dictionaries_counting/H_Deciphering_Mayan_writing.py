import math

def Mayan_writing():
    g, len_S = map(int, input().split())
    W = input()
    S = input()
    dict_W = {}
    ans = 0
    for letter in W:
        if letter not in dict_W:
            dict_W[letter] = 1
        else:
            dict_W[letter] += 1
    word = S[0: g]
    dict_word = {}
    for letter in word:
        if letter not in dict_word:
            dict_word[letter] = 1
        else:
            dict_word[letter] += 1
    if dict_word == dict_W:
        ans += 1
    for index in range(1, len_S - g + 1):
        dict_word[S[index - 1]] -= 1
        if S[index + g - 1] not in dict_word:
            dict_word[S[index + g - 1]] = 1
        else:
            dict_word[S[index + g - 1]] += 1
        if dict_word[S[index - 1]] == 0:
            del dict_word[S[index - 1]]
        if dict_word == dict_W:
            ans += 1
    print(ans)

Mayan_writing()
#O(len_S * g) по времени
#O(len_S + g) по памяти