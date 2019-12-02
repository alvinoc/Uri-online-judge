a,b,c = input().split()

if (int(a)>int(b) and int(a)>int(c)):
    print("%d eh o maior"%int(a))
elif (int(b)>int(a) and int(b)>int(c)):
    print("%d eh o maior"%int(b))
elif (int(c)>int(a) and int(c)>int(b)):
    print("%d eh o maior"%int(c))