class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        dic = {}
        for ch in magazine:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1

        for ch in ransomNote:
            if ch in dic and dic[ch] > 0:
                dic[ch] -= 1
            else:
                return False

        return True
