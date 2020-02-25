def moveZeroes(nums):
        # tracks position of "0"
        # we're going to move all non-zeroes to the left of this position
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # swaps positions of i and position of zero
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                
nums = [0,1,0,3,2]
print(moveZeroes(nums))