
"""
##SELECTIONSORT
def selsort(a):
    for i in range(len(a)-1):  ## i indicates passes of selsort
        minindex=i ##smallest elements index 
        #swaps=0
        for j in range(i+1,len(a)):  ##this loop selects the smallest element  loop goes through i+1 to len(a)-1 as it for loop bitch
            if a[j] < a[minindex]:
                minindex=j
            if i!=minindex:   
                a[i],a[minindex]=a[minindex],a[i]  ##swapping  is done between the a[pass] or a[i] and minimum index,i starts from 0 and goes to n-1
                #swaps+=1   ##can there be a pass where no swaps happen and the array remain unsorted??shit this won't work...
            #if swaps==0:
                #break


a=[]
for i in range(100,0,-1):
    a.append(i)

print(a)

print("5selsort started")



selsort(a)
print(a)


##selection sort is unstable



##BUBBLESORT
##adjacent elements are compared and swapping them if they are not in oder

##at the end of first pass the biggest element of the array will be at the last position
##at the end of second pass the second biggest element comes at the sec last position
## and so on...
##after n-1 passes we will have the whole array sorted
"""
"""
def swap(a,b):
    a,b=b,a
    return a,b

def bubblesort(a):
    n=len(a)
    
    for i in range(0,n-1):
        swaps=0   ##initialisng swap at each pass to zero
        for j in range(0,n-i-1):  ##end ke elements sort  hote jaa rahe hai isiliye range goes from 0 to n-i-2(for loop)
            if a[j]>a[j+1]:  ##n-i-1 th we compare hoga...
                a[j],a[j+1]=swap(a[j],a[j+1])  ##unpacking tuples
                swaps+=1                       ##incrementing no. of swaps as they occur....
        if swaps==0:##if no swaps occur in a passs then we break
            break

    
                
a=[]
for i in range(10000,0,-1):
    a.append(i)
print(a)
bubblesort(a)
print(a)

##could have also used:
#for i in range(n-1,0,-1):
#    for j in range(i):
"""
## improvements in bubblesort       (refer swaps above)
##array of n elements can be sorted in less than n-1 pass


#########INSERTION-SORT##########
"""
def inssort(a):
    n=len(a)
    for i in range(1,n): ##n-1 passses....we couldnt start with range(0,n-1) as we wont be able to use first pass
        for j in range(0,i):
            if a[j]>a[i]:
                a[j],a[i]=a[i],a[j]


a=[5,3,1,34,4,55]
inssort(a)
print(a)
        
##here I dont know what i made.........it isnt insertion sort but it does thr job

"""
"""
## inssort according to video there are some similarities between upper and this program..watch python implementation from vid
def ins_sort(a):
    n=len(a)
    for i in range(1,n):
        temp=a[i]
        j=i-1
        while j>=0 and a[j]>=temp:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp

a=[5,3,1,34,4,55]
ins_sort(a)
print(a)
"""
"""
##SHELLSORT(improvement over insertion sort) also known as Diminishing Increment Short
        

def shell_sort(a):
    h=int(input("Enter maximum increment(odd values): "))
    while h>=1:
        for i in range(h,len(a)):
            temp=a[i]
            j=i-h
            while j>=0 and a[j]>temp:
                a[j+h]=a[j]
                j=j-h
            a[j+h]=temp
        h=h-2

a=[]
for i in range(100,0,-1):
    a.append(i)
print(a)
shell_sort(a)
print(a)
"""
"""
##merging two sorted arrays
def merging(a,b):
    n1=len(a)
    n2=len(b)
    n3=n1+n2
    c=[None]*(n3)
    i=0
    j=0
    k=0
    while i<=n1-1 and j<=n2-1:
        if a[i] < b[j]:
            c[k]=a[i]
            i+=1
            
        elif b[j] < a[i]:
            c[k]=b[j]
            j+=1

        else:####kuch toh kia apan ne to remove problem with duplicates
            c[k]=a[i]
            c[k+1]=b[j]
            i+=1
            j+=1
            k+=1

        k+=1            

    if i>n1-1:       #this means that list a has been exhauseted...
        while j<=n2-1:
            c[k]=b[j]
            k+=1
            j+=1
    else:
        while i<=n1-1:
            c[k]=a[i]
            k+=1
            i+=1
    return c

a=[1,2,3,4,5,6,7,8]
print(a)
b=[1,2,3,4]
print(b)
print("AFTER MERGING")
c=merging(a,b)
print(c)
"""
##case when duplicate elements are present......??.....check
##case when a list iS  a subseet of another list?? ....check
"""
##when we have to merge two sorted parts of the same list

def merge(a,temp,low1,up1,low2,up2):
    i=low1
    j=low2
    k=low1

    while i<=up1 and j<=up2:
        if a[i] <= a[j]:
            temp[k]=a[i]
            i+=1
        else:
            temp[k]=a[j]
            j+=1
        k+=1

    while i<=up1:
        temp[k]=a[i]
        i+=1
        k+=1

    while j<=up2:
        temp[k]=a[j]
        j+=1
        k+=1

################################
a=[1,2,4,6, 3,5,6,7,13,19]
temp=[None]*len(a)

merge(a,temp,0,3,4,9)

print("Merged List",temp)
"""


##MERGESORT RECURSIVELY....check m-way merging of lists
"""
def merge_sort(a):
    n=len(a)
    temp=[None]*n
    sort(a,temp,0,n-1)

def sort(a,temp,low,up):
    if low==up: ##only one element in the list remaining so it is sorted...
        return
    
    mid=(low+up)//2

    sort(a,temp,low,mid)  #sorts a[low] to a[mid]
    sort(a,temp,mid+1,up) #sorts a[mid+1] to a[up]

    merge(a,temp,low,mid,mid+1,up)##merges list a from a[low] to a[mid] and a[mid+1] to a[up] into temp from temp[low] to temp[up]

    copy(a,temp,low,up)   ##copies result of temp[] from low to up into a[]

def merge(a,temp,low1,up1,low2,up2):
    i=low1
    j=low2
    k=low1

    while i<=up1 and j<=up2:
        if a[i] <= a[j]:
            temp[k]=a[i]
            i+=1
        else:
            temp[k]=a[j]
            j+=1
        k+=1

    while i<=up1:
        temp[k]=a[i]
        i+=1
        k+=1

    while j<=up2:
        temp[k]=a[j]
        j+=1
        k+=1

def copy(a,temp,low,up):
    for i in range(low,up+1):
        a[i]=temp[i]

a=[]
for i in range(10000,0,-1):
    a.append(i)
merge_sort(a)
print(a)
"""

##Bottom Up Merge Sort(Iterative)
"""
def merge_sort(a):
    n=len(a)
    temp=[None]*n
    size=1  ##initially size of sublists is one
    while size<=n-1:   ##dont know why not <= n??....if size become n then no need to sort.
        sort_pass(a,temp,size,n)
        size=size*2
    #this while loop will execute for logn times and each execution is called a pass in sorting(sort_pass)

def sort_pass(a,temp,size,n):
    
    low1=0  ##value of low1=0
    while low1+size<=n-1:  ##maybe due to 1
        up1=low1+size-1   ##first sublist
        low2=up1+1
        up2=low2+size-1

        if up2 >= n:   ##if length of last sublist is less than size (left out wala sublist)
            up2=n-1

        merge(a,temp,low1,up1,low2,up2)

        low1=up2+1   #take next two sublists for merging

    for i in range(low1,n):  ##if any list is left alone..as low1 will be maxed out..
        temp[i]=a[i]

    copy(a,temp,n)

def merge(a,temp,low1,up1,low2,up2):
    i=low1
    j=low2
    k=low1

    while i<=up1 and j<=up2:
        if a[i] <= a[j]:
            temp[k]=a[i]
            i+=1
        else:
            temp[k]=a[j]
            j+=1
        k+=1

    while i<=up1:
        temp[k]=a[i]
        i+=1
        k+=1

    while j<=up2:
        temp[k]=a[j]
        j+=1
        k+=1


def copy(a,temp,n):
    for i in range(n):
        a[i]=temp[i]


a=[43,23,124,543,1,7,98,33]
merge_sort(a)
print(a)
"""    

##QUICK SORT>>>>>>> just like merging was a tool for merge sort partition is a tool for quick sort
"""

def quick_sort(a):
    sort(a,0,len(a)-1)

def sort(a,low,up):
    if low>= up:   ##for single or no element
        return

    p=partition(a,low,up)
    sort(a,low,p-1)   ##sorts left sub_list
    sort(a,p+1,up)    ##sorts right sub_list

#dont know how this works
def partition(a,low,up):  ##gets us the p that is the posiiton of pivot after a pass

    pivot=a[low]
    i=low+1   #moves from right to left
    j=up      #moves from left to right
    while i<=j:  ##while loop is used as we at some point we wouldnt have found pivot but i and j would have stopped
        
        while a[i]<pivot and i<up:  ##moves i from left to right 
            i+=1
        while a[j]>pivot:           ##moves j from right to left
            j-=1

        if i<j:                     ##swapping(check vid for demo)
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1

        else:  ##found proper place for pivot
            break
    #found proper place for pivot is j
    a[low]=a[j]
    a[j]=pivot

    return j

a=[]
for i in range(1000,0,-1):
    a.append(i)
    
quick_sort(a)
print(a)
"""

###RADIX SORT>>>>>>>
# sorting occurs digit by digit
#pass 1,digit by digit on units digit basis
#pass 2,digit by digit on units digit basis
#pass n,digit by digit on nth  digit basis
# i.e no. of passes is dependent upon no. of maximum digits in ANY of the element


