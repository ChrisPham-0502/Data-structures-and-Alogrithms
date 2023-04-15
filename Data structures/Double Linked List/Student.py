class Student:
    def __init__(self,id,names,address,score):
        self.id = id
        self.names = names
        self.address = address
        self.score = score
    
    def info(self):
        print(f'Mã số: {self.id}, tên: {self.names}, địa chỉ: {self.address}, điểm: {self.score}')