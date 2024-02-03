# your task is to complete this function
# Function should return an integer value

class Solution:
    def decimalValue(self, head):
        num = ''
        
        # Convert the linked list to a string
        while head:
            num += str(head.data)
            head = head.next
        
        res, pv = 0, 1
        
        # Traverse the string in reverse, multiplying each bit by increasing powers of 2
        for i in range(len(num) - 1, -1, -1):
            res += pv * int(num[i])
            pv = (pv * 2) % 1000000007  # Update power of 2 modulo 10^9+7
            res %= 1000000007  # Update result modulo 10^9+7
        
        return res

        # Code here


#{ 
 # Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob=Solution()
        print(ob.decimalValue(list1.head))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends