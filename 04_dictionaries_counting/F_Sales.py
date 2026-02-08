import sys


def sales():
    dict_ = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        buyer, item, quantity = line.split()
        quantity = int(quantity)

        if buyer not in dict_:
            dict_[buyer] = {item: quantity}
        else:
            if item not in dict_[buyer]:
                # Ошибка: здесь dict_[buyer][item] еще не существует
                # Нужно просто присвоить значение
                dict_[buyer][item] = quantity
            else:
                dict_[buyer][item] += quantity

    # Сортируем покупателей по алфавиту
    for buyer in sorted(dict_.keys()):
        print(buyer + ':')
        # Сортируем товары по алфавиту
        for item in sorted(dict_[buyer].keys()):
            print(item, dict_[buyer][item])


sales()
# O(NlogN) по времени
# O(N) по памяти