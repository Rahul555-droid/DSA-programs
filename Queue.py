#####Queue array implementation

class EmptyQError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items=[]
        self.front=0

    def is_empty(self):
        return len(self.items)==self.front  

    def size(self):
        return len(self.items)-self.front
        
    def enqueue(self):
        data=input("Enter value to enque:")
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQError("Queue is Empty")

        x=self.items[self.front]
        self.items[self.front]=None  ## imp line 1
        self.front+=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQError("Queue is Empty")
        
        return self.items[self.front]
        
    def display(self):
        print(self.items,end="|")        ## from imp line 1
        
        ## we can also use this
        for i in self.items:
            print(i)
            
        

q=Queue()
x=  """
    1.Enqueue
    2.Dequeue
    3.size
    4.Empty(t/f)
    5.peek
    6.display
    7.quit

    """



while True:
    print(x)
    o=int(input("Enter option:"))
    if o==1:
        q.enqueue()
    elif o==2:
        print(q.dequeue())
    elif o==3:
        print(q.size())
    elif o==4:
        print(q.is_empty())
    elif o==5:
        print(q.peek())
    elif o==6:
        q.display()
    elif o==7:
        break
    else:
        print("\n wrong input \n")
        

