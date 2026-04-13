from collections import deque


class CircularBuffer:
    def __init__(self, N):
        self.size = N
        self.head = 0
        self.tail = -1
        self.buffer = deque()

    def append(self, value):
        if self.tail == self.size - 1:
            self.buffer.popleft()
        else:
            self.tail += 1
        self.buffer.append(value)

    def get(self):
        ans = self.buffer.copy()
        return ans


buf = CircularBuffer(2)
buf.append(1)
print(buf.get())
buf.append(2)
print(buf.get())
buf.append(3)
print(buf.get())
buf.append(4)
print(buf.get())