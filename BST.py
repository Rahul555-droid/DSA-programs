from Trees import *

### BST##

class BST(BinaryTree):
    ##no need for init as inheritance

    def is_empty(self):
        return self.root == None

    

    def search1(self,x):   ##iterative
        p=self.root
        while p is not None:
            if x<p.info:
                p=p.lchild
            elif x>p.info:
                p=p.rchild
            else:
                break
        if p is None:
            return False
        else:
            return True

    def search2(self,x):
        return self._search2(self.root,x)

    def _search2(self,p,x):
        if p is None:
            return False
        elif x < p.info:
            return self._search2(p.lchild,x)
        elif x> p.info:
            return self._search2(p.rchild,x)
        elif x==p.info:
            return True

    def MinNode(self): ##recursive way
        return self._MinNode(self.root).info

    def _MinNode(self,p):
        if p.lchild is None:
            return p     ##cant write p.info here as p.info doesnt have a child
        if p.lchild is not None:
            return self._MinNode(p.lchild)

    """
    ##iterative way
    def MinNodei(self):
        p=self.start
        while p.lchild is not None:
            p=p.lchild
        return p.info

    """
    def MaxNode(self): ##recursive way
        return self._MaxNode(self.root).info

    def _MaxNode(self,p):
        if p.rchild is None:
            return p    
        if p.rchild is not None:
            return self._MaxNode(p.rchild)

    def insert1(self,x):    ##temp node is important
        p=self.root
        par=None
        

        while p is not None:
            par=p   ##as by this we will be able to access parent after p becomes None
            if x < p.info:
                p=p.lchild
            elif x > p.info:
                p=p.rchild
            elif x == p.info:
                print("ELement already present in the BST")
                return 

        temp=Node(x)

        if par == None:   ##iska matlab hai while loop kabhi chala hi nahi
            self.root=temp
        elif x < par.info:
            par.lchild=temp
        elif x>par.info:
            par.rchild=temp

    def insert2(self,x):
        self.root=self._insert2(self.root,x)

    def _insert2(self,p,x):
        if p is None:
            p=Node(x)
        elif x < p.info:
            p.lchild=self._insert2(p.lchild,x)
        elif x > p.info:
            p.rchild=self._insert2(p.rchild,x)
        else:
            print(x,"Element already in BST")
        return p

    def delete(self,x):
        pass













b=BST()




for i in range(1,11):
        b.insert1(i)
for i in range(11,21):
        b.insert2(i)
        

b.inorder()
b.postorder()
b.preorder()
##sab kuch right mein aa jayega lul





         
        
            
        
        
