n=int(input())
for i in range (0,n):
    m=0
    cnt=0
    x=int(input())
    for j in range (1,x+1):
        if x%j==0:
           
            for k in range (2,j):
                if j%k==0:
                    cnt=cnt+1
      
            if cnt==0:
                m=j
    print(m)