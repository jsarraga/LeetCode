def firstUniqChar(s):
    char_map = {}
    for c in s:
        if c in char_map.keys():
            char_map[c] += 1
        else:
            char_map[c] = 1
            
    for i in range(len(s)):
        if char_map[s[i]] == 1:
            return i
    
    return -1

# slightly faster way using Counter()

from collections import Counter
def firstUniqChar1(s):
    char_count = Counter(s)

    for i in range(len(s)):
        # .get() returns the value of given key s[i]
        if char_count.get(s[i]) == 1:
            return i
    return -1

# other option
def firstUniqChar2(s):
    count = collections.Counter(s)

    for idx, ch in enmuerate(s):
        if count[ch] == 1:
            return idx
    return -1