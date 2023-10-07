class Solution(object):
    def findTheDifference(self, s, t):
        self.s = s
        self.t = t
        for i in t:
            if i in s:
                s = s.replace(i, '', 1)
            elif i not in s:
                return i
