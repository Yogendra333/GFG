#User function Template for python3


class Solution:
    
    def missingNumber(self,array,n):
        total = (n + 1)*(n)//2  
        sum_of_A = sum(array)  
        return total - sum_of_A


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends