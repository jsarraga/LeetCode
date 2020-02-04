class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0  # start counter
        
        for i in nums:  # iterate through nums, a list of integers
            if len(str(i)) % 2 == 0: # convert i to str to find len, if len is even, add to counter
                counter += 1
        return counter 