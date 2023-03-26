#Q1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def zero_to_a_hundred(self):

        self.head = Node(0)

        node = self.head
        for i in range(1, 100):
            node.next = Node(i)
            node = node.next

    def print_ll(self):

        node = self.head
        while node != None:
            print(node.data)
            node = node.next

#Q2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def find(self, name):

        node = self
        while node!= None:
            if node.data == name:
                return node
            node = node.next

        return None


#Q3

def reverse(node):

    if node is None or node.next is None:
        return node

    info = reverse(node.next)

    node.next.next = node
    node.next = None

    return info

#Q4

class SwapNodes:
    
    def swapPairs(self, head):
        
        tmp = Node(0)
        tmp.next = head

        node = tmp

        while node.next is not None and node.next.next is not None:

            e1 = tmp.next
            e2 = tmp.next.next

            e1.next = e2.next
            tmp.next = e2
            tmp.next.next = e1

            tmp = tmp.next.next
        
        return tmp.next
    
    def print_ll(self, head):

        node = head
        while node != None:
            print(node.data)
            node = node.next

# Q5

def remove(head, n):

    fast = slow = head

    for i in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

# Testing for this lab will happen below...

if __name__ == '__main__':

    '''
    Test Q1

    test = LinkedList()
    test.print_ll()
    test.zero_to_a_hundred()
    test.print_ll()
    
    Test Q2

    head = Node("Dublin")
    another_node = Node("Galway")
    head.next = another_node
    a_third_node = Node("Cork")
    another_node.next = a_third_node

    result = head.find("Galway")
    print(result.data)

    Test Q3

    head = Node("Dublin")
    another_node = Node("Galway")
    head.next = another_node
    a_third_node = Node("Cork")
    another_node.next = a_third_node
    reversed_linked_list = reverse(head)

    Test Q4

    swap = SwapNodes()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    swap.printList(head)

    Test Q5

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    output = remove(head, 3)

    '''



    pass
