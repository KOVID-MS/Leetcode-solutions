class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        if len(s) == 1 and len(t) == 1:
            return True

        dic1 = {}

        for i in range(len(s)):
            if s[i] not in dic1:
                if t[i] in dic1.values():
                    return False
                dic1[s[i]] = t[i]
            else:
                if dic1[s[i]] != t[i]:
                    return False
        return True

