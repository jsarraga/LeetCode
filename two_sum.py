# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# brute force O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

class Solution:
    def TwoSum(self, nums: List[int], target: int) -> List[int]:
        # map complements
        hashmap = {}
        # iterate through indexes of nums
        for i in range(len(nums)):
            # calculate complement
            complement = target - nums[i] 
            if nums[i] in hashmap: 
                # if num is in the map, return it's index, and the current index being iterated
                return [hashmap[nums[i]], i] 
            else:
                # if the the number isn't in the map, store it's complement and index
                hashmap[complement] = i  
            