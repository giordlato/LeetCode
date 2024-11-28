class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stringpunt = tpunt = 0

        while stringpunt < len(s) and tpunt < len(t):
            if s[stringpunt] == t[tpunt]:
                stringpunt += 1
            tpunt += 1
        
        return stringpunt == len(s)