class MinStack:
  def __init__(self ):
    self.stack = []
    self.min_stack = []

  def push(self, val):
    self.stack.append(val)
    if len(self.stack) == 1 or val <= self.min_stack[-1]:
      self.min_stack.append(val)

  def pop(self ):
    if len(self.stack) == 0:
      raise Exception("Empty stack")
    elem = self.stack.pop()
    if elem == self.min_stack[-1]:
      self.min_stack.pop()
    return elem

  def top(self ):
    if len(self.stack) == 0:
      raise Exception("Empty stack")
    return self.stack[-1]

  def getMin(self):
    if len(self.stack) == 0:
      raise Exception("Empty stack")
    return self.min_stack[-1]

My_MinStack = MinStack()
My_MinStack.push(3)
My_MinStack.push(2)
My_MinStack.push(8)
My_MinStack.push(2)
print(My_MinStack.pop())
print(My_MinStack.getMin())
print(My_MinStack.top())
print(My_MinStack.pop())
print(My_MinStack.pop())
print(My_MinStack.pop())
print(My_MinStack.pop())