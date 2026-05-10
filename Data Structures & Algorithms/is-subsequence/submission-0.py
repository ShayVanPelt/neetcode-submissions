class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sP = 0
        tP = 0

        while sP < len(s) and tP < len(t):
            if t[tP] == s[sP]:
                sP += 1
            tP+= 1
        return sP == len(s)


       

        