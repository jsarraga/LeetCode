class Solution:
    # faster solution: using pythons intersection() function. Takes in two sets. -- 44 ms
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
    
# make a set of the results. set's rule out duplicates -- 72 ms
    def intersection1(self, nums1, nums2):
        result = set()
        for i in nums1:
            if i in nums2:
                result.add(i)
        return result