#User function Template for python3

class Solution:

    def countStr(self, n):
        res = 0
        res += 1 + (n * 2)
        res += n * ((n * n) - 1) / 2
        return int(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends