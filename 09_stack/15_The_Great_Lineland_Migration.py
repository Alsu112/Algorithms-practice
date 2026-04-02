def great_lineland_migration():
  N = int(input())
  result = [-1] * N
  average_price_list = list(map(int, input().split()))
  price_stack = []
  for index, price in enumerate(average_price_list):
    if len(price_stack) == 0 or price >= price_stack[-1][0]:
      price_stack.append([price, index])
    else:
      while len(price_stack) != 0 and price_stack[-1][0] > price:
        ind = price_stack.pop()[1]
        result[ind] = index
      price_stack.append([price, index])
  print(*result)
great_lineland_migration()
