class Solution:
    def firstUniqChar(self, s: str) -> int:
        hp = {}

        for ch in s:
            hp[ch] = hp.get(ch, 0) + 1
        
        for i in range(len(s)):
            if hp[s[i]] == 1:
                return i
        return -1