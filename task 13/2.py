n=int(input())
p=1
q=2
m=2
while m<n:
    for i in range (2,n):
        s=p+q
    if s%2==0:
        m=m+s
    else:
        pass
    p=q
    q=s
print(m)
