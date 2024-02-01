#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        
        #using a hash table to mark the characters present in the string.
        marked=[0 for i in range(26)]
        
        #iterating over the string.
        for char in s:
            
            #marking index of current character as true in hash table.
            
            #if we get uppercase character, we subtract 'A' from it
            #to get its index (in terms of 0 to 25).
            if(ord(char)<=ord('Z') and ord(char)>=ord('A')):
                marked[ord(char)-ord('A')]=1
                
            #if we get lowercase character, we subtract 'a' from it
            #to get its index (in terms of 0 to 25).
            elif(ord(char)<=ord('z') and ord(char)>=ord('a')):
                marked[ord(char)-ord('a')]=1
        
        #returning false if any letter of alphabet is unmarked.
        for i in range(26):
            if(not marked[i]):
                return False
                
        #if all letters of alphabet are present then returning true.
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends