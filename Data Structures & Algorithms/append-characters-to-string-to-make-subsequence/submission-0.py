class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointS = 0
        pointT = 0

        while pointS < len(s) and pointT < len(t):
            if s[pointS] == t[pointT]:
                pointS += 1
                pointT += 1
            else:
                pointS += 1
        return len(t) - pointT