class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min = val

        else:
            if val < self.min:
                self.stack.append(2 * val - self.min)
                self.min = val
            else:
                self.stack.append(val)

    def pop(self):
        value = self.stack.pop()

        if value < self.min:
            self.min = 2 * self.min - value

    def top(self):
        value = self.stack[-1]

        if value < self.min:
            return self.min
        else:
            return value

    def getMin(self):
        return self.min