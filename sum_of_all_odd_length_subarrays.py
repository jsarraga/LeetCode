"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

 

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
"""

#APPROACH: have two pointers. One iterating through arr. One iterating through arr by odd increments

def sumOddLengthSubarrays(arr):
    # make an array of odd numbers within arr -> [1 ,3, 5]
    odds = [i for i in range(len(arr)+1) if i % 2 != 0]
    # establish a counter
    result = 0
    # iterate through from ptr1 to ptr2. ptr 2 incrementing by elements in odds array
    for i in odds:
        beg = 0
        end = i
        # while loop that stops when end is out of index range
        while end <= len(arr):
            # sum subarray from ptr1 to ptr 2
            result += sum(arr[beg:end])
            # move pointers up
            beg += 1
            end += 1
    return result

# APPROACH: two pointers, nested in for loop.
def sumOddLengthSubarrays1(arr):
        result = 0
        for i in range(len(arr)):
            # ptr j incrememnted by two (odds)
            for j in range(i, len(arr), 2):
                # find the sum of arr from i:j+1 bc range is non-inclusive of last element
                result += sum(arr[i:j+1])
        return result



arr = [1,4,2,5,3]
print(sumOddLengthSubarrays1(arr))
