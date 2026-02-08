def conditioners():
    n = int(input())
    A_list = list(map(int, input().split()))
    m = int(input())

    MAX_POWER = 1000
    min_price_for_power = [float('inf')] * (MAX_POWER + 1)

    for _ in range(m):
        power, price = map(int, input().split())
        min_price_for_power[power] = min(min_price_for_power[power], price)

    for power in range(MAX_POWER - 1, 0, -1):
        min_price_for_power[power] = min(min_price_for_power[power], min_price_for_power[power + 1])

    total = 0
    for required in A_list:
        total += min_price_for_power[required]

    return total