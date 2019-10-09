a=input()
b=input()
c=a.replace(" ","")
d=b.replace(" ","")
m=int(c[1])
n=int(c[0])
cnt = 0
for i in range(n):
    if int(d[i])>m:
        cnt += 1
    else:
        cnt=0
print(cnt)