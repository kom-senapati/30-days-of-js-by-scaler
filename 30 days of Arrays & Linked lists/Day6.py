# Kth row of pascal triangle
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        from math import comb
        res = []
        for k in range(A+1):
            res.append(comb(A, k))
        return res