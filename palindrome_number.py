def isPalindrome(x):
    return str(x) == str(x)[::-1
                            


# Without using str()
def isPalindrome(x):                       
    orig = x
    backwards_x = 0
    # reverses number
    while x > 0:
        # starts from the ones digit, and adds it to backwards_x
        # x % 10 takes the remainder after removing 10's. (ex: 68 -> it takes the 8 and adds it to backwards_x)
        backwards_x = (backwards_x * 10) + (x % 10)
        # hacks off the last digit and starts the loop again
        x = x // 10
    return orig == back_x