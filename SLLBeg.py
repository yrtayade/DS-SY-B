#Structure of a Node
class Node:
    info = None
    next = None

class SLLBegining:    
    def __init__(self):
        self.start = None
    def insertAtBeg(self, data):
        newNode = Node()
        newNode.info = data
        newNode.next = None        

        if self.start == None:
            self.start = newNode            
        else:
            newNode.next = self.start            
            self.start = newNode

    def insertatend(self, data):
        newNode = Node()
        newNode.info = data
        newNode.next = None

        if self.start == None:
            self.start = newNode
        else:
            p =self.start
            while p.next != None:
                p = p.next
            p.next = newNode
    
    def insertatmid(self, data, pos):
        newNode = Node()
        newNode.info = data
        newNode.next = None

        if self.start == None:
            self.start = newNode
        else:
            p =self.start
            while p.info != pos:
                p = p.next
            q = p.next
            p.next = newNode
            newNode.next = q
            
    def display(self):
        if self.start == None:
            print("Empty List")
        else:
            self.p = self.start            
            while(self.p != None):
                print( self.p.info , end = " ")
                self.p = self.p.next
            print()

s1 = SLLBegining()
s1.insertAtBeg(40)
s1.insertAtBeg(60)
s1.insertAtBeg(80)
s1.display()
s1.insertatend(44)
s1.insertatend(77)
s1.display()
s1.insertatmid(22, 40)
s1.display()