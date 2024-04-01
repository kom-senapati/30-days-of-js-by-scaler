# Max Mod
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        res = float("-inf")
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[j] != 0:
                    res = max(res, A[i] % A[j])
                if A[i] != 0:
                    res = max(res, A[j] % A[i])
        return res