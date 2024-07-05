def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    buy = prices[0]
    for num in prices:
        if buy < num:
            profit += num - buy
        buy = num
    return profit