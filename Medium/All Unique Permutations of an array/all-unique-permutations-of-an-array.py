#User function Template for python3

class Solution:
    #Function to find unique permutations of the given array.
    def uniquePerms(self, arr, n):
        # code here 
        res = [] #initialize an empty list to store the result
        perm = [] #initialize an empty list to store each permutation
        count = {n:0 for n in arr} #create a dictionary to store the count of each element in the array
        for n in arr:
            count[n] += 1 #increment the count for each element in the array
        
        #Function to perform depth-first search to generate permutations.
        def dfs():
            if len(perm) == len(arr): #if length of permutation is equal to the length of array, we have found a permutation.
                res.append(perm.copy()) #add the permutation to the result list
                return
            for n in sorted(count.keys()):
                if count[n] > 0: #if count of element is greater than 0, we can include it in the permutation
                    perm.append(n) #add the element to the permutation
                    count[n] -= 1 #decrement the count of the element
                    
                    dfs() #perform recursive depth-first search
                    
                    count[n] += 1 #restore the count of the element
                    perm.pop() #remove the element from the permutation
        dfs() #call the dfs function to generate permutations
        return res #return the result list containing unique permutations.


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends