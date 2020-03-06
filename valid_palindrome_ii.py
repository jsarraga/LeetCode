# We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. 
# Whenever there is a mismatch, we can either exclude the character at the left or the right pointer. 
# We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome.


def validPalindrome(s):
    # make pointers starting from outside moving in
    left = 0
    right = len(s) - 1

    while left < right:
        # if there is a mismatch
        if s[left] != s[right]:
            # we'll move one character to the left of the right pointer ("bb")
            one = s[left:right]
            # we'll move one character to the right of the left pointer ("bc")
            two = s[left + 1:right + 1]
            # check if either are a palindrome
            return one == one[::-1] or two == two[::-1]
        #move pointers towards middle
        left, right = left + 1, right - 1
    return True
        
s = "abbca"
validPalindrome(s)