sum = 0
for i in range(1, 101):
    if(i%3 == 0):
        sum+=i

print("3의 배수의 합: "+str(sum))