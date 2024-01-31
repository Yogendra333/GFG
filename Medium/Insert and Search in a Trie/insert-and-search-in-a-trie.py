#User function Template for python3
class Solution:        
    
    def cti(self, ch):
        return ord(ch)-ord('a')
        
    #Function to insert string into TRIE.    
    def insert(self, root, key):
        
        #if not present, we insert key into trie. If the key is prefix 
        #of trie node, we just mark the leaf node.
        for e in key:
            idx = self.cti(e)
            
            if not root.children[idx]:
                root.children[idx]=TrieNode()
            
            root=root.children[idx]
        
        #marking last node as leaf.    
        root.isEndOfWord=True
    
    
    
    #Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        
        for e in key:
            idx = self.cti(e)
            
            if not root.children[idx]:
                return False
            
            root=root.children[idx]
        
        #returning true if key is present else false.
        return root.isEndOfWord

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        ob = Solution()
        
        for s in arr:
            ob.insert(t.root,s)
        
        if ob.search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends