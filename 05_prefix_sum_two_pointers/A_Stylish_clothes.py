def stylish_clothes():
  N = int(input())
  tshirts_colours = list(map(int, input().split()))
  M = int(input())
  trousers_colours = list(map(int, input().split()))
  delta, first1, first2 = float('inf'), 0, 0
  for k in range(N + M):
    if abs(tshirts_colours[first1] - trousers_colours[first2]) < delta:
      delta = abs(tshirts_colours[first1] - trousers_colours[first2])
      ans = (tshirts_colours[first1], trousers_colours[first2] )
    if tshirts_colours[first1] < trousers_colours[first2] and first1 != N - 1 :
      first1 += 1
    elif first2 != M - 1:
      first2 += 1
  return ans

print(*stylish_clothes())