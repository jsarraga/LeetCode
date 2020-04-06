# Approach:
# use a stack. Iterate through, if last item in S is in stack, pop it


def removeDuplicate(S):
    stack = []

    for c in S:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)


    