# 1. Get the sum of numbers which is total = n*(n+1)/2 --> Gauss' formula
# 2. Subtract all the numbers from sum and you will get the missing number

def missingNumber(nums):
    n = len(nums)
    total = n*(n+1) / 2
    return total - sum(nums)

