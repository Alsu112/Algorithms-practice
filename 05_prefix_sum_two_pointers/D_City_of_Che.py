def town_che():
  n, r = map(int, input().split())
  list_mountains = list(map(int, input().split()))
  count, last = 0, 0
  for first in range(len(list_mountains)):
    while last != len(list_mountains) and list_mountains[last] <= list_mountains[first] + r:
      last += 1
    count += len(list_mountains ) - last
  return count
print(town_che())