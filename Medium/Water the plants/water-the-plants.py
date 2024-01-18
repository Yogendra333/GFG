#User function Template for python3
class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        sprinklers = []                     # initialize empty list for sprinklers
        for i in range(n):
            if gallery[i]>-1:
                sprinklers.append( [i-gallery[i] , i+gallery[i]] );    # add intervals for non-negative gallery values to sprinklers list
        sprinklers.sort()                   # sort the sprinklers list
        target=0                            # initialize target variable
        sprinklers_on=0                     # initialize sprinklers_on variable
        i=0                                 # initialize i variable
        while(target<n):                    # while target is less than n
            if i==len(sprinklers) or sprinklers[i][0]>target:
                return -1                   # if i reached end of sprinklers list or current sprinkler is beyond target, return -1
            max_range = sprinklers[i][1]    # set max_range to the maximum range of current sprinkler
            while( i+1<len(sprinklers) and sprinklers[i+1][0]<=target ):
                i+=1                        # increment i and update max_range if the next sprinkler can cover the target
                max_range = max(max_range,sprinklers[i][1])
            if max_range<target:
                return -1                   # if max_range is less than target, return -1
            sprinklers_on+=1                # increment sprinklers_on as a sprinkler can cover the target
            target=max_range+1              # update target to the next position after the coverage of the last sprinkler
            i+=1                            # increment i to move to the next sprinkler
        return sprinklers_on           




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        gallery = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.min_sprinklers(gallery,n))

# } Driver Code Ends