# make a dictionary of all of the characters in s
# compare the characters of t to that dictionary
# subtract the value if it is in the dictionary
# check if values == 0


def isAnagram(s, t):
    char_map = {}

    for char in s:
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] += 1

    for char in t:
        if char not in char_map:
            return False
        else:
            char_map[char] -= 1

    for value in char_map.values():
        if value != 0:
            return False
    return True


s = "anagram"
t = "nagaram"

print(isAnagram(s, t))
