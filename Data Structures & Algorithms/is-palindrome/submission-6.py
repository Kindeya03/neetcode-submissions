import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)< 2:
            return True
        frwd = 0
        back = len(s)-1
        while back >= frwd:
            while (s[frwd] not in lowercase and s[frwd] not in uppercase and s[frwd] not in numbers):
                if frwd >= len(s)-1:
                    return True
                frwd +=1
            while s[back] not in lowercase and s[back] not in uppercase and s[back] not in numbers:
                if back<= 0:
                    return True
                back -=1
            # print(f'frwd ={s[frwd].lower()} [{frwd}] back = {s[back].lower()} [{back}]')
            if s[frwd].lower() != s[back].lower():
                return False
            frwd +=1
            back -=1
        return True
