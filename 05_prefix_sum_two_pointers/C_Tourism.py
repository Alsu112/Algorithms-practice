def tourism():
  def make_prefix_sum(nums):
    prefix_sum_positive = [0] * (len(nums) + 1)
    prefix_sum_negative = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
      if nums[i - 1] >= 0:
        prefix_sum_positive[i] = prefix_sum_positive[i - 1] + nums[i - 1]
        prefix_sum_negative[i] = prefix_sum_negative[i - 1]
      else:
        prefix_sum_negative[i] = prefix_sum_negative[i - 1] + nums[i - 1]
        prefix_sum_positive[i] = prefix_sum_positive[i - 1]
    return prefix_sum_positive, prefix_sum_negative
  N = int(input())
  delta = []
  value = 0
  for i in range(N):
    x, y = map(int, input().split())
    if i >= 1:
      delta.append(y - value)
    else:
      delta.append(0)
    value = y
  prefix_sum_positive, prefix_sum_negative = make_prefix_sum(delta)
  M = int(input())
  for i in range(M):
    s, f = map(int, input().split())
    positive_high = abs(prefix_sum_positive[f] - prefix_sum_positive[s] )
    negative_high = abs(prefix_sum_negative[f] - prefix_sum_negative[s] )
    if f >= s:
      print(positive_high)
    else:
      print(negative_high)
tourism()