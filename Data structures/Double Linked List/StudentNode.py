class StudentNode:   
    # data ở đây chính là đối tượng Student
    def __init__(self, data, next, prev):
      self.data = data
      self.next = next
      self.prev = prev
    
    def display(self):
      self.data.info()