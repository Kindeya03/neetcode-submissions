class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # S: S[i,j] = the total number of unique paths that can be taken from 0,0 to i,j
        # R: S[i, j] = S[i-1, j] + S[i, j-1]
        # T: increasing i+j
        # B: S[0, j] = S[i, 0]= 1
        # O: S[m-1, n-1]
        # T: O(mn)
        s = [[0]*(n)]*(m)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    s[i][j] = 1
                else:
                    s[i][j] = s[i-1][j] + s[i][j-1]
        return s[m-1][n-1]
        