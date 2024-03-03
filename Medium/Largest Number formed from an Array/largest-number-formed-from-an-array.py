#User function Template for python3
class Solution:

    
    def printLargest(self, n, arr):
        
        
        def myKey(a,b):
            if (a+b)>(b+a):
                return -1
            elif (a+b)<(b+a):
                return 1
            else:
                return 0
        
        ans = ""
        l = sorted(arr,key=functools.cmp_to_key(myKey))
        for i in l:
            ans += i
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends