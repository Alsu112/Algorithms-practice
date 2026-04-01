def diplomas():
  w, h, n = map(int, input().split())
  def check_stickers(size, params):
    n, w, h = params
    return (size // w) * (size // h) >= n
  def lbinsearch(l, r, check, checkparams):
    while l < r:
      m = (l + r)//2
      if check(m, checkparams):
        r = m
      else:
        l = m + 1
    return l
  ans = lbinsearch(0, max(w, h) * n, check_stickers, (n, w, h))
  return ans
print(diplomas())