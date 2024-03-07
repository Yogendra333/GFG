#User function Template for python3

class Solution:

    
    def longestSubstring(self, S , N):
        
        dp=[[0]*(N+1) for i in range(N+1)]
        
        maxi=0
        start=0
        
        for i in range(0,N):
            for j in range(i+1,N):
                
                if S[i]==S[j] and j-i>dp[i][j]:
                    
                    dp[i+1][j+1]=1+dp[i][j]
                    
                    if dp[i+1][j+1]>maxi:
                        start=j
                        maxi=dp[i+1][j+1]
       
        
        if S[start-maxi+1:start+1]=="":
            return -1
        
        return S[start-maxi+1:start+1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends