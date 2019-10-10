n=int(input())
for i in range (0,n):
    p=1
    x=int(input())
    for j in range (2,x+1):
        cnt=0   
        for k in range (2,j):
            if j%k==0:
                cnt=cnt+1
        if cnt==0:
            for l in range(0,x):
                if j**l>x:
                    o=l-1
                    p=p*j**o
                    break
                elif  j**l==x:
                    p=p*j**l
                    break
    print(p)

