n=int(input())
for i in range (0,n):
    s=1
    x=int(input())
    for j in range (2,x+1):
        if x%j==0:

            cnt=0   
            for k in range (2,j):
                if j%k==0:
                    cnt=cnt+1
                    break
                
            if cnt==0:
                m=j
    print(m)

