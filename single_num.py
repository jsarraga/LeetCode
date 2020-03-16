from collections import Counter

def single_num(nums):
    # make a dictionary counting frequencies of integers
    c = Counter(nums)

    # search dictionary keys for value
    for key, value in c.items():
        if value == 1:
            return key