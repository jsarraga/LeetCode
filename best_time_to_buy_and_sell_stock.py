def maxProfit(prices):
    # account for an empty list
    if not prices:
        return 0

    # set profit counter and min to 1st element
    profit = 0
    minimum = prices[0]
    
    
    for i in prices:
        # if i bigger than the smallest number
        if i > minimum:
            # and it generates more profit that the counter
            if i - minimum > profit:
                # update profit
                profit = i - minimum
        else:
            # account for last element as min
            minimum = i
    
    return profit
            
            

            
        



prices = [ 7,1,5,3,6,4 ]
print(maxProfit(prices))