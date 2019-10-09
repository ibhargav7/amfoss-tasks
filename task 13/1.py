n=int(input())
for j in range(0,n):
    x=int(input())
    s=0
    for i in range(0,x,3):
        s=s+i
    for j in range(0,x,5):
        if j%3!=0:
         s=s+j       
    print(s)

