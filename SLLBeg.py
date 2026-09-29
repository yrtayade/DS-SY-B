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
    
    def delete(self, data):
        if self.start == None:
            print("Empty List")
        else:
            temp = self.start 
            while temp.info != data:
                p= temp
                temp = temp.next
                if temp == None:
                    print("Not found")
                    return
            
            if temp == self.start:
                 self.start = temp.next  
                 temp.next = None
                 temp = None
            elif temp.next == None: 
                p.next = None
                temp = None
            else:
                q = temp.next
                p.next = q
                temp.next = None
                temp = None


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
s1.delete(80)
s1.display()
s1.delete(77)
s1.display()
s1.delete(22)
s1.display()
s1.delete(99)
s1.display()
