#### linked list implementation of Queue

class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
    
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def enqueue(self,data):
        temp=Node(data)
        if self.is_empty():   ##insertion in empty list
            self.front=temp
            self.rear=temp
            self.count+=1
            return
        else:         ##insertion at end
            self.rear.link=temp  #last elements link points to temp
            self.rear=temp
            self.count+=1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty cant perform dequeue")
            return
        else:
            deleted_item=self.front.info  ##to return this
            self.front=self.front.link
            self.count-=1
            return deleted_item

    def size(self):
        return self.count

    def is_empty(self):
        return self.count==0

    def peek(self):
        return self.start.info

    def display(self):
        p=self.front

        while p is not None:
            print(p.info,end="|")
            p=p.link

##########################################

q=queue()
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
        data=input("Input element:")
        q.enqueue(data)
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


            
        
            
            
        
        
