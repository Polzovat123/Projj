f = int(0)
a = int(0)

for i in range(30000000000, 50000000001):
    print(i)
    if i%7==0 and i%100000==0 and i%15!=0 and i%33!=0 and i%51!=0 and i%102!=0 :
        a = a + 1
        if f==0:
            f = i
    print(a)
    print(f)
