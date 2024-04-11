# Repeated number and missing number

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        A1 = sum(A)
        A2 = sum(x**2 for x in A)
        E1 = n*(n+1)//2
        E2 = n*(n+1)*(2*n+1)//6
        
        a_m_b = A1-E1
        a_p_b = (A2-E2)//a_m_b
        
        a = (a_m_b + a_p_b)//2
        b = a_p_b - a
        return [a,b]