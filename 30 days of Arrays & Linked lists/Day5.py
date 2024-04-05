# Best time to buy and sell stocks
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        l = 0
        profit = 0
        for r in range(1, len(A)):
            if A[l] < A[r]:
                profit = max(profit, A[r] - A[l])
            else:
                l = r
        return profit
