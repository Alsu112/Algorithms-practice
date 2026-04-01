def approx_bin_search():
  N, K = map(int, input().split())
  N_list = list(map(int, input().split()))
  K_list = list(map(int, input().split()))
  def check_is_right(index, params):
    seq, x = params
    return seq[index] <= x
  def check_is_left(index, params):
    seq, x = params
    return seq[index] >= x
  def lbin_search(l, r, check, checkparams):
    while l < r:
      m = (l + r) // 2
      if check(m, checkparams):
        r = m
      else:
        l = m + 1
    return l
  def rbin_search(l, r, check, checkparams):
    while l < r:
      m = (l + r + 1) // 2
      if check(m, checkparams):
        l = m
      else:
        r = m - 1
    return l
  for k in K_list:
    left_index = lbin_search(0, N - 1, check_is_left, (N_list, k))
    right_index = rbin_search(0, N - 1, check_is_right, (N_list, k))
    if abs(N_list[left_index] - k) < abs(N_list[right_index] - k):
      print(N_list[left_index])
    else:
      print(N_list[right_index])
approx_bin_search()