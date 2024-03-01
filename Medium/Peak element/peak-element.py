class Solution:   
    def findPeakUtil(self,arr,low,high,n):
        # calculating mid
        mid=(low+high)//2
        # if mid is last or first index with first element
        # greater than next.
        # Also, check if mid element is greater than mid - 1 and mid+1
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid] ):
            return mid
        # If mid is other than 0, then check if mid element is less than prev.
        # If so, then recurse for lower half
        elif (mid>0 and arr[mid-1]>arr[mid]):
            return self.findPeakUtil(arr,low,mid-1,n)
        # else recurse for the upper half
        else :
            return self.findPeakUtil(arr,mid+1,high,n)
    def peakElement(self,arr, n):
        return self.findPeakUtil(arr,0,n-1,n)



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends