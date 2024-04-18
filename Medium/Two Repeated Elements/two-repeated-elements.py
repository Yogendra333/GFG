#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr, n):
        
        res = []
        first = False
        
        #iterating over the array elements.
        for i in range(0,n+2):
            
            #making the visited elements negative.
            if arr[abs(arr[i])]>0:
                arr[abs(arr[i])]=-arr[abs(arr[i])]
            
            #if the number is negative, it was visited previously
            #so this would be the repeated element.
            else:
                
                #storing first and second repeated element accordingly.
                if(first == False):
                    res.append(abs(arr[i]))
                    first = True
                else:
                    res.append(abs(arr[i]))
                    
        #returning the result.
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends