from collections import deque

####Trees

class Node:
    def __init__(self,data):
        self.info=data
        self.lchild=None
        self.rchild=None

class BinaryTree:
    def __init__(self):
        self.root=None      ###Empty binary tree

    def is_empty(self):
        return self.root==None

    def create_tree(self):
        self.root=Node("P")
        self.root.lchild=Node("Q")
        self.root.rchild=Node("R")
        self.root.lchild.lchild=Node("A")
        self.root.lchild.rchild=Node("B")
        self.root.rchild.lchild=Node("X")


    

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self,p):
        if p is None:
            return             ###recursiion ka "return" return means going back to the line where it was called..after reaching that line it will start execution from the next line!!!! 
        print(p.info," ",end="")
        self._preorder(p.lchild)
        self._preorder(p.rchild)
        return                   #writing or not writing it here wont make a difference

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self,p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info," ",end="")
        self._inorder(p.rchild)
        return 

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self,p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info," ",end="")
        return

    def level_order(self):
        if self.root is None:
           return
        qu=deque()
        qu.append(self.root)
        

        while len(qu)!=0:
            p=qu.popleft()
            print(p.info," ",end="")
            if p.lchild is not None:
                qu.append(p.lchild)
            if p.lchild is not None:
                qu.append(p.lchild)
            
            

    def height(self):
        return self._height(self.root)

    def _height(self,p):
        if p is None:
            return 0
        hL=self._height(p.lchild)
        hR=self._height(p.rchild)

        if hL > hR:
            return 1 + hL
        else:
            return 1+ hR







###################################################################################################
def main():
    bt=BinaryTree()

    bt.create_tree()


    print("Preorder : ")
    bt.preorder()
    print()

    print("inorder : ")
    bt.inorder()
    print()

    print("Postrder : ")
    bt.postorder()
    print()

    print("level_order : ")
    bt.level_order()
    print("\n")

    print("Height of tree is",bt.height())

if __name__=="__main__":
    main()
