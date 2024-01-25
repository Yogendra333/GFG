#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def __init__(self):
        self.mxp=9999
        self.prime=[1 for i in range(10001)]
        self.prime[1]=0;
        #Seive Of Eratosthenes
        for i in range(2,self.mxp+1):
            if self.prime[i]==1:
                j=2
                while j*i<=self.mxp:
                    self.prime[j*i]=0
                    j+=1

    #Function to perform BFS from source to destination.
    def bfs(self,source,destination):
        dp =[-1 for i in range(10001)] #stores the shortest distance from source to destination
        vis=[0 for i in range(10001)] 
        q = []; 
        q.append(source)
        dp[source]=0
        vis[source]=0
        while len(q)>0:
            current=q.pop(0)
            if vis[current]==1:
                continue
            vis[current]=1
            s=str(current)
            for i in range(4):
                for j in range(10):
                    ch=chr(j+48)
                    if ch==s[i] or (ch=='0' and i==0):
                        continue
                    nxt=s[0:i]+ch+s[i+1:]
                    nxtN=int(nxt)
                    if self.prime[nxtN]==1 and dp[nxtN]==-1:
                        dp[nxtN]=1+dp[current]
                        q.append(nxtN)
        return dp[destination];

    #Function to solve the problem and return the result.
    def solve(self,Num1,Num2):
        return self.bfs(Num1,Num2)


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1,num2=map(int,input().split())
        ob = Solution()
        print(ob.solve(num1,num2))
# } Driver Code Ends