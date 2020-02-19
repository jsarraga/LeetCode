def isPalindrome(s):
    # change all characters to lower, and add to list if i is alpha numeric
    newString = [i.lower() for i in s if i.isalnum()]
    return newString == newString[::-1]
       

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))