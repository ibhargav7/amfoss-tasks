x=int(input())
for l in range (x):
    k=int(input())
    s=0
    p=2
    q=0 
    m=0
    while m<k:
        s+=p
        m=4*p+q
        q=p
        p=m
        
    print(s)

