# APPROACH: three pointers. triple nested loop. last layer of iterations contingent on if
# the first two layers meet the criteria

def countGoodTriplets(arr, a, b, c):
    counter = 0
    # top level iteration from [beginning:k]. so we range(len(arr)-2)
    for i in range(len(arr)-2):
        # second level: from 1 element in front of i to k. 
        for j in range(i+1, len(arr)-1):
            # First level of logic at this level. If true, move on to next level
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j+1, len(arr)):
                    # last logic check on lowest level 
                    if abs(arr[i] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        counter += 1
    return counter



arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3  
print(countGoodTriplets(arr, a,b,c))