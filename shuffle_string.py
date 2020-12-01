def restoreString(s,indices):
    # make a list of elements = len(s)
    res = [0] * len(s)
    j = 0
    # match up indices array with s. 
    # It will assign the index of it using indices to res
    # "c" will be the 4th element in result, "o" will be the 5th element in result, etc.
    for i in indices:
        res[i] = s[j]
        # move the pointer (j) up after every iteration
        j += 1
    # join the list, it will already be in order
    return ''.join(res)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
restoreString(s,indices)