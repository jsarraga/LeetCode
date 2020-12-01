def createTargetArray(nums, index):
        target = []
        # .insert(position, x) allows you to insert an element without replacing
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target
            