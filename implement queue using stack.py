class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        stack2 = []
        for i in range(len(self.stack) - 1):
            stack2.append(self.stack.pop())
        p = self.stack.pop()
        for i in range(len(stack2)):
            self.stack.append(stack2.pop())
        return p

    def peek(self):
        stack2 = []
        for i in range(len(self.stack) - 1):
            stack2.append(self.stack.pop())
        p = self.stack[-1]
        for i in range(len(stack2)):
            self.stack.append(stack2.pop())
        return p

    def empty(self):
        return len(self.stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()