import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
valid = lowercase + uppercase+numbers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)< 2:
            return True
        frwd = 0
        back = len(s)-1
        while back >= frwd:
            while (s[frwd] not in valid):
                if frwd >= len(s)-1:
                    return True
                frwd +=1
            while s[back] not in valid:
                if back<= 0:
                    return True
                back -=1
            # print(f'frwd ={s[frwd].lower()} [{frwd}] back = {s[back].lower()} [{back}]')
            if s[frwd].lower() != s[back].lower():
                return False
            frwd +=1
            back -=1
        return True
