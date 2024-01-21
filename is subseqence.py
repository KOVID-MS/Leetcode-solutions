class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        subsequence = 0
        for i in range(len(s)):
            found = False
            for j in range(subsequence, len(t)):
                if t[j] == s[i]:
                    subsequence = j + 1
                    found = True
                    break
            if not found:
                return False
        return True
