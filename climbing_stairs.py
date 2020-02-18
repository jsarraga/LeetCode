# question is similar to fibonacci where the solution is equal to the sum of the two previous numbers

def climbingStairs(n):
    # account for base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    # make a dictionary to store the n's. Need to populate with starter numbers in order to calculate for n=3
    mydict = {1:1, 2:2}

    for i in range(3, n + 1):
        # the value of n in the dictionary {n:?} equals the value of the two previous n's
        current = mydict[i-1] + mydict[i-2]
        mydict[i] = current
        print(mydict)
    
    return mydict[n]



n = 5

print(climbingStairs(n))