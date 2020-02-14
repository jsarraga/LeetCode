def reverseString(s):
        """
        s is a list of characters
        Do not return anything, modify s in-place instead.
        """
        # easiest solution:
        s.reverse()
        
        
        # must use s[:] instead of s[::-1] because the latter creates a whole new list. Whereas s[:] = s[s::-1] creates an intermediary list and reassigns it back to s
        s[:] = s[::-1]

        # both are similar in speed