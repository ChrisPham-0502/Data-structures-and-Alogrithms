import tree_node as node


class TreeBinary:

    def __init__(self):
        self._root = None

    def is_empty(self):
        if self._root is None:
            return True
        return False

    def addLeftNode(self, new_data, leafNode):
        new_item = node.Node(new_data, None, None)
        if self.is_empty():
            self._root = new_item
            return self._root
        else:
            leafNode.pleft = new_item
            return leafNode.pleft

    def addRightNode(self, new_data, rightNode):
        new_item = node.Node(new_data, None, None)
        if self.is_empty():
            self._root = new_item
            return self._root
        else:
            rightNode.pright = new_item
            return rightNode.pright

    def preorder_traversalNLR(self, root_test):
        if root_test is None:
            return
        print(root_test.data, end=' --> ')
        self.preorder_traversalNLR(root_test.pleft)
        self.preorder_traversalNLR(root_test.pright)

    def inorder_traversalLNR(self, root_test):
        if root_test is None:
            return

        self.inorder_traversalLNR(root_test.pleft)
        print(root_test.data, end=' --> ')
        self.inorder_traversalLNR(root_test.pright)

    def preorder_traversalLRN(self, root_test):
        if root_test is None:
            return

        self.preorder_traversalLRN(root_test.pleft)
        self.preorder_traversalLRN(root_test.pright)
        print(root_test.data, end=' --> ')

    def deleteNode(self,root, x):
        if root==None:
            return root
        if x< root.key:
            root.pleft=self.deleteNode(root.pleft, x)
        elif x> root.key:
            root.pright=self.deleteNode(root.pright, x)
        else:
            if root.pleft ==None:
                temp=root.pright
                del root
                return temp
            elif root.pright==None:
                temp=root.pleft
                del root
                return temp
            temp = self.minValueNode(root.pright)
            root.key=temp.key
            root.pright=self.deleteNode(root.pright,temp.key)
        return root

    def minValueNode(self,node):
        current=node
        while current.pleft!=None:
            current=current.pleft
        return current