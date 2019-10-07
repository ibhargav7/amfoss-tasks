n=int(input())
for i in range (0,n):
    x=int(input())
    o=0
    l=0
    for j in range (100,1000):
        for k in range (100,1000):
            s=j*k
           
            while s>0:
                n=s%10
                o=o*10+n
                s/10
            if o==j*k and o<n:
                l=o
    print(l)