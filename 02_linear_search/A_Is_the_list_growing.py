def is_ascending_list():
    input_list = list(map(int, input().split()))
    elem = input_list[0]
    for i in range(1, len(input_list)): # O(n)
        if input_list[i] <= elem:
            return 'NO'
        elem = input_list[i] #Доступ за O(1), так как мгновенно вычисляет адрес нужной ячейки по формуле: адрес_начала_списка + i * размер_указателя.
    return 'YES'
#Временная сложность O(n)
#Сложность по памяти, если не считать входные данные O(1)
#Чтобы оптимизировать память входных данных, можно не создавать list, а пройти по итератеру с помощью next
print(is_ascending_list())