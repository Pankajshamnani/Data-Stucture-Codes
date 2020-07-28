
# Declare a class Node with two enitities data,next(a pointer to next node)
class Node:
    #Constructor to initialize data with some value and next to point to null
    def __init__(self,data):
        self.data=data
        self.next=None #next points to NULL

class LinkedList:
    def __init__(self):
        self.head=None      #head denotes the first node of the linked list

    #printing linked list
    def printLinkedList(self):
        temp=self.head          #temp holds the first node i.e present in head
        while(temp):            #traverse temp until NULL not found
            print(temp.data)
            temp=temp.next

    #function to insert data at beginning in linked list
    #here element is a node to be inserted at beginning
    def insertBeginning(self,elementData):
        element=Node(elementData)
        temp=self.head
        element.next = temp
        self.head=element

    # function to insert data after some node
    def insertAfterNode(self,prev_node,elementData):
        if(prev_node==None):
            print("node not found in linked list")
        else:
            element = Node(elementData)
            temp=prev_node.next
            prev_node.next=element
            element.next=temp

    # function to insert data at the end
    def insertEnd(self, elementData):
        element = Node(elementData)
        if (self.head == None):
            self.head=element
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=element

    # key is the data of the element to be deleted
    def deleteNode(self,key):
        if self.head==None:  #if the list is empty
            print("sorry cannot delete as linked list is empty")
        else:
            if(self.head.data==key):      #if element found on the head i.e on first node
                temp=self.head.next
                self.head=temp
            else:
                found=0
                previousNode=self.head         #keep track of the previous node of key found
                temp=self.head.next            #if element not found on first node then start traversing from second node
                while(temp):
                    if(temp.data==key):
                        found=1
                        foundNode=temp
                        break
                    previousNode=temp           #keep track of previous Node
                    temp=temp.next
                if(found==0):
                    print("Node not Found")
                else:
                    previousNode.next=foundNode.next    #make the previous node point to next node of found node
                    foundNode=None

linkedlist=LinkedList()
node1=Node(10)
linkedlist.head=node1
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
# linkedlist.insertBeginning(1000)
# linkedlist.insertAfterNode(node2,2000)
# linkedlist.insertEnd(1000)
linkedlist.deleteNode(20)
linkedlist.printLinkedList()





