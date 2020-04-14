# Approach

# we'll see if the number is divisible by three, if it is, we'll divide the remainder by 3
# if we get down to n == 1, then we'll know if it's a power of three



def isPowerOfThree(n):
    if n < 1:
        return False

    while n % 3 == 0:
        n /= 3
    
    return n == 1