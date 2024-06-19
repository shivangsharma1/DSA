def max_profit(ls):
    profit = 0
    buy_price = float('inf')
   
    for i in range(len(ls)):
        if buy_price > ls[i]:
            buy_price = ls[i]
        elif profit < (ls[i] - buy_price):
            profit =  ls[i] - buy_price
    return profit





#driver code
prices = [7, 1, 5, 3, 6, 4, 16]
print(max_profit(prices))