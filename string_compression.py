from collections import Counter
def compress(chars):
    chars = Counter(chars)
    
    char_list = []
    for key, value in chars.items():
        char_list.append(key)
        char_list.append(str(value))
    
    print(char_list)
    
chars = ["a","a","b","b","c","c","c"]

compress(chars)