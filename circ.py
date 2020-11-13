
#####Circular Linked List




class Node:
    def __init__(self,data):
        self.info=data
        self.link=None

class circular_LL:
    def __init__(self):
        self.last=None
        self.count=0

    def create_list(self):
        n=int(input("ENter no. of nodes you want:"))
        if n==0:
            return
        else:
            i=1
            while i<=n:
                       ##shit that i do
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
                i+=1
        

    def display_list(self):
        if self.last==None:
            print("List is empty")
            return
        else:
            p=self.last.link

            while True:
                print(p.info,end=" ")
                p=p.link
                if p==self.last.link:
                    break
            print()

    def insert_at_beginning(self,data):
        temp=Node(data)
        self.count+=1
        if self.last == None:    ##insertion in empty list
            self.last=temp
            temp.link=temp
            
        
        temp.link=self.last.link
        self.last.link=temp

    def insert_at_end(self,data):
        temp=Node(data)
        self.count+=1
        if self.last == None:
            self.last=temp
            temp.link=temp
            
        
        temp.link=self.last.link
        self.last.link=temp
        self.last=temp

    def delete_first(self):
        if self.last == None:
            print("List empty,cannot be deleted")
            return
        elif self.count ==1:
            self.last=None
            self.count-=1
        else:
            self.last.link=self.last.link.link
            self.count-=1
            
            

    def delete_last(self):
        if self.last == None:
            print("List empty,cannot be deleted")
            return
        elif self.count ==1:
            self.last=None
            self.count-=1
        else:
            p=self.last
            while True:  ##no need to write p is not none
                p=p.link
                if p.link == self.last:
                    break
            p.link=self.last.link
            self.last=p
            self.count-=1
            
            
            
            
            

    def delete(self):
        ###wwhy does it print x again when i m taking input "x" from main()???  answer found boi
        x=input("Enter value to delete :")
        if self.last == None:
            print("List empty cannot be deleted")
            
        elif self.count==1:
            if self.last.info==x:
                self.last=None
            else:
                print("Element not a part of list")

        else:
            p=self.last
            inf_count=0   ### infinite count is used to figure if loop doesnt breakkkss and goes till infinite when we are not able to find the element
            while True:
                inf_count+=1
                if p.link.info==x:        ###this works but how to search an element in a circular linked list
                    break
                p=p.link
                if inf_count > self.count:   ##imp
                    print("Element Not Found in the list")
                    return  ###cos by this there wont be made any changes

            p.link=p.link.link
            self.count-=1
            

def main():
    a=circular_LL()
    a.create_list()
    x=  """
    \n\t#####CIRCULAR LINKED LIST########\n
    1.Insert at beginning
    2.insert at end
    3.display
    4.delete first node
    5.delete last node
    6.delete specific node
    7.Get size of list
    8.Quit
    """
    
    while True:
        print(x)
        o=input("Enter Option:")
        if o=="1":
            data=input("Enter Data:")
            a.insert_at_beginning(data)
        elif o=="2":
            data=input("Enter Data:")
            a.insert_at_end(data)
        elif o=="3":
            a.display_list()
        elif o=="4":
            a.delete_first()
        elif o=="5":
            a.delete_last()
        elif o=="7":
            print("No. of node is ",a.count)
        elif o=="6":
            #x=input("enter element:")   ###o ki value 7 hi hai aur loop terminate nhi hua h isiliye we get x printed over and overrrrr
            a.delete()
        elif o=="8":
            break
        else:
            print("Wrong Input")


if __name__ == "__main__":
    main()
