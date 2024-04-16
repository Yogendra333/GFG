from typing import List

class Solution:
    
    #Function to minimize the difference between maximum and minimum element in subarrays of length k.
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        
        #list to store the maximum element of subarrays starting from i to end.
        post_max = [0]*n
        
        #list to store the minimum element of subarrays starting from i to end.
        post_min = [0]*n

        #initializing the last elements of post_max and post_min.
        post_min[-1] = arr[-1]
        post_max[-1] = arr[-1]

        #iterating backwards to calculate post_max and post_min.
        for i in range(n-2,-1,-1):
            post_max[i] = max(arr[i],post_max[i+1])
            post_min[i] = min(arr[i] , post_min[i+1])

        #calculating initial difference by removing the first subarray of length k.
        min_diff = post_max[k] - post_min[k]

        #initializing variables for storing current min and max values.
        p_min = arr[0]
        p_max = arr[0]

        #iterating to find the minimum difference.
        for i in range(1,n-k):
            curr_min = max(p_max , post_max[i+k]) - min(p_min , post_min[i+k])
            min_diff = min(min_diff,curr_min)
            p_max = max(arr[i],p_max)
            p_min  = min(arr[i],p_min)
        
        #calculating difference by removing the last subarray of length k.
        min_diff = min(min_diff,p_max-p_min)

        #returning the minimum difference.
        return min_diff



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minimizeDifference(n, k, arr)
        
        print(res)
        

# } Driver Code Ends