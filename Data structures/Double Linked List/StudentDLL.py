import StudentNode as stunode

class StudentDLL:
    def __init__(self):
        self.head = None
        self.tail = None 
       
    def is_empty(self):
        if self.head == None:
            return True
        return False
           
    def removeHead(self):
        if self.is_empty():
            print('Students DLL is empty')
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None   
        
        if self.is_empty():                     
            self.tail = None                    
        
    def addTail(self, newdata):
        new_item = stunode.StudentNode(newdata, None, None)
        
        if self.is_empty():
            self.head = new_item            
        else:
            self.tail.next = new_item
            new_item.prev = self.tail

        self.tail = new_item    

    def addHead(self, newdata):
        new_item = stunode.StudentNode(newdata, None, None)
        if self.is_empty():        
            self.tail = new_item
        else:
            self.head.prev = new_item
            new_item.next = self.head
        
        self.head = new_item

    def removeTail(self):
        if self.is_empty():
            print('Student DLL is empty')
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return
            
        self.tail = self.tail.prev
        self.tail.next = None

        if self.is_empty():                     
            self.head = None

    def traversal(self):
        if self.is_empty():
            print("Student DLL is empty")
            return
        current = self.head
        while current != None:
            current.display()
            current = current.next
    
    def isDuplicated(self,_id):
        if self.is_empty():
            return False
        current = self.head
        while current != None:
            if(current.data.id == _id):
                return True
            current = current.next
        return False
    
    def update(self,newData):
        if self.is_empty():
            print("Student DLL is empty")
            return
        current = self.head
        while current != None:
            if(current.data.id == newData.id):
                current.data.names = newData.names
                current.data.address = newData.address
                current.data.score = newData.score
                return
            current = current.next
         