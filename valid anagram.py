class Solution(object):
    def isAnagram(self, s, t):
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            return False

        for c in s:
            dic1[c] = dic1.get(c, 0) + 1

        for c in t:
            dic2[c] = dic2.get(c, 0) + 1

        return sorted(dic1.items()) == sorted(dic2.items())