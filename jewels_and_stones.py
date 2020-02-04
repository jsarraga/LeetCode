from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_dict = Counter(J)  # builds a dict with the count of characters in it
        jewel_count = 0
        
        for i in S:
            if i in J_dict:
                jewel_count += 1
        return jewel_count 
            
        # one-liner using list comprehension. same run time:
        # return len([i for i in S if i in J])