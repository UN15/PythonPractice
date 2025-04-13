s = "Python is awesome"
find_list = ['a', 'e', 'i', 'o', 'u']
sum = 0
for l in find_list:
    sum+=s.count(l)

print("모음 개수: "+ str(sum))
    