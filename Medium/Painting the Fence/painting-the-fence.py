#User function Template for python3

class Solution:
    def countWays(self,n,k):
        # code here.
        if n==0:
            return 0
        if n==1:
            return k
        if n==2:
            return k*k
        
        # initializing the dp list with 0's
        dp = [0] * (n + 1)
        total = k
        mod = 1000000007
        
        # setting the base cases for n=1 and n=2
        dp[1] = k
        dp[2] = k * k   
         
        # calculating the number of ways for n>2
        for i in range(3,n+1):
            dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod
             
        return dp[n]


#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends