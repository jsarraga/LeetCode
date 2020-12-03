def twoSum(nums, target):
        ndict = {}
        #store the complement of each element in dict with index as value 
        # {comp : index of element it complements}
        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] in ndict:
                return [i, ndict[nums[i]]]
            else:
                ndict[comp] = i
        #iterate through nums to check if i is in dict
        #if so, return current index, and index of comp (ndict[comp])
        
nums = [2,7,11,15] 
target = 9
print(twoSum(nums, target))