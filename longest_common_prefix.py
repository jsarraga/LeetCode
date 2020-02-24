# 1. make a list of chars with zip - all 1st chars, all 2nd chars, all 3rd chars...
# 2. turn zip list into sets - eliminates duplicates
# 3. for any set that is only 1 char (all strings share this letter in the same position)
# 4. return letters in a string

def longestCommonPrefix(strs):
    l = list(zip(*strs))
    # l:  [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
    prefix = ""

    for i in l:
        if len(set(i)) == 1:
            # set1:  {'f'}
            # set2:  {'l'}
            # set3:  {'i', 'o'}
            prefix += i[0]
        else:
            break
    return prefix
    

strs = ["flower","flow","flight"]
longestCommonPrefix(strs)