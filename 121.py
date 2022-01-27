def maxProfit(prices):
    
    min_prices = prices[0]

    result = 0 

    for price in prices: 
        if price < min_prices: 
            min_prices = price
        
        profit = price - min_prices

        result = max(result, profit)

    return result

