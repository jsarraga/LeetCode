
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

nums = [1,2,3,4]

def runningSum(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]  # 1, 3, 6, 10
    return nums


# If you continuously add the elements next to each other, when you get to the end
# you will have iterated through every element and have have found the sum of every one
# then just add it to the last element

# Time: O(n)
# Space 0(1)
