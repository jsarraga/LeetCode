# Given a 32-bit signed integer, reverse digits of an integer.
# NOTE: Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



class Solution:
    def reverse(self, x: int) -> int:
        # handling for edge case if out of range
        if x <= -2 ** 31 or x >= 2 ** 31 - 1:
            return 0
        else: 
            # convert to string, reverse using splice. 
            # converts negative integer by skipping the "-" in the neg number when splicing to reverse then concatenating it on the end.
            rev = int(str(x)[::-1] if x>= 0 else "-" + str(x)[1:][::-1])
            # handling for edge case if out of range
            if rev <= -2 ** 31 or rev >= 2 ** 31:
                return 0
            else:
                return rev