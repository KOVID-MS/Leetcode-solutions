class Solution(object):
    def plusOne(self, digits):
        self.digits = digits
        string = ''
        for i in digits:
            string += str(i)
        res = int(string) + 1
        return [int(i) for i in str(res)]
