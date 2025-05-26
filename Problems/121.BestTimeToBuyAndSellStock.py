class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # Initialize the minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0

        # Iterate through the list of prices
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit if selling at the current price
            profit = price - min_price
            # Update the maximum profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit
    
if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))  # Output: 5

    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))  # Output: 0

    prices = [1, 2]
    print(Solution().maxProfit(prices))  # Output: 1

    prices = [2, 1]
    print(Solution().maxProfit(prices))  # Output: 0

    prices = [3, 2, 6, 5, 0, 3]
    print(Solution().maxProfit(prices))  # Output: 4