#User function Template for python3

class Solution:
    def search(self,pat,txt):
        res = []

        q =101;d = 26

        M = len(pat);N = len(txt);  

        i=0; j=0  
        
        p = 0; # hash value for pattern  
        t = 0; # hash value for txt  
        h = 1;  
      
        # The value of h would be "pow(d, M-1)%q"  
        for i in range(M-1) :
            h = (h * d) % q 
      
        # Calculate the hash value of pattern and first  
        # window of text  
        for i in range(M):  
            p = (d * p + ord(pat[i])) % q  
            t = (d * t + ord(txt[i])) % q
      
        # Slide the pattern over text one by one  
        for i in range(N-M+1):
            # Check the hash values of current window of text  
            # and pattern. If the hash values match then only  
            # check for characters on by one  
            if  p == t :  
                # Check for characters one by one 
                j = 0 
                while j < M :
                    if txt[i+j] != pat[j]:
                        break
                    j+=1
      
                # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]  
                if j == M :  
                    res.append(i+1)  
            
      
            # Calculate hash value for next window of text: Remove  
            # leading digit, add trailing digit  
            if i < N-M :  
                t = (d*(t - ord(txt[i])*h) + ord(txt[i+M]))%q
      
                # We might get negative value of t, converting it  
                # to positive  
                if t < 0 :
                    t = (t + q)
            

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends