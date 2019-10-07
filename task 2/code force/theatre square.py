x=input()
y=x.replace(" ","")
if int(x[0])%int(x[2])==0 :
     sum=int(x[0])/int(x[2])
else: sum=(int(x[0])/int(x[2]))+1
if int(x[1])%int(x[2])==0 :
     sum1=int(x[1])/int(x[2])
else: sum1=(int(x[1])/int(x[2]))+1
print(sum*sum1)

