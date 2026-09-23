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
    
    def display(self):
        if self.start == None:
            print("Empty List")
        else:
            self.p = self.start            
            while(self.p != None):
                print( self.p.info , end = " ")
                self.p = self.p.next


s1 = SLLBegining()
s1.insertAtBeg(40)
s1.insertAtBeg(60)
s1.insertAtBeg(80)
s1.display()