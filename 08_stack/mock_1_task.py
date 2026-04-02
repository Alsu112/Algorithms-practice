def bracket_life():
  s = input()
  stack_ = []
  ans = []
  for ind, l in enumerate(s):
    if l == '(':
      stack_.append([l, ind])
    else:
      elem = stack_.pop()
      ans.append([elem[1], ind, len(stack_) + 1, ind - elem[1]])
  return ans
bracket_life()