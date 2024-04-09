# Rain water trapped problem
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        leftMax = [0] * len(A)
        rightMax = [0] * len(A)

        maxi = float("-inf")
        for i in range(len(A)):
            maxi = max(maxi, A[i])
            leftMax[i] = maxi
        maxi = float("-inf")
        for i in range(len(A) - 1, -1, -1):
            maxi = max(maxi, A[i])
            rightMax[i] = maxi

        ans = 0
        for i in range(len(A)):
            ans += min(leftMax[i], rightMax[i]) - A[i]
        return ans
