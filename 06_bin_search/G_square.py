def square():
  n = int(input())
  m = int(input())
  t = int(input())
  def check(x, params):
    n, m, t = params
    return n*m - (n - 2 * x)*(m - 2*x) <= t
  def rbinsearch(l, r, check, checkparams):
    while l < r:
      m = (l + r + 1) // 2
      if check(m, checkparams):
        l = m
      else:
        r = m - 1
    return l
  return rbinsearch(0, min(n, m)//2, check, (n, m, t))
print(square())