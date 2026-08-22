class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        uniq = {s[0]}
        lens = 1
        while r < len(s):
            if s[r] not in uniq:
                uniq.add(s[r])
                r +=1

            else:
                uniq.discard(s[l])
                l +=1
            # print(f'l: {l} r: {r}')
            lens = max(lens, r-l)
        return lens
        



