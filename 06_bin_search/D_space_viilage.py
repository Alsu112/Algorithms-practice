def space_village():
  n, a, b, w, h = map(int, input().split())
  def checkstickers(size, params):
    n, a, b, w, h = params
    return (w // (a + 2 * size)) * (h // (b + 2 * size)) >= n
  def rbinsearch(l, r, check, checkparams):
    while l < r:
      m = (l + r + 1) // 2
      if check(m, checkparams):
        l = m
      else:
        r = m - 1
    return l
  ans1 = rbinsearch(0, max(w, h), checkstickers, (n, a, b, w, h))
  ans2 = rbinsearch(0, max(w, h), checkstickers, (n, b, a, w, h))
  return max(ans1, ans2)
print(space_village())