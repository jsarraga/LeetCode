""" Given: 
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1. """

def fib(n):
    # the first two values are given: 0, 1. Account for base case
    if n == 0:
        return 0
    if n ==1:
        return 1

    # make a dictionary of n and it's value. f(0)=0 and f(1) = 1
    fib_dict = {0:0, 1:1}
    
    # iterate through range 2 -> n+1. It's 2 bc we're given the first 2 elements and n+1 bc the last number is non-inclusive in range. 
    for i in range(2, n+1):
        # given fib math, calculate current value based on adding val of prev n and two elements previous
        current = fib_dict[i-1] + fib_dict[i-2]
        # set that value
        fib_dict[i] = current
    
    # return the value of n from the dict
    return fib_dict[n]


n = 3
print(fib(n))