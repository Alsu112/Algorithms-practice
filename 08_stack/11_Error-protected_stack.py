class Stack:
    def __init__(self, capacity=100):
        self.stack = [0] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, n):
        if self.top + 1 >= self.capacity:
            print("error")
        else:
            self.top += 1
            self.stack[self.top] = n
            print("ok")

    def pop(self):
        if self.top == -1:
            print("error")
        else:
            value = self.stack[self.top]
            self.top -= 1
            self.stack[self.top + 1] = 0
            print(value)

    def back(self):
        if self.top == -1:
            print("error")
        else:
            print(self.stack[self.top])

    def size(self):
        print(self.top + 1)

    def clear(self):
        self.top = -1
        for i in range(self.capacity):
            self.stack[i] = 0
        print("ok")


def main():
    stack = Stack()

    while True:
        command = input().strip().split()

        if command[0] == "push":
            stack.push(int(command[1]))

        elif command[0] == "pop":
            stack.pop()

        elif command[0] == "back":
            stack.back()

        elif command[0] == "size":
            stack.size()

        elif command[0] == "clear":
            stack.clear()

        elif command[0] == "exit":
            print("bye")
            break


if __name__ == "__main__":
    main()