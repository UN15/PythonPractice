list1 = [1, 2, 3]
list2 = [4, 5, 6]

def add_num(a, b):
    return a+b

nlist = list(map(add_num, list1, list2))
print(nlist)
