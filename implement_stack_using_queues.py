# pretty straight forward answer here. Only thing is the boolean epmty() function

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        item = self.stack.pop()
        return item

    def top(self) -> int:
        """
        Get the top element.
        """
        item = self.stack[-1]
        return item

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()