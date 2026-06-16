class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = [i for i in s]
        if len(s)%2 != 0:
            return False
        for br in s:
            if br in ['(', '{', '[']:
                stack.append(br)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if cur == '(' and br != ')':
                    return False
                if cur == '{' and br != '}':
                    return False
                if cur == '[' and br != ']':
                    return False 
        return True if not stack else False
