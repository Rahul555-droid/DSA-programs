class node:
    def __init__(self,data):
        self.info=data
        self.link=None

class LinkedList:
   
                
    
    def __init__(self):
        self.start=None

    def display_list(self):
        if self.start is None:
            print("\n\nList is Empty\t\n")
            #return
        else:
            p=self.start                #p is a reference
            while p is not None:        #at the end p will point to None or NULL
                print(p.info,end=",")
                p=p.link
            print()
    def count_nodes(self):
        count=0
        p=self.start
        while p is not None:
            p=p.link
            count=count+1
        return count
    
    def insert_in_beggining(self,data):
        data=input("Enter value:")
        temp=node(data)
        if self.start is None:
            self.start=temp
            return
        else:
            temp.link=self.start
            self.start=temp

    def insert_at_end(self,data):
        temp=node(data)

        if self.start is None:
            self.start=temp
        else:
            p=self.start
            while p.link is not None:            ## yeh p.link no=iche wale p ka p.link nhi hai balki yeh (p=p.link).link h
                p=p.link
            ##after exec of while loop p.link will become None
            p.link=temp   #end node will now be temp

    def create_list(self):
        n=int(input("Insert the no. of element:"))
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

   

    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print("\n Element is at:",position)
                break
            position+=1
            p=p.link
        else:
            print(x,"\n ELement not found \n")

    def insert_after(self,x,data):
        temp=node(data)
        p=self.start
        while p is not None:

            if p.info==x:
                break
            p=p.link
            
        temp.link=p.link
        p.link=temp                     #why does this work

    def insert_before(self,x,data):
        temp=node(data)
        p=self.start
        if p.info==x:               #for inserting before first element 
            temp.link=self.start
            self.start=temp
            return
        while p is not None:         #using p.link  in while loop wont make much diference as we break loop at p.link.info that is p will element before "x" in original linked list
            if p.link.info==x:
                break
            p=p.link
        temp.link=p.link
        p.link=temp                     #why does this work
        

    def insert_at_pos(self,pos,data):
        temp=node(data)
        p=self.start
        i=1
        while i <pos-1 and p is not None:       #at the end of loop i==pos-1 and p will be referring to node at pos-1
            p=p.link
            i+=1

        if i==1:
            
            temp.link=self.start
            self.start=temp
            """
            temp.link=p
            p=temp
            """
            return
        
        temp.link=p.link
        p.link=temp               #why does this work..........maybe it doesnt work only when p is "start"
        


    def delete_node_first(self):
        if self.count_nodes()==1:    #with single node only present
            self.start=None
            
        else:
            
            self.start=self.start.link    #without using reference p
            """
            p=self.start          ### with using referecnce p same as above
            self.start=p.link
            """
    def delete_node_last(self):
        if self.count_nodes()==1:
            self.start=None
            
        else:
            p=self.start
            while p.link.link is not None:       ####2nd last ke liye p.link.link
                p=p.link
            p.link=None
            
        
        
    def delete_node(self,x):
        p=self.start
        while p is not None:
            if p.link.info==x:            ###this gives us "p" or node before x
                break
            p=p.link
        p.link=p.link.link          ######no need to give a fuck about next node to p
        
        
        

    def reverse_list(self):
        prev=None
        p=self.start
        while p is not None:
            next=p.link           #cos it is "next" node reference byotch
            p.link=prev           #p.link points to the previous node,we are  changing link of p hereeeee
            prev=p                #setting prev to p before setting p to next
            p=next              ###p and next will point to the nexter node
        self.start=prev


        
    def bubble_sort_ed(self):
        end=None
        while end != self.start.link:         ### as end will point to second element of list when sorting finishes
            p=self.start
            while p.link != end:             ###a single pass ends when end and plink becomes same or point to same...
                q=p.link                     ###q is next to p
                if p.info>q.info:
                    p.info,q.info=q.info,p.info       ###swapping   ####the data is being swapped the position of nodes remain the same
                p=p.link 
            end=p                ###will make end move from last node to first

    def bubble_sort_el(self):
        self.bubble_sort_ed()         ##do it when you know it
            
    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def insert_cycle_at(self,x):
        pass

    def remove_cycle(self):
        pass

    

    def _mergeto(self,p1,p2):  #assigninng p1 and p2 references to the starts of list 1 and list 2
        if p1.info<=p2.info:
            startM=node(p1.info) 
            p1=p1.link     #moving the original list  reference forward the smaller first noded list will stay at the same place
        else:
            startM=node(p2.info)
            p2=p2.link

        pM=startM                #pM is reference for merge_list just like p was for list

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = node(p1.info)  
                p1=p1.link
            else:
                pM.link=node(p2.info)
                p2=p2.link
            pM=pM.link           #agar pM=pM.link nhi likhu toh pM.link overwrite hota rahega chu

        while p1 is not None:
            pM.link=node(p1.info)
            p1=p1.link
            pM=pM.link

        while p2 is not None:
            pM.link=node(p2.info)
            p2=p2.link
            pM=pM.link

        return startM            #start hi toh baaap h sabkaaa

    def mergeto(self,list2): #will pass a list object
        merge_list=LinkedList()  #creates another linked list "object" merge_list,whose start will be None which gets changed in next line line
        merge_list.start=self._mergeto(self.start,list2.start)       ##here self is first list ......merge list ke start ki bakchodi ho ri h
        return merge_list

  

    def _mergech(self,p1,p2):
        if p1.info<=p2.info:
            startM=p1
            p1=p1.link
        else:
            startM=p2
            p2=p2.link

        pM=startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                pM=pM.link           #####this statement is different from mergeto wala segment,here pM ko move krte to the position of p1 or p2.
                p1=p1.link
            else:
                pM.link=p2
                pM=pM.link
                p2=p2.link
                      

        if p1 is not None:
            pM.link=p1
            

        if p2 is not None:
            pM.link=p2
            

        return startM

    def mergech(self,list2):
        merge_list=LinkedList()
        merge_list.start=self._mergech(self.start,list2.start)
        return merge_list


list1=LinkedList()
list1.create_list()

list2=LinkedList()
list2.create_list()

print("List 1 is:")
list1.display_list()
print("list 2 is :")
list2.display_list()
print("list 3 is:")
merge_list=list1.mergech(list2)
merge_list.display_list()
