from collections import Counter
def longestPalindrome(s):
        # create a dictionary  {char: count}
        cdict = {}
        for c in s:
            if c in cdict:
                cdict[c] += 1
            else:
                cdict[c] = 1
        
        output = 0
        odd_found = False
        
        for count in cdict.values():
            if odd_found:
                # if there is an odd count of a character, 
                # it can only take just 1 (to be in the center of the palindrome)
                # or an even amount above one (i.e. if there are 5 c's, it can only use 4)
                if count > 1:
                    if count % 2 ==0:
                        output += count
                    else:
                        output += count -1      
            else:
                if count % 2 == 0:
                    output += count
                else:
                    # it can take one char with count of 1
                    output += count
                    odd_found = True
        return output

s = "abccccdd"
print(longestPalindrome(s))