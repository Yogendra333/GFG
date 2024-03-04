#User function Template for python3

class Solution:
    # Function to swap elements of the array
    def swapElements(self, arr, n):
        n = len(arr)
        for i in range(0, n-2):
            temp = arr[i]
            arr[i] = arr[i+2]
            arr[i+2] = temp


#{ 
 # Driver Code Starts

#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.swapElements(arr, n);
        for i in arr:
            print(i, end = " ")
        print()
# } Driver Code Ends