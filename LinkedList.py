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
            count+=1 
        return count
    
    def insert_in_beggining(self):
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
            while p.link is not None: ## yeh p.link no=iche wale p ka p.link nhi hai balki yeh (p=p.link).link h
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
        p.link=temp                     #why does this work,Now i know

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
        try:
            while p is not None:
                if p.link.info==x:            ###this gives us "p" or node before x
                    break
                p=p.link
            p.link=p.link.link          ######no need to give a fuck about next node to p
        except:
            print(f"node with value {x} doesn't exist")
        
        

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
        end=None
        while end != self.start.link:
            r=p=self.start
            while p.link != end:
                q=p.link
                if p.info > q.info:
                    p.link = q.link  ## imagine how links would change 
                    q.link = p
                    
                    ## agar p self.start hi raha to r.link will be same as p.link
                    ## and hence use self.start IMAGINE LL!
                    
                    if p == self.start :  
                        self.start=q
                    else:  
                        r.link = q
                    p,q=q,p  ## link se toh original nodes swap hue references nhi
                    ## isiliye references ko swap kiya  ...to be honest think I dont know
                r=p
                p=p.link
            end=p

    

    def _mergeto(self,p1,p2):  
#assigninng p1 and p2 references to the starts of list 1 and list 2
        if p1.info<=p2.info:
            startM=node(p1.info) 
            p1=p1.link     
#moving the original list  reference forward the smaller first noded list will stay at the same place
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

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.link is None:   #we need 2 nodes atleast for a cycle
            return None
        else:
            slow=self.start   #initialising 2 references
            fast=self.start

            while fast is not None and fast.link is not None:        #cycle mein hi ghomta rahega tab tak,,,,trying with slow failed finout why?..
                slow=slow.link
                fast=fast.link.link
                if slow==fast:
                    return slow
            return None

    
    def remove_cycle(self):
        c=self.find_cycle()
        if c is None:
            return
        print("Node at which cycle is detected is:",c.info)  #this c is just a part of cycle nothing special about it

        p=c
        q=c
        len_cycle=0

        while True:
            len_cycle+=1
            q=q.link
            if p==q:
                break

        print("Length of cycle is:",len_cycle)
        
        len_rem_list=0
        p=self.start      #initial point pe bhej diya p ko
        while p!=q:
            len_rem_list+=1
            p=p.link
            q=q.link

        print("no. of nodes not included in the list",len_rem_list)
        """

        len_extra=0
        x=1
        p=self.start

        while True:
            p=p.link                    ###why does this method not work????
            len_extra+=1

            if p==q and x==1:
                x=0
                continue
            else:
                break
        
        len_list=len_extra-len_cycle
        """
        len_list=len_rem_list+len_cycle
        print("Length of list",len_list)

        p=self.start
        for i in range(len_list-1):
            p=p.link
        p.link= None

        

    def insert_cycle_at(self,x):
        if self.start is None:
            return
        p=self.start
        px=None
        prev=None

        while p is not None:
            if p.info==x:
                px=p      #px is node at which we want to insert cycle
            prev=p        #behind p at each iteration
            p=p.link

        if px is not None:
            prev.link=px
        else:
                print(x,"not present in the list")

    


######################################################################



def main():
    list=LinkedList()
    list.create_list()

    while True:
        
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
        print("12.reverse a list")
        print("13.bubble sort by exhanging data")
        print("14.bublbe sort by exchanging links")
        print("15.create another linked list and merge them by exhanging data only")
        print("16.Insert cycle")
        print("17.Detect or find cycle")
        print("18.remove cycle")
        print("19.quit")

        option=int(input("Enter from above option:"))

        if option==1:
            list.display_list()
            
        elif option==2:
            k=list.count_nodes()
            print("No. of nodes:",k)
        elif option==3:
            x=input("Enter element to be searched:")
            list.search(x)
        elif option==4:
            list.insert_in_beggining()
        elif option==5:
            data=input('enter element:')
            list.insert_at_end(data)
        elif option==6:
            x=input("Enter the element after which you want to inser the data:")
            data=input("Enter the data:")
            list.insert_after(x,data)
        elif option==7:
            x=input("Enter the element BEFORE which you want to inser the data:")
            data=input("Enter the data:")
            list.insert_before(x,data)

        elif option==8:
            pos=int(input("\n Enter the position at which element has to be entered:"))
            x=input("Enter data:")
            list.insert_at_pos(pos,x)
        elif option==9:
            list.delete_node_first()
        elif option==10:
            list.delete_node_last()
        elif option==11:
            x=input("Enter the element to be delted:")
            list.delete_node(x)
        elif option==12:
            list.reverse_list()
        elif option==13:
            list.bubble_sort_ed()
        elif option==14:
            list.bubble_sort_el()
        elif option==15:
            list2=LinkedList()
            list2.create_list()
        
            merged_list=list.mergeto(list2)  #a new list merged list has been made
            merged_list.display_list()
            list=merged_list
            list.display_list()
            
            
        elif option==16:
            x=input("Enter the node value where you want to insert cycle:")
            list.insert_cycle_at(x)
        elif option==17:
            k=list.has_cycle()
            print(k)
        elif option==18:
            list.remove_cycle()
        elif option==19:
            break
        else:
            print("\t\t wrong option!!!\n"+5*("***"))

if __name__=="__main__":
    main()
