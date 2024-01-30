class Solution(object):
    def isPowerOfThree(self, n):
        while n >= 1:
            if n == 1:
                return True
            elif n % 3 != 0:
                return False
            n /= 3
