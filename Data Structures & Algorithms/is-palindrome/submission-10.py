# import string
# lowercase = string.ascii_lowercase
# uppercase = string.ascii_uppercase
# numbers = string.digits
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)< 2:
            return True
        frwd = 0
        back = len(s)-1
        while back >= frwd:
            while not s[frwd].isalnum():
                if frwd >= len(s)-1:
                    return True
                frwd +=1
            while not s[back].isalnum():
                if back<= 0:
                    return True
                back -=1
            # print(f'frwd ={s[frwd].lower()} [{frwd}] back = {s[back].lower()} [{back}]')
            if s[frwd].lower() != s[back].lower():
                return False
            frwd +=1
            back -=1
        return True
