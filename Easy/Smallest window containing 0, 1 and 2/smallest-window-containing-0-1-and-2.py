#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        
        answerExist = False
        lastZero, lastOne, lastTwo = -1, -1, -1
        ans = len(S)
        for i in range (len(S)):
            if (S[i]== '0') :   #if current character is '0', then update lastZero position
                lastZero = i
            elif (S[i] == '1') :   #if current character is '1', then update lastOne position
                lastOne = i
            else :   #if current character is '2', then update lastTwo position
                lastTwo = i
            
            if (lastZero != -1 and lastOne != -1 and lastTwo != -1) :   #if all three positions have been updated
                answerExist = True   #set answerExist to True
                ans = min(ans, 1 + i - min(lastZero, min(lastOne, lastTwo)))   #calculate new substring length and update ans
        
        if (answerExist) :   #if answerExist is True, return ans
            return ans
        
        return -1   #if answer does not exist, return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends