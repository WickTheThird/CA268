#Q1

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_n_items(self, items):
        
        if len(items) < 2:
            return None
        
        node = Node(items[0])
        self.head = node

        for val in items[1:]:
            if val % 2 == 0:
                node.next = Node(val)
                node = node.next

    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data, ' ', end = '') 
            temp = temp.next
        print("")

#Q2

class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList2:
    def __init__(self):
        pass

#Testing all the questions

if __name__ == '__main__':

    #Testing Q1
    #test = LinkedList()
    #items = [i for i in range(0, 100)]
    #test.add_n_items(items)
    #test.printList()

    #Testing Q2
    

    pass

