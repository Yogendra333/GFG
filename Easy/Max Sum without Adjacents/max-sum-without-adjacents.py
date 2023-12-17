class Solution:
    def findMaxSum(self, arr, n):
        n = len(arr)
        if n == 0:
            return 0

        value1 = arr[0]
        if n == 1:
            return value1

        value2 = max(arr[0], arr[1])
        if n == 2:
            return value2

        # contains maximum sum at the end
        max_sum = 0

        # Fill remaining positions
        for i in range(2, n):
            max_sum = max(arr[i] + value1, value2)
            value1 = value2
            value2 = max_sum

        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends