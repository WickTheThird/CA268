# NOTE: i will try to rewrite the implementation for wither queue or satks myself
# NOTE: i will also try to rewrite them for each question if possible in order for me to better understand

#Q1

class Queue:

    def __init__(self):
        self.items = []

    def front(self):
        return self.items[-1]

    def rear(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def empty(self):
        return (self.items == [])

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self, item=  -1):
        if self.size() == 0:
            return None
        return self.items.pop(item)
    
    # reverse the k elements given k
    # in case there is no k given, the k will default to the front ;)
    def reverse(self, k=None):

        if k == 0 or self.empty():
            return

        if k is None:
            k = self.size() - 1

        tmp = self.items[k]
        self.dequeue(k)
        self.reverse(k - 1)
        self.enqueue(tmp)

# recursively ordering the elements of the queue

def frontToLast(el, size):

    if size <= 0:
        return
    
    el.enqueue(el.dequeue())

    frontToLast(el, size - 1)

def pushIn(el, tmp, size):

    if el.empty() or size == 0:
        el.enqueue(tmp)
        return
    elif tmp <= el.front():
        el.enqueue(tmp)
        frontToLast(el, size)
    else:
        el.enqueue(el.dequeue())
        pushIn(el, tmp, size - 1)

# this empties the queue and then sends 
# items one by one to test and compare to the from
# wich constantly changes till the queue is ordered
def sorting(el):

    if el.empty():
        return
    
    tmp = el.dequeue()

    sorting(el)

    pushIn(el, tmp, el.size())



#Q2

class Queue2:

    def __init__(self):
        self.items = []
    
    def front(self):
        return self.items[-1]
    
    def rear(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    
    def empty(self):
        return (self.items == [])
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, item = -1):
        if self.empty() or self.size() == 0:
            return None
        return self.items.pop(item)
    
    def reverse(self, k=None):

        if k == 0 or self.empty():
            return

        if k is None:
            k = self.size() - 1

        tmp = self.items[k]
        self.dequeue(k)
        self.reverse(k - 1)
        self.enqueue(tmp)
    
    # The function

    def bin_enqueue(self, n=0):

        bin_nr = bin(n)[2:]

        if n == 0:
            return bin_nr

        tmp = bin_nr
        self.bin_enqueue(n - 1)
        self.enqueue(tmp)
        self.reverse()


#Q3


class Stack:

    def __init__(self):
        self.items = []
    
    def top(self):
        if self.empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return (self.items == [])
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self, item = -1):
        if self.empty():
            return None
        return self.items.pop(item)
    
    def special_push(self, item):

        all_poped = []

        for i in item:

            if i == '*':
                all_poped.append(self.pop())
            else:
                self.push(i)

        return all_poped

#Q4

class Queue3:

    def __init__(self):
        self.items = []
    
    def front(self):
        return self.items[-1]
    
    def rear(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return (self.items == [])
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self, item =  -1):
        return self.items.pop(item)
    
    def special_enqueue(self, item):

        all_dequeues = []

        for i in item:

            if i == '*':
                all_dequeues.append(self.dequeue())
            else:
                self.enqueue(i)

        return all_dequeues

#Q5

class  Stack2:

    def __init__(self):
        self.items = []
    
    def top(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def empty(self):
        return (self.items == [])
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self, item = -1):
        if self.empty():
            return None
        return self.items.pop(item)

    def reverse(self, item):

        for i in item:
            self.push(i)
        
        self.items = self.items[::-1]

        return "".join(self.items)
        

#Q6

# Python program to evaluate value of a postfix
# expression with integers containing multiple digits

class Stack3:
    def __init__(self):
        self.stack = []
        self.top =-1

    def pop(self):
        if self.top ==-1:
            return
        else:
            self.top -= 1
            return self.stack.pop()

    def push(self, i):
        self.top += 1
        self.stack.append(i)

    def centralfunc(self, ab):
        for i in ab:

            try:
                self.push(int(i))

            except ValueError:

                val1 = self.pop()
                val2 = self.pop()

                if i == '/':
                    self.push(val2 / val1)

                else:	
                    switcher = {'+':val2 + val1, '-':val2-val1, '*':val2 * val1, '^':val2**val1}
                    self.push(switcher.get(i))

        return int(self.pop())


# This code is contributed by Amarnath Reddy


# this is where all the testing will happen

if __name__ == '__main__':

    # Test Q2
    #el = Queue2()
    #print(el.items)
    #el.bin_enqueue(16)
    #print(el.items)

    # Test Q3
    #el = Stack()
    #print(el.special_push('EAS*Y*QUE***ST***IO*N***') == ['S', 'Y', 'E', 'U', 'Q', 'T', 'S', 'A', 'O', 'N', 'I', 'E'])

    #Test Q4
    #el = Queue3()
    #print(el.special_enqueue('EAS*Y*QUE***ST***IO*N***') == ['E', 'A', 'S', 'Y', 'Q', 'U', 'E', 'S', 'T', 'I', 'O', 'N'])

    #Test Q5
    #el = Stack2()
    #test = "bonjour mon cheri"
    #print(test)
    #print(el.reverse(test))

    #Test Q6
    #el = Stack3()
    #print(el.centralfunc("1432^*+147--+") == 41)

    pass