def find_primes(a, b):
    p = list()
    for i in range(a, b+1):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break

        if flag == False:
            p.append(i)

    return p

print(find_primes(2, 7))