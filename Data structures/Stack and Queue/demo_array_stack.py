import array_stack_class as asc

s = asc.ArrayStack()
s.push(12)
s.push(9)
s.push(10)
print(s.pop())
print(s.pop())
s.push(0)
print(s.pop())

# chuyển đổi cơ số
z = int(input("nhập số cần chuyển đổi: "))
k = int(input("hãy nhập hệ cơ số bạn muốn chuyển sang: "))

def div_by_2(dec_num):
    l = asc.ArrayStack()
    while dec_num > 0:
        remainder = dec_num % 2
        l.push(remainder)
        dec_num = dec_num // 2
    bin_num = ""
    while not l.is_empty():
        bin_num += str(l.pop())
    return bin_num


if k == 2:
    print(f"chuyển đổi {z} sang {k} sẽ có số là: ", div_by_2(z))
if k == 8:
    print(f"chuyển đổi {z} sang {k} sẽ có số là: ", oct(z))
if k == 16:
    print(f"chuyển đổi {z} sang {k} sẽ có số là: ", hex(z))
