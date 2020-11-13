class InvalidOperation(Exception):
    pass

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


class HashTable:

    def __init__(self,tablesize=11):
        self.m=tablesize
        self.array=[None]*11
        self.n=0   ## no. of keys i guess

    def hash1(self,key):
        return (key%self.m)

    def insert(self,newrec):   ##newrec is an object of class StudentRecord
        key=newrec.get_student_id()    ##bina method ke v access kr sakte hai obviously.... newrec.id
        h=self.hash1(key)  ##address in hash table

        location=h
        for i in range(1,self.m):
            if self.array[location] == None or self.array[location].get_student_id()==-1:    ##-1 is a flag for deleted element address
                self.array[location]=newrec   ##storing objects of studentrecords in array
                self.n+=1
                return

            if self.array[location].get_student_id()==key:
                raise InvalidOperation("Duplicate Key")

            location=(h+i)%self.m  ##linear hashing bakloli

        print("Table is Full:Record can't be inserted")

    def search(self,key):
        h=self.hash1(key)
        location=h

        for i in range(1,self.m):
            if self.array[location].get_student_id()==key:
                return location   ##returns location of the found record
            if self.array[location]==None:
                return None  ##encountered an empty loc
            location=(h+i)%self.m
        return None  ##pura dekha but kuch ni mila

    def delete(self,key):
        location=self.search(key)

        if location==None:
            print("Element not present")
            return None

        else:
            self.n-=1
            temp=self.array[location]
            self.array[location].set_student_id(-1)   ##flaggingit as deleted element
            return temp

    def display(self):
        for i in range(self.m):
            print("[",i,"]",end="")
            if self.array[i] is not None and self.array[i].get_student_id() != -1:
                print(self.array[i])
            else:
                print("_____")

########################################


ht=HashTable()

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
            print(ht.array[ht.search(key)])        ##ht.search gives loc and ht.array[...] gives us the object and printing of that object due to __str__() gives us nirvana

    elif o==3:
        key=int(input("enter the key or student id:"))
        ht.delete(key)

    elif o==4:
        ht.display()

    elif o==5:
        break

    else:
        print("Wrong input")

##try rehashing         
