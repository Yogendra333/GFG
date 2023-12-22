from typing import List
class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # creating a list of tuples to store the finish time and index of meetings.
        a = [(F[i], i) for i in range(N)]

        # sorting the list in ascending order based on finish times.
        a.sort()

        # initializing the current time with the finish time of the first meeting.
        tym = a[0][0]

        # creating a list to store the indices of the meetings.
        ans = [a[0][1] + 1]

        # iterating through the remaining meetings.
        for i in range(1, N):
            # checking if the start time of the current meeting is greater than the current time.
            if S[a[i][1]] > tym:
                # if yes, then the current meeting can be scheduled,
                # so adding its index to the answer list and updating the current time.
                ans.append(a[i][1] + 1)
                tym = a[i][0]

        # returning the answer list containing the indices of the meetings.
        return sorted(ans)



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
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends