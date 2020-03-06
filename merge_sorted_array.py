# what we know:
# nums1 will have enough place holders to accomodate for nums2
# both arrays are sorted
# m and n are the initialized  == we can use these as indexes in the arrays to compare
# since there are place holders at the end of nums1, we can start comparing at the end of each array
# we'll use m and n as counters and indexes

def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    nums1[:n] = nums2[:n]
    return nums1


nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))