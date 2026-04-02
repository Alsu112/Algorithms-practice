def student_supervision():
  N, M = map(int, input().split())
  events = []
  online = 0
  notemptytime = 0
  set_one_point = set()
  for i in range(M):
    a, b = map(int, input().split())
    events.append((a, -1))
    events.append((b + 1, 1))
  events.sort()
  for i in range(len(events)):
    if online > 0:
      notemptytime += events[i][0] - events[i-1][0]
    if events[i][1] == -1:
      online += 1
    else:
      online -= 1
  return N - notemptytime
print(student_supervision())