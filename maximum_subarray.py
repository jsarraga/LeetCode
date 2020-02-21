def maxSubArray(self, nums: List[int]) -> int:
    # initialize sums to the first element
    curr_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # adding each element to curr_sum
        curr_sum += nums[i]
        # if element is higher than max sum and max sum is positive, it becomes max sum. also resets the substring sum (curr_sum)
        if nums[i] > max_sum and max_sum < 0:
            max_sum = nums[i]
            curr_sum = max_sum
        # if curr_sum is larger than max, it becomes max
        elif curr_sum > max_sum:
            max_sum = curr_sum
        # if curr_sum ever dips below 0, reset sum string. A negative number won't be the max_sum
        elif curr_sum < 0:
            curr_sum = 0     
    return max_sum