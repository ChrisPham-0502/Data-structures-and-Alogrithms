from tree_binarySearch import TreeBinary

"""
// Add some node as figure
    //                                8
    //                  5                         10
    //      1                      3         4               20
                            9            7
"""

myTree = TreeBinary()
A = myTree.addLeftNode(8, None)
C = myTree.addLeftNode(5, A)
D = myTree.addLeftNode(1, C)
E = myTree.addRightNode(6, C)
F = myTree.addLeftNode(7, E)
G = myTree.addRightNode(10, A)
H = myTree.addLeftNode(9, G)
J = myTree.addRightNode(20, G)
print(myTree.preorder_traversalNLR(A))
#print(myTree.inorder_traversalLNR(A))
#print(myTree.preorder_traversalLRN(A))
