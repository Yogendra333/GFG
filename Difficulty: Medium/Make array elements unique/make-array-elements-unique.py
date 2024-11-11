#User function Template for python3

class Solution:

    #Function to find the minimum number of increments required.
    def minIncrements(self, arr):

        ans = 0
        N = len(arr)
        #sorting the array.
        arr.sort()

        #iterating over the array.
        for i in range(1, N):

            #if the current element is less than or equal to the previous element.
            if (arr[i] <= arr[i - 1]):

                #calculating the number of increments required and updating the answer.
                ans += (arr[i - 1] - arr[i] + 1)

                #increasing the value of the current element to maintain increasing order.
                arr[i] = arr[i - 1] + 1

        #returning the minimum number of increments required.
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends