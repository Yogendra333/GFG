#User function Template for python3

class Solution:
    def kTop(self, arr, N, K):
        final_ans=[]
      
        # list of size k + 1 to store elements 
        top = [0 for i in range(K + 1)] 
       
        # dictionary to keep track of frequency 
        freq = {i:0 for i in range(K + 1)} 
      
        # iterate till the end of stream 
        for m in range(N): 
      
            # increase the frequency 
            if a[m] in freq.keys(): 
                freq[a[m]] += 1
            else: 
                freq[a[m]] = 1
      
            # store that element in top vector 
            top[k] = a[m] 
       
            i = top.index(a[m]) 
            i -= 1
              
            while i >= 0: 
      
                # compare the frequency and swap if higher 
                # frequency element is stored next to it 
                if (freq[top[i]] < freq[top[i + 1]]): 
                    t = top[i] 
                    top[i] = top[i + 1] 
                    top[i + 1] = t 
                  
                # if frequency is same compare the elements 
                # and swap if next element is high 
                elif ((freq[top[i]] == freq[top[i + 1]]) and (top[i] > top[i + 1])): 
                    t = top[i] 
                    top[i] = top[i + 1] 
                    top[i + 1] = t 
                else: 
                    break
                i -= 1
              
            # print top k elements 
            i = 0
            ans = []
            while i < K and top[i] != 0: 
                ans.append(top[i]) 
                i += 1
            
            final_ans += [ans]
        return final_ans

#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    for line in ans:
        print(*line)



# } Driver Code Ends