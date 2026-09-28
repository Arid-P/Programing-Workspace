class Solution:
    def __init__(self):
        self.stack: list[int] = []
        self.min: int = float('inf')

    # Add an element to the top of Stack
    def push(self, x) -> None:
        self.stack.append(x)
        if len(self.stack) <= 1 :
            self.min = x
        elif self.min > x :
            self.min = x
        
        return

    # Remove the top element from the Stack
    def pop(self) -> None:
        if self.stack :
            poped: int = self.stack.pop(-1)
        
        if self.stack :
            if self.min == poped :
                self.min = min(self.stack)
        return
        

    # Returns top element of Stack
    def peek(self) -> int:
        if self.stack :
            return self.stack[-1]
        else :
            return -1

    # Finds minimum element of Stack
    def getMin(self):
        if self.stack :
            return self.min
        else :
            return -1

