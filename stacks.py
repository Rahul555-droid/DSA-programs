

##### array implementation of stack#######
"""
###python list

class empty_stack_error(Exception):
    pass

class stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        if len(self.items)==0:         ###or could use self.items == []
            return True
        else:
            False

    def size(self):
        return len(self.items)

    def push(self):
        x=input("Enter element to push:")
        self.items.append(x)

    def pops(self):
        self.items.pop()

    def peek(self):
        print(self.items[-1])

    def show(self):
        if self.size() == 0:
            print("STACK IS EMPTY")
        for i in range(self.size()):
            print(self.items[i],end=" ")         ##could have used print(self.items)

    #######################################


a=stack()
x="""
"""
    ######STACK########
    1.Show stack
    2.push element
    3.pop element
    4.peek(get TOP element)
    5.size of stack
    6.is stack empty(TRUE OR FALSE)
    7.quit
    """
"""

while True:
    print(x)
    o=int(input("Input Option:"))
    if o==1:
        a.show()
    elif o==2:
        a.push()
    elif o==3:
        if a.size()==0:
            print("STACK IS EMPTY POP CANNOT BE DONE")
        print("pop has been done")
        a.pops()
    elif o==4:
        a.peek()
    elif o==5:
        print(a.size())
    elif o==6:
        print(a.is_empty())
    elif o==7:
        break
    else:
        print("WRONG INPUT")
    
"""

"""

### actual array###     ### this implementation is better as we will have a size of arrray fixed rather than appending at the end of list..as this implementation
                        ### appending n items will take O(n) as(n*O(1)) and if we have fixed size then it is just a different way

class StackEmpty(Exception):
    pass

class StackFull(Exception):
    pass



class stack:
    def __init__(self,max_size=10):           ###we can't use push and pop like pylist will have to use current position of top to do that
        self.items=[None]*max_size
        self.max_size=max_size
        self.count=0
        
    def size(self):
        return self.count

    def is_empty(self):
        return self.count==0

    def is_full(self):
        return self.count==self.max_size

    def push(self,x):
        if self.is_full():
            raise StackFull("Stack is Full")
        self.items[self.count]=x
        self.count+=1        ###count badhaya h
        
            

    def pop(self):
        if self.is_empty():
            raise StackEmpty("Stack is Empty")
        x=self.items[self.count-1]
        self.items[self.count-1]=None        ###upar(push) dekh if doubt...
        self.count-=1
        return x

    def peek(self):
        print(self.items[self.count-1])

    def show(self):
        if self.size() == 0:
            print("STACK IS EMPTY")
        for i in range(self.size()):
            print(self.items[i],end="|")

a=stack()
x="""
"""
    ######STACK########
    1.Show stack
    2.push element
    3.pop element
    4.peek(get TOP element)
    5.size of stack
    6.is stack empty(TRUE OR FALSE)
    7.quit
  """
"""

while True:
    print(x)
    o=int(input("Input Option:"))
    if o==1:
        a.show()
    elif o==2:
        x=input("ENTER ELEMENT")
        a.push(x)
    elif o==3:
        a.pop()
    elif o==4:
        print("TOP ELEMENT IS:",a.peek())
    elif o==5:
        print("SIZE OF STACK:",a.size())
    elif o==6:
        print(a.is_empty())
    elif o==7:
        break
    else:
        print("WRONG INPUT")

"""

### Linked list implementation###
from LinkedList import LinkedList,node   ##try import *

k=LinkedList()

class stack:
    def push(self):
        k.insert_in_beggining()

    def pop(self):
        k.delete_node_first()

    def show(self):
        k.display_list()

    def IsEmpty(self):
        return k.count_nodes()==0

    def peek(self):
        top=k.start
        return top.info
    

st=stack()
a=  """
    1.push
    2.pop
    3.show
    4.stack Empty or not
    5.PEEK
    6.QUIT
    """


while True:
    print(a)
    o=int(input("Enter from above"))
    if o==1:
        st.push()
    elif o==2:
        st.pop()
    elif o==3:
        st.show()
    elif o==4:
        print(st.IsEmpty())
    elif o==5:
        print("Top element is:",st.peek())
    elif o==6:
        break
    else:
        print("\n\n WRONG INPUT\n")


        




