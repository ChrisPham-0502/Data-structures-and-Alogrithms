import Single_Linked_List as Single_list


my_single_list = Single_list.Single_List_Array()

my_single_list.add_tail("Hello")
my_single_list.add_tail("CF")
my_single_list.add_tail("Teacher")
my_single_list.add_tail("Mr.Nam")
my_single_list.add_tail("FPTU")

print(my_single_list.is_empty())

my_single_list.traversal()
print(30*'=')
my_single_list.remove_head()

my_single_list.traversal()
