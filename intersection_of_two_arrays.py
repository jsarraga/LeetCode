class Solution:
    # faster solution: using pythons intersection() function. Takes in two sets. -- 44 ms
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))

    # alternate solution using hashmap and sets
    def intersection1(self, nums1, nums2):
        hashmap = {}
        result = set()

        for x in nums1:
            if x not in hashmap:
                hashmap[x] = True

        for y in nums2:
            if y in hashmap:
                result.add(y)
        
        return result
    
    # make a set of the results. set's rule out duplicates -- 72 ms
    def intersection2(self, nums1, nums2):
        result = set()
        for i in nums1:
            if i in nums2:
                result.add(i)
        return result