# %% Question 1.3 -done
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:    
    def __init__(self):
        self.head = None
 
    # insert list items after head
    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Add two lists and show results
    def sumLists(self, first, second):
        prev = None
        temp = None
        carry = 0
 
        while(first is not None or second is not None):
 
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
 
            carry = 1 if Sum >= 10 else 0
 
            Sum = Sum if Sum < 10 else Sum % 10
 
            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
 
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
 
        if carry > 0:
            temp.next = Node(carry)
 
    def printList(self):
        temp = self.head
        a=[];
        while(temp):
            a.append(temp.data);
            temp = temp.next
        print(a)

first = LinkedList()
second = LinkedList() 
# list 1
first.insert(6)
first.insert(4)
first.insert(9)
print ("List1: ")
first.printList()
# list 2
second.insert(4)
second.insert(8)
second.insert(5)
print ("List2: "),
second.printList()
# result
res = LinkedList()
res.sumLists(first.head, second.head)
print ("Sum: "),
res.printList()
