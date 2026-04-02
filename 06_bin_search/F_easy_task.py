def easy_task():
  N, x, y = map(int, input().split())
  def check(t, params):
    N, x, y = params
    return t//x + (t - x)//y >= N
  def lbinsearch(l, r, check, checkparams):
    while l < r:
      m = (l + r) //2
      if check(m, checkparams):
        r = m
      else:
        l = m + 1
    return l
  return lbinsearch(0, max(x, y) * N, check, (N, min(x, y), max(x, y)))
print(easy_task())