# Rotation of matrix by 90 degree
class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for i in range(len(A)):
            A[i] = A[i][::-1]
        return A