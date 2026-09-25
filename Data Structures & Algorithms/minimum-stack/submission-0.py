class MinStack:

    def __init__(self):
        self.list_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.list_stack.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val,self.min_stack[-1]))


    def pop(self) -> None:
        self.list_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.list_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
