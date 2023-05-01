class Node:
    def __init__(self, data, pleft, pright):
        self.data = data
        self.pleft = pleft
        self.pright = pright


    def display(self):
        print(self.data)
        print(self.pleft)
        print(self.pright)
