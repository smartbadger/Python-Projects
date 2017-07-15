# Created by Connor Bailes
# Date: March 20th
# Purpose - shows how link lists work

# the item in the list
class ListItem(object):

    def __init__(self, data):

        self.data = data
        self.next = None

#the link list
class LinkedList(object):

    def __init__(self):

        self.current = None
        self.front = None

    def addToFront(self, item):
        link = ListItem(item)
        if self.front == None:
            self.front = link
        else:
            link.next = self.front
            self.front = link
            
    def addToBack(self, item):
        self.current = self.front
        while True:     
            if self.current.next == None:
                self.current.next = ListItem(item)
                break
            else:
                self.current = self.current.next

    def removeFromFront(self):
        print self.front.data
        self.front = self.front.next

    def addToPosition(self, position, item):
        self.current = self.front
        for i in range(position-1):
            self.current = self.current.next
        temp = self.current.next
        self.current.next = ListItem(item)
        self.current = self.current.next
        self.current.next = temp
            
            

    def printTheList(self):
        self.current = self.front
        while True:
            print self.current.data
            if self.current.next == None:
                break
            else:
                self.current = self.current.next
##############################################            
def Main():

    newlist = LinkedList()

    newlist.addToFront(30)
    newlist.addToFront(15)
    newlist.addToFront(45)
    newlist.addToFront(85)

    newlist.addToBack(35)
    newlist.addToBack(10)

    newlist.addToPosition(2, 40)
    newlist.addToPosition(4, 67)

    newlist.removeFromFront()

    newlist.printTheList()

##################################
Main()
