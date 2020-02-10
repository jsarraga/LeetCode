def isValid(s):
        # create empty stack
        stack = []
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                # if we didn't get any lefts before reaching a right, return false
                if len(stack) == 0:
                    return False
                # if parentheses we get is not the same type with the last element in the list
                if right.index(i) != left.index(stack.pop()):
                    return False
        return not stack


s = "([)]"

print(isValid(s))