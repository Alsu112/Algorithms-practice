def improving_academic_perfomance():
  a = int(input())
  b = int(input())
  c = int(input())
  def check(x, params):
    a, b, c = params
    return (2 * a + 3 * b + 4 * c + 5 * x) >= 3.5 * (a + b + c + x)
  def lbinsearch(l, r, check, checkparams):
    while l < r:
      m = (l + r) // 2
      if check(m, checkparams):
        r = m
      else:
        l = m + 1
    return l
  return lbinsearch(0, 2 * (a + b + c) , check, (a, b, c))
print(improving_academic_perfomance())