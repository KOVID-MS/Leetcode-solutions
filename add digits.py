class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            sum = 0
            num = str(num)
            for c in num:
                sum += int(c)
            num = sum
        return num



