class Node:
    def __init__(self,data):
        self.info=data
        self.next=None
        self.prev=None



class DoubleLinkedList:
    def __init__(self):
        self.start=None

    def create_list(self):
        n=int(input("Enter no. of nodes:"))

        if n==0:
            return
        else:
            for i in range(1,n+1):
                if i%10==1:
                    print("Enter",i,"st element")
                elif i%10==2:
                    print("Enter",i,"nd element")
                elif i%10==3:
                    print("Enter",i,"rd element")
                else:
                    print("Enter",i,"th element")
                data=input()
                self.insert_at_end(data)

    def display_list(self):
        if self.start is None:
            print("\n\nList is Empty\t\n")
            #return
        else:
            p=self.start               
            while p is not None:        
                print(p.info,end=",")
                p=p.next
            print()
            
    def count_nodes(self):
        count=0
        if self.start is None:
            return count
        else:
            p=self.start
            while p is not None:
                p=p.next
                count+=1
            return count
        

    def display_list_rev(self):
        if self.start is None:
            print("\n\nList is Empty\t\n")
        else:
            p=self.start
            while p.next is not None:
                p=p.next
            while p is not None:
                print(p.info,end=",")
                p=p.prev
            
            print()
                
        

    def insert_at_beginning(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        else:
            self.start.prev=temp   #order is important for allof them
            temp.next=self.start
            self.start=temp
            
            return
        

    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
        else:
            p=self.start
            while p.next is not None:
                p=p.next
            p.next=temp
            temp.prev=p
        

    def insert_before(self,x,data):  ##havent wrked on corner cases in insert_after and insert_before and insert_at methods...
        p=self.start
        temp=Node(data)
        while p is not None:
            if p.next.info==x:
                break
            p=p.next
        ##rather than using next i can use prev tooo at most next's places
        temp.next=p.next
        temp.prev=p
        p.next=temp
        temp.next.prev=temp
        

    def insert_after(self,x,data):
        p=self.start
        temp=Node(data)
        while p is not None:
            if p.info==x:
                break
            p=p.next
        temp.next=p.next
        temp.prev=p
        p.next=temp
        temp.next.prev=temp
        
        
            

    def insert_at(self,pos,data):
        temp=Node(data)
        i=1
        p=self.start
        for i in range(pos-2):          #kyonki mujhe p ko next pos-2 times hi karna hoga start se
            p=p.next                  # i got p before position mentioned

        temp.next=p.next
        temp.prev=p
        p.next=temp
        temp.next.prev=temp
            
        
            
        

    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print("\n Element is at:",position)
                break
            position+=1
            p=p.next
        else:
            print(x,"\n ELement not found \n")

    def delete_first(self):
        ### deletion for case of only single element IS NOT DONE
            

        self.start=self.start.next
        self.start.prev=None

    def delete_last(self):
        p=self.start
        while p.next.next is not None:  #will give us the second last Node
            p=p.next

        p.next=None
        
    def delete(self,x):
        p=self.start
        while p is not None:
            if p.next.info == x:           ###corner cases not worked upon
                break
            p=p.next
        p.next=p.next.next
        p.next.prev=p

    def reverse(self):
        """
        need to review reversing in linked lists rightlyyy
        """
        if self.start is None:
            return

        p1=self.start
        p2=p1.next
        p1.next=None
        p1.prev=p2
        while p2 is not None:
            p2.prev=p2.next
            p2.next=p1
            p1=p2
            p2=p2.prev
        self.start=p1

    
############################################
list=DoubleLinkedList()
list.create_list()

while True:
    print("\n\n")
    print(5*"#*#"+" LINKED LIST "+5*"#*#")
    print("1.display list")
    print("2.Count number of nodes")
    print("3.search for an element")
    print("4.Insert in empty list/insert in beggining of list")
    print("5.Insert a node at the end of a list")
    print("6.Insert a node after a specified node")
    print("7.Insert a node before a specified node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10.Delete last node")
    print("11.delete any node")
    print("12.print list in reverse order,without changing the list")
    print("13.reverse List")
    print("14.QUIT")

    o=int(input("\n\nEnter from above OPTIONSSS:"))

    if o==1:
        list.display_list()
    elif o==2:
        print("No. of nodes is:",list.count_nodes())
    elif o==3:
        x=input("Enter element to be searched:")
        list.search(x)
    elif o==4:
        data=input("Enter the element's data:")
        list.insert_at_beginning(data)
    elif o==5:
        data=input("Enter element's data:")
        list.insert_at_end(data)
    elif o==6:
        x=input("enter element after which you want to insert data:")
        data=input("Enter your element's data:")
        list.insert_after(x,data)
    elif o==7:
        x=input("enter element after which you want to insert data:")
        data=input("Enter your element's data:")
        list.insert_before(x,data)
    elif o==8:
        pos=int(input("Enter the position where you want to insert the element:"))
        data=input("Enter your element's data:")
        list.insert_at(pos,data)
    elif o==9:
        list.delete_first()
    elif o==10:
        list.delete_last()
    elif o==11:
        x=input("Enter element you want to delete:")
        list.delete(x)
    elif o==12:
        list.display_list_rev()
    elif o==13:
        list.reverse()
    elif o==14:
        break
    else:
        print("\t\t Wrong Option TRY AGAIN.... \n\n")
        
        

        
