class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [0, 0]
        for pos in reversed(range(len(prices))):
            dp_old = dp
            dp = [0, 0]
            for bought in [True, False]:
                max_profit = 0
                if not bought:
                    # Buy stock
                    max_profit = max(max_profit, dp_old[True] - prices[pos] - fee)
                else:
                    # Sell stock
                    max_profit = max(max_profit, dp_old[False] + prices[pos])
                # Do nothing
                max_profit = max(max_profit, dp_old[bought])
                dp[bought] = max_profit
        return dp[False]