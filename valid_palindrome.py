def isPalindrome(s):
        
    newString = [i.lower() for i in s if i.isalnum()]
    return newString == newString[::-1]
       

s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))