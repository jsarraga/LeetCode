# Approach:
# we know that if S[0] == "I", then the list will start with 0
# if S[0] == "D", the list will start with N
# the answer is a list, so we'll just append low, or high depending on the character in the string
# return the answer



def diStringMatch(S):
    low = 0
    high = len(S)
    answer = []

    for x in S:
        if x == "I":
            answer.append(low)
            low += 1
        else:
            answer.append(high)
            high -= 1
    
    return answer + [low]

