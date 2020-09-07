class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
            return
        curr_min = self.stack[-1][1]
        self.stack.append((x, min(curr_min, x)))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()