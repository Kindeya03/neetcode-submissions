class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)< 2:
            return True
        frwd = 0
        back = len(s)-1
        while back >= frwd:
            while not self.alphaNum(s[frwd]):
                if frwd >= len(s)-1:
                    return True
                frwd +=1
            while not self.alphaNum(s[back]):
                if back<= 0:
                    return True
                back -=1
            if s[frwd].lower() != s[back].lower():
                return False
            frwd +=1
            back -=1
        return True
    def alphaNum(self, c):
        return (ord('A')<=ord(c)<= ord('Z')or
        ord('a')<=ord(c)<= ord('z')or
        ord('0')<=ord(c)<= ord('9'))
