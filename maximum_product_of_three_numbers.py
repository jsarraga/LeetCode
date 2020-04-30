# APPROACH:
# sort the array in ascending order, and multiply the last three (largest) elements
# HOWEVER, if there are negative numbers in the array, we'll need to multiply the first two (smallest) 
# elements because a negative * negative = positive --> example [-4, -3, -1, 0, 1, 10]
# so we'll multiply the two smallest negative numbers and the largest positive (-4 * -3 * 10)
# to get the largest product




def maximumProduct(nums):
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])