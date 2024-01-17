class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        s = s.strip()
        arr = s.split(' ')
        return len(arr[len(arr) - 1])