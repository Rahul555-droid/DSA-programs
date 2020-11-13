class StudentRecord:   ##makes a single students record or details...
    def __init__(self,i,name):
        self.id=i
        self.name=name

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.id

    def set_student_id(self,i):  ##to change id.......method ke bina v  change ho sakta h
        self.id=i

    def __str__(self):  ## __str__ used to print objects in a way we want otherwise error...
        return str(self.id) + " " + self.name

######################################
class Node:
    def __init__(self,data):
        self.info=data
        self.link=None

class SingleLinkedList:
    def __init__(self):
        self.start=None

    def display_list(self):
        if self.start is None:
            print("____")

        p=self.start
        while p is not None:
            print(p.info,end=" ")
            p=p.link
        print()

    def search(self,x):
        p=self.start
        while p is not None:
            if p.info.get_student_id() == x:
                return p.info
            p=p.link

        return None

    def insert_in_beginning(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
        else:
            temp.link=self.start
            self.start=temp

    def delete(self,x):
        if self.start is None:
            print("List is Empty")
            return None

        if self.start.info.get_student_id()==x:  ##first node is the element
            self.start=self.start.link

        p=self.start

        while p.link is not None:
            if p.link.info.get_student_id()==x:
                break
            p=p.link

        if p.link is None:   ##loop khatam ho gaya lekin last element tak search nhi hua so element is not in the list
            print("Element",x,"not in the list")
        else:
            p.link=p.link.link

######################################

class HashTable:
    def __init__(self,TableSize):
        self.m=TableSize
        self.array=[None]*self.m
        self.n=0

    def hash(self,key):
        return key%self.m

    def display_table(self):
        for i in range(self.m):
            print("[",i,"]  --->  ",end="")
            if self.array[i]!=None:
                self.array[i].display_list()
            else:
                print("_____")

    def search(self,key):
        location=self.hash(key)
        if self.array[location]!=None:
            return self.array[location].search(key)
        else:
            return None

    def insert(self,newrec):
        key=newrec.get_student_id()
        location=self.hash(key)
        if self.array[location]==None:  ##pehli pehli baar hua 17 18 saalon mein
            self.array[location]=SingleLinkedList()
        self.array[location].insert_in_beginning(newrec)
        self.n+=1

    def delete(self,key):
        location=self.hash(key)
        if self.array[location]!=None:
            self.array[location].delete(key)
            self.n-=1
        else:
            print("value",key,"is not present")

###############################################

size=int(input("Enter size of hash table:"))
ht=HashTable(size)

c="""
    1.Insert
    2.Search
    3.Delete
    4.Display
    5.Quit
"""

while True:
    print(c)
    o=int(input("Enter an option:"))

    if o==1:
        i=int(input("enter Id:"))
        name=input("Enter name:")
        sr=StudentRecord(i,name)
        ht.insert(sr)

    elif o==2:
        key=int(input("enter the key or student id:"))
        if ht.search(key)==None:
            print("record not found")
        else:
            print(ht.search(key))       

    elif o==3:
        key=int(input("enter the key or student id:"))
        ht.delete(key)

    elif o==4:
        ht.display_table()

    elif o==5:
        break

