class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min = val
        elif val < self.min:
            self.stack.append(2 * val - self.min)
            self.min = val
        else:
            self.stack.append(val)

    def pop(self):
        x = self.stack.pop()

        if x < self.min:
            self.min = 2 * self.min - x

    def top(self):
        x = self.stack[-1]

        if x < self.min:
            return self.min

        return x

    def getMin(self):
        return self.min