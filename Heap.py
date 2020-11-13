##HEAP

class HeapEmpty(Exception):
    pass

class Heap:

    def __init__(self,maxsize=10):
        self.a=[None]*maxsize
        self.n=0
        self.a[0]=10000000  ##sentinal value

    def insert(self,value):
        self.n += 1  ##incrementing value of Heap
        self.a[self.n]=value
        self.restore_up(self.n)
##try usingb swap here...
    def restore_up(self,i):  ## i is self.n or last element of the array that is disrupting the heap order
        k=self.a[i]
        iparent=i//2
        while self.a[iparent] < k:
            self.a[i]=self.a[iparent]   ###we are moving parent key(i.e value in iparent) down by this
            i=iparent
            iparent=i//2   ##we could also write iparent//2
        self.a[i]=k    ##at the end i will be at its right position and we give it its right value
        
    def delete_root(self):  ##maybe using recursion we can implement it for any of the element
         if self.n==0:
             raise HeapEmpty("Heap is Empty")
        root=self.a[1]
        self.a[1]=self.a[self.n]   ##first step
        self.n -= 1   ##kam kr diya size
        self.restore_down(1)
        return root

    def restore_down(self,i):
        k=self.a[i]
        lchild=2*i
        rchild=2*i+1

        while rchild <= self.n:
        pass
    
        
