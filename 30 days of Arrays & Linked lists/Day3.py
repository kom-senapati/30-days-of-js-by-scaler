# Minimum elements to be removed so that adjacent elements difference is even
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        c = 0
        for n in A:
            if n&1:
                c += 1
        return min(c, len(A)-c)