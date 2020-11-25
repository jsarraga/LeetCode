'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
'''

nums = [1,2,3,1,1,3]

def numIdenticalPairs(nums):
    h = {}
    count = 0
    for i in nums:
        if i in h:
            count += h[i]
            h[i] += 1
        else:
            h[i] = 1
    return count

numIdenticalPairs(nums)