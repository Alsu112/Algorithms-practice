def control_of_blows():
    N = int(input())
    dictionary = {}
    for i in range(N):
        word = input()
        dictionary[word] = sum(1 for char in word if char.isupper())
        dictionary[word.lower()] = 0
    phrase = list(input().split())
    ans = 0
    for word in phrase:
        if word.lower() not in dictionary and sum(1 for char in word if char.isupper()) != 1:
            ans += 1
        elif word.lower() in dictionary and (word not in dictionary or sum(1 for char in word if char.isupper()) == 0):
            ans += 1
    return ans

print(control_of_blows())
#O(L) по времени
#O(L) по памяти 