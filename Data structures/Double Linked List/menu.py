import StudentDLL as studll
import Student as stu

stuList = studll.StudentDLL()
menu_options = {
    1: 'Thêm sinh viên 1',
    2: 'Hiển thị danh sách 2',
    3: 'Xóa sinh viên 3',
    4: 'Chỉnh sửa thông tin 4',
    5: 'Exit 5'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

if __name__=='__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            while True:
                a = input('Hãy nhập id:')
                b = input('Hãy nhập tên:')
                c = input('Hãy nhập địa chỉ:')
                d = input('Hãy nhập điểm:')
                e = input('Thêm đầu danh sách a \nThêm cuối danh sách b \nEnter your choice:')
                stu_add = stu.Student(a,b,c,d)
                if e == 'a':
                    stuList.addHead(stu_add)
                else:
                    stuList.addTail(stu_add)
                n = input('Bạn còn muốn thêm sinh viên không (Y/n):')
                if n=='Y':
                    continue
                else:
                    break
            print('Đã thêm nhân viên')
        elif option == 2:
            stuList.traversal()
        elif option == 3:
            n = input('Xóa đầu danh sách a \nXóa cuối danh sách b \nEnter your choice:')
            if n == 'a':
                stuList.removeHead()
            else:
                stuList.removeTail()
        elif option == 4:
            a = input('Hãy nhập id:')
            b = input('Hãy nhập tên:')
            c = input('Hãy nhập địa chỉ:')
            d = input('Hãy nhập điểm:')
            stu_add = stu.Student(a, b, c, d)
            stuList.update(stu_add)
            print('Hoàn tất chỉnh sửa')
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')