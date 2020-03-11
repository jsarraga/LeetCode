class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # set to intinity to start
        self.minVal = float("inf")

    # push element to stack
    # if element is less than minVal, update minVal
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.minVal:
            self.minVal = x
            
    # helper function finds the new min value after popping off an element        
    def updateMin(self):
        newMin = float("inf")
        for item in self.stack:
            if item < newMin:
                newMin = item
        self.minVal = newMin
        
    # pops last element. then updates minVal
    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.minVal:
            # helper function finds the new minVal of the stack after it's popped
            # and updates minVal
            self.updateMin()
        return item
    
    # returns the last element of the stack
    def top(self) -> int:
        return self.stack[-1]
        
    # returns the minVal
    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()