# 1. Get the sum of numbers which is total = n*(n+1)/2 --> Gauss' formula
# 2. Subtract all the numbers from sum and you will get the missing number

def missingNumber(nums):
    # Gauss' formula approach
    n = len(nums)
    total = n*(n+1) / 2
    return total - sum(nums)

def missingNumber1(nums):
    # sorting approach
    nums.sort()
    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i-1] + 1
        if nums[i] != expected_num:
            return expected_num