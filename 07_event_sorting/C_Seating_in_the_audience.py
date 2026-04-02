from collections import deque
def func():
  N, D = map(int, input().split())
  X_list = list(map(int, input().split()))
  X = [(x, i) for i, x in enumerate(X_list)]
  X.sort()
  first = 0
  second = 0
  i = 1
  re_i = 1
  dq = deque()
  dq_free = deque()
  variants = [0] * len(X_list)
  while first < len(X_list):
    while second < len(X_list) and abs(X[first][0] - X[second][0]) <= D:
      if len(dq_free) == 0:
        dq.append(i)
        variants[second] = i
        i += 1
      else:
        re_i = dq_free.popleft()
        dq.append(re_i)
        variants[second] = re_i
      second += 1
    dq_free.append(dq.popleft())
    first += 1
  ans = []
  for i in range(len(X)):
    ans.append((X[i][1], variants[i]))
  ans.sort()
  anss = [0] * len(X_list)
  for i in range(len(ans)):
    anss[i] = ans[i][1]
  print(len(set(anss)))
  print(*anss)

func()
