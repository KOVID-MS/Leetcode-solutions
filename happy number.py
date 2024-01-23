class Solution(object):
    def isHappy(self, n):
        arr = []
        while n != 1 and n not in arr:
            arr.append(n)
            n = str(n)
            sum = 0
            for i in range(len(n)):
                sum += int(n[i]) ** 2
            n = sum

        if n == 1:
            return True
        else:
            return False

