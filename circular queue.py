### circular queue
#we start with a list of some fix size
#when dequeing we empty that place in list with None
#when we have to add elements we add as if there is no end to the list i.e circular

class circular_queue:
    def __init__(self,max_size=10):
        self.items=[None]*max_size
        self.count=0  #no. of elements in the queue
        self.front=0   #front

    def enqueue(self,item):
        if self.count==len(self.items):     ##resizing queue
            self.resize(2*len(self.items))
        i=(self.front+self.count)%len(self.items)
        self.items[i]=item
        self.count+=1
    
    def dequeue(self):
        x=self.items[self.front]
        self.items[self.front]=None
        self.front=(self.front+1)%len(self.items)
        self.count-=1
        return x
    


    def size(self):
        return self.count

    def is_empty(self):
        return self.count==0

    def peek(self):
        if self.is_empty():
            print("fuck off")
            return
        return self.items[self.front]

    def display(self):
        print(self.items)  ##doubt about how it will work...

    def resize(self,newsize):
        old_list=self.items   ###is there a different way to do this??
        self.items=[None]*newsize    ##changing the list to a none list of new size
        i=self.front     ##imp line 1
        for j in range(self.count):
            self.items[j]=old_list[i]   ## from imp line 1 we get that all the elements of the QUEUE NOT LIST WILL BE COPIED TO THE NEW LIST from starting j='0'
            i=(i+1)%len(old_list)  ## moving just like we were moving front in dequeue

        self.front=0  ## as the changed list will have eleements starting from 0

################################


q=circular_queue()
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
        item=input("Enter element")
        q.enqueue(item)
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
        
        
        
