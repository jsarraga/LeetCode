def maxProfit(prices):
    # account for an empty list
    if not prices:
        return 0

    # set profit counter and min to 1st element
    profit = 0
    minimum = prices[0]
    
    
   for i in prices:
       # if i is less than min
            if i < min_price:
                # min becomes i
                min_price = i
            else:
                # calculate profit
                profit = i - min_price
                # if profit > max profit
                if profit > max_profit:
                    # max_profit becomes profit
                    max_profit = profit
                
        return max_profit
    
    return profit
            
            

            
        



prices = [ 7,1,5,3,6,4 ]
print(maxProfit(prices))