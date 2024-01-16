class Solution(object):
    def isPalindrome(self, x):
        self.x = x
        y = str(x)
        if len(y) == 1:
            return True

        if x < 0:
            return False

        for i in range(len(y) // 2):
            if y[i] != y[len(y) - i - 1]:
                return False
        return True


