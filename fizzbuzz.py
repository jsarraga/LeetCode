def fizzBuzz(n):
    fizzList = []
        
    # tricky part here is to have range include last element (n) by putting n + 1
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizzList.append("FizzBuzz")
        elif i % 5 == 0:
            fizzList.append("Buzz")
        elif i % 3 == 0:
            fizzList.append("Fizz")
        else:
            fizzList.append(str(i))
            
    return fizzList
            


n = 1

print(fizzBuzz(n))