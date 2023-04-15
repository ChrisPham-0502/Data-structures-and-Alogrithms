import hashmap as hm

h=hm.HashTable(10)
#Nhập lần lượt các key sau vào theo thứ tự: 100,25,16,19,21,50,66,70,82,44,46,99,78,86
l=[100,25,16,19,21,50,66,70,82,44,46,99,78,86]
for x in l:
    h.add(x,x)
#Hãy xuất ra màn hình các vị trí index trong bảng băm chưa lưu trữ khóa nào
h.check()
#Hãy xuất ra danh sách các khóa được lưu trữ tại index = 6
h.get_by_index(6)
#Hãy xuất ra khóa nhỏ nhất được lưu trữ tại index = 0
h.minimum(0)
