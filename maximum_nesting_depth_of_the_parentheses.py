# count the number of open parentheses
# decrease count if closed parentheses
# find max count of open parentheses

def maxDepth(s):
    count = 0
    mcount = 0
    for c in s:
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
        else:
            pass
        if count > mcount:
            mcount = count
    return mcount        





s = "(1+(2*3)+((8)/4))+1"