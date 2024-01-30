class Solution(object):
    def isPowerOfTwo(self, n):
        while n >=1:
            if n == 1:
                return True
            elif n%2 == 1:
                return False
            n = n/2