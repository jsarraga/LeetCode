# if you've calculated n before, it'll get you into an infinite loop

# i.e. n = 20 
# --> 2^2 + 0^2 = 4
# --> 4^@ = 16
# --> 1^2 + 6^2 = 37
# --> 3^2 + 7^2 = 58
# --> 5^2 + 8^2 = 74
# --> 7^2 + 4^2 = 65
# --> 6^2 + 5^2 = 61
# --> 6^2 + 1^2 = 37  -----> this will just keep repeating and will go on forever

# so keep track of the numbers you've already calculated in a set
# why set? Because it is space efficient



def isHappy(n):
    # make an empty set to keep track of seen numbers
    memory = set()

    while n != 1:
        # turn n into a string to make it iterable.
        # iterate through digits and square them, then sum then. Set n to this.
        n = sum([int(i) ** 2 for i in str(n)])
        # if we've seen the number before, it'll return an infinite loop so return False
        if n in memory:
            return False
        # if not, add it to the set
        else:
            memory.add(n)
    return True