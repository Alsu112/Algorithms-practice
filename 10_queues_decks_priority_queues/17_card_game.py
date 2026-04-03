from collections import deque
def card_game():
    cards1 = list(map(int, input().split()))
    cards2 = list(map(int, input().split()))
    d1 = deque(cards1, maxlen=10)
    d2 = deque(cards2, maxlen=10)
    count = 0
    while count != 10 ** 6 and len(d1) != 0 and len(d2) != 0:
        elem1 = d1.popleft()
        elem2 = d2.popleft()
        if (elem1 > elem2 and not (elem1 == 9 and elem2 == 0)) or (elem1 == 0 and elem2 == 9):
            d1.append(elem1)
            d1.append(elem2)
        else:
            d2.append(elem1)
            d2.append(elem2)
        count += 1
    if len(d2) == 0:
        print('first', count)
    elif len(d1) == 0:
        print('second', count)
    else:
        print('botva')
card_game()