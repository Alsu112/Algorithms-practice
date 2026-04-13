from collections import deque


def task1(deq):
  ans = []
  while len(deq) != 0:
    ans.append(deq.popleft())
    if len(deq) != 0:
      ans.append(deq.pop())
  return ans

print(task1(deque([1])))