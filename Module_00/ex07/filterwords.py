import sys

def del_elements(list1, n):
    for x in list1[:]: #iterate through a copy of the list
        if len(x) <= n:
            list1.remove(x)

if len(sys.argv) == 3 and sys.argv[2].isdigit():
    list1 = sys.argv[1].split()
    n = int(sys.argv[2])
    del_elements(list1, n)
    print(list1)
else:
    print("ERROR")
