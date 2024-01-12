class Solution(object):
    def mySqrt(self, x):
        self.x = x
        if x == 0:
            return 0
        if x <= 3:
            return 1

        start, end = 1, x
        while (start <= end):
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
        return end
