# Maximum sum of subarray
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_ = float("-inf")
        max_h = 0
        
        for i in range(len(A)):
            max_h += A[i]
            if max_ < max_h:
                max_ = max_h
            if max_h < 0:
                max_h = 0
        return max_