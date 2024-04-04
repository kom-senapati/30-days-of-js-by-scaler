# Longest odd even subsequence but can delete any number of middle elements
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 1
        for i in range(len(A)-1):
            if (A[i] + A[i + 1]) % 2:
                count += 1
        
        return count