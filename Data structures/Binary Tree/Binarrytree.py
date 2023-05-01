class Tnode:
    def __init__(self,data,pleft,pright):
        self.data = data
        self.pleft = pleft
        self.pright=pright

    def display(self):
        print(self.data)
        print(self.pleft)
        print(self.pright)

class BinaryTree:
    def __init__(self):
        self.root=None

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def addLeftNode(self, newdata, leafNode):
        new_node =Tnode(newdata, None, None)
        if self.is_empty():
            self.root=new_node
            return self.root
        else:
            leafNode.pleft=new_node
            return leafNode.pleft

    def addRightNode(self,newdata, leafNode):
        newdata = Tnode(newdata,None,None)
        if self.is_empty():
            self.root=newdata
            return self.root
        else:
            leafNode.pright=newdata
            return leafNode.pright

    def preordertraversalNLR(self,test_root):
        if test_root is None:
            return
        print(test_root.data, end='-->')
        self.preordertraversalNLR(test_root.pleft)
        self.preordertraversalNLR(test_root.pright)

    def preordertraversalLNR(self,test_root):
        if test_root is None:
            return
        self.preordertraversalNLR(test_root.pleft)
        print(test_root.data, end='-->')
        self.preordertraversalNLR(test_root.pright)

    def preordertraversalLRN(self, test_root):
        if test_root is None:
            return

        self.preordertraversalNLR(test_root.pleft)
        self.preordertraversalNLR(test_root.pright)
        print(test_root.data, end='-->')

    def searchNode(self, key):
        current = self.root
        if self.root is None:
            print('Binary tree is empty')
            return
        while current!=None:
            if key>current.data:
                current=current.pright
                continue
            elif key<current.data:
                current=current.pleft
                continue
            elif current.data == key:
                print(f'Node bạn cần tìm là:{current.data}')
                return

    def minValue(self):
        current = self.root
        if self.root is None:
            print('None')
            return
        while current!=None:
            if current.pleft == None:
                print(current.data)
                return
            current = current.pleft

    def maxValue(self):
        current = self.root
        if self.root is None:
            print('None')
            return
        while current!=None:
            if current.pright == None:
                print(current.data)
                return
            current = current.pright


"""
// Add some node as figure
    //                                8
    //                  5                         10
    //      1                      3         4               20
                            9            7
"""
mytree = BinaryTree()
a = mytree.addLeftNode(8,None)
b = mytree.addLeftNode(5,a)
c = mytree.addLeftNode(1,b)
d = mytree.addRightNode(3,b)
e = mytree.addLeftNode(9, d)
f = mytree.addRightNode(10,a)
g = mytree.addLeftNode(4,f)
i = mytree.addLeftNode(7,g)
h = mytree.addRightNode(20,f)

mytree.preordertraversalNLR(a)
print(' ')
mytree.minValue()
mytree.maxValue()