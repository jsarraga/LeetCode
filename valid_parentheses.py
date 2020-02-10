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

# OPTIMIZED
def optimalIsValid(s):
        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char =="{":
                stack.append(char)
                continue
            
            if len(stack) == 0:
                return False
            
            if char == ")":
                prev = stack.pop()
                if prev == "{" or prev == "[":
                    return False
            
            if char == "]":
                prev = stack.pop()
                if prev == "(" or prev == "{":
                    return False
            
            if char == "}":
                prev = stack.pop()
                if prev == "(" or prev == "[":
                    return False
        
        if len(stack) == 0:
            return True
        else: 
            return False
            


s = "([)]"

print(isValid(s))