class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s)-1
        start = 0
        while start < end:
            while start < end and not s[end].isalnum():
                end = end - 1
            while start < end and not s[start].isalnum():
                start = start + 1
            #print(s[start] + "..." + s[end])
            if s[start].lower() != s[end].lower():
                return False
            end = end - 1
            start = start + 1
        return True
        