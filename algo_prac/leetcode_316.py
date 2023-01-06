class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) <= 1:
            return s
        output = ""
        for c in sorted(set(s)):
            if set(s[s.index(c):]) == set(s):
                output = output + c
                s = s[s.index(c):]
                s = s.replace(c, '')
                break

        return output + self.removeDuplicateLetters(s)