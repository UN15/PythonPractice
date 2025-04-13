d1 = {"name": "John", "age": 30}
print("나이:"+str(d1['age']))

d2 = {"math": 90, "science": 85, "history": 78}
print("과목들:", end = '')
print(list(d2.keys()))

d3 = {'apple': 3, 'banana': 5}
d3['apple']+=2
print(d3)