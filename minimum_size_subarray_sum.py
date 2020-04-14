# Approach:

# use two pointers: left and right. total up the entire array, then while the total > s
# move the left pointer to the right until total < s, then return the min 


def minSubArrayLen(s, nums) -> int:
    total = 0
    left = 0
    result = len(nums) + 1

    # use enumerate becuase we'll use the indexes to calculate the min length
    for right, n in enumerate(nums):
        # add all elements in the array
        total += n
        # while the total is larger than s, we'll subtract theleft elements 
        # and keep sliding the left pointer until total is less than s
        while total >= s:
            # need the min of len(nums) and the right and left pointers +1 (sub array)
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    
    return result if result <= len(nums) else 0


s = 11
nums = [1,2,3,4,5]

minSubArrayLen(s, nums)