# Approach:
#   the tricky part about this is to modify IN-PLACE
#   two pointers. one to traverse the list ahead of the other to the end of the list
#   the other to track the index used to override with the str(count) 
#   

def compress(chars):
    # make a count variable. need to track count of chars
        # i variable will track the index to override
        n = len(chars)
        count = 1
        i = 0
        
        # j will traverse the list starting at index 1
        for j in range(1, n+1):
            # while j is in range and chars[j] is the same as it's prev element
            if j < n and chars[j] == chars[j-1]:
                # increase the count
                count += 1
            else:
                # makes sure the two prev elements from j are the same, important if count > 9
                chars[i] = chars[j-1]
                # move i pointer up
                i += 1
                # if count is more than 1, overwrite i pointer to str(count)
                if count > 1:
                    # handles if count > 9
                    for k in str(count):
                        chars[i] = k
                        i +=1 
                # reset count
                count = 1
        # reset to account for full chars list once i reaches the end        
        chars = chars[:i]
        # returning index same as returning len(chars)
        return i

# Time = O(n)
# Space O(1)
                
        
            
            
    
chars = ["a","a","b","b","c","c","c"]

compress(chars)