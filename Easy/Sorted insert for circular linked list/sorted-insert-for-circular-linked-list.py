#User function Template for python3

class Solution:
    def sortedInsert(self, head, data):
        new_node=Node(data)
        
        current =head 
    
        # Case 1 of the above algo 
        if current is None: 
            new_node.next = new_node  
            head = new_node
            return head
          
        # Case 2 of the above algo 
        elif (current.data >= new_node.data): 
              
            # If value is smaller than head's value then we 
            # need to change next of last node 
    
            while current.next != head:
                current=current.next
    
            
            current.next=new_node
            new_node.next=head
            return new_node
        
        # Case 3 of the above algo 
        else: 
              
            # Locate the node before the point of insertion 
            while (current.next != head  and 
                   current.next.data < new_node.data): 
                current = current.next
    
            new_node.next = current.next
            current.next = new_node
            return head


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.last=None
  
    # Function to insert a new node  
    def push(self, data):
        if not self.head:
            nn=Node(data)
            self.head=nn
            self.last=nn
            nn.next=nn
            return
        nn=Node(data)
        nn.next=self.head
        self.last.next=nn
        self.last=nn 
  

# Utility function to print the linked LinkedList

def printList(head):
    if not head:
        return
    temp = head 
    print (temp.data,end=' ') 
    temp = temp.next
    while(temp != head): 
        print (temp.data,end=' ') 
        temp = temp.next
  
    
if __name__ =='__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        data=int(input())

        cll=LinkedList()
        for e in arr:
            cll.push(e)
            
        reshead=Solution().sortedInsert(cll.head,data)
        printList(reshead)
        print()
        


# } Driver Code Ends