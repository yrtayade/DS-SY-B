class Node:
    prev = None
    info = None
    next = None

class Operation:
    start = None
    def insertAtBeg(self,data):
        newNode =Node()
        newNode.prev = None
        newNode.info = data
        newNode.next = None

        if self.start == None:
            self.start= newNode
        else:
            newNode.next = self.start
            self.start.prev = newNode
            self.start = newNode

    def insertAtEnd(self,data):
        newNode =Node()
        newNode.prev = None
        newNode.info = data
        newNode.next = None

        if self.start == None:
            self.start= newNode
        else:
            p = self.start
            while p.next != None:
                p = p.next
            
            p.next= newNode
            newNode.prev = p

    def insertAtMid(self, data, pos):
        newNode =Node()
        newNode.prev = None
        newNode.info = data
        newNode.next = None

        if self.start == None:
            self.start= newNode
        else:
            p = self.start
            while p.info != pos:
                p = p.next
            
            q = p.next 
            p.next = newNode
            newNode.prev = p
            newNode.next = q
            q.prev = newNode
    
    def delete(self, data):
        if self.start == None:
            print("Empty")
        else:
            temp = self.start
            while temp.info != data:
                p=temp
                temp = temp.next
                if temp == None:
                    print("Data not found")
                    return
            
            if temp == self.start:
                self.start = temp.next
                self.start.prev = None
                temp.prev = None
                temp = None
            elif temp.next == None:
                p.next = None
                temp.prev = None
                temp = None
            else:
                q = temp.next
                p.next = q
                q.prev = p
                temp.prev = None
                temp.next = None
                temp = None

    def display(self):
        if self.start == None:
            print("Empty List")
        else:
            p =self.start

            while p!= None:
                print(p.info, end = " ")
                p = p.next
            print()

s1 = Operation()
s1.insertAtBeg(44)
s1.insertAtBeg(55)
s1.insertAtBeg(88)
s1.display()
s1.insertAtEnd(99)
s1.insertAtEnd(22)
s1.display()
s1.insertAtMid(33, 99)
s1.display()
s1.delete(888)
s1.display()