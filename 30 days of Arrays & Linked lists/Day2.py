# Return the count of such elements which have strictly smaller and greater elements
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        a,b = max(A), min(A)
        c=0
        for j in range(len(A)):
            if A[j] > b and A[j] < a:
                c += 1
        return c