def sum_numbers():
  def make_prefix_sum(nums):
    prefix_sum = [0] * (N + 1)
    for j in range(1, N + 1):
      prefix_sum[j] = prefix_sum[j-1 ] + nums[j - 1]
    return prefix_sum
  N, K = map(int, input().split())
  car_numbers = list(map(int, input().split()))
  count = 0
  sum_set = set()
  prefix_sum = make_prefix_sum(car_numbers)
  for j in range(0, N + 1):
    if prefix_sum[j] + K not in sum_set:
      sum_set.add(prefix_sum[j] + K)
    if prefix_sum[j] in sum_set:
      count += 1
  return count

print(sum_numbers())