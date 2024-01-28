class Solution:
    def findNthNumber(self, n, k):
        low, high = 0, 10 ** 18
        self.dp = [[[-1] * 65 for _ in range(65)] for _ in range(2)]

        while low <= high:
            mid = low + (high - low) // 2
            count = self.find(mid, k)
            if count >= n:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def find(self, n, k):
        s = format(n, 'b').zfill(64)
        self.reset()
        return self.dpf(s, len(s), 1, k)

    def dpf(self, s, n, tight, k):
        if k < 0:
            return 0
        if n == 0:
            return 1
        if self.dp[tight][k][n] is not None:
            return self.dp[tight][k][n]

        ub = int(s[len(s) - n]) if tight == 1 else 1
        ans = 0
        for dig in range(ub + 1):
            if dig == ub:
                ans += self.dpf(s, n - 1, tight, k - dig)
            else:
                ans += self.dpf(s, n - 1, 0, k - dig)
        self.dp[tight][k][n] = ans
        return ans

    def reset(self):
        for i in range(65):
            for j in range(65):
                self.dp[0][i][j] = None
                self.dp[1][i][j] = None


#{ 
 # Driver Code Starts



if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k=map(int,input().split())
        
        obj = Solution()
        res = obj.findNthNumber(n,k)
        
        print(res)
        

# } Driver Code Ends